.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-get-vpd-page:

=================
scsi_get_vpd_page
=================

*man scsi_get_vpd_page(9)*

*4.6.0-rc5*

Get Vital Product Data from a SCSI device


Synopsis
========

.. c:function:: int scsi_get_vpd_page( struct scsi_device * sdev, u8 page, unsigned char * buf, int buf_len )

Arguments
=========

``sdev``
    The device to ask

``page``
    Which Vital Product Data to return

``buf``
    where to store the VPD

``buf_len``
    number of bytes in the VPD buffer area


Description
===========

SCSI devices may optionally supply Vital Product Data. Each 'page' of
VPD is defined in the appropriate SCSI document (eg SPC, SBC). If the
device supports this VPD page, this routine returns a pointer to a
buffer containing the data from that page. The caller is responsible for
calling ``kfree`` on this pointer when it is no longer needed. If we
cannot retrieve the VPD page this routine returns ``NULL``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
