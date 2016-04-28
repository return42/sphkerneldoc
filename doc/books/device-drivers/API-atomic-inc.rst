.. -*- coding: utf-8; mode: rst -*-

.. _API-atomic-inc:

==========
atomic_inc
==========

*man atomic_inc(9)*

*4.6.0-rc5*

increment atomic variable


Synopsis
========

.. c:function:: void atomic_inc( atomic_t * v )

Arguments
=========

``v``
    pointer of type atomic_t


Description
===========

Atomically increments ``v`` by 1.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
