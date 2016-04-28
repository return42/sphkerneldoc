.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-hpa-resize:

==============
ata_hpa_resize
==============

*man ata_hpa_resize(9)*

*4.6.0-rc5*

Resize a device with an HPA set


Synopsis
========

.. c:function:: int ata_hpa_resize( struct ata_device * dev )

Arguments
=========

``dev``
    Device to resize


Description
===========

Read the size of an LBA28 or LBA48 disk with HPA features and resize it
if required to the full size of the media. The caller must check the
drive has the HPA feature set enabled.


RETURNS
=======

0 on success, -errno on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
