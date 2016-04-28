.. -*- coding: utf-8; mode: rst -*-

.. _API-is-sas-attached:

===============
is_sas_attached
===============

*man is_sas_attached(9)*

*4.6.0-rc5*

check if device is SAS attached


Synopsis
========

.. c:function:: int is_sas_attached( struct scsi_device * sdev )

Arguments
=========

``sdev``
    scsi device to check


Description
===========

returns true if the device is SAS attached


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
