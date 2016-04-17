.. -*- coding: utf-8; mode: rst -*-

============
scsi_ioctl.c
============


.. _`omax_sb_len`:

OMAX_SB_LEN
===========

.. c:function:: OMAX_SB_LEN ()

    - handle deprecated SCSI_IOCTL_SEND_COMMAND ioctl



.. _`omax_sb_len.description`:

Description
-----------

Send down the scsi command described by ``sic`` to the device below
the request queue ``q``\ .  If ``file`` is non-NULL it's used to perform
fine-grained permission checks that allow users to send down
non-destructive SCSI commands.  If the caller has a struct gendisk
available it should be passed in as ``disk`` to allow the low level
driver to use the information contained in it.  A non-NULL ``disk``
is only allowed if the caller knows that the low level driver doesn't
need it (e.g. in the scsi subsystem).



.. _`omax_sb_len.notes`:

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

