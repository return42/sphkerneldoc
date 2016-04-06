
.. _API-nand-release-device:

===================
nand_release_device
===================

*man nand_release_device(9)*

*4.6.0-rc1*

[GENERIC] release chip


Synopsis
========

.. c:function:: void nand_release_device( struct mtd_info * mtd )

Arguments
=========

``mtd``
    MTD device structure


Description
===========

Release chip lock and wake up anyone waiting on the device.
