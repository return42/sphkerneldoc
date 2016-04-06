
.. _API-struct-fence:

============
struct fence
============

*man struct fence(9)*

*4.6.0-rc1*

software synchronization primitive


Synopsis
========

.. code-block:: c

    struct fence {
      struct kref refcount;
      const struct fence_ops * ops;
      struct rcu_head rcu;
      struct list_head cb_list;
      spinlock_t * lock;
      unsigned context;
      unsigned seqno;
      unsigned long flags;
      ktime_t timestamp;
      int status;
    };


Members
=======

refcount
    refcount for this fence

ops
    fence_ops associated with this fence

rcu
    used for releasing fence with kfree_rcu

cb_list
    list of all callbacks to call

lock
    spin_lock_irqsave used for locking

context
    execution context this fence belongs to, returned by ``fence_context_alloc``

seqno
    the sequence number of this fence inside the execution context, can be compared to decide which fence would be signaled later.

flags
    A mask of FENCE_FLAG_⋆ defined below

timestamp
    Timestamp when the fence was signaled.

status
    Optional, only valid if < 0, must be set before calling fence_signal, indicates that the fence has completed with an error.


Description
===========

the flags member must be manipulated and read using the appropriate atomic ops (bit_⋆), so taking the spinlock will not be needed most of the time.

FENCE_FLAG_SIGNALED_BIT - fence is already signaled FENCE_FLAG_ENABLE_SIGNAL_BIT - enable_signaling might have been called⋆ FENCE_FLAG_USER_BITS - start of the unused
bits, can be used by the implementer of the fence for its own purposes. Can be used in different ways by different fence implementers, so do not rely on this.

⋆) Since atomic bitops are used, this is not guaranteed to be the case. Particularly, if the bit was set, but fence_signal was called right before this bit was set, it would have
been able to set the FENCE_FLAG_SIGNALED_BIT, before enable_signaling was called. Adding a check for FENCE_FLAG_SIGNALED_BIT after setting FENCE_FLAG_ENABLE_SIGNAL_BIT
closes this race, and makes sure that after fence_signal was called, any enable_signaling call will have either been completed, or never called at all.
