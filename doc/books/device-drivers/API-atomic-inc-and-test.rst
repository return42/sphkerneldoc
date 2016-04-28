.. -*- coding: utf-8; mode: rst -*-

.. _API-atomic-inc-and-test:

===================
atomic_inc_and_test
===================

*man atomic_inc_and_test(9)*

*4.6.0-rc5*

increment and test


Synopsis
========

.. c:function:: int atomic_inc_and_test( atomic_t * v )

Arguments
=========

``v``
    pointer of type atomic_t


Description
===========

Atomically increments ``v`` by 1 and returns true if the result is zero,
or false for all other cases.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
