.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-do-read-ops:

================
nand_do_read_ops
================

*man nand_do_read_ops(9)*

*4.6.0-rc5*

[INTERN] Read data with ECC


Synopsis
========

.. c:function:: int nand_do_read_ops( struct mtd_info * mtd, loff_t from, struct mtd_oob_ops * ops )

Arguments
=========

``mtd``
    MTD device structure

``from``
    offset to read from

``ops``
    oob ops structure


Description
===========

Internal function. Called with chip held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
