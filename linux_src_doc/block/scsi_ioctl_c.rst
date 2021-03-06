.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/scsi_ioctl.c

.. _`sg_scsi_ioctl`:

sg_scsi_ioctl
=============

.. c:function:: int sg_scsi_ioctl(struct request_queue *q, struct gendisk *disk, fmode_t mode, struct scsi_ioctl_command __user *sic)

    -  handle deprecated SCSI_IOCTL_SEND_COMMAND ioctl

    :param q:
        request queue to send scsi commands down
    :type q: struct request_queue \*

    :param disk:
        gendisk to operate on (option)
    :type disk: struct gendisk \*

    :param mode:
        mode used to open the file through which the ioctl has been
        submitted
    :type mode: fmode_t

    :param sic:
        userspace structure describing the command to perform
    :type sic: struct scsi_ioctl_command __user \*

.. _`sg_scsi_ioctl.description`:

Description
-----------

Send down the scsi command described by \ ``sic``\  to the device below
the request queue \ ``q``\ .  If \ ``file``\  is non-NULL it's used to perform
fine-grained permission checks that allow users to send down
non-destructive SCSI commands.  If the caller has a struct gendisk
available it should be passed in as \ ``disk``\  to allow the low level
driver to use the information contained in it.  A non-NULL \ ``disk``\ 
is only allowed if the caller knows that the low level driver doesn't
need it (e.g. in the scsi subsystem).

.. _`sg_scsi_ioctl.notes`:

Notes
-----

-  This interface is deprecated - users should use the SG_IO
interface instead, as this is a more flexible approach to
performing SCSI commands on a device.
-  The SCSI command length is determined by examining the 1st byte
of the given command. There is no way to override this.
-  Data transfers are limited to PAGE_SIZE
-  The length (x + y) must be at least OMAX_SB_LEN bytes long to
accommodate the sense buffer when an error occurs.
The sense buffer is truncated to OMAX_SB_LEN (16) bytes so that
old code will not be surprised.
-  If a Unix error occurs (e.g. ENOMEM) then the user will receive
a negative return and the Unix error code in 'errno'.
If the SCSI command succeeds then 0 is returned.
Positive numbers returned are the compacted SCSI error codes (4
bytes in one int) where the lowest byte is the SCSI status.

.. _`scsi_req_init`:

scsi_req_init
=============

.. c:function:: void scsi_req_init(struct scsi_request *req)

    initialize certain fields of a scsi_request structure

    :param req:
        Pointer to a scsi_request structure.
        Initializes .__cmd[], .cmd, .cmd_len and .sense_len but no other members
        of struct scsi_request.
    :type req: struct scsi_request \*

.. This file was automatic generated / don't edit.

