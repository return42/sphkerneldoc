.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_scan.c

.. _`scsi_complete_async_scans`:

scsi_complete_async_scans
=========================

.. c:function:: int scsi_complete_async_scans( void)

    Wait for asynchronous scans to complete

    :param  void:
        no arguments

.. _`scsi_complete_async_scans.description`:

Description
-----------

When this function returns, any host which started scanning before
this function was called will have finished its scan.  Hosts which
started scanning after this function was called may or may not have
finished.

.. _`scsi_unlock_floptical`:

scsi_unlock_floptical
=====================

.. c:function:: void scsi_unlock_floptical(struct scsi_device *sdev, unsigned char *result)

    unlock device via a special MODE SENSE command

    :param struct scsi_device \*sdev:
        scsi device to send command to

    :param unsigned char \*result:
        area to store the result of the MODE SENSE

.. _`scsi_unlock_floptical.description`:

Description
-----------

Send a vendor specific MODE SENSE (not a MODE SELECT) command.
Called for BLIST_KEY devices.

.. _`scsi_alloc_sdev`:

scsi_alloc_sdev
===============

.. c:function:: struct scsi_device *scsi_alloc_sdev(struct scsi_target *starget, u64 lun, void *hostdata)

    allocate and setup a scsi_Device

    :param struct scsi_target \*starget:
        which target to allocate a \ :c:type:`struct scsi_device <scsi_device>` for

    :param u64 lun:
        which lun

    :param void \*hostdata:
        usually NULL and set by ->slave_alloc instead

.. _`scsi_alloc_sdev.description`:

Description
-----------

Allocate, initialize for io, and return a pointer to a scsi_Device.
Stores the \ ``shost``\ , \ ``channel``\ , \ ``id``\ , and \ ``lun``\  in the scsi_Device, and
adds scsi_Device to the appropriate list.

.. _`scsi_alloc_sdev.return-value`:

Return value
------------

scsi_Device pointer, or NULL on failure.

.. _`scsi_target_reap_ref_release`:

scsi_target_reap_ref_release
============================

.. c:function:: void scsi_target_reap_ref_release(struct kref *kref)

    remove target from visibility

    :param struct kref \*kref:
        the reap_ref in the target being released

.. _`scsi_target_reap_ref_release.description`:

Description
-----------

Called on last put of reap_ref, which is the indication that no device
under this target is visible anymore, so render the target invisible in
sysfs.  Note: we have to be in user context here because the target reaps
should be done in places where the scsi device visibility is being removed.

.. _`scsi_alloc_target`:

scsi_alloc_target
=================

.. c:function:: struct scsi_target *scsi_alloc_target(struct device *parent, int channel, uint id)

    allocate a new or find an existing target

    :param struct device \*parent:
        parent of the target (need not be a scsi host)

    :param int channel:
        target channel number (zero if no channels)

    :param uint id:
        target id number

.. _`scsi_alloc_target.description`:

Description
-----------

Return an existing target if one exists, provided it hasn't already
gone into STARGET_DEL state, otherwise allocate a new target.

The target is returned with an incremented reference, so the caller
is responsible for both reaping and doing a last put

.. _`scsi_target_reap`:

scsi_target_reap
================

.. c:function:: void scsi_target_reap(struct scsi_target *starget)

    check to see if target is in use and destroy if not

    :param struct scsi_target \*starget:
        target to be checked

.. _`scsi_target_reap.description`:

Description
-----------

This is used after removing a LUN or doing a last put of the target
it checks atomically that nothing is using the target and removes
it if so.

.. _`scsi_sanitize_inquiry_string`:

scsi_sanitize_inquiry_string
============================

.. c:function:: void scsi_sanitize_inquiry_string(unsigned char *s, int len)

    remove non-graphical chars from an INQUIRY result string

    :param unsigned char \*s:
        INQUIRY result string to sanitize

    :param int len:
        length of the string

.. _`scsi_sanitize_inquiry_string.description`:

Description
-----------

The SCSI spec says that INQUIRY vendor, product, and revision
strings must consist entirely of graphic ASCII characters,
padded on the right with spaces.  Since not all devices obey
this rule, we will replace non-graphic or non-ASCII characters
with spaces.  Exception: a NUL character is interpreted as a
string terminator, so all the following characters are set to
spaces.

.. _`scsi_probe_lun`:

scsi_probe_lun
==============

.. c:function:: int scsi_probe_lun(struct scsi_device *sdev, unsigned char *inq_result, int result_len, int *bflags)

    probe a single LUN using a SCSI INQUIRY

    :param struct scsi_device \*sdev:
        scsi_device to probe

    :param unsigned char \*inq_result:
        area to store the INQUIRY result

    :param int result_len:
        len of inq_result

    :param int \*bflags:
        store any bflags found here

