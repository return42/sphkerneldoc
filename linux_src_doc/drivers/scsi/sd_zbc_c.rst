.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/sd_zbc.c

.. _`sd_zbc_parse_report`:

sd_zbc_parse_report
===================

.. c:function:: void sd_zbc_parse_report(struct scsi_disk *sdkp, u8 *buf, struct blk_zone *zone)

    Convert a zone descriptor to a struct blk_zone,

    :param sdkp:
        The disk the report originated from
    :type sdkp: struct scsi_disk \*

    :param buf:
        Address of the report zone descriptor
    :type buf: u8 \*

    :param zone:
        the destination zone structure
    :type zone: struct blk_zone \*

.. _`sd_zbc_parse_report.description`:

Description
-----------

All LBA sized values are converted to 512B sectors unit.

.. _`sd_zbc_do_report_zones`:

sd_zbc_do_report_zones
======================

.. c:function:: int sd_zbc_do_report_zones(struct scsi_disk *sdkp, unsigned char *buf, unsigned int buflen, sector_t lba, bool partial)

    Issue a REPORT ZONES scsi command.

    :param sdkp:
        The target disk
    :type sdkp: struct scsi_disk \*

    :param buf:
        Buffer to use for the reply
    :type buf: unsigned char \*

    :param buflen:
        the buffer size
    :type buflen: unsigned int

    :param lba:
        Start LBA of the report
    :type lba: sector_t

    :param partial:
        Do partial report
    :type partial: bool

.. _`sd_zbc_do_report_zones.description`:

Description
-----------

For internal use during device validation.
Using partial=true can significantly speed up execution of a report zones
command because the disk does not have to count all possible report matching
zones and will only report the count of zones fitting in the command reply
buffer.

.. _`sd_zbc_report_zones`:

sd_zbc_report_zones
===================

.. c:function:: int sd_zbc_report_zones(struct gendisk *disk, sector_t sector, struct blk_zone *zones, unsigned int *nr_zones, gfp_t gfp_mask)

    Disk report zones operation.

    :param disk:
        The target disk
    :type disk: struct gendisk \*

    :param sector:
        Start 512B sector of the report
    :type sector: sector_t

    :param zones:
        Array of zone descriptors
    :type zones: struct blk_zone \*

    :param nr_zones:
        Number of descriptors in the array
    :type nr_zones: unsigned int \*

    :param gfp_mask:
        Memory allocation mask
    :type gfp_mask: gfp_t

.. _`sd_zbc_report_zones.description`:

Description
-----------

Execute a report zones command on the target disk.

.. _`sd_zbc_zone_sectors`:

sd_zbc_zone_sectors
===================

.. c:function:: sector_t sd_zbc_zone_sectors(struct scsi_disk *sdkp)

    Get the device zone size in number of 512B sectors.

    :param sdkp:
        The target disk
    :type sdkp: struct scsi_disk \*

.. _`sd_zbc_setup_reset_cmnd`:

sd_zbc_setup_reset_cmnd
=======================

.. c:function:: int sd_zbc_setup_reset_cmnd(struct scsi_cmnd *cmd)

    Prepare a RESET WRITE POINTER scsi command.

    :param cmd:
        the command to setup
    :type cmd: struct scsi_cmnd \*

.. _`sd_zbc_setup_reset_cmnd.description`:

Description
-----------

Called from \ :c:func:`sd_init_command`\  for a REQ_OP_ZONE_RESET request.

.. _`sd_zbc_complete`:

sd_zbc_complete
===============

.. c:function:: void sd_zbc_complete(struct scsi_cmnd *cmd, unsigned int good_bytes, struct scsi_sense_hdr *sshdr)

    ZBC command post processing.

    :param cmd:
        Completed command
    :type cmd: struct scsi_cmnd \*

    :param good_bytes:
        Command reply bytes
    :type good_bytes: unsigned int

    :param sshdr:
        command sense header
    :type sshdr: struct scsi_sense_hdr \*

.. _`sd_zbc_complete.description`:

Description
-----------

Called from \ :c:func:`sd_done`\ . Process report zones reply and handle reset zone
and write commands errors.

.. _`sd_zbc_check_zoned_characteristics`:

sd_zbc_check_zoned_characteristics
==================================

.. c:function:: int sd_zbc_check_zoned_characteristics(struct scsi_disk *sdkp, unsigned char *buf)

    Check zoned block device characteristics

    :param sdkp:
        Target disk
    :type sdkp: struct scsi_disk \*

    :param buf:
        Buffer where to store the VPD page data
    :type buf: unsigned char \*

.. _`sd_zbc_check_zoned_characteristics.description`:

Description
-----------

Read VPD page B6, get information and check that reads are unconstrained.

.. _`sd_zbc_check_zones`:

sd_zbc_check_zones
==================

.. c:function:: int sd_zbc_check_zones(struct scsi_disk *sdkp, u32 *zblocks)

    Check the device capacity and zone sizes

    :param sdkp:
        Target disk
    :type sdkp: struct scsi_disk \*

    :param zblocks:
        *undescribed*
    :type zblocks: u32 \*

.. _`sd_zbc_check_zones.description`:

Description
-----------

Check that the device capacity as reported by READ CAPACITY matches the
max_lba value (plus one)of the report zones command reply. Also check that
all zones of the device have an equal size, only allowing the last zone of
the disk to have a smaller size (runt zone). The zone size must also be a
power of two.

Returns the zone size in number of blocks upon success or an error code
upon failure.

.. This file was automatic generated / don't edit.

