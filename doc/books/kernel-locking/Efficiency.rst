.. -*- coding: utf-8; mode: rst -*-

.. _Efficiency:

*************
Locking Speed
*************

There are three main things to worry about when considering speed of
some code which does locking. First is concurrency: how many things are
going to be waiting while someone else is holding a lock. Second is the
time taken to actually acquire and release an uncontended lock. Third is
using fewer, or smarter locks. I'm assuming that the lock is used fairly
often: otherwise, you wouldn't be concerned about efficiency.

Concurrency depends on how long the lock is usually held: you should
hold the lock for as long as needed, but no longer. In the cache
example, we always create the object without the lock held, and then
grab the lock only when we are ready to insert it in the list.

Acquisition times depend on how much damage the lock operations do to
the pipeline (pipeline stalls) and how likely it is that this CPU was
the last one to grab the lock (ie. is the lock cache-hot for this CPU):
on a machine with more CPUs, this likelihood drops fast. Consider a
700MHz Intel Pentium III: an instruction takes about 0.7ns, an atomic
increment takes about 58ns, a lock which is cache-hot on this CPU takes
160ns, and a cacheline transfer from another CPU takes an additional 170
to 360ns. (These figures from Paul McKenney's
`Linux Journal RCU article <http://www.linuxjournal.com/article.php?sid=6993>`__).

These two aims conflict: holding a lock for a short time might be done
by splitting locks into parts (such as in our final per-object-lock
example), but this increases the number of lock acquisitions, and the
results are often slower than having a single lock. This is another
reason to advocate locking simplicity.

The third concern is addressed below: there are some methods to reduce
the amount of locking which needs to be done.


.. _efficiency-rwlocks:

Read/Write Lock Variants
========================

Both spinlocks and mutexes have read/write variants: ``rwlock_t`` and
``struct rw_semaphore``. These divide users into two classes: the
readers and the writers. If you are only reading the data, you can get a
read lock, but to write to the data you need the write lock. Many people
can hold a read lock, but a writer must be sole holder.

If your code divides neatly along reader/writer lines (as our cache code
does), and the lock is held by readers for significant lengths of time,
using these locks can help. They are slightly slower than the normal
locks though, so in practice ``rwlock_t`` is not usually worthwhile.


.. _efficiency-read-copy-update:

Avoiding Locks: Read Copy Update
================================

There is a special method of read/write locking called Read Copy Update.
Using RCU, the readers can avoid taking a lock altogether: as we expect
our cache to be read more often than updated (otherwise the cache is a
waste of time), it is a candidate for this optimization.

How do we get rid of read locks? Getting rid of read locks means that
writers may be changing the list underneath the readers. That is
actually quite simple: we can read a linked list while an element is
being added if the writer adds the element very carefully. For example,
adding ``new`` to a single linked list called ``list``:


.. code-block:: c

            new->next = list->next;
            wmb();
            list->next = new;

