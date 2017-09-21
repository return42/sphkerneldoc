.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi.c

.. _`scsi_put_command`:

scsi_put_command
================

.. c:function:: void scsi_put_command(struct scsi_cmnd *cmd)

    Free a scsi command block

    :param struct scsi_cmnd \*cmd:
        command block to free

.. _`scsi_put_command.return`:

Return
------

Nothing.

.. _`scsi_put_command.notes`:

Notes
-----

The command must not belong to any lists.

.. _`scsi_cmd_get_serial`:

scsi_cmd_get_serial
===================

.. c:function:: void scsi_cmd_get_serial(struct Scsi_Host *host, struct scsi_cmnd *cmd)

    Assign a serial number to a command

    :param struct Scsi_Host \*host:
        the scsi host

    :param struct scsi_cmnd \*cmd:
        command to assign serial number to

.. _`scsi_cmd_get_serial.description`:

Description
-----------

a serial number identifies a request for error recovery
and debugging purposes.  Protected by the Host_Lock of host.

.. _`scsi_finish_command`:

scsi_finish_command
===================

.. c:function:: void scsi_finish_command(struct scsi_cmnd *cmd)

    cleanup and pass command back to upper layer

    :param struct scsi_cmnd \*cmd:
        the command

.. _`scsi_finish_command.description`:

Description
-----------

Pass command off to upper layer for finishing of I/O
             request, waking processes that are waiting on results,
             etc.

.. _`scsi_change_queue_depth`:

scsi_change_queue_depth
=======================

.. c:function:: int scsi_change_queue_depth(struct scsi_device *sdev, int depth)

    change a device's queue depth

    :param struct scsi_device \*sdev:
        SCSI Device in question

    :param int depth:
        number of commands allowed to be queued to the driver

.. _`scsi_change_queue_depth.description`:

Description
-----------

Sets the device queue depth and returns the new value.

.. _`scsi_track_queue_full`:

scsi_track_queue_full
=====================

.. c:function:: int scsi_track_queue_full(struct scsi_device *sdev, int depth)

    track QUEUE_FULL events to adjust queue depth

    :param struct scsi_device \*sdev:
        SCSI Device in question

    :param int depth:
        Current number of outstanding SCSI commands on this device,
        not counting the one returned as QUEUE_FULL.

.. _`scsi_track_queue_full.description`:

Description
-----------

This function will track successive QUEUE_FULL events on a
             specific SCSI device to determine if and when there is a
             need to adjust the queue depth on the device.

.. _`scsi_track_queue_full.return`:

Return
------

0 - No change needed, >0 - Adjust queue depth to this new depth,
             -1 - Drop back to untagged operation using host->cmd_per_lun
                     as the untagged command depth

Lock Status: None held on entry

.. _`scsi_track_queue_full.notes`:

Notes
-----

Low level drivers may call this at any time and we will do
             "The Right Thing."  We are interrupt context safe.

.. _`scsi_vpd_inquiry`:

scsi_vpd_inquiry
================

.. c:function:: int scsi_vpd_inquiry(struct scsi_device *sdev, unsigned char *buffer, u8 page, unsigned len)

    Request a device provide us with a VPD page

    :param struct scsi_device \*sdev:
        The device to ask

    :param unsigned char \*buffer:
        Where to put the result

    :param u8 page:
        Which Vital Product Data to return

    :param unsigned len:
        The length of the buffer

.. _`scsi_vpd_inquiry.description`:

Description
-----------

This is an internal helper function.  You probably want to use
scsi_get_vpd_page instead.

Returns size of the vpd page on success or a negative error number.

.. _`scsi_get_vpd_page`:

scsi_get_vpd_page
=================

.. c:function:: int scsi_get_vpd_page(struct scsi_device *sdev, u8 page, unsigned char *buf, int buf_len)

    Get Vital Product Data from a SCSI device

    :param struct scsi_device \*sdev:
        The device to ask

    :param u8 page:
        Which Vital Product Data to return

    :param unsigned char \*buf:
        where to store the VPD

    :param int buf_len:
        number of bytes in the VPD buffer area

