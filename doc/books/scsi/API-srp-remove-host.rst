.. -*- coding: utf-8; mode: rst -*-

.. _API-srp-remove-host:

===============
srp_remove_host
===============

*man srp_remove_host(9)*

*4.6.0-rc5*

tear down a Scsi_Host's SRP data structures


Synopsis
========

.. c:function:: void srp_remove_host( struct Scsi_Host * shost )

Arguments
=========

``shost``
    Scsi Host that is torn down


Description
===========

Removes all SRP remote ports for a given Scsi_Host. Must be called just
before scsi_remove_host for SRP HBAs.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
