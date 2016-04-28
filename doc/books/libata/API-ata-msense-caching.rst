.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-msense-caching:

==================
ata_msense_caching
==================

*man ata_msense_caching(9)*

*4.6.0-rc5*

Simulate MODE SENSE caching info page


Synopsis
========

.. c:function:: unsigned int ata_msense_caching( u16 * id, u8 * buf, bool changeable )

Arguments
=========

``id``
    device IDENTIFY data

``buf``
    output buffer

``changeable``
    whether changeable parameters are requested


Description
===========

Generate a caching info page, which conditionally indicates write
caching to the SCSI layer, depending on device capabilities.


LOCKING
=======

None.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
