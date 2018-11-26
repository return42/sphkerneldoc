.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/sd.c

.. _`sd_setup_write_same_cmnd`:

sd_setup_write_same_cmnd
========================

.. c:function:: int sd_setup_write_same_cmnd(struct scsi_cmnd *cmd)

    write the same data to multiple blocks

    :param cmd:
        command to prepare
    :type cmd: struct scsi_cmnd \*

.. _`sd_setup_write_same_cmnd.description`:

Description
-----------

Will set up either WRITE SAME(10) or WRITE SAME(16) depending on
the preference indicated by the target device.

.. _`sd_open`:

sd_open
=======

.. c:function:: int sd_open(struct block_device *bdev, fmode_t mode)

    open a scsi disk device

    :param bdev:
        Block device of the scsi disk to open
    :type bdev: struct block_device \*

    :param mode:
        FMODE\_\* mask
    :type mode: fmode_t

.. _`sd_open.description`:

Description
-----------

Returns 0 if successful. Returns a negated errno value in case
of error.

.. _`sd_open.note`:

Note
----

This can be called from a user context (e.g. fsck(1) )
or from within the kernel (e.g. as a result of a mount(1) ).
In the latter case \ ``inode``\  and \ ``filp``\  carry an abridged amount
of information as noted above.

.. _`sd_open.locking`:

Locking
-------

called with bdev->bd_mutex held.

.. _`sd_release`:

sd_release
==========

.. c:function:: void sd_release(struct gendisk *disk, fmode_t mode)

    invoked when the (last) close(2) is called on this scsi disk.

    :param disk:
        disk to release
    :type disk: struct gendisk \*

    :param mode:
        FMODE\_\* mask
    :type mode: fmode_t

.. _`sd_release.description`:

Description
-----------

Returns 0.

.. _`sd_release.note`:

Note
----

may block (uninterruptible) if error recovery is underway
on this disk.

.. _`sd_release.locking`:

Locking
-------

called with bdev->bd_mutex held.

.. _`sd_ioctl`:

sd_ioctl
========

.. c:function:: int sd_ioctl(struct block_device *bdev, fmode_t mode, unsigned int cmd, unsigned long arg)

    process an ioctl

    :param bdev:
        target block device
    :type bdev: struct block_device \*

    :param mode:
        FMODE\_\* mask
    :type mode: fmode_t

    :param cmd:
        ioctl command number
    :type cmd: unsigned int

    :param arg:
        this is third argument given to ioctl(2) system call.
        Often contains a pointer.
    :type arg: unsigned long

.. _`sd_ioctl.description`:

Description
-----------

Returns 0 if successful (some ioctls return positive numbers on
success as well). Returns a negated errno value in case of error.

.. _`sd_ioctl.note`:

Note
----

most ioctls are forward onto the block subsystem or further
down in the scsi subsystem.

.. _`sd_check_events`:

sd_check_events
===============

.. c:function:: unsigned int sd_check_events(struct gendisk *disk, unsigned int clearing)

    check media events

    :param disk:
        kernel device descriptor
    :type disk: struct gendisk \*

    :param clearing:
        disk events currently being cleared
    :type clearing: unsigned int

.. _`sd_check_events.description`:

Description
-----------

Returns mask of DISK_EVENT\_\*.

.. _`sd_check_events.note`:

Note
----

this function is invoked from the block subsystem.

.. _`sd_eh_reset`:

sd_eh_reset
===========

.. c:function:: void sd_eh_reset(struct scsi_cmnd *scmd)

    reset error handling callback

    :param scmd:
        sd-issued command that has failed
    :type scmd: struct scsi_cmnd \*

.. _`sd_eh_reset.description`:

Description
-----------

This function is called by the SCSI midlayer before starting
SCSI EH. When counting medium access failures we have to be
careful to register it only only once per device and SCSI EH run;
there might be several timed out commands which will cause the
'max_medium_access_timeouts' counter to trigger after the first
SCSI EH run already and set the device to offline.
So this function resets the internal counter before starting SCSI EH.

.. _`sd_eh_action`:

sd_eh_action
============

.. c:function:: int sd_eh_action(struct scsi_cmnd *scmd, int eh_disp)

    error handling callback

    :param scmd:
        sd-issued command that has failed
    :type scmd: struct scsi_cmnd \*

    :param eh_disp:
        The recovery disposition suggested by the midlayer
    :type eh_disp: int

.. _`sd_eh_action.description`:

Description
-----------

This function is called by the SCSI midlayer upon completion of an
error test command (currently TEST UNIT READY). The result of sending
the eh command is passed in eh_disp.  We're looking for devices that
fail medium access commands but are OK with non access commands like
test unit ready (so wrongly see the device as having a successful
recovery)

.. _`sd_done`:

sd_done
=======

.. c:function:: int sd_done(struct scsi_cmnd *SCpnt)

    bottom half handler: called when the lower level driver has completed (successfully or otherwise) a scsi command.

    :param SCpnt:
        mid-level's per command structure.
    :type SCpnt: struct scsi_cmnd \*

.. _`sd_done.note`:

Note
----

potentially run from within an ISR. Must not block.

.. _`sd_read_block_limits`:

sd_read_block_limits
====================

.. c:function:: void sd_read_block_limits(struct scsi_disk *sdkp)

    Query disk device for preferred I/O sizes.

    :param sdkp:
        disk to query
    :type sdkp: struct scsi_disk \*

