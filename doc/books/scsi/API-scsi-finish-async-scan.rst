
.. _API-scsi-finish-async-scan:

======================
scsi_finish_async_scan
======================

*man scsi_finish_async_scan(9)*

*4.6.0-rc1*

asynchronous scan has finished


Synopsis
========

.. c:function:: void scsi_finish_async_scan( struct async_scan_data * data )

Arguments
=========

``data``
    cookie returned from earlier call to ``scsi_prep_async_scan``


Description
===========

All the devices currently attached to this host have been found. This function announces all the devices it has found to the rest of the system.
