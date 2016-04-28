.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-get-address:

===============
sas_get_address
===============

*man sas_get_address(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
