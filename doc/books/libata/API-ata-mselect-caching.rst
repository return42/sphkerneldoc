.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-mselect-caching:

===================
ata_mselect_caching
===================

*man ata_mselect_caching(9)*

*4.6.0-rc5*

Simulate MODE SELECT for caching info page


Synopsis
========

.. c:function:: int ata_mselect_caching( struct ata_queued_cmd * qc, const u8 * buf, int len )

Arguments
=========

``qc``
    Storage for translated ATA taskfile

``buf``
    input buffer

``len``
    number of valid bytes in the input buffer


Description
===========

Prepare a taskfile to modify caching information for the device.


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
