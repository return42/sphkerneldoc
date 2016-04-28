.. -*- coding: utf-8; mode: rst -*-

.. _Examples:

===============
Common Examples
===============

Let's step through a simple example: a cache of number to name mappings.
The cache keeps a count of how often each of the objects is used, and
when it gets full, throws out the least used one.


.. _examples-usercontext:

All In User Context
===================

For our first example, we assume that all operations are in user context
(ie. from system calls), so we can sleep. This means we can use a mutex
to protect the cache and all the objects within it. Here's the code:


.. code-block:: c

    #include <linux/list.h>
    #include <linux/slab.h>
    #include <linux/string.h>
    #include <linux/mutex.h>
    #include <asm/errno.h>

    struct object
    {
            struct list_head list;
            int id;
            char name[32];
            int popularity;
    };

    /* Protects the cache, cache_num, and the objects within it */
    static DEFINE_MUTEX(cache_lock);
    static LIST_HEAD(cache);
    static unsigned int cache_num = 0;
    #define MAX_CACHE_SIZE 10

    /* Must be holding cache_lock */
    static struct object *__cache_find(int id)
    {
            struct object *i;

            list_for_each_entry(i, &cache, list)
                    if (i->id == id) {
                            i->popularity++;
                            return i;
                    }
            return NULL;
    }

    /* Must be holding cache_lock */
    static void __cache_delete(struct object *obj)
    {
            BUG_ON(!obj);
            list_del(&obj->list);
            kfree(obj);
            cache_num--;
    }

    /* Must be holding cache_lock */
    static void __cache_add(struct object *obj)
    {
            list_add(&obj->list, &cache);
            if (++cache_num > MAX_CACHE_SIZE) {
                    struct object *i, *outcast = NULL;
                    list_for_each_entry(i, &cache, list) {
                            if (!outcast || i->popularity < outcast->popularity)
                                    outcast = i;
                    }
                    __cache_delete(outcast);
            }
    }

    int cache_add(int id, const char *name)
    {
            struct object *obj;

            if ((obj = kmalloc(sizeof(*obj), GFP_KERNEL)) == NULL)
                    return -ENOMEM;

            strlcpy(obj->name, name, sizeof(obj->name));
            obj->id = id;
            obj->popularity = 0;

            mutex_lock(&cache_lock);
            __cache_add(obj);
            mutex_unlock(&cache_lock);
            return 0;
    }

    void cache_delete(int id)
    {
            mutex_lock(&cache_lock);
            __cache_delete(__cache_find(id));
            mutex_unlock(&cache_lock);
    }

    int cache_find(int id, char *name)
    {
            struct object *obj;
            int ret = -ENOENT;

            mutex_lock(&cache_lock);
            obj = __cache_find(id);
            if (obj) {
                    ret = 0;
                    strcpy(name, obj->name);
            }
            mutex_unlock(&cache_lock);
            return ret;
    }

Note that we always make sure we have the cache_lock when we add,
delete, or look up the cache: both the cache infrastructure itself and
the contents of the objects are protected by the lock. In this case it's
easy, since we copy the data for the user, and never let them access the
objects directly.

There is a slight (and common) optimization here: in ``cache_add`` we
set up the fields of the object before grabbing the lock. This is safe,
as no-one else can access it until we put it in cache.


.. _examples-interrupt:

Accessing From Interrupt Context
================================

Now consider the case where ``cache_find`` can be called from interrupt
context: either a hardware interrupt or a softirq. An example would be a
timer which deletes object from the cache.

The change is shown below, in standard patch format: the ``-`` are lines
which are taken away, and the ``+`` are lines which are added.


