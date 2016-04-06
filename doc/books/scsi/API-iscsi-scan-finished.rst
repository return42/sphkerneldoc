
.. _API-iscsi-scan-finished:

===================
iscsi_scan_finished
===================

*man iscsi_scan_finished(9)*

*4.6.0-rc1*

helper to report when running scans are done


Synopsis
========

.. c:function:: int iscsi_scan_finished( struct Scsi_Host * shost, unsigned long time )

Arguments
=========

``shost``
    scsi host

``time``
    scan run time


Description
===========

This function can be used by drives like qla4xxx to report to the scsi layer when the scans it kicked off at module load time are done.
