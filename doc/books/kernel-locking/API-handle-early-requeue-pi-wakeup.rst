
.. _API-handle-early-requeue-pi-wakeup:

==============================
handle_early_requeue_pi_wakeup
==============================

*man handle_early_requeue_pi_wakeup(9)*

*4.6.0-rc1*

Detect early wakeup on the initial futex


Synopsis
========

.. c:function:: int handle_early_requeue_pi_wakeup( struct futex_hash_bucket * hb, struct futex_q * q, union futex_key * key2, struct hrtimer_sleeper * timeout )

Arguments
=========

``hb``
    the hash_bucket futex_q was original enqueued on

``q``
    the futex_q woken while waiting to be requeued

``key2``
    the futex_key of the requeue target futex

``timeout``
    the timeout associated with the wait (NULL if none)


Description
===========

Detect if the task was woken on the initial futex as opposed to the requeue target futex. If so, determine if it was a timeout or a signal that caused the wakeup and return the
appropriate error code to the caller. Must be called with the hb lock held.


Return
======

0 = no early wakeup detected; <0 = -ETIMEDOUT or -ERESTARTNOINTR
