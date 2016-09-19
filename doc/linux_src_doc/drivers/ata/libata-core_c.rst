.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/libata-core.c

.. _`ata_link_next`:

ata_link_next
=============

.. c:function:: struct ata_link *ata_link_next(struct ata_link *link, struct ata_port *ap, enum ata_link_iter_mode mode)

    link iteration helper

    :param struct ata_link \*link:
        the previous link, NULL to start

    :param struct ata_port \*ap:
        ATA port containing links to iterate

    :param enum ata_link_iter_mode mode:
        iteration mode, one of ATA_LITER\_\*

.. _`ata_link_next.locking`:

LOCKING
-------

Host lock or EH context.

.. _`ata_link_next.return`:

Return
------

Pointer to the next link.

.. _`ata_dev_next`:

ata_dev_next
============

.. c:function:: struct ata_device *ata_dev_next(struct ata_device *dev, struct ata_link *link, enum ata_dev_iter_mode mode)

    device iteration helper

    :param struct ata_device \*dev:
        the previous device, NULL to start

    :param struct ata_link \*link:
        ATA link containing devices to iterate

    :param enum ata_dev_iter_mode mode:
        iteration mode, one of ATA_DITER\_\*

.. _`ata_dev_next.locking`:

LOCKING
-------

Host lock or EH context.

.. _`ata_dev_next.return`:

Return
------

Pointer to the next device.

.. _`ata_dev_phys_link`:

ata_dev_phys_link
=================

.. c:function:: struct ata_link *ata_dev_phys_link(struct ata_device *dev)

    find physical link for a device

    :param struct ata_device \*dev:
        ATA device to look up physical link for

.. _`ata_dev_phys_link.description`:

Description
-----------

Look up physical link which \ ``dev``\  is attached to.  Note that
this is different from \ ``dev``\ ->link only when \ ``dev``\  is on slave
link.  For all other cases, it's the same as \ ``dev``\ ->link.

.. _`ata_dev_phys_link.locking`:

LOCKING
-------

Don't care.

.. _`ata_dev_phys_link.return`:

Return
------

Pointer to the found physical link.

.. _`ata_force_cbl`:

ata_force_cbl
=============

.. c:function:: void ata_force_cbl(struct ata_port *ap)

    force cable type according to libata.force

    :param struct ata_port \*ap:
        ATA port of interest

.. _`ata_force_cbl.description`:

Description
-----------

Force cable type according to libata.force and whine about it.
The last entry which has matching port number is used, so it
can be specified as part of device force parameters.  For
example, both "a:40c,1.00:udma4" and "1.00:40c,udma4" have the
same effect.

.. _`ata_force_cbl.locking`:

LOCKING
-------

EH context.

.. _`ata_force_link_limits`:

ata_force_link_limits
=====================

.. c:function:: void ata_force_link_limits(struct ata_link *link)

    force link limits according to libata.force

    :param struct ata_link \*link:
        ATA link of interest

.. _`ata_force_link_limits.description`:

Description
-----------

Force link flags and SATA spd limit according to libata.force
and whine about it.  When only the port part is specified
(e.g. 1:), the limit applies to all links connected to both
the host link and all fan-out ports connected via PMP.  If the
device part is specified as 0 (e.g. 1.00:), it specifies the
first fan-out link not the host link.  Device number 15 always
points to the host link whether PMP is attached or not.  If the
controller has slave link, device number 16 points to it.

.. _`ata_force_link_limits.locking`:

LOCKING
-------

EH context.

.. _`ata_force_xfermask`:

ata_force_xfermask
==================

.. c:function:: void ata_force_xfermask(struct ata_device *dev)

    force xfermask according to libata.force

    :param struct ata_device \*dev:
        ATA device of interest

.. _`ata_force_xfermask.description`:

Description
-----------

Force xfer_mask according to libata.force and whine about it.
For consistency with link selection, device number 15 selects
the first device connected to the host link.

.. _`ata_force_xfermask.locking`:

LOCKING
-------

EH context.

.. _`ata_force_horkage`:

ata_force_horkage
=================

.. c:function:: void ata_force_horkage(struct ata_device *dev)

    force horkage according to libata.force

    :param struct ata_device \*dev:
        ATA device of interest

.. _`ata_force_horkage.description`:

Description
-----------

Force horkage according to libata.force and whine about it.
For consistency with link selection, device number 15 selects
the first device connected to the host link.

.. _`ata_force_horkage.locking`:

LOCKING
-------

EH context.

.. _`atapi_cmd_type`:

atapi_cmd_type
==============

.. c:function:: int atapi_cmd_type(u8 opcode)

    Determine ATAPI command type from SCSI opcode

    :param u8 opcode:
        SCSI opcode

.. _`atapi_cmd_type.description`:

Description
-----------

Determine ATAPI command type from \ ``opcode``\ .

.. _`atapi_cmd_type.locking`:

LOCKING
-------

None.

.. _`atapi_cmd_type.return`:

Return
------

ATAPI_{READ\|WRITE\|READ_CD\|PASS_THRU\|MISC}

.. _`ata_tf_to_fis`:

ata_tf_to_fis
=============

.. c:function:: void ata_tf_to_fis(const struct ata_taskfile *tf, u8 pmp, int is_cmd, u8 *fis)

    Convert ATA taskfile to SATA FIS structure

    :param const struct ata_taskfile \*tf:
        Taskfile to convert

    :param u8 pmp:
        Port multiplier port

    :param int is_cmd:
        This FIS is for command

    :param u8 \*fis:
        Buffer into which data will output

.. _`ata_tf_to_fis.description`:

Description
-----------

Converts a standard ATA taskfile to a Serial ATA
FIS structure (Register - Host to Device).

.. _`ata_tf_to_fis.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_tf_from_fis`:

ata_tf_from_fis
===============

.. c:function:: void ata_tf_from_fis(const u8 *fis, struct ata_taskfile *tf)

    Convert SATA FIS to ATA taskfile

    :param const u8 \*fis:
        Buffer from which data will be input

    :param struct ata_taskfile \*tf:
        Taskfile to output

.. _`ata_tf_from_fis.description`:

Description
-----------

Converts a serial ATA FIS structure to a standard ATA taskfile.

.. _`ata_tf_from_fis.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_rwcmd_protocol`:

ata_rwcmd_protocol
==================

.. c:function:: int ata_rwcmd_protocol(struct ata_taskfile *tf, struct ata_device *dev)

    set taskfile r/w commands and protocol

    :param struct ata_taskfile \*tf:
        command to examine and configure

    :param struct ata_device \*dev:
        device tf belongs to

.. _`ata_rwcmd_protocol.description`:

Description
-----------

Examine the device configuration and tf->flags to calculate
the proper read/write commands and protocol to use.

.. _`ata_rwcmd_protocol.locking`:

LOCKING
-------

caller.

.. _`ata_tf_read_block`:

ata_tf_read_block
=================

.. c:function:: u64 ata_tf_read_block(const struct ata_taskfile *tf, struct ata_device *dev)

    Read block address from ATA taskfile

    :param const struct ata_taskfile \*tf:
        ATA taskfile of interest

    :param struct ata_device \*dev:
        ATA device \ ``tf``\  belongs to

.. _`ata_tf_read_block.locking`:

LOCKING
-------

None.

Read block address from \ ``tf``\ .  This function can handle all
three address formats - LBA, LBA48 and CHS.  tf->protocol and
flags select the address format to use.

.. _`ata_tf_read_block.return`:

Return
------

Block address read from \ ``tf``\ .

.. _`ata_build_rw_tf`:

ata_build_rw_tf
===============

.. c:function:: int ata_build_rw_tf(struct ata_taskfile *tf, struct ata_device *dev, u64 block, u32 n_block, unsigned int tf_flags, unsigned int tag)

    Build ATA taskfile for given read/write request

    :param struct ata_taskfile \*tf:
        Target ATA taskfile

    :param struct ata_device \*dev:
        ATA device \ ``tf``\  belongs to

    :param u64 block:
        Block address

    :param u32 n_block:
        Number of blocks

    :param unsigned int tf_flags:
        RW/FUA etc...

    :param unsigned int tag:
        tag

.. _`ata_build_rw_tf.locking`:

LOCKING
-------

None.

Build ATA taskfile \ ``tf``\  for read/write request described by
\ ``block``\ , \ ``n_block``\ , \ ``tf_flags``\  and \ ``tag``\  on \ ``dev``\ .

.. _`ata_build_rw_tf.return`:

Return
------


0 on success, -ERANGE if the request is too large for \ ``dev``\ ,
-EINVAL if the request is invalid.

.. _`ata_pack_xfermask`:

ata_pack_xfermask
=================

.. c:function:: unsigned long ata_pack_xfermask(unsigned long pio_mask, unsigned long mwdma_mask, unsigned long udma_mask)

    Pack pio, mwdma and udma masks into xfer_mask

    :param unsigned long pio_mask:
        pio_mask

    :param unsigned long mwdma_mask:
        mwdma_mask

    :param unsigned long udma_mask:
        udma_mask

