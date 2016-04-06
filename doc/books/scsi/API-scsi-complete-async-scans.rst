
.. _API-scsi-complete-async-scans:

=========================
scsi_complete_async_scans
=========================

*man scsi_complete_async_scans(9)*

*4.6.0-rc1*

Wait for asynchronous scans to complete


Synopsis
========

.. c:function:: int scsi_complete_async_scans( void )

Arguments
=========

``void``
    no arguments


Description
===========

When this function returns, any host which started scanning before this function was called will have finished its scan. Hosts which started scanning after this function was called
may or may not have finished.
