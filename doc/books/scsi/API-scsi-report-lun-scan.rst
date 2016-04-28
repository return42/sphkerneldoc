.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-report-lun-scan:

====================
scsi_report_lun_scan
====================

*man scsi_report_lun_scan(9)*

*4.6.0-rc5*

Scan using SCSI REPORT LUN results


Synopsis
========

.. c:function:: int scsi_report_lun_scan( struct scsi_target * starget, int bflags, int rescan )

Arguments
=========

``starget``
    which target

``bflags``
    Zero or a mix of BLIST_NOLUN, BLIST_REPORTLUN2, or
    BLIST_NOREPORTLUN

``rescan``
    nonzero if we can skip code only needed on first scan


Description
===========

Fast scanning for modern (SCSI-3) devices by sending a REPORT LUN
command. Scan the resulting list of LUNs by calling
scsi_probe_and_add_lun.

If BLINK_REPORTLUN2 is set, scan a target that supports more than 8
LUNs even if it's older than SCSI-3. If BLIST_NOREPORTLUN is set,
return 1 always. If BLIST_NOLUN is set, return 0 always. If
starget->no_report_luns is set, return 1 always.


0
=

scan completed (or no memory, so further scanning is futile)


1
=

could not scan with REPORT LUN


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