.. code-block:: c

    --- cache.c.usercontext 2003-12-09 13:58:54.000000000 +1100
    +++ cache.c.interrupt   2003-12-09 14:07:49.000000000 +1100
    @@ -12,7 +12,7 @@
             int popularity;
     };

    -static DEFINE_MUTEX(cache_lock);
    +static DEFINE_SPINLOCK(cache_lock);
     static LIST_HEAD(cache);
     static unsigned int cache_num = 0;
     #define MAX_CACHE_SIZE 10
    @@ -55,6 +55,7 @@
     int cache_add(int id, const char *name)
     {
             struct object *obj;
    +        unsigned long flags;

             if ((obj = kmalloc(sizeof(*obj), GFP_KERNEL)) == NULL)
                     return -ENOMEM;
    @@ -63,30 +64,33 @@
             obj->id = id;
             obj->popularity = 0;

    -        mutex_lock(&cache_lock);
    +        spin_lock_irqsave(&cache_lock, flags);
             __cache_add(obj);
    -        mutex_unlock(&cache_lock);
    +        spin_unlock_irqrestore(&cache_lock, flags);
             return 0;
     }

     void cache_delete(int id)
     {
    -        mutex_lock(&cache_lock);
    +        unsigned long flags;
    +
    +        spin_lock_irqsave(&cache_lock, flags);
             __cache_delete(__cache_find(id));
    -        mutex_unlock(&cache_lock);
    +        spin_unlock_irqrestore(&cache_lock, flags);
     }

     int cache_find(int id, char *name)
     {
             struct object *obj;
             int ret = -ENOENT;
    +        unsigned long flags;

    -        mutex_lock(&cache_lock);
    +        spin_lock_irqsave(&cache_lock, flags);
             obj = __cache_find(id);
             if (obj) {
                     ret = 0;
                     strcpy(name, obj->name);
             }
    -        mutex_unlock(&cache_lock);
    +        spin_unlock_irqrestore(&cache_lock, flags);
             return ret;
     }

Note that the ``spin_lock_irqsave`` will turn off interrupts if they are
on, otherwise does nothing (if we are already in an interrupt handler),
hence these functions are safe to call from any context.

Unfortunately, ``cache_add`` calls ``kmalloc`` with the ``GFP_KERNEL``
flag, which is only legal in user context. I have assumed that
``cache_add`` is still only called in user context, otherwise this
should become a parameter to ``cache_add``.


.. _examples-refcnt:

Exposing Objects Outside This File
==================================

If our objects contained more information, it might not be sufficient to
copy the information in and out: other parts of the code might want to
keep pointers to these objects, for example, rather than looking up the
id every time. This produces two problems.

The first problem is that we use the ``cache_lock`` to protect objects:
we'd need to make this non-static so the rest of the code can use it.
This makes locking trickier, as it is no longer all in one place.

The second problem is the lifetime problem: if another structure keeps a
pointer to an object, it presumably expects that pointer to remain
valid. Unfortunately, this is only guaranteed while you hold the lock,
otherwise someone might call ``cache_delete`` and even worse, add
another object, re-using the same address.

As there is only one lock, you can't hold it forever: no-one else would
get any work done.

The solution to this problem is to use a reference count: everyone who
has a pointer to the object increases it when they first get the object,
and drops the reference count when they're finished with it. Whoever
drops it to zero knows it is unused, and can actually delete it.

Here is the code:


