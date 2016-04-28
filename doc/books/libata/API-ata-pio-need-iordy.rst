.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-pio-need-iordy:

==================
ata_pio_need_iordy
==================

*man ata_pio_need_iordy(9)*

*4.6.0-rc5*

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

Check if the current speed of the device requires IORDY. Used by various
controllers for chip configuration.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
