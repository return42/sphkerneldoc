
.. _API-unqueue-me:

==========
unqueue_me
==========

*man unqueue_me(9)*

*4.6.0-rc1*

Remove the futex_q from its futex_hash_bucket


Synopsis
========

.. c:function:: int unqueue_me( struct futex_q * q )

Arguments
=========

``q``
    The futex_q to unqueue


Description
===========

The q->lock_ptr must not be held by the caller. A call to ``unqueue_me`` must be paired with exactly one earlier call to ``queue_me``.


Return
======

1 - if the futex_q was still queued (and we removed unqueued it); 0 - if the futex_q was already removed by the waking thread