.. _`scsi_get_vpd_page.description`:

Description
-----------

SCSI devices may optionally supply Vital Product Data.  Each 'page'
of VPD is defined in the appropriate SCSI document (eg SPC, SBC).
If the device supports this VPD page, this routine returns a pointer
to a buffer containing the data from that page.  The caller is
responsible for calling \ :c:func:`kfree`\  on this pointer when it is no longer
needed.  If we cannot retrieve the VPD page this routine returns \ ``NULL``\ .

.. _`scsi_get_vpd_buf`:

scsi_get_vpd_buf
================

.. c:function:: struct scsi_vpd *scsi_get_vpd_buf(struct scsi_device *sdev, u8 page)

    Get Vital Product Data from a SCSI device

    :param struct scsi_device \*sdev:
        The device to ask

    :param u8 page:
        Which Vital Product Data to return

.. _`scsi_get_vpd_buf.description`:

Description
-----------

Returns \ ``NULL``\  upon failure.

.. _`scsi_attach_vpd`:

scsi_attach_vpd
===============

.. c:function:: void scsi_attach_vpd(struct scsi_device *sdev)

    Attach Vital Product Data to a SCSI device structure

    :param struct scsi_device \*sdev:
        The device to ask

.. _`scsi_attach_vpd.description`:

Description
-----------

Attach the 'Device Identification' VPD page (0x83) and the
'Unit Serial Number' VPD page (0x80) to a SCSI device
structure. This information can be used to identify the device
uniquely.

.. _`scsi_report_opcode`:

scsi_report_opcode
==================

.. c:function:: int scsi_report_opcode(struct scsi_device *sdev, unsigned char *buffer, unsigned int len, unsigned char opcode)

    Find out if a given command opcode is supported

    :param struct scsi_device \*sdev:
        scsi device to query

    :param unsigned char \*buffer:
        scratch buffer (must be at least 20 bytes long)

    :param unsigned int len:
        length of buffer

    :param unsigned char opcode:
        opcode for command to look up

.. _`scsi_report_opcode.description`:

Description
-----------

Uses the REPORT SUPPORTED OPERATION CODES to look up the given
opcode. Returns -EINVAL if RSOC fails, 0 if the command opcode is
unsupported and 1 if the device claims to support the command.

.. _`scsi_device_get`:

scsi_device_get
===============

.. c:function:: int scsi_device_get(struct scsi_device *sdev)

    get an additional reference to a scsi_device

    :param struct scsi_device \*sdev:
        device to get a reference to

.. _`scsi_device_get.description`:

Description
-----------

Gets a reference to the scsi_device and increments the use count
of the underlying LLDD module.  You must hold host_lock of the
parent Scsi_Host or already have a reference when calling this.

This will fail if a device is deleted or cancelled, or when the LLD module
is in the process of being unloaded.

.. _`scsi_device_put`:

scsi_device_put
===============

.. c:function:: void scsi_device_put(struct scsi_device *sdev)

    release a reference to a scsi_device

    :param struct scsi_device \*sdev:
        device to release a reference on.

.. _`scsi_device_put.description`:

Description
-----------

Release a reference to the scsi_device and decrements the use
count of the underlying LLDD module.  The device is freed once the last
user vanishes.

.. _`starget_for_each_device`:

starget_for_each_device
=======================

.. c:function:: void starget_for_each_device(struct scsi_target *starget, void *data, void (*fn)(struct scsi_device *, void *))

    helper to walk all devices of a target

    :param struct scsi_target \*starget:
        target whose devices we want to iterate over.

    :param void \*data:
        Opaque passed to each function call.

    :param void (\*fn)(struct scsi_device \*, void \*):
        Function to call on each device

.. _`starget_for_each_device.description`:

Description
-----------

This traverses over each device of \ ``starget``\ .  The devices have
a reference that must be released by scsi_host_put when breaking
out of the loop.

.. _`__starget_for_each_device`:

__starget_for_each_device
=========================

