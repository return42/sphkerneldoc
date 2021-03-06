.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_scan.c

.. _`scsi_complete_async_scans`:

scsi_complete_async_scans
=========================

.. c:function:: int scsi_complete_async_scans( void)

    Wait for asynchronous scans to complete

    :param void:
        no arguments
    :type void: 

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

    :param sdev:
        scsi device to send command to
    :type sdev: struct scsi_device \*

    :param result:
        area to store the result of the MODE SENSE
    :type result: unsigned char \*

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

    :param starget:
        which target to allocate a \ :c:type:`struct scsi_device <scsi_device>`\  for
    :type starget: struct scsi_target \*

    :param lun:
        which lun
    :type lun: u64

    :param hostdata:
        usually NULL and set by ->slave_alloc instead
    :type hostdata: void \*

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

    :param kref:
        the reap_ref in the target being released
    :type kref: struct kref \*

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

    :param parent:
        parent of the target (need not be a scsi host)
    :type parent: struct device \*

    :param channel:
        target channel number (zero if no channels)
    :type channel: int

    :param id:
        target id number
    :type id: uint

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

    :param starget:
        target to be checked
    :type starget: struct scsi_target \*

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

    :param s:
        INQUIRY result string to sanitize
    :type s: unsigned char \*

    :param len:
        length of the string
    :type len: int

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

.. c:function:: int scsi_probe_lun(struct scsi_device *sdev, unsigned char *inq_result, int result_len, blist_flags_t *bflags)

    probe a single LUN using a SCSI INQUIRY

    :param sdev:
        scsi_device to probe
    :type sdev: struct scsi_device \*

    :param inq_result:
        area to store the INQUIRY result
    :type inq_result: unsigned char \*

    :param result_len:
        len of inq_result
    :type result_len: int

    :param bflags:
        store any bflags found here
    :type bflags: blist_flags_t \*

.. _`scsi_probe_lun.description`:

Description
-----------

    Probe the lun associated with \ ``req``\  using a standard SCSI INQUIRY;

    If the INQUIRY is successful, zero is returned and the
    INQUIRY data is in \ ``inq_result``\ ; the scsi_level and INQUIRY length
    are copied to the scsi_device any flags value is stored in *@bflags.

.. _`scsi_add_lun`:

scsi_add_lun
============

.. c:function:: int scsi_add_lun(struct scsi_device *sdev, unsigned char *inq_result, blist_flags_t *bflags, int async)

    allocate and fully initialze a scsi_device

    :param sdev:
        holds information to be stored in the new scsi_device
    :type sdev: struct scsi_device \*

    :param inq_result:
        holds the result of a previous INQUIRY to the LUN
    :type inq_result: unsigned char \*

    :param bflags:
        black/white list flag
    :type bflags: blist_flags_t \*

    :param async:
        1 if this device is being scanned asynchronously
    :type async: int

.. _`scsi_add_lun.description`:

Description
-----------

    Initialize the scsi_device \ ``sdev``\ .  Optionally set fields based
    on values in *@bflags.

.. _`scsi_add_lun.return`:

Return
------

    SCSI_SCAN_NO_RESPONSE: could not allocate or setup a scsi_device
    SCSI_SCAN_LUN_PRESENT: a new scsi_device was allocated and initialized

.. _`scsi_inq_str`:

scsi_inq_str
============

.. c:function:: unsigned char *scsi_inq_str(unsigned char *buf, unsigned char *inq, unsigned first, unsigned end)

    print INQUIRY data from min to max index, strip trailing whitespace

    :param buf:
        Output buffer with at least end-first+1 bytes of space
    :type buf: unsigned char \*

    :param inq:
        Inquiry buffer (input)
    :type inq: unsigned char \*

    :param first:
        Offset of string into inq
    :type first: unsigned

    :param end:
        Index after last character in inq
    :type end: unsigned

.. _`scsi_probe_and_add_lun`:

scsi_probe_and_add_lun
======================

