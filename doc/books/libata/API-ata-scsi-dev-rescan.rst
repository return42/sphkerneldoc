.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-dev-rescan:

===================
ata_scsi_dev_rescan
===================

*man ata_scsi_dev_rescan(9)*

*4.6.0-rc5*

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

After ATA pass thru (SAT) commands are executed successfully, libata
need to propagate the changes to SCSI layer.


LOCKING
=======

Kernel thread context (may sleep).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
