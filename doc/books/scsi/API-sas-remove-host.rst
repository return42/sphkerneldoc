
.. _API-sas-remove-host:

===============
sas_remove_host
===============

*man sas_remove_host(9)*

*4.6.0-rc1*

tear down a Scsi_Host's SAS data structures


Synopsis
========

.. c:function:: void sas_remove_host( struct Scsi_Host * shost )

Arguments
=========

``shost``
    Scsi Host that is torn down


Description
===========

Removes all SAS PHYs and remote PHYs for a given Scsi_Host. Must be called just before scsi_remove_host for SAS HBAs.
