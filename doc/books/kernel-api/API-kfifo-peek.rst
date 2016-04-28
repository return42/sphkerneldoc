.. -*- coding: utf-8; mode: rst -*-

.. _API-kfifo-peek:

==========
kfifo_peek
==========

*man kfifo_peek(9)*

*4.6.0-rc5*

get data from the fifo without removing


Synopsis
========

.. c:function:: kfifo_peek( fifo, val )

Arguments
=========

``fifo``
    address of the fifo to be used

``val``
    address where to store the data


Description
===========

This reads the data from the fifo without removing it from the fifo. It
returns 0 if the fifo was empty. Otherwise it returns the number
processed elements.

Note that with only one concurrent reader and one concurrent writer, you
don't need extra locking to use these macro.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
