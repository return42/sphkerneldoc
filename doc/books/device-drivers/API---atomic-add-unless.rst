.. -*- coding: utf-8; mode: rst -*-

.. _API---atomic-add-unless:

===================
__atomic_add_unless
===================

*man __atomic_add_unless(9)*

*4.6.0-rc5*

add unless the number is already a given value


Synopsis
========

.. c:function:: int __atomic_add_unless( atomic_t * v, int a, int u )

Arguments
=========

``v``
    pointer of type atomic_t

``a``
    the amount to add to v...

``u``
    ...unless v is equal to u.


Description
===========

Atomically adds ``a`` to ``v``, so long as ``v`` was not already ``u``.
Returns the old value of ``v``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
