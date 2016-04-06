
.. _API-sas-disable-tlr:

===============
sas_disable_tlr
===============

*man sas_disable_tlr(9)*

*4.6.0-rc1*

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
