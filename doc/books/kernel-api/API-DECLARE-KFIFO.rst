
.. _API-DECLARE-KFIFO:

=============
DECLARE_KFIFO
=============

*man DECLARE_KFIFO(9)*

*4.6.0-rc1*

macro to declare a fifo object


Synopsis
========

.. c:function:: DECLARE_KFIFO( fifo, type, size )

Arguments
=========

``fifo``
    name of the declared fifo

``type``
    type of the fifo elements

``size``
    the number of elements in the fifo, this must be a power of 2
