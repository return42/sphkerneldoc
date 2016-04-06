
.. _API-kfifo-reset-out:

===============
kfifo_reset_out
===============

*man kfifo_reset_out(9)*

*4.6.0-rc1*

skip fifo content


Synopsis
========

.. c:function:: kfifo_reset_out( fifo )

Arguments
=========

``fifo``
    address of the fifo to be used


Note
====

The usage of ``kfifo_reset_out`` is safe until it will be only called from the reader thread and there is only one concurrent reader. Otherwise it is dangerous and must be handled
in the same way as ``kfifo_reset``.
