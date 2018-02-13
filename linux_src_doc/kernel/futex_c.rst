.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/futex.c

.. _`futex_q`:

struct futex_q
==============

.. c:type:: struct futex_q

    The hashed futex queue entry, one per waiting task

.. _`futex_q.definition`:

Definition
----------

.. code-block:: c

    struct futex_q {
        struct plist_node list;
        struct task_struct *task;
        spinlock_t *lock_ptr;
        union futex_key key;
        struct futex_pi_state *pi_state;
        struct rt_mutex_waiter *rt_waiter;
        union futex_key *requeue_pi_key;
        u32 bitset;
    }

.. _`futex_q.members`:

Members
-------

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

.. _`futex_q.description`:

Description
-----------

We use this hashed waitqueue, instead of a normal wait_queue_entry_t, so
we can wake only the relevant ones (hashed queues may be shared).

A futex_q has a woken state, just like tasks have TASK_RUNNING.
It is considered woken when plist_node_empty(&q->list) || q->lock_ptr == 0.
The order of wakeup is always to make the first condition true, then
the second.

PI futexes are typically woken before they are removed from the hash list via
the rt_mutex code. See \ :c:func:`unqueue_me_pi`\ .

.. _`hash_futex`:

hash_futex
==========

.. c:function:: struct futex_hash_bucket *hash_futex(union futex_key *key)

    Return the hash bucket in the global hash

    :param union futex_key \*key:
        Pointer to the futex key for which the hash is calculated

.. _`hash_futex.description`:

Description
-----------

We hash on the keys returned from get_futex_key (see below) and return the
corresponding hash bucket in the global hash.

.. _`match_futex`:

match_futex
===========

.. c:function:: int match_futex(union futex_key *key1, union futex_key *key2)

    Check whether two futex keys are equal

    :param union futex_key \*key1:
        Pointer to key1

    :param union futex_key \*key2:
        Pointer to key2

.. _`match_futex.description`:

Description
-----------

Return 1 if two futex_keys are equal, 0 otherwise.

.. _`get_futex_key`:

get_futex_key
=============

.. c:function:: int get_futex_key(u32 __user *uaddr, int fshared, union futex_key *key, int rw)

    Get parameters which are the keys for a futex

    :param u32 __user \*uaddr:
        virtual address of the futex

    :param int fshared:
        0 for a PROCESS_PRIVATE futex, 1 for PROCESS_SHARED

    :param union futex_key \*key:
        address where result is stored.

    :param int rw:
        mapping needs to be read/write (values: VERIFY_READ,
        VERIFY_WRITE)

.. _`get_futex_key.return`:

Return
------

a negative error code or 0

The key words are stored in \ ``key``\  on success.

For shared mappings, it's (page->index, file_inode(vma->vm_file),
offset_within_page).  For private mappings, it's (uaddr, current->mm).
We can usually work out the index without swapping in the page.

\ :c:func:`lock_page`\  might sleep, the caller should not hold a spinlock.

.. _`fault_in_user_writeable`:

fault_in_user_writeable
=======================

.. c:function:: int fault_in_user_writeable(u32 __user *uaddr)

    Fault in user address and verify RW access

    :param u32 __user \*uaddr:
        pointer to faulting user space address

.. _`fault_in_user_writeable.description`:

Description
-----------

Slow path to fixup the fault we just took in the atomic write
access to \ ``uaddr``\ .

We have no generic implementation of a non-destructive write to the
user address. We know that we faulted in the atomic pagefault
disabled section so we can as well avoid the #PF overhead by
calling \ :c:func:`get_user_pages`\  right away.

.. _`futex_top_waiter`:

futex_top_waiter
================

