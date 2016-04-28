.. -*- coding: utf-8; mode: rst -*-

.. _API-w1-read-block:

=============
w1_read_block
=============

*man w1_read_block(9)*

*4.6.0-rc5*

Reads a series of bytes.


Synopsis
========

.. c:function:: u8 w1_read_block( struct w1_master * dev, u8 * buf, int len )

Arguments
=========

``dev``
    the master device

``buf``
    pointer to the buffer to fill

``len``
    the number of bytes to read


Return
======

the number of bytes read


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
