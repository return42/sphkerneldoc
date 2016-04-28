.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-tlr-supported:

=================
sas_tlr_supported
=================

*man sas_tlr_supported(9)*

*4.6.0-rc5*

checking TLR bit in vpd 0x90


Synopsis
========

.. c:function:: unsigned int sas_tlr_supported( struct scsi_device * sdev )

Arguments
=========

``sdev``
    scsi device struct


Description
===========

Check Transport Layer Retries are supported or not. If vpd page 0x90 is
present, TRL is supported.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
