
.. _API-kfifo-out:

=========
kfifo_out
=========

*man kfifo_out(9)*

*4.6.0-rc1*

get data from the fifo


Synopsis
========

.. c:function:: kfifo_out( fifo, buf, n )

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

This macro get some data from the fifo and return the numbers of elements copied.

Note that with only one concurrent reader and one concurrent writer, you don't need extra locking to use these macro.
