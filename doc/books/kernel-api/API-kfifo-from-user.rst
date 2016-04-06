
.. _API-kfifo-from-user:

===============
kfifo_from_user
===============

*man kfifo_from_user(9)*

*4.6.0-rc1*

puts some data from user space into the fifo


Synopsis
========

.. c:function:: kfifo_from_user( fifo, from, len, copied )

Arguments
=========

``fifo``
    address of the fifo to be used

``from``
    pointer to the data to be added

``len``
    the length of the data to be added

``copied``
    pointer to output variable to store the number of copied bytes


Description
===========

This macro copies at most ``len`` bytes from the ``from`` into the fifo, depending of the available space and returns -EFAULT/0.

Note that with only one concurrent reader and one concurrent writer, you don't need extra locking to use these macro.
