.. -*- coding: utf-8; mode: rst -*-

.. _API-iscsi-scan-finished:

===================
iscsi_scan_finished
===================

*man iscsi_scan_finished(9)*

*4.6.0-rc5*

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

This function can be used by drives like qla4xxx to report to the scsi
layer when the scans it kicked off at module load time are done.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