.. _`ata_pack_xfermask.description`:

Description
-----------

Pack \ ``pio_mask``\ , \ ``mwdma_mask``\  and \ ``udma_mask``\  into a single
unsigned int xfer_mask.

.. _`ata_pack_xfermask.locking`:

LOCKING
-------

None.

.. _`ata_pack_xfermask.return`:

Return
------

Packed xfer_mask.

.. _`ata_unpack_xfermask`:

ata_unpack_xfermask
===================

.. c:function:: void ata_unpack_xfermask(unsigned long xfer_mask, unsigned long *pio_mask, unsigned long *mwdma_mask, unsigned long *udma_mask)

    Unpack xfer_mask into pio, mwdma and udma masks

    :param unsigned long xfer_mask:
        xfer_mask to unpack

    :param unsigned long \*pio_mask:
        resulting pio_mask

    :param unsigned long \*mwdma_mask:
        resulting mwdma_mask

    :param unsigned long \*udma_mask:
        resulting udma_mask

.. _`ata_unpack_xfermask.description`:

Description
-----------

Unpack \ ``xfer_mask``\  into \ ``pio_mask``\ , \ ``mwdma_mask``\  and \ ``udma_mask``\ .
Any NULL destination masks will be ignored.

.. _`ata_xfer_mask2mode`:

ata_xfer_mask2mode
==================

.. c:function:: u8 ata_xfer_mask2mode(unsigned long xfer_mask)

    Find matching XFER\_\* for the given xfer_mask

    :param unsigned long xfer_mask:
        xfer_mask of interest

.. _`ata_xfer_mask2mode.description`:

Description
-----------

Return matching XFER\_\* value for \ ``xfer_mask``\ .  Only the highest
bit of \ ``xfer_mask``\  is considered.

.. _`ata_xfer_mask2mode.locking`:

LOCKING
-------

None.

.. _`ata_xfer_mask2mode.return`:

Return
------

Matching XFER\_\* value, 0xff if no match found.

.. _`ata_xfer_mode2mask`:

ata_xfer_mode2mask
==================

.. c:function:: unsigned long ata_xfer_mode2mask(u8 xfer_mode)

    Find matching xfer_mask for XFER\_\*

    :param u8 xfer_mode:
        XFER\_\* of interest

.. _`ata_xfer_mode2mask.description`:

Description
-----------

Return matching xfer_mask for \ ``xfer_mode``\ .

.. _`ata_xfer_mode2mask.locking`:

LOCKING
-------

None.

.. _`ata_xfer_mode2mask.return`:

Return
------

Matching xfer_mask, 0 if no match found.

.. _`ata_xfer_mode2shift`:

ata_xfer_mode2shift
===================

.. c:function:: int ata_xfer_mode2shift(unsigned long xfer_mode)

    Find matching xfer_shift for XFER\_\*

    :param unsigned long xfer_mode:
        XFER\_\* of interest

.. _`ata_xfer_mode2shift.description`:

Description
-----------

Return matching xfer_shift for \ ``xfer_mode``\ .

.. _`ata_xfer_mode2shift.locking`:

LOCKING
-------

None.

.. _`ata_xfer_mode2shift.return`:

Return
------

Matching xfer_shift, -1 if no match found.

.. _`ata_mode_string`:

ata_mode_string
===============

.. c:function:: const char *ata_mode_string(unsigned long xfer_mask)

    convert xfer_mask to string

    :param unsigned long xfer_mask:
        mask of bits supported; only highest bit counts.

.. _`ata_mode_string.description`:

Description
-----------

Determine string which represents the highest speed
(highest bit in \ ``modemask``\ ).

.. _`ata_mode_string.locking`:

LOCKING
-------

None.

.. _`ata_mode_string.return`:

Return
------

Constant C string representing highest speed listed in
\ ``mode_mask``\ , or the constant C string "<n/a>".

.. _`ata_dev_classify`:

ata_dev_classify
================

.. c:function:: unsigned int ata_dev_classify(const struct ata_taskfile *tf)

    determine device type based on ATA-spec signature

    :param const struct ata_taskfile \*tf:
        ATA taskfile register set for device to be identified

.. _`ata_dev_classify.description`:

Description
-----------

Determine from taskfile register contents whether a device is
ATA or ATAPI, as per "Signature and persistence" section
of ATA/PI spec (volume 1, sect 5.14).

.. _`ata_dev_classify.locking`:

LOCKING
-------

None.

.. _`ata_dev_classify.return`:

Return
------

Device type, \ ``ATA_DEV_ATA``\ , \ ``ATA_DEV_ATAPI``\ , \ ``ATA_DEV_PMP``\ ,
\ ``ATA_DEV_ZAC``\ , or \ ``ATA_DEV_UNKNOWN``\  the event of failure.

.. _`ata_id_string`:

ata_id_string
=============

.. c:function:: void ata_id_string(const u16 *id, unsigned char *s, unsigned int ofs, unsigned int len)

    Convert IDENTIFY DEVICE page into string

    :param const u16 \*id:
        IDENTIFY DEVICE results we will examine

    :param unsigned char \*s:
        string into which data is output

    :param unsigned int ofs:
        offset into identify device page

    :param unsigned int len:
        length of string to return. must be an even number.

.. _`ata_id_string.description`:

Description
-----------

The strings in the IDENTIFY DEVICE page are broken up into
16-bit chunks.  Run through the string, and output each
8-bit chunk linearly, regardless of platform.

.. _`ata_id_string.locking`:

LOCKING
-------

caller.

.. _`ata_id_c_string`:

ata_id_c_string
===============

.. c:function:: void ata_id_c_string(const u16 *id, unsigned char *s, unsigned int ofs, unsigned int len)

    Convert IDENTIFY DEVICE page into C string

    :param const u16 \*id:
        IDENTIFY DEVICE results we will examine

    :param unsigned char \*s:
        string into which data is output

    :param unsigned int ofs:
        offset into identify device page

    :param unsigned int len:
        length of string to return. must be an odd number.

.. _`ata_id_c_string.description`:

Description
-----------

This function is identical to ata_id_string except that it
trims trailing spaces and terminates the resulting string with
null.  \ ``len``\  must be actual maximum length (even number) + 1.

.. _`ata_id_c_string.locking`:

LOCKING
-------

caller.

.. _`ata_read_native_max_address`:

ata_read_native_max_address
===========================

.. c:function:: int ata_read_native_max_address(struct ata_device *dev, u64 *max_sectors)

    Read native max address

    :param struct ata_device \*dev:
        target device

    :param u64 \*max_sectors:
        out parameter for the result native max address

.. _`ata_read_native_max_address.description`:

Description
-----------

Perform an LBA48 or LBA28 native size query upon the device in
question.

.. _`ata_read_native_max_address.return`:

Return
------

0 on success, -EACCES if command is aborted by the drive.
-EIO on other errors.

.. _`ata_set_max_sectors`:

ata_set_max_sectors
===================

.. c:function:: int ata_set_max_sectors(struct ata_device *dev, u64 new_sectors)

    Set max sectors

    :param struct ata_device \*dev:
        target device

    :param u64 new_sectors:
        new max sectors value to set for the device

.. _`ata_set_max_sectors.description`:

Description
-----------

Set max sectors of \ ``dev``\  to \ ``new_sectors``\ .

.. _`ata_set_max_sectors.return`:

Return
------

0 on success, -EACCES if command is aborted or denied (due to
previous non-volatile SET_MAX) by the drive.  -EIO on other
errors.

.. _`ata_hpa_resize`:

ata_hpa_resize
==============

.. c:function:: int ata_hpa_resize(struct ata_device *dev)

    Resize a device with an HPA set

    :param struct ata_device \*dev:
        Device to resize

.. _`ata_hpa_resize.description`:

Description
-----------

Read the size of an LBA28 or LBA48 disk with HPA features and resize
it if required to the full size of the media. The caller must check
the drive has the HPA feature set enabled.

.. _`ata_hpa_resize.return`:

Return
------

0 on success, -errno on failure.

.. _`ata_dump_id`:

ata_dump_id
===========

.. c:function:: void ata_dump_id(const u16 *id)

    IDENTIFY DEVICE info debugging output

    :param const u16 \*id:
        IDENTIFY DEVICE page to dump

.. _`ata_dump_id.description`:

Description
-----------

Dump selected 16-bit words from the given IDENTIFY DEVICE
page.

.. _`ata_dump_id.locking`:

LOCKING
-------

caller.

.. _`ata_id_xfermask`:

ata_id_xfermask
===============

.. c:function:: unsigned long ata_id_xfermask(const u16 *id)

    Compute xfermask from the given IDENTIFY data

    :param const u16 \*id:
        IDENTIFY data to compute xfer mask from

