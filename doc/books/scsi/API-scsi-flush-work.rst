
.. _API-scsi-flush-work:

===============
scsi_flush_work
===============

*man scsi_flush_work(9)*

*4.6.0-rc1*

Flush a Scsi_Host's workqueue.


Synopsis
========

.. c:function:: void scsi_flush_work( struct Scsi_Host * shost )

Arguments
=========

``shost``
    Pointer to Scsi_Host.
