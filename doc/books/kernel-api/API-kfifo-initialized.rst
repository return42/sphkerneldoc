.. -*- coding: utf-8; mode: rst -*-

.. _API-kfifo-initialized:

=================
kfifo_initialized
=================

*man kfifo_initialized(9)*

*4.6.0-rc5*

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

Return ``true`` if fifo is initialized, otherwise ``false``. Assumes the
fifo was 0 before.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
