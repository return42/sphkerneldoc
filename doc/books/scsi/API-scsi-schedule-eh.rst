
.. _API-scsi-schedule-eh:

================
scsi_schedule_eh
================

*man scsi_schedule_eh(9)*

*4.6.0-rc1*

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
