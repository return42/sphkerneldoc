.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-device-supports-vpd:

========================
scsi_device_supports_vpd
========================

*man scsi_device_supports_vpd(9)*

*4.6.0-rc5*

test if a device supports VPD pages


Synopsis
========

.. c:function:: int scsi_device_supports_vpd( struct scsi_device * sdev )

Arguments
=========

``sdev``
    the ``struct scsi_device`` to test


Description
===========

If the 'try_vpd_pages' flag is set it takes precedence. Otherwise we
will assume VPD pages are supported if the SCSI level is at least SPC-3
and 'skip_vpd_pages' is not set.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
