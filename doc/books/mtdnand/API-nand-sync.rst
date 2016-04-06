
.. _API-nand-sync:

=========
nand_sync
=========

*man nand_sync(9)*

*4.6.0-rc1*

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
