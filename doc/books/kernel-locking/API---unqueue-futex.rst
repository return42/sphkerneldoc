.. -*- coding: utf-8; mode: rst -*-

.. _API---unqueue-futex:

===============
__unqueue_futex
===============

*man __unqueue_futex(9)*

*4.6.0-rc5*

Remove the futex_q from its futex_hash_bucket


Synopsis
========

.. c:function:: void __unqueue_futex( struct futex_q * q )

Arguments
=========

``q``
    The futex_q to unqueue


Description
===========

The q->lock_ptr must not be NULL and must be held by the caller.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