.. _`sd_read_block_characteristics`:

sd_read_block_characteristics
=============================

.. c:function:: void sd_read_block_characteristics(struct scsi_disk *sdkp)

    Query block dev. characteristics

    :param sdkp:
        disk to query
    :type sdkp: struct scsi_disk \*

.. _`sd_read_block_provisioning`:

sd_read_block_provisioning
==========================

.. c:function:: void sd_read_block_provisioning(struct scsi_disk *sdkp)

    Query provisioning VPD page

    :param sdkp:
        disk to query
    :type sdkp: struct scsi_disk \*

.. _`sd_revalidate_disk`:

sd_revalidate_disk
==================

.. c:function:: int sd_revalidate_disk(struct gendisk *disk)

    called the first time a new disk is seen, performs disk spin up, read_capacity, etc.

    :param disk:
        struct gendisk we care about
    :type disk: struct gendisk \*

.. _`sd_unlock_native_capacity`:

sd_unlock_native_capacity
=========================

.. c:function:: void sd_unlock_native_capacity(struct gendisk *disk)

    unlock native capacity

    :param disk:
        struct gendisk to set capacity for
    :type disk: struct gendisk \*

.. _`sd_unlock_native_capacity.description`:

Description
-----------

Block layer calls this function if it detects that partitions
on \ ``disk``\  reach beyond the end of the device.  If the SCSI host
implements ->unlock_native_capacity() method, it's invoked to
give it a chance to adjust the device capacity.

.. _`sd_unlock_native_capacity.context`:

Context
-------

Defined by block layer.  Might sleep.

.. _`sd_format_disk_name`:

sd_format_disk_name
===================

.. c:function:: int sd_format_disk_name(char *prefix, int index, char *buf, int buflen)

    format disk name

    :param prefix:
        name prefix - ie. "sd" for SCSI disks
    :type prefix: char \*

    :param index:
        index of the disk to format name for
    :type index: int

    :param buf:
        output buffer
    :type buf: char \*

    :param buflen:
        length of the output buffer
    :type buflen: int

.. _`sd_format_disk_name.description`:

Description
-----------

SCSI disk names starts at sda.  The 26th device is sdz and the
27th is sdaa.  The last one for two lettered suffix is sdzz
which is followed by sdaaa.

This is basically 26 base counting with one extra 'nil' entry
at the beginning from the second digit on and can be
determined using similar method as 26 base conversion with the
index shifted -1 after each digit is computed.

.. _`sd_format_disk_name.context`:

Context
-------

Don't care.

.. _`sd_format_disk_name.return`:

Return
------

0 on success, -errno on failure.

.. _`sd_probe`:

sd_probe
========

.. c:function:: int sd_probe(struct device *dev)

    called during driver initialization and whenever a new scsi device is attached to the system. It is called once for each scsi device (not just disks) present.

    :param dev:
        pointer to device object
    :type dev: struct device \*

.. _`sd_probe.description`:

Description
-----------

Returns 0 if successful (or not interested in this scsi device
(e.g. scanner)); 1 when there is an error.

.. _`sd_probe.note`:

Note
----

this function is invoked from the scsi mid-level.
This function sets up the mapping between a given
<host,channel,id,lun> (found in sdp) and new device name
(e.g. /dev/sda). More precisely it is the block device major
and minor number that is chosen here.

Assume sd_probe is not re-entrant (for time being)
Also think about \ :c:func:`sd_probe`\  and \ :c:func:`sd_remove`\  running coincidentally.

.. _`sd_remove`:

sd_remove
=========

.. c:function:: int sd_remove(struct device *dev)

    called whenever a scsi disk (previously recognized by sd_probe) is detached from the system. It is called (potentially multiple times) during sd module unload.

    :param dev:
        pointer to device object
    :type dev: struct device \*

.. _`sd_remove.note`:

Note
----

this function is invoked from the scsi mid-level.
This function potentially frees up a device name (e.g. /dev/sdc)
that could be re-used by a subsequent \ :c:func:`sd_probe`\ .
This function is not called when the built-in sd driver is "exit-ed".

.. _`scsi_disk_release`:

scsi_disk_release
=================

.. c:function:: void scsi_disk_release(struct device *dev)

    Called to free the scsi_disk structure

    :param dev:
        pointer to embedded class device
    :type dev: struct device \*

.. _`scsi_disk_release.description`:

Description
-----------

sd_ref_mutex must be held entering this routine.  Because it is
called on last put, you should always use the \ :c:func:`scsi_disk_get`\ 
\ :c:func:`scsi_disk_put`\  helpers which manipulate the semaphore directly
and never do a direct put_device.

.. _`init_sd`:

init_sd
=======

.. c:function:: int init_sd( void)

    entry point for this driver (both when built in or when a module).

    :param void:
        no arguments
    :type void: 

.. _`init_sd.note`:

Note
----

this function registers this driver with the scsi mid-level.

.. _`exit_sd`:

exit_sd
=======

.. c:function:: void __exit exit_sd( void)

    exit point for this driver (when it is a module).

    :param void:
        no arguments
    :type void: 

.. _`exit_sd.note`:

Note
----

this function unregisters this driver from the scsi mid-level.

.. This file was automatic generated / don't edit.