.. _`ata_id_xfermask.description`:

Description
-----------

Compute the xfermask for this device. This is not as trivial
as it seems if we must consider early devices correctly.

.. _`ata_id_xfermask.fixme`:

FIXME
-----

pre IDE drive timing (do we care ?).

.. _`ata_id_xfermask.locking`:

LOCKING
-------

None.

.. _`ata_id_xfermask.return`:

Return
------

Computed xfermask

.. _`ata_exec_internal_sg`:

ata_exec_internal_sg
====================

.. c:function:: unsigned ata_exec_internal_sg(struct ata_device *dev, struct ata_taskfile *tf, const u8 *cdb, int dma_dir, struct scatterlist *sgl, unsigned int n_elem, unsigned long timeout)

    execute libata internal command

    :param struct ata_device \*dev:
        Device to which the command is sent

    :param struct ata_taskfile \*tf:
        Taskfile registers for the command and the result

    :param const u8 \*cdb:
        CDB for packet command

    :param int dma_dir:
        Data transfer direction of the command

    :param struct scatterlist \*sgl:
        sg list for the data buffer of the command

    :param unsigned int n_elem:
        Number of sg entries

    :param unsigned long timeout:
        Timeout in msecs (0 for default)

.. _`ata_exec_internal_sg.description`:

Description
-----------

Executes libata internal command with timeout.  \ ``tf``\  contains
command on entry and result on return.  Timeout and error
conditions are reported via return value.  No recovery action
is taken after a command times out.  It's caller's duty to
clean up after timeout.

.. _`ata_exec_internal_sg.locking`:

LOCKING
-------

None.  Should be called with kernel context, might sleep.

.. _`ata_exec_internal_sg.return`:

Return
------

Zero on success, AC_ERR\_\* mask on failure

.. _`ata_exec_internal`:

ata_exec_internal
=================

.. c:function:: unsigned ata_exec_internal(struct ata_device *dev, struct ata_taskfile *tf, const u8 *cdb, int dma_dir, void *buf, unsigned int buflen, unsigned long timeout)

    execute libata internal command

    :param struct ata_device \*dev:
        Device to which the command is sent

    :param struct ata_taskfile \*tf:
        Taskfile registers for the command and the result

    :param const u8 \*cdb:
        CDB for packet command

    :param int dma_dir:
        Data transfer direction of the command

    :param void \*buf:
        Data buffer of the command

    :param unsigned int buflen:
        Length of data buffer

    :param unsigned long timeout:
        Timeout in msecs (0 for default)

.. _`ata_exec_internal.description`:

Description
-----------

Wrapper around \ :c:func:`ata_exec_internal_sg`\  which takes simple
buffer instead of sg list.

.. _`ata_exec_internal.locking`:

LOCKING
-------

None.  Should be called with kernel context, might sleep.

.. _`ata_exec_internal.return`:

Return
------

Zero on success, AC_ERR\_\* mask on failure

.. _`ata_pio_need_iordy`:

ata_pio_need_iordy
==================

.. c:function:: unsigned int ata_pio_need_iordy(const struct ata_device *adev)

    check if iordy needed

    :param const struct ata_device \*adev:
        ATA device

.. _`ata_pio_need_iordy.description`:

Description
-----------

Check if the current speed of the device requires IORDY. Used
by various controllers for chip configuration.

.. _`ata_pio_mask_no_iordy`:

ata_pio_mask_no_iordy
=====================

.. c:function:: u32 ata_pio_mask_no_iordy(const struct ata_device *adev)

    Return the non IORDY mask

    :param const struct ata_device \*adev:
        ATA device

.. _`ata_pio_mask_no_iordy.description`:

Description
-----------

Compute the highest mode possible if we are not using iordy. Return
-1 if no iordy mode is available.

.. _`ata_do_dev_read_id`:

ata_do_dev_read_id
==================

.. c:function:: unsigned int ata_do_dev_read_id(struct ata_device *dev, struct ata_taskfile *tf, u16 *id)

    default ID read method

    :param struct ata_device \*dev:
        device

    :param struct ata_taskfile \*tf:
        proposed taskfile

    :param u16 \*id:
        data buffer

.. _`ata_do_dev_read_id.description`:

Description
-----------

Issue the identify taskfile and hand back the buffer containing
identify data. For some RAID controllers and for pre ATA devices
this function is wrapped or replaced by the driver

.. _`ata_dev_read_id`:

ata_dev_read_id
===============

.. c:function:: int ata_dev_read_id(struct ata_device *dev, unsigned int *p_class, unsigned int flags, u16 *id)

    Read ID data from the specified device

    :param struct ata_device \*dev:
        target device

    :param unsigned int \*p_class:
        pointer to class of the target device (may be changed)

    :param unsigned int flags:
        ATA_READID\_\* flags

    :param u16 \*id:
        buffer to read IDENTIFY data into

.. _`ata_dev_read_id.description`:

Description
-----------

Read ID data from the specified device.  ATA_CMD_ID_ATA is
performed on ATA devices and ATA_CMD_ID_ATAPI on ATAPI
devices.  This function also issues ATA_CMD_INIT_DEV_PARAMS
for pre-ATA4 drives.

.. _`ata_dev_read_id.fixme`:

FIXME
-----

ATA_CMD_ID_ATA is optional for early drives and right
now we abort if we hit that case.

.. _`ata_dev_read_id.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`ata_dev_read_id.return`:

Return
------

0 on success, -errno otherwise.

.. _`ata_dev_configure`:

ata_dev_configure
=================

.. c:function:: int ata_dev_configure(struct ata_device *dev)

    Configure the specified ATA/ATAPI device

    :param struct ata_device \*dev:
        Target device to configure

.. _`ata_dev_configure.description`:

Description
-----------

Configure \ ``dev``\  according to \ ``dev``\ ->id.  Generic and low-level
driver specific fixups are also applied.

.. _`ata_dev_configure.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`ata_dev_configure.return`:

Return
------

0 on success, -errno otherwise

.. _`ata_cable_40wire`:

ata_cable_40wire
================

.. c:function:: int ata_cable_40wire(struct ata_port *ap)

    return 40 wire cable type

    :param struct ata_port \*ap:
        port

.. _`ata_cable_40wire.description`:

Description
-----------

Helper method for drivers which want to hardwire 40 wire cable
detection.

.. _`ata_cable_80wire`:

ata_cable_80wire
================

.. c:function:: int ata_cable_80wire(struct ata_port *ap)

    return 80 wire cable type

    :param struct ata_port \*ap:
        port

.. _`ata_cable_80wire.description`:

Description
-----------

Helper method for drivers which want to hardwire 80 wire cable
detection.

.. _`ata_cable_unknown`:

ata_cable_unknown
=================

.. c:function:: int ata_cable_unknown(struct ata_port *ap)

    return unknown PATA cable.

    :param struct ata_port \*ap:
        port

.. _`ata_cable_unknown.description`:

Description
-----------

Helper method for drivers which have no PATA cable detection.

.. _`ata_cable_ignore`:

ata_cable_ignore
================

.. c:function:: int ata_cable_ignore(struct ata_port *ap)

    return ignored PATA cable.

    :param struct ata_port \*ap:
        port

.. _`ata_cable_ignore.description`:

Description
-----------

Helper method for drivers which don't use cable type to limit
transfer mode.

.. _`ata_cable_sata`:

ata_cable_sata
==============

.. c:function:: int ata_cable_sata(struct ata_port *ap)

    return SATA cable type

    :param struct ata_port \*ap:
        port

.. _`ata_cable_sata.description`:

Description
-----------

Helper method for drivers which have SATA cables

.. _`ata_bus_probe`:

ata_bus_probe
=============

.. c:function:: int ata_bus_probe(struct ata_port *ap)

    Reset and probe ATA bus

    :param struct ata_port \*ap:
        Bus to probe

.. _`ata_bus_probe.description`:

Description
-----------

Master ATA bus probing function.  Initiates a hardware-dependent
bus reset, then attempts to identify any devices found on
the bus.

.. _`ata_bus_probe.locking`:

LOCKING
-------

PCI/etc. bus probe sem.

.. _`ata_bus_probe.return`:

Return
------

Zero on success, negative errno otherwise.

.. _`sata_print_link_status`:

sata_print_link_status
======================

.. c:function:: void sata_print_link_status(struct ata_link *link)

    Print SATA link status

    :param struct ata_link \*link:
        SATA link to printk link status about

.. _`sata_print_link_status.description`:

Description
-----------

This function prints link speed and status of a SATA link.

.. _`sata_print_link_status.locking`:

LOCKING
-------

None.

.. _`ata_dev_pair`:

ata_dev_pair
============

.. c:function:: struct ata_device *ata_dev_pair(struct ata_device *adev)

    return other device on cable

    :param struct ata_device \*adev:
        device

.. _`ata_dev_pair.description`:

Description
-----------

