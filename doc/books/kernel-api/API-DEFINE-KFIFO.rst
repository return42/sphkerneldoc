
.. _API-DEFINE-KFIFO:

============
DEFINE_KFIFO
============

*man DEFINE_KFIFO(9)*

*4.6.0-rc1*

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
