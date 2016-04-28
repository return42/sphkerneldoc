.. -*- coding: utf-8; mode: rst -*-

.. _API-verify-bbt-descr:

================
verify_bbt_descr
================

*man verify_bbt_descr(9)*

*4.6.0-rc5*

verify the bad block description


Synopsis
========

.. c:function:: void verify_bbt_descr( struct mtd_info * mtd, struct nand_bbt_descr * bd )

Arguments
=========

``mtd``
    MTD device structure

``bd``
    the table to verify


Description
===========

This functions performs a few sanity checks on the bad block description
table.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