Obtain the other device on the same cable, or if none is
present NULL is returned

.. _`sata_down_spd_limit`:

sata_down_spd_limit
===================

.. c:function:: int sata_down_spd_limit(struct ata_link *link, u32 spd_limit)

    adjust SATA spd limit downward

    :param struct ata_link \*link:
        Link to adjust SATA spd limit for

    :param u32 spd_limit:
        Additional limit

.. _`sata_down_spd_limit.description`:

Description
-----------

Adjust SATA spd limit of \ ``link``\  downward.  Note that this
function only adjusts the limit.  The change must be applied
using \ :c:func:`sata_set_spd`\ .

If \ ``spd_limit``\  is non-zero, the speed is limited to equal to or
lower than \ ``spd_limit``\  if such speed is supported.  If
\ ``spd_limit``\  is slower than any supported speed, only the lowest
supported speed is allowed.

.. _`sata_down_spd_limit.locking`:

LOCKING
-------

Inherited from caller.

.. _`sata_down_spd_limit.return`:

Return
------

0 on success, negative errno on failure

.. _`sata_set_spd_needed`:

sata_set_spd_needed
===================

.. c:function:: int sata_set_spd_needed(struct ata_link *link)

    is SATA spd configuration needed

    :param struct ata_link \*link:
        Link in question

.. _`sata_set_spd_needed.description`:

Description
-----------

Test whether the spd limit in SControl matches
\ ``link``\ ->sata_spd_limit.  This function is used to determine
whether hardreset is necessary to apply SATA spd
configuration.

.. _`sata_set_spd_needed.locking`:

LOCKING
-------

Inherited from caller.

.. _`sata_set_spd_needed.return`:

Return
------

1 if SATA spd configuration is needed, 0 otherwise.

.. _`sata_set_spd`:

sata_set_spd
============

.. c:function:: int sata_set_spd(struct ata_link *link)

    set SATA spd according to spd limit

    :param struct ata_link \*link:
        Link to set SATA spd for

.. _`sata_set_spd.description`:

Description
-----------

Set SATA spd of \ ``link``\  according to sata_spd_limit.

.. _`sata_set_spd.locking`:

LOCKING
-------

Inherited from caller.

.. _`sata_set_spd.return`:

Return
------

0 if spd doesn't need to be changed, 1 if spd has been
changed.  Negative errno if SCR registers are inaccessible.

.. _`ata_timing_cycle2mode`:

ata_timing_cycle2mode
=====================

.. c:function:: u8 ata_timing_cycle2mode(unsigned int xfer_shift, int cycle)

    find xfer mode for the specified cycle duration

    :param unsigned int xfer_shift:
        ATA_SHIFT\_\* value for transfer type to examine.

    :param int cycle:
        cycle duration in ns

.. _`ata_timing_cycle2mode.description`:

Description
-----------

Return matching xfer mode for \ ``cycle``\ .  The returned mode is of
the transfer type specified by \ ``xfer_shift``\ .  If \ ``cycle``\  is too
slow for \ ``xfer_shift``\ , 0xff is returned.  If \ ``cycle``\  is faster
than the fastest known mode, the fasted mode is returned.

.. _`ata_timing_cycle2mode.locking`:

LOCKING
-------

None.

.. _`ata_timing_cycle2mode.return`:

Return
------

Matching xfer_mode, 0xff if no match found.

.. _`ata_down_xfermask_limit`:

ata_down_xfermask_limit
=======================

.. c:function:: int ata_down_xfermask_limit(struct ata_device *dev, unsigned int sel)

    adjust dev xfer masks downward

    :param struct ata_device \*dev:
        Device to adjust xfer masks

    :param unsigned int sel:
        ATA_DNXFER\_\* selector

.. _`ata_down_xfermask_limit.description`:

Description
-----------

Adjust xfer masks of \ ``dev``\  downward.  Note that this function
does not apply the change.  Invoking \ :c:func:`ata_set_mode`\  afterwards
will apply the limit.

.. _`ata_down_xfermask_limit.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_down_xfermask_limit.return`:

Return
------

0 on success, negative errno on failure

.. _`ata_do_set_mode`:

ata_do_set_mode
===============

.. c:function:: int ata_do_set_mode(struct ata_link *link, struct ata_device **r_failed_dev)

    Program timings and issue SET FEATURES - XFER

    :param struct ata_link \*link:
        link on which timings will be programmed

    :param struct ata_device \*\*r_failed_dev:
        out parameter for failed device

.. _`ata_do_set_mode.description`:

Description
-----------

Standard implementation of the function used to tune and set
ATA device disk transfer mode (PIO3, UDMA6, etc.).  If
\ :c:func:`ata_dev_set_mode`\  fails, pointer to the failing device is
returned in \ ``r_failed_dev``\ .

.. _`ata_do_set_mode.locking`:

LOCKING
-------

PCI/etc. bus probe sem.

.. _`ata_do_set_mode.return`:

Return
------

0 on success, negative errno otherwise

.. _`ata_wait_ready`:

ata_wait_ready
==============

.. c:function:: int ata_wait_ready(struct ata_link *link, unsigned long deadline, int (*check_ready)(struct ata_link *link))

    wait for link to become ready

    :param struct ata_link \*link:
        link to be waited on

    :param unsigned long deadline:
        deadline jiffies for the operation

    :param int (\*check_ready)(struct ata_link \*link):
        callback to check link readiness

.. _`ata_wait_ready.description`:

Description
-----------

Wait for \ ``link``\  to become ready.  \ ``check_ready``\  should return
positive number if \ ``link``\  is ready, 0 if it isn't, -ENODEV if
link doesn't seem to be occupied, other errno for other error
conditions.

Transient -ENODEV conditions are allowed for
ATA_TMOUT_FF_WAIT.

.. _`ata_wait_ready.locking`:

LOCKING
-------

EH context.

.. _`ata_wait_ready.return`:

Return
------

0 if \ ``link``\  is ready before \ ``deadline``\ ; otherwise, -errno.

.. _`ata_wait_after_reset`:

ata_wait_after_reset
====================

.. c:function:: int ata_wait_after_reset(struct ata_link *link, unsigned long deadline, int (*check_ready)(struct ata_link *link))

    wait for link to become ready after reset

    :param struct ata_link \*link:
        link to be waited on

    :param unsigned long deadline:
        deadline jiffies for the operation

    :param int (\*check_ready)(struct ata_link \*link):
        callback to check link readiness

.. _`ata_wait_after_reset.description`:

Description
-----------

Wait for \ ``link``\  to become ready after reset.

.. _`ata_wait_after_reset.locking`:

LOCKING
-------

EH context.

.. _`ata_wait_after_reset.return`:

Return
------

0 if \ ``link``\  is ready before \ ``deadline``\ ; otherwise, -errno.

.. _`sata_link_debounce`:

sata_link_debounce
==================

.. c:function:: int sata_link_debounce(struct ata_link *link, const unsigned long *params, unsigned long deadline)

    debounce SATA phy status

    :param struct ata_link \*link:
        ATA link to debounce SATA phy status for

    :param const unsigned long \*params:
        timing parameters { interval, duration, timeout } in msec

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`sata_link_debounce.description`:

Description
-----------

Make sure SStatus of \ ``link``\  reaches stable state, determined by
holding the same value where DET is not 1 for \ ``duration``\  polled
every \ ``interval``\ , before \ ``timeout``\ .  Timeout constraints the
beginning of the stable state.  Because DET gets stuck at 1 on
some controllers after hot unplugging, this functions waits
until timeout then returns 0 if DET is stable at 1.

\ ``timeout``\  is further limited by \ ``deadline``\ .  The sooner of the
two is used.

.. _`sata_link_debounce.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`sata_link_debounce.return`:

Return
------

0 on success, -errno on failure.

.. _`sata_link_resume`:

sata_link_resume
================

.. c:function:: int sata_link_resume(struct ata_link *link, const unsigned long *params, unsigned long deadline)

    resume SATA link

    :param struct ata_link \*link:
        ATA link to resume SATA

    :param const unsigned long \*params:
        timing parameters { interval, duration, timeout } in msec

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`sata_link_resume.description`:

Description
-----------

Resume SATA phy \ ``link``\  and debounce it.

.. _`sata_link_resume.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`sata_link_resume.return`:

Return
------

0 on success, -errno on failure.

.. _`sata_link_scr_lpm`:

sata_link_scr_lpm
=================

.. c:function:: int sata_link_scr_lpm(struct ata_link *link, enum ata_lpm_policy policy, bool spm_wakeup)

    manipulate SControl IPM and SPM fields

    :param struct ata_link \*link:
        ATA link to manipulate SControl for

    :param enum ata_lpm_policy policy:
        LPM policy to configure

    :param bool spm_wakeup:
        initiate LPM transition to active state

.. _`sata_link_scr_lpm.description`:

Description
-----------

