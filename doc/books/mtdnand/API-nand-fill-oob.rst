.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-fill-oob:

=============
nand_fill_oob
=============

*man nand_fill_oob(9)*

*4.6.0-rc5*

[INTERN] Transfer client buffer to oob


Synopsis
========

.. c:function:: uint8_t * nand_fill_oob( struct mtd_info * mtd, uint8_t * oob, size_t len, struct mtd_oob_ops * ops )

Arguments
=========

``mtd``
    MTD device structure

``oob``
    oob data buffer

``len``
    oob data write length

``ops``
    oob ops structure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
