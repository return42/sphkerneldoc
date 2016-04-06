
.. _API-sas-get-address:

===============
sas_get_address
===============

*man sas_get_address(9)*

*4.6.0-rc1*

return the SAS address of the device


Synopsis
========

.. c:function:: u64 sas_get_address( struct scsi_device * sdev )

Arguments
=========

``sdev``
    scsi device


Description
===========

Returns the SAS address of the scsi device