Manipulate the IPM field of the SControl register of \ ``link``\ 
according to \ ``policy``\ .  If \ ``policy``\  is ATA_LPM_MAX_POWER and
\ ``spm_wakeup``\  is \ ``true``\ , the SPM field is manipulated to wake up
the link.  This function also clears PHYRDY_CHG before
returning.

.. _`sata_link_scr_lpm.locking`:

LOCKING
-------

EH context.

.. _`sata_link_scr_lpm.return`:

Return
------

0 on success, -errno otherwise.

.. _`ata_std_prereset`:

ata_std_prereset
================

.. c:function:: int ata_std_prereset(struct ata_link *link, unsigned long deadline)

    prepare for reset

    :param struct ata_link \*link:
        ATA link to be reset

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`ata_std_prereset.description`:

Description
-----------

\ ``link``\  is about to be reset.  Initialize it.  Failure from
prereset makes libata abort whole reset sequence and give up
that port, so prereset should be best-effort.  It does its
best to prepare for reset sequence but if things go wrong, it
should just whine, not fail.

.. _`ata_std_prereset.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`ata_std_prereset.return`:

Return
------

0 on success, -errno otherwise.

.. _`sata_link_hardreset`:

sata_link_hardreset
===================

.. c:function:: int sata_link_hardreset(struct ata_link *link, const unsigned long *timing, unsigned long deadline, bool *online, int (*check_ready)(struct ata_link *))

    reset link via SATA phy reset

    :param struct ata_link \*link:
        link to reset

    :param const unsigned long \*timing:
        timing parameters { interval, duration, timeout } in msec

    :param unsigned long deadline:
        deadline jiffies for the operation

    :param bool \*online:
        optional out parameter indicating link onlineness

    :param int (\*check_ready)(struct ata_link \*):
        optional callback to check link readiness

.. _`sata_link_hardreset.description`:

Description
-----------

SATA phy-reset \ ``link``\  using DET bits of SControl register.
After hardreset, link readiness is waited upon using
\ :c:func:`ata_wait_ready`\  if \ ``check_ready``\  is specified.  LLDs are
allowed to not specify \ ``check_ready``\  and wait itself after this
function returns.  Device classification is LLD's
responsibility.

\*\ ``online``\  is set to one iff reset succeeded and \ ``link``\  is online
after reset.

.. _`sata_link_hardreset.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`sata_link_hardreset.return`:

Return
------

0 on success, -errno otherwise.

.. _`sata_std_hardreset`:

sata_std_hardreset
==================

.. c:function:: int sata_std_hardreset(struct ata_link *link, unsigned int *class, unsigned long deadline)

    COMRESET w/o waiting or classification

    :param struct ata_link \*link:
        link to reset

    :param unsigned int \*class:
        resulting class of attached device

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`sata_std_hardreset.description`:

Description
-----------

Standard SATA COMRESET w/o waiting or classification.

.. _`sata_std_hardreset.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`sata_std_hardreset.return`:

Return
------

0 if link offline, -EAGAIN if link online, -errno on errors.

.. _`ata_std_postreset`:

ata_std_postreset
=================

.. c:function:: void ata_std_postreset(struct ata_link *link, unsigned int *classes)

    standard postreset callback

    :param struct ata_link \*link:
        the target ata_link

    :param unsigned int \*classes:
        classes of attached devices

.. _`ata_std_postreset.description`:

Description
-----------

This function is invoked after a successful reset.  Note that
the device might have been reset more than once using
different reset methods before postreset is invoked.

.. _`ata_std_postreset.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`ata_dev_same_device`:

ata_dev_same_device
===================

.. c:function:: int ata_dev_same_device(struct ata_device *dev, unsigned int new_class, const u16 *new_id)

    Determine whether new ID matches configured device

    :param struct ata_device \*dev:
        device to compare against

    :param unsigned int new_class:
        class of the new device

    :param const u16 \*new_id:
        IDENTIFY page of the new device

.. _`ata_dev_same_device.description`:

Description
-----------

Compare \ ``new_class``\  and \ ``new_id``\  against \ ``dev``\  and determine
whether \ ``dev``\  is the device indicated by \ ``new_class``\  and
\ ``new_id``\ .

.. _`ata_dev_same_device.locking`:

LOCKING
-------

None.

.. _`ata_dev_same_device.return`:

Return
------

1 if \ ``dev``\  matches \ ``new_class``\  and \ ``new_id``\ , 0 otherwise.

.. _`ata_dev_reread_id`:

ata_dev_reread_id
=================

.. c:function:: int ata_dev_reread_id(struct ata_device *dev, unsigned int readid_flags)

    Re-read IDENTIFY data

    :param struct ata_device \*dev:
        target ATA device

    :param unsigned int readid_flags:
        read ID flags

.. _`ata_dev_reread_id.description`:

Description
-----------

Re-read IDENTIFY page and make sure \ ``dev``\  is still attached to
the port.

.. _`ata_dev_reread_id.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`ata_dev_reread_id.return`:

Return
------

0 on success, negative errno otherwise

.. _`ata_dev_revalidate`:

ata_dev_revalidate
==================

.. c:function:: int ata_dev_revalidate(struct ata_device *dev, unsigned int new_class, unsigned int readid_flags)

    Revalidate ATA device

    :param struct ata_device \*dev:
        device to revalidate

    :param unsigned int new_class:
        new class code

    :param unsigned int readid_flags:
        read ID flags

.. _`ata_dev_revalidate.description`:

Description
-----------

Re-read IDENTIFY page, make sure \ ``dev``\  is still attached to the
port and reconfigure it according to the new IDENTIFY page.

.. _`ata_dev_revalidate.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`ata_dev_revalidate.return`:

Return
------

0 on success, negative errno otherwise

.. _`ata_is_40wire`:

ata_is_40wire
=============

.. c:function:: int ata_is_40wire(struct ata_device *dev)

    check drive side detection

    :param struct ata_device \*dev:
        device

.. _`ata_is_40wire.description`:

Description
-----------

Perform drive side detection decoding, allowing for device vendors
who can't follow the documentation.

.. _`cable_is_40wire`:

cable_is_40wire
===============

.. c:function:: int cable_is_40wire(struct ata_port *ap)

    40/80/SATA decider

    :param struct ata_port \*ap:
        port to consider

.. _`cable_is_40wire.description`:

Description
-----------

This function encapsulates the policy for speed management
in one place. At the moment we don't cache the result but
there is a good case for setting ap->cbl to the result when
we are called with unknown cables (and figuring out if it
impacts hotplug at all).

Return 1 if the cable appears to be 40 wire.

.. _`ata_dev_xfermask`:

ata_dev_xfermask
================

.. c:function:: void ata_dev_xfermask(struct ata_device *dev)

    Compute supported xfermask of the given device

    :param struct ata_device \*dev:
        Device to compute xfermask for

.. _`ata_dev_xfermask.description`:

Description
-----------

Compute supported xfermask of \ ``dev``\  and store it in
dev->\*\_mask.  This function is responsible for applying all
known limits including host controller limits, device
blacklist, etc...

.. _`ata_dev_xfermask.locking`:

LOCKING
-------

None.

.. _`ata_dev_set_xfermode`:

ata_dev_set_xfermode
====================

.. c:function:: unsigned int ata_dev_set_xfermode(struct ata_device *dev)

    Issue SET FEATURES - XFER MODE command

    :param struct ata_device \*dev:
        Device to which command will be sent

.. _`ata_dev_set_xfermode.description`:

Description
-----------

Issue SET FEATURES - XFER MODE command to device \ ``dev``\ 
on port \ ``ap``\ .

.. _`ata_dev_set_xfermode.locking`:

LOCKING
-------

PCI/etc. bus probe sem.

.. _`ata_dev_set_xfermode.return`:

Return
------

0 on success, AC_ERR\_\* mask otherwise.

.. _`ata_dev_set_feature`:

ata_dev_set_feature
===================

.. c:function:: unsigned int ata_dev_set_feature(struct ata_device *dev, u8 enable, u8 feature)

    Issue SET FEATURES - SATA FEATURES

    :param struct ata_device \*dev:
        Device to which command will be sent

    :param u8 enable:
        Whether to enable or disable the feature

    :param u8 feature:
        The sector count represents the feature to set

.. _`ata_dev_set_feature.description`:

Description
-----------

Issue SET FEATURES - SATA FEATURES command to device \ ``dev``\ 
on port \ ``ap``\  with sector count

.. _`ata_dev_set_feature.locking`:

LOCKING
-------

PCI/etc. bus probe sem.

.. _`ata_dev_set_feature.return`:

Return
------

0 on success, AC_ERR\_\* mask otherwise.

.. _`ata_dev_init_params`:

ata_dev_init_params
===================