The ``wmb()`` is a write memory barrier. It ensures that the first
operation (setting the new element's ``next`` pointer) is complete and
will be seen by all CPUs, before the second operation is (putting the
new element into the list). This is important, since modern compilers
and modern CPUs can both reorder instructions unless told otherwise: we
want a reader to either not see the new element at all, or see the new
element with the ``next`` pointer correctly pointing at the rest of the
list.

Fortunately, there is a function to do this for standard
``struct list_head`` lists: ``list_add_rcu()``
(``include/linux/list.h``).

Removing an element from the list is even simpler: we replace the
pointer to the old element with a pointer to its successor, and readers
will either see it, or skip over it.


.. code-block:: c

            list->next = old->next;

There is ``list_del_rcu()`` (``include/linux/list.h``) which does this
(the normal version poisons the old object, which we don't want).

The reader must also be careful: some CPUs can look through the ``next``
pointer to start reading the contents of the next element early, but
don't realize that the pre-fetched contents is wrong when the ``next``
pointer changes underneath them. Once again, there is a
``list_for_each_entry_rcu()`` (``include/linux/list.h``) to help you. Of
course, writers can just use ``list_for_each_entry()``, since there
cannot be two simultaneous writers.

Our final dilemma is this: when can we actually destroy the removed
element? Remember, a reader might be stepping through this element in
the list right now: if we free this element and the ``next`` pointer
changes, the reader will jump off into garbage and crash. We need to
wait until we know that all the readers who were traversing the list
when we deleted the element are finished. We use ``call_rcu()`` to
register a callback which will actually destroy the object once all
pre-existing readers are finished. Alternatively, ``synchronize_rcu()``
may be used to block until all pre-existing are finished.

But how does Read Copy Update know when the readers are finished? The
method is this: firstly, the readers always traverse the list inside
``rcu_read_lock()``/``rcu_read_unlock()`` pairs: these simply disable
preemption so the reader won't go to sleep while reading the list.

RCU then waits until every other CPU has slept at least once: since
readers cannot sleep, we know that any readers which were traversing the
list during the deletion are finished, and the callback is triggered.
The real Read Copy Update code is a little more optimized than this, but
this is the fundamental idea.


.. code-block:: c

    --- cache.c.perobjectlock   2003-12-11 17:15:03.000000000 +1100
    +++ cache.c.rcupdate    2003-12-11 17:55:14.000000000 +1100
    @@ -1,15 +1,18 @@
     #include <linux/list.h>
     #include <linux/slab.h>
     #include <linux/string.h>
    +#include <linux/rcupdate.h>
     #include <linux/mutex.h>
     #include <asm/errno.h>

     struct object
     {
    -        /* These two protected by cache_lock. */
    +        /* This is protected by RCU */
             struct list_head list;
             int popularity;

    +        struct rcu_head rcu;
    +
             atomic_t refcnt;

             /* Doesn't change once created. */
    @@ -40,7 +43,7 @@
     {
             struct object *i;

    -        list_for_each_entry(i, &cache, list) {
    +        list_for_each_entry_rcu(i, &cache, list) {
                     if (i->id == id) {
                             i->popularity++;
                             return i;
    @@ -49,19 +52,25 @@
             return NULL;
     }

    +/* Final discard done once we know no readers are looking. */
    +static void cache_delete_rcu(void *arg)
    +{
    +        object_put(arg);
    +}
    +
     /* Must be holding cache_lock */
     static void __cache_delete(struct object *obj)
     {
             BUG_ON(!obj);
    -        list_del(&obj->list);
    -        object_put(obj);
    +        list_del_rcu(&obj->list);
             cache_num--;
    +        call_rcu(&obj->rcu, cache_delete_rcu);
     }

     /* Must be holding cache_lock */
     static void __cache_add(struct object *obj)
     {
    -        list_add(&obj->list, &cache);
    +        list_add_rcu(&obj->list, &cache);
             if (++cache_num > MAX_CACHE_SIZE) {
                     struct object *i, *outcast = NULL;
                     list_for_each_entry(i, &cache, list) {
    @@ -104,12 +114,11 @@
     struct object *cache_find(int id)
     {
             struct object *obj;
    -        unsigned long flags;

    -        spin_lock_irqsave(&cache_lock, flags);
    +        rcu_read_lock();
             obj = __cache_find(id);
             if (obj)
                     object_get(obj);
    -        spin_unlock_irqrestore(&cache_lock, flags);
    +        rcu_read_unlock();
             return obj;
     }

Note that the reader will alter the ``popularity`` member in
``__cache_find()``, and now it doesn't hold a lock. One solution would
be to make it an ``atomic_t``, but for this usage, we don't really care
about races: an approximate result is good enough, so I didn't change
it.

The result is that ``cache_find()`` requires no synchronization with any
other functions, so is almost as fast on SMP as it would be on UP.

There is a further optimization possible here: remember our original
cache code, where there were no reference counts and the caller simply
held the lock whenever using the object? This is still possible: if you
hold the lock, no one can delete the object, so you don't need to get
and put the reference count.

Now, because the 'read lock' in RCU is simply disabling preemption, a
caller which always has preemption disabled between calling
``cache_find()`` and ``object_put()`` does not need to actually get and
put the reference count: we could expose ``__cache_find()`` by making it
non-static, and such callers could simply call that.

The benefit here is that the reference count is not written to: the
object is not altered in any way, which is much faster on SMP machines
due to caching.


.. _per-cpu:

Per-CPU Data
============

Another technique for avoiding locking which is used fairly widely is to
duplicate information for each CPU. For example, if you wanted to keep a
count of a common condition, you could use a spin lock and a single
counter. Nice and simple.

If that was too slow (it's usually not, but if you've got a really big
machine to test on and can show that it is), you could instead use a
counter for each CPU, then none of them need an exclusive lock. See
``DEFINE_PER_CPU()``, ``get_cpu_var()`` and ``put_cpu_var()``
(``include/linux/percpu.h``).

Of particular use for simple per-cpu counters is the ``local_t`` type,
and the ``cpu_local_inc()`` and related functions, which are more
efficient than simple code on some architectures
(``include/asm/local.h``).

Note that there is no simple, reliable way of getting an exact value of
such a counter, without introducing more locks. This is not a problem
for some uses.


.. _mostly-hardirq:

Data Which Mostly Used By An IRQ Handler
========================================

If data is always accessed from within the same IRQ handler, you don't
need a lock at all: the kernel already guarantees that the irq handler
will not run simultaneously on multiple CPUs.

Manfred Spraul points out that you can still do this, even if the data
is very occasionally accessed in user context or softirqs/tasklets. The
irq handler doesn't use a lock, and all other accesses are done as so:


.. code-block:: c

        spin_lock(&lock);
        disable_irq(irq);
        ...
        enable_irq(irq);
        spin_unlock(&lock);

The ``disable_irq()`` prevents the irq handler from running (and waits
for it to finish if it's currently running on other CPUs). The spinlock
prevents any other accesses happening at the same time. Naturally, this
is slower than just a ``spin_lock_irq()`` call, so it only makes sense
if this type of access happens extremely rarely.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
