
.. _API-futex-wait-queue-me:

===================
futex_wait_queue_me
===================

*man futex_wait_queue_me(9)*

*4.6.0-rc1*

``queue_me`` and wait for wakeup, timeout, or signal


Synopsis
========

.. c:function:: void futex_wait_queue_me( struct futex_hash_bucket * hb, struct futex_q * q, struct hrtimer_sleeper * timeout )

Arguments
=========

``hb``
    the futex hash bucket, must be locked by the caller

``q``
    the futex_q to queue up on

``timeout``
    the prepared hrtimer_sleeper, or null for no timeout
