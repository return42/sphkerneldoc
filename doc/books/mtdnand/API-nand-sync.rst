.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-sync:

=========
nand_sync
=========

*man nand_sync(9)*

*4.6.0-rc5*

[MTD Interface] sync


Synopsis
========

.. c:function:: void nand_sync( struct mtd_info * mtd )

Arguments
=========

``mtd``
    MTD device structure


Description
===========

Sync is actually a wait for chip ready function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
