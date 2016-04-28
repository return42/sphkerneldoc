.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-mport-get-feature:

=====================
rio_mport_get_feature
=====================

*man rio_mport_get_feature(9)*

*4.6.0-rc5*

query for devices' extended features


Synopsis
========

.. c:function:: u32 rio_mport_get_feature( struct rio_mport * port, int local, u16 destid, u8 hopcount, int ftr )

Arguments
=========

``port``
    Master port to issue transaction

``local``
    Indicate a local master port or remote device access

``destid``
    Destination ID of the device

``hopcount``
    Number of switch hops to the device

``ftr``
    Extended feature code


Description
===========

Tell if a device supports a given RapidIO capability. Returns the offset
of the requested extended feature block within the device's RIO
configuration space or 0 in case the device does not support it.
Possible values for ``ftr``:

``RIO_EFB_PAR_EP_ID`` LP/LVDS EP Devices

``RIO_EFB_PAR_EP_REC_ID`` LP/LVDS EP Recovery Devices

``RIO_EFB_PAR_EP_FREE_ID`` LP/LVDS EP Free Devices

``RIO_EFB_SER_EP_ID`` LP/Serial EP Devices

``RIO_EFB_SER_EP_REC_ID`` LP/Serial EP Recovery Devices

``RIO_EFB_SER_EP_FREE_ID`` LP/Serial EP Free Devices


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
