.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-write-buf16:

================
nand_write_buf16
================

*man nand_write_buf16(9)*

*4.6.0-rc5*

[DEFAULT] write buffer to chip


Synopsis
========

.. c:function:: void nand_write_buf16( struct mtd_info * mtd, const uint8_t * buf, int len )

Arguments
=========

``mtd``
    MTD device structure

``buf``
    data buffer

``len``
    number of bytes to write


Description
===========

Default write function for 16bit buswidth.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
