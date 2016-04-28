.. -*- coding: utf-8; mode: rst -*-

.. _API-atomic-dec:

==========
atomic_dec
==========

*man atomic_dec(9)*

*4.6.0-rc5*

decrement atomic variable


Synopsis
========

.. c:function:: void atomic_dec( atomic_t * v )

Arguments
=========

``v``
    pointer of type atomic_t


Description
===========

Atomically decrements ``v`` by 1.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