.. c:function:: unsigned int ata_dev_init_params(struct ata_device *dev, u16 heads, u16 sectors)

    Issue INIT DEV PARAMS command

    :param struct ata_device \*dev:
        Device to which command will be sent

    :param u16 heads:
        Number of heads (taskfile parameter)

    :param u16 sectors:
        Number of sectors (taskfile parameter)

.. _`ata_dev_init_params.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`ata_dev_init_params.return`:

Return
------

0 on success, AC_ERR\_\* mask otherwise.

.. _`ata_sg_clean`:

ata_sg_clean
============

.. c:function:: void ata_sg_clean(struct ata_queued_cmd *qc)

    Unmap DMA memory associated with command

    :param struct ata_queued_cmd \*qc:
        Command containing DMA memory to be released

.. _`ata_sg_clean.description`:

Description
-----------

Unmap all mapped DMA memory associated with this command.

.. _`ata_sg_clean.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`atapi_check_dma`:

atapi_check_dma
===============

.. c:function:: int atapi_check_dma(struct ata_queued_cmd *qc)

    Check whether ATAPI DMA can be supported

    :param struct ata_queued_cmd \*qc:
        Metadata associated with taskfile to check

.. _`atapi_check_dma.description`:

Description
-----------

Allow low-level driver to filter ATA PACKET commands, returning
a status indicating whether or not it is OK to use DMA for the
supplied PACKET command.

.. _`atapi_check_dma.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`atapi_check_dma.return`:

Return
------

0 when ATAPI DMA can be used
nonzero otherwise

.. _`ata_std_qc_defer`:

ata_std_qc_defer
================

.. c:function:: int ata_std_qc_defer(struct ata_queued_cmd *qc)

    Check whether a qc needs to be deferred

    :param struct ata_queued_cmd \*qc:
        ATA command in question

.. _`ata_std_qc_defer.description`:

Description
-----------

Non-NCQ commands cannot run with any other command, NCQ or
not.  As upper layer only knows the queue depth, we are
responsible for maintaining exclusion.  This function checks
whether a new command \ ``qc``\  can be issued.

.. _`ata_std_qc_defer.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_std_qc_defer.return`:

Return
------

ATA_DEFER\_\* if deferring is needed, 0 otherwise.

.. _`ata_sg_init`:

ata_sg_init
===========

.. c:function:: void ata_sg_init(struct ata_queued_cmd *qc, struct scatterlist *sg, unsigned int n_elem)

    Associate command with scatter-gather table.

    :param struct ata_queued_cmd \*qc:
        Command to be associated

    :param struct scatterlist \*sg:
        Scatter-gather table.

    :param unsigned int n_elem:
        Number of elements in s/g table.

.. _`ata_sg_init.description`:

Description
-----------

Initialize the data-related elements of queued_cmd \ ``qc``\ 
to point to a scatter-gather table \ ``sg``\ , containing \ ``n_elem``\ 
elements.

.. _`ata_sg_init.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_sg_setup`:

ata_sg_setup
============

.. c:function:: int ata_sg_setup(struct ata_queued_cmd *qc)

    DMA-map the scatter-gather table associated with a command.

    :param struct ata_queued_cmd \*qc:
        Command with scatter-gather table to be mapped.

.. _`ata_sg_setup.description`:

Description
-----------

DMA-map the scatter-gather table associated with queued_cmd \ ``qc``\ .

.. _`ata_sg_setup.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_sg_setup.return`:

Return
------

Zero on success, negative on error.

.. _`swap_buf_le16`:

swap_buf_le16
=============

.. c:function:: void swap_buf_le16(u16 *buf, unsigned int buf_words)

    swap halves of 16-bit words in place

    :param u16 \*buf:
        Buffer to swap

    :param unsigned int buf_words:
        Number of 16-bit words in buffer.

.. _`swap_buf_le16.description`:

Description
-----------

Swap halves of 16-bit words if needed to convert from
little-endian byte order to native cpu byte order, or
vice-versa.

.. _`swap_buf_le16.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_qc_new_init`:

ata_qc_new_init
===============

.. c:function:: struct ata_queued_cmd *ata_qc_new_init(struct ata_device *dev, int tag)

    Request an available ATA command, and initialize it

    :param struct ata_device \*dev:
        Device from whom we request an available command structure

    :param int tag:
        tag

.. _`ata_qc_new_init.locking`:

LOCKING
-------

None.

.. _`ata_qc_free`:

ata_qc_free
===========

.. c:function:: void ata_qc_free(struct ata_queued_cmd *qc)

    free unused ata_queued_cmd

    :param struct ata_queued_cmd \*qc:
        Command to complete

.. _`ata_qc_free.description`:

Description
-----------

Designed to free unused ata_queued_cmd object
in case something prevents using it.

.. _`ata_qc_free.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_qc_complete`:

ata_qc_complete
===============

.. c:function:: void ata_qc_complete(struct ata_queued_cmd *qc)

    Complete an active ATA command

    :param struct ata_queued_cmd \*qc:
        Command to complete

.. _`ata_qc_complete.description`:

Description
-----------

Indicate to the mid and upper layers that an ATA command has
completed, with either an ok or not-ok status.

Refrain from calling this function multiple times when
successfully completing multiple NCQ commands.
\ :c:func:`ata_qc_complete_multiple`\  should be used instead, which will
properly update IRQ expect state.

.. _`ata_qc_complete.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_qc_complete_multiple`:

ata_qc_complete_multiple
========================

.. c:function:: int ata_qc_complete_multiple(struct ata_port *ap, u32 qc_active)

    Complete multiple qcs successfully

    :param struct ata_port \*ap:
        port in question

    :param u32 qc_active:
        new qc_active mask

.. _`ata_qc_complete_multiple.description`:

Description
-----------

Complete in-flight commands.  This functions is meant to be
called from low-level driver's interrupt routine to complete
requests normally.  ap->qc_active and \ ``qc_active``\  is compared
and commands are completed accordingly.

Always use this function when completing multiple NCQ commands
from IRQ handlers instead of calling \ :c:func:`ata_qc_complete`\ 
multiple times to keep IRQ expect status properly in sync.

.. _`ata_qc_complete_multiple.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_qc_complete_multiple.return`:

Return
------

Number of completed commands on success, -errno otherwise.

.. _`ata_qc_issue`:

ata_qc_issue
============

.. c:function:: void ata_qc_issue(struct ata_queued_cmd *qc)

    issue taskfile to device

    :param struct ata_queued_cmd \*qc:
        command to issue to device

.. _`ata_qc_issue.description`:

Description
-----------

Prepare an ATA command to submission to device.
This includes mapping the data into a DMA-able
area, filling in the S/G table, and finally
writing the taskfile to hardware, starting the command.

.. _`ata_qc_issue.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`sata_scr_valid`:

sata_scr_valid
==============

.. c:function:: int sata_scr_valid(struct ata_link *link)

    test whether SCRs are accessible

    :param struct ata_link \*link:
        ATA link to test SCR accessibility for

.. _`sata_scr_valid.description`:

Description
-----------

Test whether SCRs are accessible for \ ``link``\ .

.. _`sata_scr_valid.locking`:

LOCKING
-------

None.

.. _`sata_scr_valid.return`:

Return
------

1 if SCRs are accessible, 0 otherwise.

.. _`sata_scr_read`:

sata_scr_read
=============

.. c:function:: int sata_scr_read(struct ata_link *link, int reg, u32 *val)

    read SCR register of the specified port

    :param struct ata_link \*link:
        ATA link to read SCR for

    :param int reg:
        SCR to read

    :param u32 \*val:
        Place to store read value

.. _`sata_scr_read.description`:

Description
-----------

Read SCR register \ ``reg``\  of \ ``link``\  into \*\ ``val``\ .  This function is
guaranteed to succeed if \ ``link``\  is ap->link, the cable type of
the port is SATA and the port implements ->scr_read.

.. _`sata_scr_read.locking`:

LOCKING
-------

None if \ ``link``\  is ap->link.  Kernel thread context otherwise.

.. _`sata_scr_read.return`:

Return
------

0 on success, negative errno on failure.

.. _`sata_scr_write`:

sata_scr_write
==============

.. c:function:: int sata_scr_write(struct ata_link *link, int reg, u32 val)

    write SCR register of the specified port

    :param struct ata_link \*link:
        ATA link to write SCR for

    :param int reg:
        SCR to write

    :param u32 val:
        value to write

.. _`sata_scr_write.description`:

Description
-----------

Write \ ``val``\  to SCR register \ ``reg``\  of \ ``link``\ .  This function is
guaranteed to succeed if \ ``link``\  is ap->link, the cable type of
the port is SATA and the port implements ->scr_read.

.. _`sata_scr_write.locking`:

LOCKING
-------

None if \ ``link``\  is ap->link.  Kernel thread context otherwise.

.. _`sata_scr_write.return`:

Return
------

0 on success, negative errno on failure.

.. _`sata_scr_write_flush`:

sata_scr_write_flush
====================

