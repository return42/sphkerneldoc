
.. _API-scsi-host-alloc:

===============
scsi_host_alloc
===============

*man scsi_host_alloc(9)*

*4.6.0-rc1*

register a scsi host adapter instance.


Synopsis
========

.. c:function:: struct Scsi_Host ⋆ scsi_host_alloc( struct scsi_host_template * sht, int privsize )

Arguments
=========

``sht``
    pointer to scsi host template

``privsize``
    extra bytes to allocate for driver


Note
====

Allocate a new Scsi_Host and perform basic initialization. The host is not published to the scsi midlayer until scsi_add_host is called.


Return value
============

Pointer to a new Scsi_Host