.. _`scsi_probe_lun.description`:

Description
-----------

Probe the lun associated with \ ``req``\  using a standard SCSI INQUIRY;

If the INQUIRY is successful, zero is returned and the
INQUIRY data is in \ ``inq_result``\ ; the scsi_level and INQUIRY length
are copied to the scsi_device any flags value is stored in \*\ ``bflags``\ .

.. _`scsi_add_lun`:

scsi_add_lun
============

.. c:function:: int scsi_add_lun(struct scsi_device *sdev, unsigned char *inq_result, int *bflags, int async)

    allocate and fully initialze a scsi_device

    :param struct scsi_device \*sdev:
        holds information to be stored in the new scsi_device

    :param unsigned char \*inq_result:
        holds the result of a previous INQUIRY to the LUN

    :param int \*bflags:
        black/white list flag

    :param int async:
        1 if this device is being scanned asynchronously

.. _`scsi_add_lun.description`:

Description
-----------

Initialize the scsi_device \ ``sdev``\ .  Optionally set fields based
on values in \*\ ``bflags``\ .

.. _`scsi_add_lun.scsi_scan_no_response`:

SCSI_SCAN_NO_RESPONSE
---------------------

could not allocate or setup a scsi_device

.. _`scsi_add_lun.scsi_scan_lun_present`:

SCSI_SCAN_LUN_PRESENT
---------------------

a new scsi_device was allocated and initialized

.. _`scsi_inq_str`:

scsi_inq_str
============

.. c:function:: unsigned char *scsi_inq_str(unsigned char *buf, unsigned char *inq, unsigned first, unsigned end)

    print INQUIRY data from min to max index, strip trailing whitespace

    :param unsigned char \*buf:
        Output buffer with at least end-first+1 bytes of space

    :param unsigned char \*inq:
        Inquiry buffer (input)

    :param unsigned first:
        Offset of string into inq

    :param unsigned end:
        Index after last character in inq

.. _`scsi_probe_and_add_lun`:

scsi_probe_and_add_lun
======================

.. c:function:: int scsi_probe_and_add_lun(struct scsi_target *starget, u64 lun, int *bflagsp, struct scsi_device **sdevp, enum scsi_scan_mode rescan, void *hostdata)

    probe a LUN, if a LUN is found add it

    :param struct scsi_target \*starget:
        pointer to target device structure

    :param u64 lun:
        LUN of target device

    :param int \*bflagsp:
        store bflags here if not NULL

    :param struct scsi_device \*\*sdevp:
        probe the LUN corresponding to this scsi_device

    :param enum scsi_scan_mode rescan:
        if not equal to SCSI_SCAN_INITIAL skip some code only
        needed on first scan

    :param void \*hostdata:
        passed to \ :c:func:`scsi_alloc_sdev`\ 

.. _`scsi_probe_and_add_lun.description`:

Description
-----------

Call scsi_probe_lun, if a LUN with an attached device is found,
allocate and set it up by calling scsi_add_lun.

.. _`scsi_probe_and_add_lun.scsi_scan_no_response`:

SCSI_SCAN_NO_RESPONSE
---------------------

could not allocate or setup a scsi_device

.. _`scsi_probe_and_add_lun.scsi_scan_target_present`:

SCSI_SCAN_TARGET_PRESENT
------------------------

target responded, but no device is
attached at the LUN

.. _`scsi_probe_and_add_lun.scsi_scan_lun_present`:

SCSI_SCAN_LUN_PRESENT
---------------------

a new scsi_device was allocated and initialized

.. _`scsi_sequential_lun_scan`:

scsi_sequential_lun_scan
========================

.. c:function:: void scsi_sequential_lun_scan(struct scsi_target *starget, int bflags, int scsi_level, enum scsi_scan_mode rescan)

    sequentially scan a SCSI target

    :param struct scsi_target \*starget:
        pointer to target structure to scan

    :param int bflags:
        black/white list flag for LUN 0

    :param int scsi_level:
        Which version of the standard does this device adhere to

    :param enum scsi_scan_mode rescan:
        passed to \ :c:func:`scsi_probe_add_lun`\ 

.. _`scsi_sequential_lun_scan.description`:

Description
-----------

Generally, scan from LUN 1 (LUN 0 is assumed to already have been
scanned) to some maximum lun until a LUN is found with no device
attached. Use the bflags to figure out any oddities.

Modifies sdevscan->lun.

.. _`scsi_report_lun_scan`:

scsi_report_lun_scan
====================

