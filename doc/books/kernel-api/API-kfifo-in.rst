
.. _API-kfifo-in:

========
kfifo_in
========

*man kfifo_in(9)*

*4.6.0-rc1*

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

This macro copies the given buffer into the fifo and returns the number of copied elements.

Note that with only one concurrent reader and one concurrent writer, you don't need extra locking to use these macro.
