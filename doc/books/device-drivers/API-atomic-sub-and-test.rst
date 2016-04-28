.. -*- coding: utf-8; mode: rst -*-

.. _API-atomic-sub-and-test:

===================
atomic_sub_and_test
===================

*man atomic_sub_and_test(9)*

*4.6.0-rc5*

subtract value from variable and test result


Synopsis
========

.. c:function:: int atomic_sub_and_test( int i, atomic_t * v )

Arguments
=========

``i``
    integer value to subtract

``v``
    pointer of type atomic_t


Description
===========

Atomically subtracts ``i`` from ``v`` and returns true if the result is
zero, or false for all other cases.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