.. c:function:: int sata_scr_write_flush(struct ata_link *link, int reg, u32 val)

    write SCR register of the specified port and flush

    :param struct ata_link \*link:
        ATA link to write SCR for

    :param int reg:
        SCR to write

    :param u32 val:
        value to write

.. _`sata_scr_write_flush.description`:

Description
-----------

This function is identical to \ :c:func:`sata_scr_write`\  except that this
function performs flush after writing to the register.

.. _`sata_scr_write_flush.locking`:

LOCKING
-------

None if \ ``link``\  is ap->link.  Kernel thread context otherwise.

.. _`sata_scr_write_flush.return`:

Return
------

0 on success, negative errno on failure.

.. _`ata_phys_link_online`:

ata_phys_link_online
====================

.. c:function:: bool ata_phys_link_online(struct ata_link *link)

    test whether the given link is online

    :param struct ata_link \*link:
        ATA link to test

.. _`ata_phys_link_online.description`:

Description
-----------

Test whether \ ``link``\  is online.  Note that this function returns
0 if online status of \ ``link``\  cannot be obtained, so
ata_link_online(link) != !ata_link_offline(link).

.. _`ata_phys_link_online.locking`:

LOCKING
-------

None.

.. _`ata_phys_link_online.return`:

Return
------

True if the port online status is available and online.

.. _`ata_phys_link_offline`:

ata_phys_link_offline
=====================

.. c:function:: bool ata_phys_link_offline(struct ata_link *link)

    test whether the given link is offline

    :param struct ata_link \*link:
        ATA link to test

.. _`ata_phys_link_offline.description`:

Description
-----------

Test whether \ ``link``\  is offline.  Note that this function
returns 0 if offline status of \ ``link``\  cannot be obtained, so
ata_link_online(link) != !ata_link_offline(link).

.. _`ata_phys_link_offline.locking`:

LOCKING
-------

None.

.. _`ata_phys_link_offline.return`:

Return
------

True if the port offline status is available and offline.

.. _`ata_link_online`:

ata_link_online
===============

.. c:function:: bool ata_link_online(struct ata_link *link)

    test whether the given link is online

    :param struct ata_link \*link:
        ATA link to test

.. _`ata_link_online.description`:

Description
-----------

Test whether \ ``link``\  is online.  This is identical to
\ :c:func:`ata_phys_link_online`\  when there's no slave link.  When
there's a slave link, this function should only be called on
the master link and will return true if any of M/S links is
online.

.. _`ata_link_online.locking`:

LOCKING
-------

None.

.. _`ata_link_online.return`:

Return
------

True if the port online status is available and online.

.. _`ata_link_offline`:

ata_link_offline
================

.. c:function:: bool ata_link_offline(struct ata_link *link)

    test whether the given link is offline

    :param struct ata_link \*link:
        ATA link to test

.. _`ata_link_offline.description`:

Description
-----------

Test whether \ ``link``\  is offline.  This is identical to
\ :c:func:`ata_phys_link_offline`\  when there's no slave link.  When
there's a slave link, this function should only be called on
the master link and will return true if both M/S links are
offline.

.. _`ata_link_offline.locking`:

LOCKING
-------

None.

.. _`ata_link_offline.return`:

Return
------

True if the port offline status is available and offline.

.. _`ata_host_suspend`:

ata_host_suspend
================

.. c:function:: int ata_host_suspend(struct ata_host *host, pm_message_t mesg)

    suspend host

    :param struct ata_host \*host:
        host to suspend

    :param pm_message_t mesg:
        PM message

.. _`ata_host_suspend.description`:

Description
-----------

Suspend \ ``host``\ .  Actual operation is performed by port suspend.

.. _`ata_host_resume`:

ata_host_resume
===============

.. c:function:: void ata_host_resume(struct ata_host *host)

    resume host

    :param struct ata_host \*host:
        host to resume

.. _`ata_host_resume.description`:

Description
-----------

Resume \ ``host``\ .  Actual operation is performed by port resume.

.. _`ata_dev_init`:

ata_dev_init
============

.. c:function:: void ata_dev_init(struct ata_device *dev)

    Initialize an ata_device structure

    :param struct ata_device \*dev:
        Device structure to initialize

.. _`ata_dev_init.description`:

Description
-----------

Initialize \ ``dev``\  in preparation for probing.

.. _`ata_dev_init.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_link_init`:

ata_link_init
=============

.. c:function:: void ata_link_init(struct ata_port *ap, struct ata_link *link, int pmp)

    Initialize an ata_link structure

    :param struct ata_port \*ap:
        ATA port link is attached to

    :param struct ata_link \*link:
        Link structure to initialize

    :param int pmp:
        Port multiplier port number

.. _`ata_link_init.description`:

Description
-----------

Initialize \ ``link``\ .

.. _`ata_link_init.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`sata_link_init_spd`:

sata_link_init_spd
==================

.. c:function:: int sata_link_init_spd(struct ata_link *link)

    Initialize link->sata_spd_limit

    :param struct ata_link \*link:
        Link to configure sata_spd_limit for

.. _`sata_link_init_spd.description`:

Description
-----------

Initialize \ ``link``\ ->[hw_]sata_spd_limit to the currently
configured value.

.. _`sata_link_init_spd.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`sata_link_init_spd.return`:

Return
------

0 on success, -errno on failure.

.. _`ata_port_alloc`:

ata_port_alloc
==============

.. c:function:: struct ata_port *ata_port_alloc(struct ata_host *host)

    allocate and initialize basic ATA port resources

    :param struct ata_host \*host:
        ATA host this allocated port belongs to

.. _`ata_port_alloc.description`:

Description
-----------

Allocate and initialize basic ATA port resources.

.. _`ata_port_alloc.return`:

Return
------

Allocate ATA port on success, NULL on failure.

.. _`ata_port_alloc.locking`:

LOCKING
-------

Inherited from calling layer (may sleep).

.. _`ata_host_alloc`:

ata_host_alloc
==============

.. c:function:: struct ata_host *ata_host_alloc(struct device *dev, int max_ports)

    allocate and init basic ATA host resources

    :param struct device \*dev:
        generic device this host is associated with

    :param int max_ports:
        maximum number of ATA ports associated with this host

.. _`ata_host_alloc.description`:

Description
-----------

Allocate and initialize basic ATA host resources.  LLD calls
this function to allocate a host, initializes it fully and
attaches it using \ :c:func:`ata_host_register`\ .

\ ``max_ports``\  ports are allocated and host->n_ports is
initialized to \ ``max_ports``\ .  The caller is allowed to decrease
host->n_ports before calling \ :c:func:`ata_host_register`\ .  The unused
ports will be automatically freed on registration.

.. _`ata_host_alloc.return`:

Return
------

Allocate ATA host on success, NULL on failure.

.. _`ata_host_alloc.locking`:

LOCKING
-------

Inherited from calling layer (may sleep).

.. _`ata_host_alloc_pinfo`:

ata_host_alloc_pinfo
====================

.. c:function:: struct ata_host *ata_host_alloc_pinfo(struct device *dev, const struct ata_port_info * const *ppi, int n_ports)

    alloc host and init with port_info array

    :param struct device \*dev:
        generic device this host is associated with

    :param const struct ata_port_info \* const \*ppi:
        array of ATA port_info to initialize host with

    :param int n_ports:
        number of ATA ports attached to this host

.. _`ata_host_alloc_pinfo.description`:

Description
-----------

Allocate ATA host and initialize with info from \ ``ppi``\ .  If NULL
terminated, \ ``ppi``\  may contain fewer entries than \ ``n_ports``\ .  The
last entry will be used for the remaining ports.

.. _`ata_host_alloc_pinfo.return`:

Return
------

Allocate ATA host on success, NULL on failure.

.. _`ata_host_alloc_pinfo.locking`:

LOCKING
-------

Inherited from calling layer (may sleep).

.. _`ata_slave_link_init`:

ata_slave_link_init
===================

.. c:function:: int ata_slave_link_init(struct ata_port *ap)

    initialize slave link

    :param struct ata_port \*ap:
        port to initialize slave link for

.. _`ata_slave_link_init.description`:

Description
-----------

Create and initialize slave link for \ ``ap``\ .  This enables slave
link handling on the port.

In libata, a port contains links and a link contains devices.
There is single host link but if a PMP is attached to it,
there can be multiple fan-out links.  On SATA, there's usually
a single device connected to a link but PATA and SATA
controllers emulating TF based interface can have two - master
and slave.

However, there are a few controllers which don't fit into this
abstraction too well - SATA controllers which emulate TF
interface with both master and slave devices but also have
separate SCR register sets for each device.  These controllers
need separate links for physical link handling
(e.g. onlineness, link speed) but should be treated like a
traditional M/S controller for everything else (e.g. command
issue, softreset).

