.. -*- coding: utf-8; mode: rst -*-

.. _API-queue-me:

========
queue_me
========

*man queue_me(9)*

*4.6.0-rc5*

Enqueue the futex_q on the futex_hash_bucket


Synopsis
========

.. c:function:: void queue_me( struct futex_q * q, struct futex_hash_bucket * hb )

Arguments
=========

``q``
    The futex_q to enqueue

``hb``
    The destination hash bucket


Description
===========

The hb->lock must be held by the caller, and is released here. A call to
``queue_me`` is typically paired with exactly one call to
``unqueue_me``. The exceptions involve the PI related operations, which
may use ``unqueue_me_pi`` or nothing if the unqueue is done as part of
the wake process and the unqueue state is implicit in the state of woken
task (see ``futex_wait_requeue_pi`` for an example).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
