.. -*- coding: utf-8; mode: rst -*-

.. _API-DEFINE-KFIFO:

============
DEFINE_KFIFO
============

*man DEFINE_KFIFO(9)*

*4.6.0-rc5*

macro to define and initialize a fifo


Synopsis
========

.. c:function:: DEFINE_KFIFO( fifo, type, size )

Arguments
=========

``fifo``
    name of the declared fifo datatype

``type``
    type of the fifo elements

``size``
    the number of elements in the fifo, this must be a power of 2


Note
====

the macro can be used for global and local fifo data type variables.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
