
.. _API-nand-shutdown:

=============
nand_shutdown
=============

*man nand_shutdown(9)*

*4.6.0-rc1*

[MTD Interface] Finish the current NAND operation and prevent further operations


Synopsis
========

.. c:function:: void nand_shutdown( struct mtd_info * mtd )

Arguments
=========

``mtd``
    MTD device structure