.. c:function:: int scsi_probe_and_add_lun(struct scsi_target *starget, u64 lun, blist_flags_t *bflagsp, struct scsi_device **sdevp, enum scsi_scan_mode rescan, void *hostdata)

    probe a LUN, if a LUN is found add it

    :param starget:
        pointer to target device structure
    :type starget: struct scsi_target \*

    :param lun:
        LUN of target device
    :type lun: u64

    :param bflagsp:
        store bflags here if not NULL
    :type bflagsp: blist_flags_t \*

    :param sdevp:
        probe the LUN corresponding to this scsi_device
    :type sdevp: struct scsi_device \*\*

    :param rescan:
        if not equal to SCSI_SCAN_INITIAL skip some code only
        needed on first scan
    :type rescan: enum scsi_scan_mode

    :param hostdata:
        passed to \ :c:func:`scsi_alloc_sdev`\ 
    :type hostdata: void \*

.. _`scsi_probe_and_add_lun.description`:

Description
-----------

    Call scsi_probe_lun, if a LUN with an attached device is found,
    allocate and set it up by calling scsi_add_lun.

.. _`scsi_probe_and_add_lun.return`:

Return
------


  - SCSI_SCAN_NO_RESPONSE: could not allocate or setup a scsi_device
  - SCSI_SCAN_TARGET_PRESENT: target responded, but no device is
        attached at the LUN
  - SCSI_SCAN_LUN_PRESENT: a new scsi_device was allocated and initialized

.. _`scsi_sequential_lun_scan`:

scsi_sequential_lun_scan
========================

.. c:function:: void scsi_sequential_lun_scan(struct scsi_target *starget, blist_flags_t bflags, int scsi_level, enum scsi_scan_mode rescan)

    sequentially scan a SCSI target

    :param starget:
        pointer to target structure to scan
    :type starget: struct scsi_target \*

    :param bflags:
        black/white list flag for LUN 0
    :type bflags: blist_flags_t

    :param scsi_level:
        Which version of the standard does this device adhere to
    :type scsi_level: int

    :param rescan:
        passed to \ :c:func:`scsi_probe_add_lun`\ 
    :type rescan: enum scsi_scan_mode

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

.. c:function:: int scsi_report_lun_scan(struct scsi_target *starget, blist_flags_t bflags, enum scsi_scan_mode rescan)

    Scan using SCSI REPORT LUN results

    :param starget:
        which target
    :type starget: struct scsi_target \*

    :param bflags:
        Zero or a mix of BLIST_NOLUN, BLIST_REPORTLUN2, or BLIST_NOREPORTLUN
    :type bflags: blist_flags_t

    :param rescan:
        nonzero if we can skip code only needed on first scan
    :type rescan: enum scsi_scan_mode

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

    :param parent:
        host to scan
    :type parent: struct device \*

    :param channel:
        channel to scan
    :type channel: unsigned int

    :param id:
        target id to scan
    :type id: unsigned int

    :param lun:
        Specific LUN to scan or SCAN_WILD_CARD
    :type lun: u64

    :param rescan:
        passed to LUN scanning routines; SCSI_SCAN_INITIAL for
        no rescan, SCSI_SCAN_RESCAN to rescan existing LUNs,
        and SCSI_SCAN_MANUAL to force scanning even if
        'scan=manual' is set.
    :type rescan: enum scsi_scan_mode

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

    :param shost:
        the host which will be scanned
    :type shost: struct Scsi_Host \*

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

    :param data:
        cookie returned from earlier call to \ :c:func:`scsi_prep_async_scan`\ 
    :type data: struct async_scan_data \*

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

    :param shost:
        adapter to scan
    :type shost: struct Scsi_Host \*

.. _`scsi_get_host_dev`:

scsi_get_host_dev
=================

.. c:function:: struct scsi_device *scsi_get_host_dev(struct Scsi_Host *shost)

    Create a scsi_device that points to the host adapter itself

    :param shost:
        Host that needs a scsi_device
    :type shost: struct Scsi_Host \*

.. _`scsi_get_host_dev.description`:

Description
-----------

Lock status: None assumed.

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

    :param sdev:
        Host device to be freed
    :type sdev: struct scsi_device \*

.. _`scsi_free_host_dev.description`:

Description
-----------

Lock status: None assumed.

.. _`scsi_free_host_dev.return`:

Return
------

Nothing

.. This file was automatic generated / don't edit.

