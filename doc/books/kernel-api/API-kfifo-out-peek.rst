
.. _API-kfifo-out-peek:

==============
kfifo_out_peek
==============

*man kfifo_out_peek(9)*

*4.6.0-rc1*

gets some data from the fifo


Synopsis
========

.. c:function:: kfifo_out_peek( fifo, buf, n )

Arguments
=========

``fifo``
    address of the fifo to be used

``buf``
    pointer to the storage buffer

``n``
    max. number of elements to get


Description
===========

This macro get the data from the fifo and return the numbers of elements copied. The data is not removed from the fifo.

Note that with only one concurrent reader and one concurrent writer, you don't need extra locking to use these macro.