.. c:function:: struct futex_q *futex_top_waiter(struct futex_hash_bucket *hb, union futex_key *key)

    Return the highest priority waiter on a futex

    :param struct futex_hash_bucket \*hb:
        the hash bucket the futex_q's reside in

    :param union futex_key \*key:
        the futex key (to distinguish it from other futex futex_q's)

.. _`futex_top_waiter.description`:

Description
-----------

Must be called with the hb lock held.

.. _`futex_lock_pi_atomic`:

futex_lock_pi_atomic
====================

.. c:function:: int futex_lock_pi_atomic(u32 __user *uaddr, struct futex_hash_bucket *hb, union futex_key *key, struct futex_pi_state **ps, struct task_struct *task, int set_waiters)

    Atomic work required to acquire a pi aware futex

    :param u32 __user \*uaddr:
        the pi futex user address

    :param struct futex_hash_bucket \*hb:
        the pi futex hash bucket

    :param union futex_key \*key:
        the futex key associated with uaddr and hb

    :param struct futex_pi_state \*\*ps:
        the pi_state pointer where we store the result of the
        lookup

    :param struct task_struct \*task:
        the task to perform the atomic lock work for.  This will
        be "current" except in the case of requeue pi.

    :param int set_waiters:
        force setting the FUTEX_WAITERS bit (1) or not (0)

.. _`futex_lock_pi_atomic.return`:

Return
------

 -  0 - ready to wait;
 -  1 - acquired the lock;
 - <0 - error

The hb->lock and futex_key refs shall be held by the caller.

.. _`__unqueue_futex`:

__unqueue_futex
===============

.. c:function:: void __unqueue_futex(struct futex_q *q)

    Remove the futex_q from its futex_hash_bucket

    :param struct futex_q \*q:
        The futex_q to unqueue

.. _`__unqueue_futex.description`:

Description
-----------

The q->lock_ptr must not be NULL and must be held by the caller.

.. _`requeue_futex`:

requeue_futex
=============

.. c:function:: void requeue_futex(struct futex_q *q, struct futex_hash_bucket *hb1, struct futex_hash_bucket *hb2, union futex_key *key2)

    Requeue a futex_q from one hb to another

    :param struct futex_q \*q:
        the futex_q to requeue

    :param struct futex_hash_bucket \*hb1:
        the source hash_bucket

    :param struct futex_hash_bucket \*hb2:
        the target hash_bucket

    :param union futex_key \*key2:
        the new key for the requeued futex_q

.. _`requeue_pi_wake_futex`:

requeue_pi_wake_futex
=====================

.. c:function:: void requeue_pi_wake_futex(struct futex_q *q, union futex_key *key, struct futex_hash_bucket *hb)

    Wake a task that acquired the lock during requeue

    :param struct futex_q \*q:
        the futex_q

    :param union futex_key \*key:
        the key of the requeue target futex

    :param struct futex_hash_bucket \*hb:
        the hash_bucket of the requeue target futex

.. _`requeue_pi_wake_futex.description`:

Description
-----------

During futex_requeue, with requeue_pi=1, it is possible to acquire the
target futex if it is uncontended or via a lock steal.  Set the futex_q key
to the requeue target futex so the waiter can detect the wakeup on the right
futex, but remove it from the hb and NULL the rt_waiter so it can detect
atomic lock acquisition.  Set the q->lock_ptr to the requeue target hb->lock
to protect access to the pi_state to fixup the owner later.  Must be called
with both q->lock_ptr and hb->lock held.

.. _`futex_proxy_trylock_atomic`:

futex_proxy_trylock_atomic
==========================

.. c:function:: int futex_proxy_trylock_atomic(u32 __user *pifutex, struct futex_hash_bucket *hb1, struct futex_hash_bucket *hb2, union futex_key *key1, union futex_key *key2, struct futex_pi_state **ps, int set_waiters)

    Attempt an atomic lock for the top waiter

    :param u32 __user \*pifutex:
        the user address of the to futex

    :param struct futex_hash_bucket \*hb1:
        the from futex hash bucket, must be locked by the caller

    :param struct futex_hash_bucket \*hb2:
        the to futex hash bucket, must be locked by the caller

    :param union futex_key \*key1:
        the from futex key

    :param union futex_key \*key2:
        the to futex key

    :param struct futex_pi_state \*\*ps:
        address to store the pi_state pointer

    :param int set_waiters:
        force setting the FUTEX_WAITERS bit (1) or not (0)

.. _`futex_proxy_trylock_atomic.description`:

Description
-----------

Try and get the lock on behalf of the top waiter if we can do it atomically.
Wake the top waiter if we succeed.  If the caller specified set_waiters,
then direct \ :c:func:`futex_lock_pi_atomic`\  to force setting the FUTEX_WAITERS bit.
hb1 and hb2 must be held by the caller.

.. _`futex_proxy_trylock_atomic.return`:

Return
------

 -  0 - failed to acquire the lock atomically;
 - >0 - acquired the lock, return value is vpid of the top_waiter
 - <0 - error

.. _`futex_requeue`:

futex_requeue
=============

.. c:function:: int futex_requeue(u32 __user *uaddr1, unsigned int flags, u32 __user *uaddr2, int nr_wake, int nr_requeue, u32 *cmpval, int requeue_pi)

    Requeue waiters from uaddr1 to uaddr2

    :param u32 __user \*uaddr1:
        source futex user address

    :param unsigned int flags:
        futex flags (FLAGS_SHARED, etc.)

    :param u32 __user \*uaddr2:
        target futex user address

    :param int nr_wake:
        number of waiters to wake (must be 1 for requeue_pi)

    :param int nr_requeue:
        number of waiters to requeue (0-INT_MAX)

    :param u32 \*cmpval:
        \ ``uaddr1``\  expected value (or \ ``NULL``\ )

    :param int requeue_pi:
        if we are attempting to requeue from a non-pi futex to a
        pi futex (pi to pi requeue is not supported)

.. _`futex_requeue.description`:

Description
-----------

Requeue waiters on uaddr1 to uaddr2. In the requeue_pi case, try to acquire
uaddr2 atomically on behalf of the top waiter.

.. _`futex_requeue.return`:

Return
------

 - >=0 - on success, the number of tasks requeued or woken;
 -  <0 - on error

.. _`queue_me`:

queue_me
========

.. c:function:: void queue_me(struct futex_q *q, struct futex_hash_bucket *hb)

    Enqueue the futex_q on the futex_hash_bucket

    :param struct futex_q \*q:
        The futex_q to enqueue

    :param struct futex_hash_bucket \*hb:
        The destination hash bucket

.. _`queue_me.description`:

Description
-----------

The hb->lock must be held by the caller, and is released here. A call to
\ :c:func:`queue_me`\  is typically paired with exactly one call to \ :c:func:`unqueue_me`\ .  The
exceptions involve the PI related operations, which may use \ :c:func:`unqueue_me_pi`\ 
or nothing if the unqueue is done as part of the wake process and the unqueue
state is implicit in the state of woken task (see \ :c:func:`futex_wait_requeue_pi`\  for
an example).

.. _`unqueue_me`:

unqueue_me
==========

.. c:function:: int unqueue_me(struct futex_q *q)

    Remove the futex_q from its futex_hash_bucket

    :param struct futex_q \*q:
        The futex_q to unqueue

.. _`unqueue_me.description`:

Description
-----------

The q->lock_ptr must not be held by the caller. A call to \ :c:func:`unqueue_me`\  must
be paired with exactly one earlier call to \ :c:func:`queue_me`\ .

.. _`unqueue_me.return`:

Return
------

 - 1 - if the futex_q was still queued (and we removed unqueued it);
 - 0 - if the futex_q was already removed by the waking thread

.. _`fixup_owner`:

fixup_owner
===========

.. c:function:: int fixup_owner(u32 __user *uaddr, struct futex_q *q, int locked)

    Post lock pi_state and corner case management

    :param u32 __user \*uaddr:
        user address of the futex

    :param struct futex_q \*q:
        futex_q (contains pi_state and access to the rt_mutex)

    :param int locked:
        if the attempt to take the rt_mutex succeeded (1) or not (0)

.. _`fixup_owner.description`:

Description
-----------

After attempting to lock an rt_mutex, this function is called to cleanup
the pi_state owner as well as handle race conditions that may allow us to
acquire the lock. Must be called with the hb lock held.

.. _`fixup_owner.return`:

Return
------

 -  1 - success, lock taken;
 -  0 - success, lock not taken;
 - <0 - on error (-EFAULT)

.. _`futex_wait_queue_me`:

futex_wait_queue_me
===================

.. c:function:: void futex_wait_queue_me(struct futex_hash_bucket *hb, struct futex_q *q, struct hrtimer_sleeper *timeout)

    \ :c:func:`queue_me`\  and wait for wakeup, timeout, or signal

    :param struct futex_hash_bucket \*hb:
        the futex hash bucket, must be locked by the caller

    :param struct futex_q \*q:
        the futex_q to queue up on

    :param struct hrtimer_sleeper \*timeout:
        the prepared hrtimer_sleeper, or null for no timeout

.. _`futex_wait_setup`:

futex_wait_setup
================

.. c:function:: int futex_wait_setup(u32 __user *uaddr, u32 val, unsigned int flags, struct futex_q *q, struct futex_hash_bucket **hb)

    Prepare to wait on a futex

    :param u32 __user \*uaddr:
        the futex userspace address

    :param u32 val:
        the expected value

    :param unsigned int flags:
        futex flags (FLAGS_SHARED, etc.)

    :param struct futex_q \*q:
        the associated futex_q

    :param struct futex_hash_bucket \*\*hb:
        storage for hash_bucket pointer to be returned to caller

.. _`futex_wait_setup.description`:

Description
-----------

Setup the futex_q and locate the hash_bucket.  Get the futex value and
compare it with the expected value.  Handle atomic faults internally.
Return with the hb lock held and a q.key reference on success, and unlocked
with no q.key reference on failure.

.. _`futex_wait_setup.return`:

Return
------

 -  0 - uaddr contains val and hb has been locked;
 - <1 - -EFAULT or -EWOULDBLOCK (uaddr does not contain val) and hb is unlocked

.. _`handle_early_requeue_pi_wakeup`:

handle_early_requeue_pi_wakeup
==============================

.. c:function:: int handle_early_requeue_pi_wakeup(struct futex_hash_bucket *hb, struct futex_q *q, union futex_key *key2, struct hrtimer_sleeper *timeout)

    Detect early wakeup on the initial futex

    :param struct futex_hash_bucket \*hb:
        the hash_bucket futex_q was original enqueued on

    :param struct futex_q \*q:
        the futex_q woken while waiting to be requeued

    :param union futex_key \*key2:
        the futex_key of the requeue target futex

    :param struct hrtimer_sleeper \*timeout:
        the timeout associated with the wait (NULL if none)

.. _`handle_early_requeue_pi_wakeup.description`:

Description
-----------

Detect if the task was woken on the initial futex as opposed to the requeue
target futex.  If so, determine if it was a timeout or a signal that caused
the wakeup and return the appropriate error code to the caller.  Must be
called with the hb lock held.

.. _`handle_early_requeue_pi_wakeup.return`:

Return
------

 -  0 = no early wakeup detected;
 - <0 = -ETIMEDOUT or -ERESTARTNOINTR

.. _`futex_wait_requeue_pi`:

futex_wait_requeue_pi
=====================

.. c:function:: int futex_wait_requeue_pi(u32 __user *uaddr, unsigned int flags, u32 val, ktime_t *abs_time, u32 bitset, u32 __user *uaddr2)

    Wait on uaddr and take uaddr2

    :param u32 __user \*uaddr:
        the futex we initially wait on (non-pi)

    :param unsigned int flags:
        futex flags (FLAGS_SHARED, FLAGS_CLOCKRT, etc.), they must be
        the same type, no requeueing from private to shared, etc.

    :param u32 val:
        the expected value of uaddr

    :param ktime_t \*abs_time:
        absolute timeout

    :param u32 bitset:
        32 bit wakeup bitset set by userspace, defaults to all

    :param u32 __user \*uaddr2:
        the pi futex we will take prior to returning to user-space

.. _`futex_wait_requeue_pi.description`:

Description
-----------

The caller will wait on uaddr and will be requeued by \ :c:func:`futex_requeue`\  to
uaddr2 which must be PI aware and unique from uaddr.  Normal wakeup will wake
on uaddr2 and complete the acquisition of the rt_mutex prior to returning to
userspace.  This ensures the rt_mutex maintains an owner when it has waiters;
without one, the pi logic would not know which task to boost/deboost, if
there was a need to.

We call schedule in \ :c:func:`futex_wait_queue_me`\  when we enqueue and return there
via the following--
1) wakeup on uaddr2 after an atomic lock acquisition by \ :c:func:`futex_requeue`\ 
2) wakeup on uaddr2 after a requeue
3) signal
4) timeout

