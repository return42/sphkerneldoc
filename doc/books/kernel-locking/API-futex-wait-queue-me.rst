.. -*- coding: utf-8; mode: rst -*-

.. _API-futex-wait-queue-me:

===================
futex_wait_queue_me
===================

*man futex_wait_queue_me(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
