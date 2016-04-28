.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-unlock-native-capacity:

===============================
ata_scsi_unlock_native_capacity
===============================

*man ata_scsi_unlock_native_capacity(9)*

*4.6.0-rc5*

unlock native capacity


Synopsis
========

.. c:function:: void ata_scsi_unlock_native_capacity( struct scsi_device * sdev )

Arguments
=========

``sdev``
    SCSI device to adjust device capacity for


Description
===========

This function is called if a partition on ``sdev`` extends beyond the
end of the device. It requests EH to unlock HPA.


LOCKING
=======

Defined by the SCSI layer. Might sleep.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
