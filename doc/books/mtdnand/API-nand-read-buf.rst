.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-read-buf:

=============
nand_read_buf
=============

*man nand_read_buf(9)*

*4.6.0-rc5*

[DEFAULT] read chip data into buffer


Synopsis
========

.. c:function:: void nand_read_buf( struct mtd_info * mtd, uint8_t * buf, int len )

Arguments
=========

``mtd``
    MTD device structure

``buf``
    buffer to store date

``len``
    number of bytes to read


Description
===========

Default read function for 8bit buswidth.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
