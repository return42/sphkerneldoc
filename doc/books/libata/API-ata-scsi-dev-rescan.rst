
.. _API-ata-scsi-dev-rescan:

===================
ata_scsi_dev_rescan
===================

*man ata_scsi_dev_rescan(9)*

*4.6.0-rc1*

initiate ``scsi_rescan_device``


Synopsis
========

.. c:function:: void ata_scsi_dev_rescan( struct work_struct * work )

Arguments
=========

``work``
    Pointer to ATA port to perform ``scsi_rescan_device``


Description
===========

After ATA pass thru (SAT) commands are executed successfully, libata need to propagate the changes to SCSI layer.


LOCKING
=======

Kernel thread context (may sleep).