If 3, cleanup and return -ERESTARTNOINTR.

If 2, we may then block on trying to take the rt_mutex and return via:
5) successful lock
6) signal
7) timeout
8) other lock acquisition failure

If 6, return -EWOULDBLOCK (restarting the syscall would do the same).

If 4 or 7, we cleanup and return with -ETIMEDOUT.

.. _`futex_wait_requeue_pi.return`:

Return
------

 -  0 - On success;
 - <0 - On error

.. _`sys_set_robust_list`:

sys_set_robust_list
===================

.. c:function:: long sys_set_robust_list(struct robust_list_head __user *head, size_t len)

    Set the robust-futex list head of a task

    :param struct robust_list_head __user \*head:
        pointer to the list-head

    :param size_t len:
        length of the list-head, as userspace expects

.. _`sys_get_robust_list`:

sys_get_robust_list
===================

.. c:function:: long sys_get_robust_list(int pid, struct robust_list_head __user * __user *head_ptr, size_t __user *len_ptr)

    Get the robust-futex list head of a task

    :param int pid:
        pid of the process [zero for current task]

    :param struct robust_list_head __user \* __user \*head_ptr:
        pointer to a list-head pointer, the kernel fills it in

    :param size_t __user \*len_ptr:
        pointer to a length field, the kernel fills in the header size

.. This file was automatic generated / don't edit.

