
.. _API-kfifo-initialized:

=================
kfifo_initialized
=================

*man kfifo_initialized(9)*

*4.6.0-rc1*

Check if the fifo is initialized


Synopsis
========

.. c:function:: kfifo_initialized( fifo )

Arguments
=========

``fifo``
    address of the fifo to check


Description
===========

Return ``true`` if fifo is initialized, otherwise ``false``. Assumes the fifo was 0 before.
