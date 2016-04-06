
.. _API-nand-get-device:

===============
nand_get_device
===============

*man nand_get_device(9)*

*4.6.0-rc1*

[GENERIC] Get chip for selected access


Synopsis
========

.. c:function:: int nand_get_device( struct mtd_info * mtd, int new_state )

Arguments
=========

``mtd``
    MTD device structure

``new_state``
    the state which is requested


Description
===========

Get the device and lock it for exclusive access
