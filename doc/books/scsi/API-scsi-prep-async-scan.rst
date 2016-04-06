
.. _API-scsi-prep-async-scan:

====================
scsi_prep_async_scan
====================

*man scsi_prep_async_scan(9)*

*4.6.0-rc1*

prepare for an async scan


Synopsis
========

.. c:function:: struct async_scan_data ⋆ scsi_prep_async_scan( struct Scsi_Host * shost )

Arguments
=========

``shost``
    the host which will be scanned


Returns
=======

a cookie to be passed to ``scsi_finish_async_scan``

Tells the midlayer this host is going to do an asynchronous scan. It reserves the host's position in the scanning list and ensures that other asynchronous scans started after this
one won't affect the ordering of the discovered devices.
