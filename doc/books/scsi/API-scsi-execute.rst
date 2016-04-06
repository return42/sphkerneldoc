
.. _API-scsi-execute:

============
scsi_execute
============

*man scsi_execute(9)*

*4.6.0-rc1*

insert request and wait for the result


Synopsis
========

.. c:function:: int scsi_execute( struct scsi_device * sdev, const unsigned char * cmd, int data_direction, void * buffer, unsigned bufflen, unsigned char * sense, int timeout, int retries, u64 flags, int * resid )

Arguments
=========

``sdev``
    scsi device

``cmd``
    scsi command

``data_direction``
    data direction

``buffer``
    data buffer

``bufflen``
    len of buffer

``sense``
    optional sense buffer

``timeout``
    request timeout in seconds

``retries``
    number of times to retry request

``flags``
    or into request flags;

``resid``
    optional residual length


Description
===========

returns the req->errors value which is the scsi_cmnd result field.
