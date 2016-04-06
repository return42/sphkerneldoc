
.. _common-problems:

===============
Common Problems
===============


.. _deadlock:

Deadlock: Simple and Advanced
=============================

There is a coding bug where a piece of code tries to grab a spinlock twice: it will spin forever, waiting for the lock to be released (spinlocks, rwlocks and mutexes are not
recursive in Linux). This is trivial to diagnose: not a stay-up-five-nights-talk-to-fluffy-code-bunnies kind of problem.

For a slightly more complex case, imagine you have a region shared by a softirq and user context. If you use a ``spin_lock()`` call to protect it, it is possible that the user
context will be interrupted by the softirq while it holds the lock, and the softirq will then spin forever trying to get the same lock.

Both of these are called deadlock, and as shown above, it can occur even with a single CPU (although not on UP compiles, since spinlocks vanish on kernel compiles with
``CONFIG_SMP``\ =n. You'll still get data corruption in the second example).

This complete lockup is easy to diagnose: on SMP boxes the watchdog timer or compiling with ``DEBUG_SPINLOCK`` set (``include/linux/spinlock.h``) will show this up immediately when
it happens.

A more complex problem is the so-called 'deadly embrace', involving two or more locks. Say you have a hash table: each entry in the table is a spinlock, and a chain of hashed
objects. Inside a softirq handler, you sometimes want to alter an object from one place in the hash to another: you grab the spinlock of the old hash chain and the spinlock of the
new hash chain, and delete the object from the old one, and insert it in the new one.

There are two problems here. First, if your code ever tries to move the object to the same chain, it will deadlock with itself as it tries to lock it twice. Secondly, if the same
softirq on another CPU is trying to move another object in the reverse direction, the following could happen:



.. table:: Consequences

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | CPU 1                                                                                      | CPU 2                                                                                      |
    +============================================================================================+============================================================================================+
    | Grab lock A -> OK                                                                          | Grab lock B -> OK                                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | Grab lock B -> spin                                                                        | Grab lock A -> spin                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


The two CPUs will spin forever, waiting for the other to give up their lock. It will look, smell, and feel like a crash.


.. _techs-deadlock-prevent:

Preventing Deadlock
===================

Textbooks will tell you that if you always lock in the same order, you will never get this kind of deadlock. Practice will tell you that this approach doesn't scale: when I create
a new lock, I don't understand enough of the kernel to figure out where in the 5000 lock hierarchy it will fit.

The best locks are encapsulated: they never get exposed in headers, and are never held around calls to non-trivial functions outside the same file. You can read through this code
and see that it will never deadlock, because it never tries to grab another lock while it has that one. People using your code don't even need to know you are using a lock.

A classic problem here is when you provide callbacks or hooks: if you call these with the lock held, you risk simple deadlock, or a deadly embrace (who knows what the callback will
do?). Remember, the other programmers are out to get you, so don't do this.


.. _techs-deadlock-overprevent:

Overzealous Prevention Of Deadlocks
===================================

Deadlocks are problematic, but not as bad as data corruption. Code which grabs a read lock, searches a list, fails to find what it wants, drops the read lock, grabs a write lock
and inserts the object has a race condition.

If you don't see why, please stay the fuck away from my code.


.. _racing-timers:

Racing Timers: A Kernel Pastime
===============================

Timers can produce their own special problems with races. Consider a collection of objects (list, hash, etc) where each object has a timer which is due to destroy it.

If you want to destroy the entire collection (say on module removal), you might do the following:


.. code-block:: c

            /* THIS CODE BAD BAD BAD BAD: IF IT WAS ANY WORSE IT WOULD USE
               HUNGARIAN NOTATION */
            spin_lock_bh(&list_lock);

            while (list) {
                    struct foo *next = list->next;
                    del_timer(&list->timer);
                    kfree(list);
                    list = next;
            }

            spin_unlock_bh(&list_lock);

Sooner or later, this will crash on SMP, because a timer can have just gone off before the ``spin_lock_bh()``, and it will only get the lock after we ``spin_unlock_bh()``, and then
try to free the element (which has already been freed!).

This can be avoided by checking the result of ``del_timer()``: if it returns 1, the timer has been deleted. If 0, it means (in this case) that it is currently running, so we can
do:


.. code-block:: c

            retry:
                    spin_lock_bh(&list_lock);

                    while (list) {
                            struct foo *next = list->next;
                            if (!del_timer(&list->timer)) {
                                    /* Give timer a chance to delete this */
                                    spin_unlock_bh(&list_lock);
                                    goto retry;
                            }
                            kfree(list);
                            list = next;
                    }

                    spin_unlock_bh(&list_lock);

Another common problem is deleting timers which restart themselves (by calling ``add_timer()`` at the end of their timer function). Because this is a fairly common case which is
prone to races, you should use ``del_timer_sync()`` (``include/linux/timer.h``) to handle this case. It returns the number of times the timer had to be deleted before we finally
stopped it from adding itself back in.
