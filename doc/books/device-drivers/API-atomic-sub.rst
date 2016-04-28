.. -*- coding: utf-8; mode: rst -*-

.. _API-atomic-sub:

==========
atomic_sub
==========

*man atomic_sub(9)*

*4.6.0-rc5*

subtract integer from atomic variable


Synopsis
========

.. c:function:: void atomic_sub( int i, atomic_t * v )

Arguments
=========

``i``
    integer value to subtract

``v``
    pointer of type atomic_t


Description
===========

Atomically subtracts ``i`` from ``v``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