.. c:function:: void __starget_for_each_device(struct scsi_target *starget, void *data, void (*fn)(struct scsi_device *, void *))

    helper to walk all devices of a target (UNLOCKED)

    :param struct scsi_target \*starget:
        target whose devices we want to iterate over.

    :param void \*data:
        parameter for callback \ ``fn``\ ()

    :param void (\*fn)(struct scsi_device \*, void \*):
        callback function that is invoked for each device

.. _`__starget_for_each_device.description`:

Description
-----------

This traverses over each device of \ ``starget``\ .  It does _not_
take a reference on the scsi_device, so the whole loop must be
protected by shost->host_lock.

.. _`__starget_for_each_device.note`:

Note
----

The only reason why drivers would want to use this is because
they need to access the device list in irq context.  Otherwise you
really want to use starget_for_each_device instead.

.. _`__scsi_device_lookup_by_target`:

__scsi_device_lookup_by_target
==============================

.. c:function:: struct scsi_device *__scsi_device_lookup_by_target(struct scsi_target *starget, u64 lun)

    find a device given the target (UNLOCKED)

    :param struct scsi_target \*starget:
        SCSI target pointer

    :param u64 lun:
        SCSI Logical Unit Number

.. _`__scsi_device_lookup_by_target.description`:

Description
-----------

Looks up the scsi_device with the specified \ ``lun``\  for a given
\ ``starget``\ .  The returned scsi_device does not have an additional
reference.  You must hold the host's host_lock over this call and
any access to the returned scsi_device. A scsi_device in state
SDEV_DEL is skipped.

.. _`__scsi_device_lookup_by_target.note`:

Note
----

The only reason why drivers should use this is because
they need to access the device list in irq context.  Otherwise you
really want to use scsi_device_lookup_by_target instead.

.. _`scsi_device_lookup_by_target`:

scsi_device_lookup_by_target
============================

.. c:function:: struct scsi_device *scsi_device_lookup_by_target(struct scsi_target *starget, u64 lun)

    find a device given the target

    :param struct scsi_target \*starget:
        SCSI target pointer

    :param u64 lun:
        SCSI Logical Unit Number

.. _`scsi_device_lookup_by_target.description`:

Description
-----------

Looks up the scsi_device with the specified \ ``lun``\  for a given
\ ``starget``\ .  The returned scsi_device has an additional reference that
needs to be released with scsi_device_put once you're done with it.

.. _`__scsi_device_lookup`:

__scsi_device_lookup
====================

.. c:function:: struct scsi_device *__scsi_device_lookup(struct Scsi_Host *shost, uint channel, uint id, u64 lun)

    find a device given the host (UNLOCKED)

    :param struct Scsi_Host \*shost:
        SCSI host pointer

    :param uint channel:
        SCSI channel (zero if only one channel)

    :param uint id:
        SCSI target number (physical unit number)

    :param u64 lun:
        SCSI Logical Unit Number

.. _`__scsi_device_lookup.description`:

Description
-----------

Looks up the scsi_device with the specified \ ``channel``\ , \ ``id``\ , \ ``lun``\ 
for a given host. The returned scsi_device does not have an additional
reference.  You must hold the host's host_lock over this call and any access
to the returned scsi_device.

.. _`__scsi_device_lookup.note`:

Note
----

The only reason why drivers would want to use this is because
they need to access the device list in irq context.  Otherwise you
really want to use scsi_device_lookup instead.

.. _`scsi_device_lookup`:

scsi_device_lookup
==================

.. c:function:: struct scsi_device *scsi_device_lookup(struct Scsi_Host *shost, uint channel, uint id, u64 lun)

    find a device given the host

    :param struct Scsi_Host \*shost:
        SCSI host pointer

    :param uint channel:
        SCSI channel (zero if only one channel)

    :param uint id:
        SCSI target number (physical unit number)

    :param u64 lun:
        SCSI Logical Unit Number

.. _`scsi_device_lookup.description`:

Description
-----------

Looks up the scsi_device with the specified \ ``channel``\ , \ ``id``\ , \ ``lun``\ 
for a given host.  The returned scsi_device has an additional reference that
needs to be released with scsi_device_put once you're done with it.

.. This file was automatic generated / don't edit.

