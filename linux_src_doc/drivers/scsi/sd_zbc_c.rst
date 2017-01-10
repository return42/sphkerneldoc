.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/sd_zbc.c

.. _`sd_zbc_parse_report`:

sd_zbc_parse_report
===================

.. c:function:: void sd_zbc_parse_report(struct scsi_disk *sdkp, u8 *buf, struct blk_zone *zone)

    :param struct scsi_disk \*sdkp:
        *undescribed*

    :param u8 \*buf:
        *undescribed*

    :param struct blk_zone \*zone:
        *undescribed*

.. _`sd_zbc_report_zones`:

sd_zbc_report_zones
===================

.. c:function:: int sd_zbc_report_zones(struct scsi_disk *sdkp, unsigned char *buf, unsigned int buflen, sector_t lba)

    :param struct scsi_disk \*sdkp:
        *undescribed*

    :param unsigned char \*buf:
        *undescribed*

    :param unsigned int buflen:
        *undescribed*

    :param sector_t lba:
        *undescribed*

.. _`sd_zbc_read_zoned_characteristics`:

sd_zbc_read_zoned_characteristics
=================================

.. c:function:: int sd_zbc_read_zoned_characteristics(struct scsi_disk *sdkp, unsigned char *buf)

    :param struct scsi_disk \*sdkp:
        *undescribed*

    :param unsigned char \*buf:
        *undescribed*

.. _`sd_zbc_check_capacity`:

sd_zbc_check_capacity
=====================

.. c:function:: int sd_zbc_check_capacity(struct scsi_disk *sdkp, unsigned char *buf)

    :param struct scsi_disk \*sdkp:
        *undescribed*

    :param unsigned char \*buf:
        *undescribed*

.. This file was automatic generated / don't edit.

