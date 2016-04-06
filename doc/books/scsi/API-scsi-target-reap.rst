
.. _API-scsi-target-reap:

================
scsi_target_reap
================

*man scsi_target_reap(9)*

*4.6.0-rc1*

check to see if target is in use and destroy if not


Synopsis
========

.. c:function:: void scsi_target_reap( struct scsi_target * starget )

Arguments
=========

``starget``
    target to be checked


Description
===========

This is used after removing a LUN or doing a last put of the target it checks atomically that nothing is using the target and removes it if so.