.. code-block:: c

    --- cache.c.interrupt   2003-12-09 14:25:43.000000000 +1100
    +++ cache.c.refcnt  2003-12-09 14:33:05.000000000 +1100
    @@ -7,6 +7,7 @@
     struct object
     {
             struct list_head list;
    +        unsigned int refcnt;
             int id;
             char name[32];
             int popularity;
    @@ -17,6 +18,35 @@
     static unsigned int cache_num = 0;
     #define MAX_CACHE_SIZE 10

    +static void __object_put(struct object *obj)
    +{
    +        if (--obj->refcnt == 0)
    +                kfree(obj);
    +}
    +
    +static void __object_get(struct object *obj)
    +{
    +        obj->refcnt++;
    +}
    +
    +void object_put(struct object *obj)
    +{
    +        unsigned long flags;
    +
    +        spin_lock_irqsave(&cache_lock, flags);
    +        __object_put(obj);
    +        spin_unlock_irqrestore(&cache_lock, flags);
    +}
    +
    +void object_get(struct object *obj)
    +{
    +        unsigned long flags;
    +
    +        spin_lock_irqsave(&cache_lock, flags);
    +        __object_get(obj);
    +        spin_unlock_irqrestore(&cache_lock, flags);
    +}
    +
     /* Must be holding cache_lock */
     static struct object *__cache_find(int id)
     {
    @@ -35,6 +65,7 @@
     {
             BUG_ON(!obj);
             list_del(&obj->list);
    +        __object_put(obj);
             cache_num--;
     }

    @@ -63,6 +94,7 @@
             strlcpy(obj->name, name, sizeof(obj->name));
             obj->id = id;
             obj->popularity = 0;
    +        obj->refcnt = 1; /* The cache holds a reference */

             spin_lock_irqsave(&cache_lock, flags);
             __cache_add(obj);
    @@ -79,18 +111,15 @@
             spin_unlock_irqrestore(&cache_lock, flags);
     }

    -int cache_find(int id, char *name)
    +struct object *cache_find(int id)
     {
             struct object *obj;
    -        int ret = -ENOENT;
             unsigned long flags;

             spin_lock_irqsave(&cache_lock, flags);
             obj = __cache_find(id);
    -        if (obj) {
    -                ret = 0;
    -                strcpy(name, obj->name);
    -        }
    +        if (obj)
    +                __object_get(obj);
             spin_unlock_irqrestore(&cache_lock, flags);
    -        return ret;
    +        return obj;
     }

We encapsulate the reference counting in the standard 'get' and 'put'
functions. Now we can return the object itself from ``cache_find`` which
has the advantage that the user can now sleep holding the object (eg. to
``copy_to_user`` to name to userspace).

The other point to note is that I said a reference should be held for
every pointer to the object: thus the reference count is 1 when first
inserted into the cache. In some versions the framework does not hold a
reference count, but they are more complicated.


.. _examples-refcnt-atomic:

Using Atomic Operations For The Reference Count
-----------------------------------------------

In practice, ``atomic_t`` would usually be used for ``refcnt``. There
are a number of atomic operations defined in ``include/asm/atomic.h``:
these are guaranteed to be seen atomically from all CPUs in the system,
so no lock is required. In this case, it is simpler than using
spinlocks, although for anything non-trivial using spinlocks is clearer.
The ``atomic_inc`` and ``atomic_dec_and_test`` are used instead of the
standard increment and decrement operators, and the lock is no longer
used to protect the reference count itself.


.. code-block:: c

    --- cache.c.refcnt  2003-12-09 15:00:35.000000000 +1100
    +++ cache.c.refcnt-atomic   2003-12-11 15:49:42.000000000 +1100
    @@ -7,7 +7,7 @@
     struct object
     {
             struct list_head list;
    -        unsigned int refcnt;
    +        atomic_t refcnt;
             int id;
             char name[32];
             int popularity;
    @@ -18,33 +18,15 @@
     static unsigned int cache_num = 0;
     #define MAX_CACHE_SIZE 10

    -static void __object_put(struct object *obj)
    -{
    -        if (--obj->refcnt == 0)
    -                kfree(obj);
    -}
    -
    -static void __object_get(struct object *obj)
    -{
    -        obj->refcnt++;
    -}
    -
     void object_put(struct object *obj)
     {
    -        unsigned long flags;
    -
    -        spin_lock_irqsave(&cache_lock, flags);
    -        __object_put(obj);
    -        spin_unlock_irqrestore(&cache_lock, flags);
    +        if (atomic_dec_and_test(&obj->refcnt))
    +                kfree(obj);
     }

     void object_get(struct object *obj)
     {
    -        unsigned long flags;
    -
    -        spin_lock_irqsave(&cache_lock, flags);
    -        __object_get(obj);
    -        spin_unlock_irqrestore(&cache_lock, flags);
    +        atomic_inc(&obj->refcnt);
     }

     /* Must be holding cache_lock */
    @@ -65,7 +47,7 @@
     {
             BUG_ON(!obj);
             list_del(&obj->list);
    -        __object_put(obj);
    +        object_put(obj);
             cache_num--;
     }

    @@ -94,7 +76,7 @@
             strlcpy(obj->name, name, sizeof(obj->name));
             obj->id = id;
             obj->popularity = 0;
    -        obj->refcnt = 1; /* The cache holds a reference */
    +        atomic_set(&obj->refcnt, 1); /* The cache holds a reference */

             spin_lock_irqsave(&cache_lock, flags);
             __cache_add(obj);
    @@ -119,7 +101,7 @@
             spin_lock_irqsave(&cache_lock, flags);
             obj = __cache_find(id);
             if (obj)
    -                __object_get(obj);
    +                object_get(obj);
             spin_unlock_irqrestore(&cache_lock, flags);
             return obj;
     }


.. _examples-lock-per-obj:

Protecting The Objects Themselves
=================================

In these examples, we assumed that the objects (except the reference
counts) never changed once they are created. If we wanted to allow the
name to change, there are three possibilities:

-  You can make ``cache_lock`` non-static, and tell people to grab that
   lock before changing the name in any object.

-  You can provide a ``cache_obj_rename`` which grabs this lock and
   changes the name for the caller, and tell everyone to use that
   function.

-  You can make the ``cache_lock`` protect only the cache itself, and
   use another lock to protect the name.

Theoretically, you can make the locks as fine-grained as one lock for
every field, for every object. In practice, the most common variants
are:

-  One lock which protects the infrastructure (the ``cache`` list in
   this example) and all the objects. This is what we have done so far.

-  One lock which protects the infrastructure (including the list
   pointers inside the objects), and one lock inside the object which
   protects the rest of that object.

-  Multiple locks to protect the infrastructure (eg. one lock per hash
   chain), possibly with a separate per-object lock.

Here is the "lock-per-object" implementation:


.. code-block:: c

    --- cache.c.refcnt-atomic   2003-12-11 15:50:54.000000000 +1100
    +++ cache.c.perobjectlock   2003-12-11 17:15:03.000000000 +1100
    @@ -6,11 +6,17 @@

     struct object
     {
    +        /* These two protected by cache_lock. */
             struct list_head list;
    +        int popularity;
    +
             atomic_t refcnt;
    +
    +        /* Doesn't change once created. */
             int id;
    +
    +        spinlock_t lock; /* Protects the name */
             char name[32];
    -        int popularity;
     };

     static DEFINE_SPINLOCK(cache_lock);
    @@ -77,6 +84,7 @@
             obj->id = id;
             obj->popularity = 0;
             atomic_set(&obj->refcnt, 1); /* The cache holds a reference */
    +        spin_lock_init(&obj->lock);

             spin_lock_irqsave(&cache_lock, flags);
             __cache_add(obj);

Note that I decide that the ``popularity`` count should be protected by
the ``cache_lock`` rather than the per-object lock: this is because it
(like the ``struct list_head`` inside the object) is logically part of
the infrastructure. This way, I don't need to grab the lock of every
object in ``__cache_add`` when seeking the least popular.

I also decided that the ``id`` member is unchangeable, so I don't need
to grab each object lock in ``__cache_find()`` to examine the ``id``:
the object lock is only used by a caller who wants to read or write the
``name`` field.

Note also that I added a comment describing what data was protected by
which locks. This is extremely important, as it describes the runtime
behavior of the code, and can be hard to gain from just reading. And as
Alan Cox says, “Lock data, not code”.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
