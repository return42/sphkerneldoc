.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-mode-select:

================
scsi_mode_select
================

*man scsi_mode_select(9)*

*4.6.0-rc5*

issue a mode select


Synopsis
========

.. c:function:: int scsi_mode_select( struct scsi_device * sdev, int pf, int sp, int modepage, unsigned char * buffer, int len, int timeout, int retries, struct scsi_mode_data * data, struct scsi_sense_hdr * sshdr )

Arguments
=========

``sdev``
    SCSI device to be queried

``pf``
    Page format bit (1 == standard, 0 == vendor specific)

``sp``
    Save page bit (0 == don't save, 1 == save)

``modepage``
    mode page being requested

``buffer``
    request buffer (may not be smaller than eight bytes)

``len``
    length of request buffer.

``timeout``
    command timeout

``retries``
    number of retries before failing

``data``
    returns a structure abstracting the mode header data

``sshdr``
    place to put sense data (or NULL if no sense to be collected). must
    be SCSI_SENSE_BUFFERSIZE big.


Description
===========

Returns zero if successful; negative error number or scsi status on
error


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
