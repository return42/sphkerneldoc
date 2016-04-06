
.. _API-scsi-mode-sense:

===============
scsi_mode_sense
===============

*man scsi_mode_sense(9)*

*4.6.0-rc1*

issue a mode sense, falling back from 10 to six bytes if necessary.


Synopsis
========

.. c:function:: int scsi_mode_sense( struct scsi_device * sdev, int dbd, int modepage, unsigned char * buffer, int len, int timeout, int retries, struct scsi_mode_data * data, struct scsi_sense_hdr * sshdr )

Arguments
=========

``sdev``
    SCSI device to be queried

``dbd``
    set if mode sense will allow block descriptors to be returned

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
    place to put sense data (or NULL if no sense to be collected). must be SCSI_SENSE_BUFFERSIZE big.


Description
===========

Returns zero if unsuccessful, or the header offset (either 4 or 8 depending on whether a six or ten byte command was issued) if successful.
