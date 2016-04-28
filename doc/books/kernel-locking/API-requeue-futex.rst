.. -*- coding: utf-8; mode: rst -*-

.. _API-requeue-futex:

=============
requeue_futex
=============

*man requeue_futex(9)*

*4.6.0-rc5*

Requeue a futex_q from one hb to another


Synopsis
========

.. c:function:: void requeue_futex( struct futex_q * q, struct futex_hash_bucket * hb1, struct futex_hash_bucket * hb2, union futex_key * key2 )

Arguments
=========

``q``
    the futex_q to requeue

``hb1``
    the source hash_bucket

``hb2``
    the target hash_bucket

``key2``
    the new key for the requeued futex_q


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
