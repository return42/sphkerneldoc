
.. _API-scsi-report-opcode:

==================
scsi_report_opcode
==================

*man scsi_report_opcode(9)*

*4.6.0-rc1*

Find out if a given command opcode is supported


Synopsis
========

.. c:function:: int scsi_report_opcode( struct scsi_device * sdev, unsigned char * buffer, unsigned int len, unsigned char opcode )

Arguments
=========

``sdev``
    scsi device to query

``buffer``
    scratch buffer (must be at least 20 bytes long)

``len``
    length of buffer

``opcode``
    opcode for command to look up


Description
===========

Uses the REPORT SUPPORTED OPERATION CODES to look up the given opcode. Returns -EINVAL if RSOC fails, 0 if the command opcode is unsupported and 1 if the device claims to support
the command.
