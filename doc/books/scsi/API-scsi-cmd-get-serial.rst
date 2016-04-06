
.. _API-scsi-cmd-get-serial:

===================
scsi_cmd_get_serial
===================

*man scsi_cmd_get_serial(9)*

*4.6.0-rc1*

Assign a serial number to a command


Synopsis
========

.. c:function:: void scsi_cmd_get_serial( struct Scsi_Host * host, struct scsi_cmnd * cmd )

Arguments
=========

``host``
    the scsi host

``cmd``
    command to assign serial number to


Description
===========

a serial number identifies a request for error recovery and debugging purposes. Protected by the Host_Lock of host.
