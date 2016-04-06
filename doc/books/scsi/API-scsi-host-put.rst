
.. _API-scsi-host-put:

=============
scsi_host_put
=============

*man scsi_host_put(9)*

*4.6.0-rc1*

dec a Scsi_Host ref count


Synopsis
========

.. c:function:: void scsi_host_put( struct Scsi_Host * shost )

Arguments
=========

``shost``
    Pointer to Scsi_Host to dec.
