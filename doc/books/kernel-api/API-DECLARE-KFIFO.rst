.. -*- coding: utf-8; mode: rst -*-

.. _API-DECLARE-KFIFO:

=============
DECLARE_KFIFO
=============

*man DECLARE_KFIFO(9)*

*4.6.0-rc5*

macro to declare a fifo object


Synopsis
========

.. c:function:: DECLARE_KFIFO( fifo, type, size )

Arguments
=========

``fifo``
    name of the declared fifo

``type``
    type of the fifo elements

``size``
    the number of elements in the fifo, this must be a power of 2


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
