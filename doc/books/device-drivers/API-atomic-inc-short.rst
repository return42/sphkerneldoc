.. -*- coding: utf-8; mode: rst -*-

.. _API-atomic-inc-short:

================
atomic_inc_short
================

*man atomic_inc_short(9)*

*4.6.0-rc5*

increment of a short integer


Synopsis
========

.. c:function:: short int atomic_inc_short( short int * v )

Arguments
=========

``v``
    pointer to type int


Description
===========

Atomically adds 1 to ``v`` Returns the new value of ``u``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
