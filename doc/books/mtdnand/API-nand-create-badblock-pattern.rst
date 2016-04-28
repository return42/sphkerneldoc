.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-create-badblock-pattern:

============================
nand_create_badblock_pattern
============================

*man nand_create_badblock_pattern(9)*

*4.6.0-rc5*

[INTERN] Creates a BBT descriptor structure


Synopsis
========

.. c:function:: int nand_create_badblock_pattern( struct nand_chip * this )

Arguments
=========

``this``
    NAND chip to create descriptor for


Description
===========

This function allocates and initializes a nand_bbt_descr for BBM
detection based on the properties of ``this``. The new descriptor is
stored in this->badblock_pattern. Thus, this->badblock_pattern should
be NULL when passed to this function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
