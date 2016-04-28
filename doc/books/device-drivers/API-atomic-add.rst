.. -*- coding: utf-8; mode: rst -*-

.. _API-atomic-add:

==========
atomic_add
==========

*man atomic_add(9)*

*4.6.0-rc5*

add integer to atomic variable


Synopsis
========

.. c:function:: void atomic_add( int i, atomic_t * v )

Arguments
=========

``i``
    integer value to add

``v``
    pointer of type atomic_t


Description
===========

Atomically adds ``i`` to ``v``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
