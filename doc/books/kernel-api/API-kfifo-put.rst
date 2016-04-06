
.. _API-kfifo-put:

=========
kfifo_put
=========

*man kfifo_put(9)*

*4.6.0-rc1*

put data into the fifo


Synopsis
========

.. c:function:: kfifo_put( fifo, val )

Arguments
=========

``fifo``
    address of the fifo to be used

``val``
    the data to be added


Description
===========

This macro copies the given value into the fifo. It returns 0 if the fifo was full. Otherwise it returns the number processed elements.

Note that with only one concurrent reader and one concurrent writer, you don't need extra locking to use these macro.
