.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-do-write-oob:

=================
nand_do_write_oob
=================

*man nand_do_write_oob(9)*

*4.6.0-rc5*

[MTD Interface] NAND write out-of-band


Synopsis
========

.. c:function:: int nand_do_write_oob( struct mtd_info * mtd, loff_t to, struct mtd_oob_ops * ops )

Arguments
=========

``mtd``
    MTD device structure

``to``
    offset to write to

``ops``
    oob operation description structure


Description
===========

NAND write out-of-band.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
