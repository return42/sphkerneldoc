
.. _API-struct-futex-q:

==============
struct futex_q
==============

*man struct futex_q(9)*

*4.6.0-rc1*

The hashed futex queue entry, one per waiting task


Synopsis
========

.. code-block:: c

    struct futex_q {
      struct plist_node list;
      struct task_struct * task;
      spinlock_t * lock_ptr;
      union futex_key key;
      struct futex_pi_state * pi_state;
      struct rt_mutex_waiter * rt_waiter;
      union futex_key * requeue_pi_key;
      u32 bitset;
    };


Members
=======

list
    priority-sorted list of tasks waiting on this futex

task
    the task waiting on the futex

lock_ptr
    the hash bucket lock

key
    the key the futex is hashed on

pi_state
    optional priority inheritance state

rt_waiter
    rt_waiter storage for use with requeue_pi

requeue_pi_key
    the requeue_pi target futex key

bitset
    bitset for the optional bitmasked wakeup


Description
===========

We use this hashed waitqueue, instead of a normal wait_queue_t, so we can wake only the relevant ones (hashed queues may be shared).

A futex_q has a woken state, just like tasks have TASK_RUNNING. It is considered woken when plist_node_empty( ``q``->list) || q->lock_ptr == 0. The order of wakeup is
always to make the first condition true, then the second.

PI futexes are typically woken before they are removed from the hash list via the rt_mutex code. See ``unqueue_me_pi``.
