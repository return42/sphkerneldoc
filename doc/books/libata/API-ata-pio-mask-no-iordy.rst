
.. _API-ata-pio-mask-no-iordy:

=====================
ata_pio_mask_no_iordy
=====================

*man ata_pio_mask_no_iordy(9)*

*4.6.0-rc1*

Return the non IORDY mask


Synopsis
========

.. c:function:: u32 ata_pio_mask_no_iordy( const struct ata_device * adev )

Arguments
=========

``adev``
    ATA device


Description
===========

Compute the highest mode possible if we are not using iordy. Return -1 if no iordy mode is available.
