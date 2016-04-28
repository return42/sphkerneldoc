.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-schedule-eh:

================
scsi_schedule_eh
================

*man scsi_schedule_eh(9)*

*4.6.0-rc5*

schedule EH for SCSI host


Synopsis
========

.. c:function:: void scsi_schedule_eh( struct Scsi_Host * shost )

Arguments
=========

``shost``
    SCSI host to invoke error handling on.


Description
===========

Schedule SCSI EH without scmd.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
