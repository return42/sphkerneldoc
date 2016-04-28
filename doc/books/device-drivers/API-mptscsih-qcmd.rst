.. -*- coding: utf-8; mode: rst -*-

.. _API-mptscsih-qcmd:

=============
mptscsih_qcmd
=============

*man mptscsih_qcmd(9)*

*4.6.0-rc5*

Primary Fusion MPT SCSI initiator IO start routine.


Synopsis
========

.. c:function:: int mptscsih_qcmd( struct scsi_cmnd * SCpnt )

Arguments
=========

``SCpnt``
    Pointer to scsi_cmnd structure


Description
===========

(linux scsi_host_template.queuecommand routine) This is the primary
SCSI IO start routine. Create a MPI SCSIIORequest from a linux
scsi_cmnd request and send it to the IOC.

Returns 0. (rtn value discarded by linux scsi mid-layer)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
