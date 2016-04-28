.. -*- coding: utf-8; mode: rst -*-

.. _API-kfifo-in:

========
kfifo_in
========

*man kfifo_in(9)*

*4.6.0-rc5*

put data into the fifo


Synopsis
========

.. c:function:: kfifo_in( fifo, buf, n )

Arguments
=========

``fifo``
    address of the fifo to be used

``buf``
    the data to be added

``n``
    number of elements to be added


Description
===========

This macro copies the given buffer into the fifo and returns the number
of copied elements.

Note that with only one concurrent reader and one concurrent writer, you
don't need extra locking to use these macro.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
