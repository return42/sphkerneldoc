.. -*- coding: utf-8; mode: rst -*-

.. _API-atomic-add-negative:

===================
atomic_add_negative
===================

*man atomic_add_negative(9)*

*4.6.0-rc5*

add and test if negative


Synopsis
========

.. c:function:: int atomic_add_negative( int i, atomic_t * v )

Arguments
=========

``i``
    integer value to add

``v``
    pointer of type atomic_t


Description
===========

Atomically adds ``i`` to ``v`` and returns true if the result is
negative, or false when result is greater than or equal to zero.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
