
.. _API-mptspi-is-raid:

==============
mptspi_is_raid
==============

*man mptspi_is_raid(9)*

*4.6.0-rc1*

Determines whether target is belonging to volume


Synopsis
========

.. c:function:: int mptspi_is_raid( struct _MPT_SCSI_HOST * hd, u32 id )

Arguments
=========

``hd``
    Pointer to a SCSI HOST structure

``id``
    target device id


Return
======

non-zero = true zero = false
