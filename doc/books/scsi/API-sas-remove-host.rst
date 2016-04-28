.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-remove-host:

===============
sas_remove_host
===============

*man sas_remove_host(9)*

*4.6.0-rc5*

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

Removes all SAS PHYs and remote PHYs for a given Scsi_Host. Must be
called just before scsi_remove_host for SAS HBAs.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
