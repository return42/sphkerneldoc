.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/sd_zbc.c

.. _`sd_zbc_parse_report`:

sd_zbc_parse_report
===================

.. c:function:: void sd_zbc_parse_report(struct scsi_disk *sdkp, u8 *buf, struct blk_zone *zone)

    Convert a zone descriptor to a struct blk_zone,

    :param struct scsi_disk \*sdkp:
        The disk the report originated from

    :param u8 \*buf:
        Address of the report zone descriptor

    :param struct blk_zone \*zone:
        the destination zone structure

.. _`sd_zbc_parse_report.description`:

Description
-----------

All LBA sized values are converted to 512B sectors unit.

.. _`sd_zbc_report_zones`:

sd_zbc_report_zones
===================

.. c:function:: int sd_zbc_report_zones(struct scsi_disk *sdkp, unsigned char *buf, unsigned int buflen, sector_t lba)

    Issue a REPORT ZONES scsi command.

    :param struct scsi_disk \*sdkp:
        The target disk

    :param unsigned char \*buf:
        Buffer to use for the reply

    :param unsigned int buflen:
        the buffer size

    :param sector_t lba:
        Start LBA of the report

.. _`sd_zbc_report_zones.description`:

Description
-----------

For internal use during device validation.

.. _`sd_zbc_setup_report_cmnd`:

sd_zbc_setup_report_cmnd
========================

.. c:function:: int sd_zbc_setup_report_cmnd(struct scsi_cmnd *cmd)

    Prepare a REPORT ZONES scsi command

    :param struct scsi_cmnd \*cmd:
        The command to setup

.. _`sd_zbc_setup_report_cmnd.description`:

Description
-----------

Call in \ :c:func:`sd_init_command`\  for a REQ_OP_ZONE_REPORT request.

.. _`sd_zbc_report_zones_complete`:

sd_zbc_report_zones_complete
============================

.. c:function:: void sd_zbc_report_zones_complete(struct scsi_cmnd *scmd, unsigned int good_bytes)

    Process a REPORT ZONES scsi command reply.

    :param struct scsi_cmnd \*scmd:
        The completed report zones command

    :param unsigned int good_bytes:
        reply size in bytes

.. _`sd_zbc_report_zones_complete.description`:

Description
-----------

Convert all reported zone descriptors to struct blk_zone. The conversion
is done in-place, directly in the request specified sg buffer.

.. _`sd_zbc_zone_sectors`:

sd_zbc_zone_sectors
===================

.. c:function:: sector_t sd_zbc_zone_sectors(struct scsi_disk *sdkp)

    Get the device zone size in number of 512B sectors.

    :param struct scsi_disk \*sdkp:
        The target disk

.. _`sd_zbc_zone_no`:

sd_zbc_zone_no
==============

.. c:function:: unsigned int sd_zbc_zone_no(struct scsi_disk *sdkp, sector_t sector)

    Get the number of the zone conataining a sector.

    :param struct scsi_disk \*sdkp:
        The target disk

    :param sector_t sector:
        512B sector address contained in the zone

.. _`sd_zbc_setup_reset_cmnd`:

sd_zbc_setup_reset_cmnd
=======================

.. c:function:: int sd_zbc_setup_reset_cmnd(struct scsi_cmnd *cmd)

    Prepare a RESET WRITE POINTER scsi command.

    :param struct scsi_cmnd \*cmd:
        the command to setup

.. _`sd_zbc_setup_reset_cmnd.description`:

Description
-----------

Called from \ :c:func:`sd_init_command`\  for a REQ_OP_ZONE_RESET request.

.. _`sd_zbc_write_lock_zone`:

sd_zbc_write_lock_zone
======================

.. c:function:: int sd_zbc_write_lock_zone(struct scsi_cmnd *cmd)

    Write lock a sequential zone.

    :param struct scsi_cmnd \*cmd:
        write command

.. _`sd_zbc_write_lock_zone.description`:

Description
-----------

Called from \ :c:func:`sd_init_cmd`\  for write requests (standard write, write same or
write zeroes operations). If the request target zone is not already locked,
the zone is locked and BLKPREP_OK returned, allowing the request to proceed
through dispatch in \ :c:func:`scsi_request_fn`\ . Otherwise, BLKPREP_DEFER is returned,
forcing the request to wait for the zone to be unlocked, that is, for the
previously issued write request targeting the same zone to complete.

This is called from \ :c:func:`blk_peek_request`\  context with the queue lock held and
before the request is removed from the scheduler. As a result, multiple
contexts executing concurrently \ :c:func:`scsi_request_fn`\  cannot result in write
sequence reordering as only a single write request per zone is allowed to
proceed.

.. _`sd_zbc_write_unlock_zone`:

sd_zbc_write_unlock_zone
========================

.. c:function:: void sd_zbc_write_unlock_zone(struct scsi_cmnd *cmd)

    Write unlock a sequential zone.

    :param struct scsi_cmnd \*cmd:
        write command

.. _`sd_zbc_write_unlock_zone.description`:

Description
-----------

Called from \ :c:func:`sd_uninit_cmd`\ . Unlocking the request target zone will allow
dispatching the next write request for the zone.

.. _`sd_zbc_complete`:

sd_zbc_complete
===============

.. c:function:: void sd_zbc_complete(struct scsi_cmnd *cmd, unsigned int good_bytes, struct scsi_sense_hdr *sshdr)

    ZBC command post processing.

    :param struct scsi_cmnd \*cmd:
        Completed command

    :param unsigned int good_bytes:
        Command reply bytes

    :param struct scsi_sense_hdr \*sshdr:
        command sense header

.. _`sd_zbc_complete.description`:

Description
-----------

Called from \ :c:func:`sd_done`\ . Process report zones reply and handle reset zone
and write commands errors.

.. _`sd_zbc_read_zoned_characteristics`:

sd_zbc_read_zoned_characteristics
=================================

.. c:function:: int sd_zbc_read_zoned_characteristics(struct scsi_disk *sdkp, unsigned char *buf)

    Read zoned block device characteristics

    :param struct scsi_disk \*sdkp:
        Target disk

    :param unsigned char \*buf:
        Buffer where to store the VPD page data

.. _`sd_zbc_read_zoned_characteristics.description`:

Description
-----------

Read VPD page B6.

.. _`sd_zbc_check_capacity`:

sd_zbc_check_capacity
=====================

.. c:function:: int sd_zbc_check_capacity(struct scsi_disk *sdkp, unsigned char *buf)

    Check reported capacity.

    :param struct scsi_disk \*sdkp:
        Target disk

    :param unsigned char \*buf:
        Buffer to use for commands

.. _`sd_zbc_check_capacity.description`:

Description
-----------

ZBC drive may report only the capacity of the first conventional zones at
LBA 0. This is indicated by the RC_BASIS field of the read capacity reply.
Check this here. If the disk reported only its conventional zones capacity,
get the total capacity by doing a report zones.

.. _`sd_zbc_check_zone_size`:

sd_zbc_check_zone_size
======================

.. c:function:: int sd_zbc_check_zone_size(struct scsi_disk *sdkp)

    Check the device zone sizes

    :param struct scsi_disk \*sdkp:
        Target disk

.. _`sd_zbc_check_zone_size.description`:

Description
-----------

Check that all zones of the device are equal. The last zone can however
be smaller. The zone size must also be a power of two number of LBAs.

.. This file was automatic generated / don't edit.

