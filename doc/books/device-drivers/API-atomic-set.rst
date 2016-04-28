.. -*- coding: utf-8; mode: rst -*-

.. _API-atomic-set:

==========
atomic_set
==========

*man atomic_set(9)*

*4.6.0-rc5*

set atomic variable


Synopsis
========

.. c:function:: void atomic_set( atomic_t * v, int i )

Arguments
=========

``v``
    pointer of type atomic_t

``i``
    required value


Description
===========

Atomically sets the value of ``v`` to ``i``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
