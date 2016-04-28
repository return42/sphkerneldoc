.. -*- coding: utf-8; mode: rst -*-

.. _API-kfifo-init:

==========
kfifo_init
==========

*man kfifo_init(9)*

*4.6.0-rc5*

initialize a fifo using a preallocated buffer


Synopsis
========

.. c:function:: kfifo_init( fifo, buffer, size )

Arguments
=========

``fifo``
    the fifo to assign the buffer

``buffer``
    the preallocated buffer to be used

``size``
    the size of the internal buffer, this have to be a power of 2


Description
===========

This macro initialize a fifo using a preallocated buffer.

The numer of elements will be rounded-up to a power of 2. Return 0 if no
error, otherwise an error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
