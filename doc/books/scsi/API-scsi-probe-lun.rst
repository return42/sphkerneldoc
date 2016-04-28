.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-probe-lun:

==============
scsi_probe_lun
==============

*man scsi_probe_lun(9)*

*4.6.0-rc5*

probe a single LUN using a SCSI INQUIRY


Synopsis
========

.. c:function:: int scsi_probe_lun( struct scsi_device * sdev, unsigned char * inq_result, int result_len, int * bflags )

Arguments
=========

``sdev``
    scsi_device to probe

``inq_result``
    area to store the INQUIRY result

``result_len``
    len of inq_result

``bflags``
    store any bflags found here


Description
===========

Probe the lun associated with ``req`` using a standard SCSI INQUIRY;

If the INQUIRY is successful, zero is returned and the INQUIRY data is
in ``inq_result``; the scsi_level and INQUIRY length are copied to the
scsi_device any flags value is stored in * ``bflags``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
