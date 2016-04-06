
.. _API-scsi-probe-and-add-lun:

======================
scsi_probe_and_add_lun
======================

*man scsi_probe_and_add_lun(9)*

*4.6.0-rc1*

probe a LUN, if a LUN is found add it


Synopsis
========

.. c:function:: int scsi_probe_and_add_lun( struct scsi_target * starget, u64 lun, int * bflagsp, struct scsi_device ** sdevp, int rescan, void * hostdata )

Arguments
=========

``starget``
    pointer to target device structure

``lun``
    LUN of target device

``bflagsp``
    store bflags here if not NULL

``sdevp``
    probe the LUN corresponding to this scsi_device

``rescan``
    if nonzero skip some code only needed on first scan

``hostdata``
    passed to ``scsi_alloc_sdev``


Description
===========

Call scsi_probe_lun, if a LUN with an attached device is found, allocate and set it up by calling scsi_add_lun.


SCSI_SCAN_NO_RESPONSE
=====================

could not allocate or setup a scsi_device


SCSI_SCAN_TARGET_PRESENT
========================

target responded, but no device is attached at the LUN


SCSI_SCAN_LUN_PRESENT
=====================

a new scsi_device was allocated and initialized