.. c:function:: int scsi_report_lun_scan(struct scsi_target *starget, int bflags, enum scsi_scan_mode rescan)

    Scan using SCSI REPORT LUN results

    :param struct scsi_target \*starget:
        which target

    :param int bflags:
        Zero or a mix of BLIST_NOLUN, BLIST_REPORTLUN2, or BLIST_NOREPORTLUN

    :param enum scsi_scan_mode rescan:
        nonzero if we can skip code only needed on first scan

.. _`scsi_report_lun_scan.description`:

Description
-----------

Fast scanning for modern (SCSI-3) devices by sending a REPORT LUN command.
Scan the resulting list of LUNs by calling scsi_probe_and_add_lun.

If BLINK_REPORTLUN2 is set, scan a target that supports more than 8
LUNs even if it's older than SCSI-3.
If BLIST_NOREPORTLUN is set, return 1 always.
If BLIST_NOLUN is set, return 0 always.
If starget->no_report_luns is set, return 1 always.

.. _`scsi_report_lun_scan.return`:

Return
------

0: scan completed (or no memory, so further scanning is futile)
1: could not scan with REPORT LUN

.. _`scsi_scan_target`:

scsi_scan_target
================

.. c:function:: void scsi_scan_target(struct device *parent, unsigned int channel, unsigned int id, u64 lun, enum scsi_scan_mode rescan)

    scan a target id, possibly including all LUNs on the target.

    :param struct device \*parent:
        host to scan

    :param unsigned int channel:
        channel to scan

    :param unsigned int id:
        target id to scan

    :param u64 lun:
        Specific LUN to scan or SCAN_WILD_CARD

    :param enum scsi_scan_mode rescan:
        passed to LUN scanning routines; SCSI_SCAN_INITIAL for
        no rescan, SCSI_SCAN_RESCAN to rescan existing LUNs,
        and SCSI_SCAN_MANUAL to force scanning even if
        'scan=manual' is set.

.. _`scsi_scan_target.description`:

Description
-----------

Scan the target id on \ ``parent``\ , \ ``channel``\ , and \ ``id``\ . Scan at least LUN 0,
and possibly all LUNs on the target id.

First try a REPORT LUN scan, if that does not scan the target, do a
sequential scan of LUNs on the target id.

.. _`scsi_prep_async_scan`:

scsi_prep_async_scan
====================

.. c:function:: struct async_scan_data *scsi_prep_async_scan(struct Scsi_Host *shost)

    prepare for an async scan

    :param struct Scsi_Host \*shost:
        the host which will be scanned

.. _`scsi_prep_async_scan.return`:

Return
------

a cookie to be passed to \ :c:func:`scsi_finish_async_scan`\ 

Tells the midlayer this host is going to do an asynchronous scan.
It reserves the host's position in the scanning list and ensures
that other asynchronous scans started after this one won't affect the
ordering of the discovered devices.

.. _`scsi_finish_async_scan`:

scsi_finish_async_scan
======================

.. c:function:: void scsi_finish_async_scan(struct async_scan_data *data)

    asynchronous scan has finished

    :param struct async_scan_data \*data:
        cookie returned from earlier call to \ :c:func:`scsi_prep_async_scan`\ 

.. _`scsi_finish_async_scan.description`:

Description
-----------

All the devices currently attached to this host have been found.
This function announces all the devices it has found to the rest
of the system.

.. _`scsi_scan_host`:

scsi_scan_host
==============

.. c:function:: void scsi_scan_host(struct Scsi_Host *shost)

    scan the given adapter

    :param struct Scsi_Host \*shost:
        adapter to scan

.. _`scsi_get_host_dev`:

scsi_get_host_dev
=================

.. c:function:: struct scsi_device *scsi_get_host_dev(struct Scsi_Host *shost)

    Create a scsi_device that points to the host adapter itself

    :param struct Scsi_Host \*shost:
        Host that needs a scsi_device

.. _`scsi_get_host_dev.lock-status`:

Lock status
-----------

None assumed.

.. _`scsi_get_host_dev.return`:

Return
------

The scsi_device or NULL

.. _`scsi_get_host_dev.notes`:

Notes
-----

Attach a single scsi_device to the Scsi_Host - this should
be made to look like a "pseudo-device" that points to the
HA itself.

Note - this device is not accessible from any high-level
drivers (including generics), which is probably not
optimal.  We can add hooks later to attach.

.. _`scsi_free_host_dev`:

scsi_free_host_dev
==================

.. c:function:: void scsi_free_host_dev(struct scsi_device *sdev)

    Free a scsi_device that points to the host adapter itself

    :param struct scsi_device \*sdev:
        Host device to be freed

.. _`scsi_free_host_dev.lock-status`:

Lock status
-----------

None assumed.

.. _`scsi_free_host_dev.return`:

Return
------

Nothing

.. This file was automatic generated / don't edit.

