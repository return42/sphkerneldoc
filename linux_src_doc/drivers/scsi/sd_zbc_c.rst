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

.. _`sd_zbc_alloc_zone_bitmap`:

sd_zbc_alloc_zone_bitmap
========================

.. c:function:: unsigned long *sd_zbc_alloc_zone_bitmap(struct scsi_disk *sdkp)

    Allocate a zone bitmap (one bit per zone).

    :param struct scsi_disk \*sdkp:
        The disk of the bitmap

.. _`sd_zbc_get_seq_zones`:

sd_zbc_get_seq_zones
====================

.. c:function:: sector_t sd_zbc_get_seq_zones(struct scsi_disk *sdkp, unsigned char *buf, unsigned int buflen, unsigned long *seq_zones_bitmap)

    Parse report zones reply to identify sequential zones

    :param struct scsi_disk \*sdkp:
        disk used

    :param unsigned char \*buf:
        report reply buffer

    :param unsigned int buflen:
        *undescribed*

    :param unsigned long \*seq_zones_bitmap:
        *undescribed*

.. _`sd_zbc_get_seq_zones.description`:

Description
-----------

Parse reported zone descriptors in \ ``buf``\  to identify sequential zones and
set the reported zone bit in \ ``seq_zones_bitmap``\  accordingly.
Since read-only and offline zones cannot be written, do not
mark them as sequential in the bitmap.
Return the LBA after the last zone reported.

.. _`sd_zbc_setup_seq_zones_bitmap`:

sd_zbc_setup_seq_zones_bitmap
=============================

.. c:function:: int sd_zbc_setup_seq_zones_bitmap(struct scsi_disk *sdkp)

    Initialize the disk seq zone bitmap.

    :param struct scsi_disk \*sdkp:
        target disk

.. _`sd_zbc_setup_seq_zones_bitmap.description`:

Description
-----------

Allocate a zone bitmap and initialize it by identifying sequential zones.

.. This file was automatic generated / don't edit.

