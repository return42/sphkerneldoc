.. -*- coding: utf-8; mode: rst -*-

.. _API-sas-disable-tlr:

===============
sas_disable_tlr
===============

*man sas_disable_tlr(9)*

*4.6.0-rc5*

setting TLR flags


Synopsis
========

.. c:function:: void sas_disable_tlr( struct scsi_device * sdev )

Arguments
=========

``sdev``
    scsi device struct


Description
===========

Seting tlr_enabled flag to 0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
