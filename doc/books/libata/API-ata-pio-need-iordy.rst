
.. _API-ata-pio-need-iordy:

==================
ata_pio_need_iordy
==================

*man ata_pio_need_iordy(9)*

*4.6.0-rc1*

check if iordy needed


Synopsis
========

.. c:function:: unsigned int ata_pio_need_iordy( const struct ata_device * adev )

Arguments
=========

``adev``
    ATA device


Description
===========

Check if the current speed of the device requires IORDY. Used by various controllers for chip configuration.
