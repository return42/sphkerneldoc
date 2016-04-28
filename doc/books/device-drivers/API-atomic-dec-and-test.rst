.. -*- coding: utf-8; mode: rst -*-

.. _API-atomic-dec-and-test:

===================
atomic_dec_and_test
===================

*man atomic_dec_and_test(9)*

*4.6.0-rc5*

decrement and test


Synopsis
========

.. c:function:: int atomic_dec_and_test( atomic_t * v )

Arguments
=========

``v``
    pointer of type atomic_t


Description
===========

Atomically decrements ``v`` by 1 and returns true if the result is 0, or
false for all other cases.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