slave_link is libata's way of handling this class of
controllers without impacting core layer too much.  For
anything other than physical link handling, the default host
link is used for both master and slave.  For physical link
handling, separate \ ``ap``\ ->slave_link is used.  All dirty details
are implemented inside libata core layer.  From LLD's POV, the
only difference is that prereset, hardreset and postreset are
called once more for the slave link, so the reset sequence
looks like the following.

prereset(M) -> prereset(S) -> hardreset(M) -> hardreset(S) ->
softreset(M) -> postreset(M) -> postreset(S)

Note that softreset is called only for the master.  Softreset
resets both M/S by definition, so SRST on master should handle
both (the standard method will work just fine).

.. _`ata_slave_link_init.locking`:

LOCKING
-------

Should be called before host is registered.

.. _`ata_slave_link_init.return`:

Return
------

0 on success, -errno on failure.

.. _`ata_finalize_port_ops`:

ata_finalize_port_ops
=====================

.. c:function:: void ata_finalize_port_ops(struct ata_port_operations *ops)

    finalize ata_port_operations

    :param struct ata_port_operations \*ops:
        ata_port_operations to finalize

.. _`ata_finalize_port_ops.description`:

Description
-----------

An ata_port_operations can inherit from another ops and that
ops can again inherit from another.  This can go on as many
times as necessary as long as there is no loop in the
inheritance chain.

Ops tables are finalized when the host is started.  NULL or
unspecified entries are inherited from the closet ancestor
which has the method and the entry is populated with it.
After finalization, the ops table directly points to all the
methods and ->inherits is no longer necessary and cleared.

Using ATA_OP_NULL, inheriting ops can force a method to NULL.

.. _`ata_finalize_port_ops.locking`:

LOCKING
-------

None.

.. _`ata_host_start`:

ata_host_start
==============

.. c:function:: int ata_host_start(struct ata_host *host)

    start and freeze ports of an ATA host

    :param struct ata_host \*host:
        ATA host to start ports for

.. _`ata_host_start.description`:

Description
-----------

Start and then freeze ports of \ ``host``\ .  Started status is
recorded in host->flags, so this function can be called
multiple times.  Ports are guaranteed to get started only
once.  If host->ops isn't initialized yet, its set to the
first non-dummy port ops.

.. _`ata_host_start.locking`:

LOCKING
-------

Inherited from calling layer (may sleep).

.. _`ata_host_start.return`:

Return
------

0 if all ports are started successfully, -errno otherwise.

.. _`ata_host_init`:

ata_host_init
=============

.. c:function:: void ata_host_init(struct ata_host *host, struct device *dev, struct ata_port_operations *ops)

    Initialize a host struct for sas (ipr, libsas)

    :param struct ata_host \*host:
        host to initialize

    :param struct device \*dev:
        device host is attached to

    :param struct ata_port_operations \*ops:
        port_ops

.. _`ata_host_register`:

ata_host_register
=================

.. c:function:: int ata_host_register(struct ata_host *host, struct scsi_host_template *sht)

    register initialized ATA host

    :param struct ata_host \*host:
        ATA host to register

    :param struct scsi_host_template \*sht:
        template for SCSI host

.. _`ata_host_register.description`:

Description
-----------

Register initialized ATA host.  \ ``host``\  is allocated using
\ :c:func:`ata_host_alloc`\  and fully initialized by LLD.  This function
starts ports, registers \ ``host``\  with ATA and SCSI layers and
probe registered devices.

.. _`ata_host_register.locking`:

LOCKING
-------

Inherited from calling layer (may sleep).

.. _`ata_host_register.return`:

Return
------

0 on success, -errno otherwise.

.. _`ata_host_activate`:

ata_host_activate
=================

.. c:function:: int ata_host_activate(struct ata_host *host, int irq, irq_handler_t irq_handler, unsigned long irq_flags, struct scsi_host_template *sht)

    start host, request IRQ and register it

    :param struct ata_host \*host:
        target ATA host

    :param int irq:
        IRQ to request

    :param irq_handler_t irq_handler:
        irq_handler used when requesting IRQ

    :param unsigned long irq_flags:
        irq_flags used when requesting IRQ

    :param struct scsi_host_template \*sht:
        scsi_host_template to use when registering the host

.. _`ata_host_activate.description`:

Description
-----------

After allocating an ATA host and initializing it, most libata
LLDs perform three steps to activate the host - start host,
request IRQ and register it.  This helper takes necessary
arguments and performs the three steps in one go.

An invalid IRQ skips the IRQ registration and expects the host to
have set polling mode on the port. In this case, \ ``irq_handler``\ 
should be NULL.

.. _`ata_host_activate.locking`:

LOCKING
-------

Inherited from calling layer (may sleep).

.. _`ata_host_activate.return`:

Return
------

0 on success, -errno otherwise.

.. _`ata_port_detach`:

ata_port_detach
===============

.. c:function:: void ata_port_detach(struct ata_port *ap)

    Detach ATA port in preparation of device removal

    :param struct ata_port \*ap:
        ATA port to be detached

.. _`ata_port_detach.description`:

Description
-----------

Detach all ATA devices and the associated SCSI devices of \ ``ap``\ ;
then, remove the associated SCSI host.  \ ``ap``\  is guaranteed to
be quiescent on return from this function.

.. _`ata_port_detach.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`ata_host_detach`:

ata_host_detach
===============

.. c:function:: void ata_host_detach(struct ata_host *host)

    Detach all ports of an ATA host

    :param struct ata_host \*host:
        Host to detach

.. _`ata_host_detach.description`:

Description
-----------

Detach all ports of \ ``host``\ .

.. _`ata_host_detach.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`ata_pci_remove_one`:

ata_pci_remove_one
==================

.. c:function:: void ata_pci_remove_one(struct pci_dev *pdev)

    PCI layer callback for device removal

    :param struct pci_dev \*pdev:
        PCI device that was removed

.. _`ata_pci_remove_one.description`:

Description
-----------

PCI layer indicates to libata via this hook that hot-unplug or
module unload event has occurred.  Detach all ports.  Resource
release is handled via devres.

.. _`ata_pci_remove_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`ata_platform_remove_one`:

ata_platform_remove_one
=======================

.. c:function:: int ata_platform_remove_one(struct platform_device *pdev)

    Platform layer callback for device removal

    :param struct platform_device \*pdev:
        Platform device that was removed

.. _`ata_platform_remove_one.description`:

Description
-----------

Platform layer indicates to libata via this hook that hot-unplug or
module unload event has occurred.  Detach all ports.  Resource
release is handled via devres.

.. _`ata_platform_remove_one.locking`:

LOCKING
-------

Inherited from platform layer (may sleep).

.. _`ata_msleep`:

ata_msleep
==========

.. c:function:: void ata_msleep(struct ata_port *ap, unsigned int msecs)

    ATA EH owner aware msleep

    :param struct ata_port \*ap:
        ATA port to attribute the sleep to

    :param unsigned int msecs:
        duration to sleep in milliseconds

.. _`ata_msleep.description`:

Description
-----------

Sleeps \ ``msecs``\ .  If the current task is owner of \ ``ap``\ 's EH, the
ownership is released before going to sleep and reacquired
after the sleep is complete.  IOW, other ports sharing the
\ ``ap``\ ->host will be allowed to own the EH while this task is
sleeping.

.. _`ata_msleep.locking`:

LOCKING
-------

Might sleep.

.. _`ata_wait_register`:

ata_wait_register
=================

.. c:function:: u32 ata_wait_register(struct ata_port *ap, void __iomem *reg, u32 mask, u32 val, unsigned long interval, unsigned long timeout)

    wait until register value changes

    :param struct ata_port \*ap:
        ATA port to wait register for, can be NULL

    :param void __iomem \*reg:
        IO-mapped register

    :param u32 mask:
        Mask to apply to read register value

    :param u32 val:
        Wait condition

    :param unsigned long interval:
        polling interval in milliseconds

    :param unsigned long timeout:
        timeout in milliseconds

.. _`ata_wait_register.description`:

Description
-----------

Waiting for some bits of register to change is a common
operation for ATA controllers.  This function reads 32bit LE
IO-mapped register \ ``reg``\  and tests for the following condition.

(\*\ ``reg``\  & mask) != val

If the condition is met, it returns; otherwise, the process is
repeated after \ ``interval_msec``\  until timeout.

.. _`ata_wait_register.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`ata_wait_register.return`:

Return
------

The final register value.

.. _`sata_lpm_ignore_phy_events`:

sata_lpm_ignore_phy_events
==========================

.. c:function:: bool sata_lpm_ignore_phy_events(struct ata_link *link)

    test if PHY event should be ignored

    :param struct ata_link \*link:
        Link receiving the event

.. _`sata_lpm_ignore_phy_events.description`:

Description
-----------

Test whether the received PHY event has to be ignored or not.

.. _`sata_lpm_ignore_phy_events.return`:

Return
------


True if the event has to be ignored.

.. This file was automatic generated / don't edit.

