
.. _API-nand-check-wp:

=============
nand_check_wp
=============

*man nand_check_wp(9)*

*4.6.0-rc1*

[GENERIC] check if the chip is write protected


Synopsis
========

.. c:function:: int nand_check_wp( struct mtd_info * mtd )

Arguments
=========

``mtd``
    MTD device structure


Description
===========

Check, if the device is write protected. The function expects, that the device is already selected.
