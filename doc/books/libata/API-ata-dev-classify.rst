.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-dev-classify:

================
ata_dev_classify
================

*man ata_dev_classify(9)*

*4.6.0-rc5*

determine device type based on ATA-spec signature


Synopsis
========

.. c:function:: unsigned int ata_dev_classify( const struct ata_taskfile * tf )

Arguments
=========

``tf``
    ATA taskfile register set for device to be identified


Description
===========

Determine from taskfile register contents whether a device is ATA or
ATAPI, as per “Signature and persistence” section of ATA/PI spec (volume
1, sect 5.14).


LOCKING
=======

None.


RETURNS
=======

Device type, ``ATA_DEV_ATA``, ``ATA_DEV_ATAPI``, ``ATA_DEV_PMP``,
``ATA_DEV_ZAC``, or ``ATA_DEV_UNKNOWN`` the event of failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
