.. -*- coding: utf-8; mode: rst -*-

.. _API-kfifo-to-user:

=============
kfifo_to_user
=============

*man kfifo_to_user(9)*

*4.6.0-rc5*

copies data from the fifo into user space


Synopsis
========

.. c:function:: kfifo_to_user( fifo, to, len, copied )

Arguments
=========

``fifo``
    address of the fifo to be used

``to``
    where the data must be copied

``len``
    the size of the destination buffer

``copied``
    pointer to output variable to store the number of copied bytes


Description
===========

This macro copies at most ``len`` bytes from the fifo into the ``to``
buffer and returns -EFAULT/0.

Note that with only one concurrent reader and one concurrent writer, you
don't need extra locking to use these macro.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
