.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-do-write-ops:

=================
nand_do_write_ops
=================

*man nand_do_write_ops(9)*

*4.6.0-rc5*

[INTERN] NAND write with ECC


Synopsis
========

.. c:function:: int nand_do_write_ops( struct mtd_info * mtd, loff_t to, struct mtd_oob_ops * ops )

Arguments
=========

``mtd``
    MTD device structure

``to``
    offset to write to

``ops``
    oob operations description structure


Description
===========

NAND write with ECC.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
