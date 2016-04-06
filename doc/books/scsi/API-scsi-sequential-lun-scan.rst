
.. _API-scsi-sequential-lun-scan:

========================
scsi_sequential_lun_scan
========================

*man scsi_sequential_lun_scan(9)*

*4.6.0-rc1*

sequentially scan a SCSI target


Synopsis
========

.. c:function:: void scsi_sequential_lun_scan( struct scsi_target * starget, int bflags, int scsi_level, int rescan )

Arguments
=========

``starget``
    pointer to target structure to scan

``bflags``
    black/white list flag for LUN 0

``scsi_level``
    Which version of the standard does this device adhere to

``rescan``
    passed to ``scsi_probe_add_lun``


Description
===========

Generally, scan from LUN 1 (LUN 0 is assumed to already have been scanned) to some maximum lun until a LUN is found with no device attached. Use the bflags to figure out any
oddities.

Modifies sdevscan->lun.
