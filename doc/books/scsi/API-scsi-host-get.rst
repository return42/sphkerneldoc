
.. _API-scsi-host-get:

=============
scsi_host_get
=============

*man scsi_host_get(9)*

*4.6.0-rc1*

inc a Scsi_Host ref count


Synopsis
========

.. c:function:: struct Scsi_Host ⋆ scsi_host_get( struct Scsi_Host * shost )

Arguments
=========

``shost``
    Pointer to Scsi_Host to inc.
