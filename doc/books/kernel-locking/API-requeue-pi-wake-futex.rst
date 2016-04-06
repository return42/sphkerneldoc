
.. _API-requeue-pi-wake-futex:

=====================
requeue_pi_wake_futex
=====================

*man requeue_pi_wake_futex(9)*

*4.6.0-rc1*

Wake a task that acquired the lock during requeue


Synopsis
========

.. c:function:: void requeue_pi_wake_futex( struct futex_q * q, union futex_key * key, struct futex_hash_bucket * hb )

Arguments
=========

``q``
    the futex_q

``key``
    the key of the requeue target futex

``hb``
    the hash_bucket of the requeue target futex


Description
===========

During futex_requeue, with requeue_pi=1, it is possible to acquire the target futex if it is uncontended or via a lock steal. Set the futex_q key to the requeue target futex so
the waiter can detect the wakeup on the right futex, but remove it from the hb and NULL the rt_waiter so it can detect atomic lock acquisition. Set the q->lock_ptr to the requeue
target hb->lock to protect access to the pi_state to fixup the owner later. Must be called with both q->lock_ptr and hb->lock held.
