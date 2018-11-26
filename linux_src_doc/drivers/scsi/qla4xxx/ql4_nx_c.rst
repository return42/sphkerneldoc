.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla4xxx/ql4_nx.c

.. _`qla4_82xx_idc_lock`:

qla4_82xx_idc_lock
==================

.. c:function:: int qla4_82xx_idc_lock(struct scsi_qla_host *ha)

    hw_lock

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4_82xx_idc_lock.description`:

Description
-----------

General purpose lock used to synchronize access to
CRB_DEV_STATE, CRB_DEV_REF_COUNT, etc.

.. _`qla4_82xx_pinit_from_rom`:

qla4_82xx_pinit_from_rom
========================

.. c:function:: int qla4_82xx_pinit_from_rom(struct scsi_qla_host *ha, int verbose)

    to put the ISP into operational state

    :param ha:
        *undescribed*
    :type ha: struct scsi_qla_host \*

    :param verbose:
        *undescribed*
    :type verbose: int

.. _`qla4_8xxx_ms_mem_write_128b`:

qla4_8xxx_ms_mem_write_128b
===========================

.. c:function:: int qla4_8xxx_ms_mem_write_128b(struct scsi_qla_host *ha, uint64_t addr, uint32_t *data, uint32_t count)

    Writes data to MS/off-chip memory

    :param ha:
        Pointer to adapter structure
    :type ha: struct scsi_qla_host \*

    :param addr:
        Flash address to write to
    :type addr: uint64_t

    :param data:
        Data to be written
    :type data: uint32_t \*

    :param count:
        word_count to be written
    :type count: uint32_t

.. _`qla4_8xxx_ms_mem_write_128b.return`:

Return
------

On success return QLA_SUCCESS
On error return QLA_ERROR

.. _`qla4_8xxx_collect_md_data`:

qla4_8xxx_collect_md_data
=========================

.. c:function:: int qla4_8xxx_collect_md_data(struct scsi_qla_host *ha)

    Retrieve firmware minidump data.

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4_8xxx_uevent_emit`:

qla4_8xxx_uevent_emit
=====================

.. c:function:: void qla4_8xxx_uevent_emit(struct scsi_qla_host *ha, u32 code)

    Send uevent when the firmware dump is ready.

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

    :param code:
        *undescribed*
    :type code: u32

.. _`qla4_8xxx_device_bootstrap`:

qla4_8xxx_device_bootstrap
==========================

.. c:function:: int qla4_8xxx_device_bootstrap(struct scsi_qla_host *ha)

    Initialize device, set DEV_READY, start fw

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4_8xxx_device_bootstrap.note`:

Note
----

IDC lock must be held upon entry

.. _`qla4_82xx_need_reset_handler`:

qla4_82xx_need_reset_handler
============================

.. c:function:: void qla4_82xx_need_reset_handler(struct scsi_qla_host *ha)

    Code to start reset sequence

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4_82xx_need_reset_handler.note`:

Note
----

IDC lock must be held upon entry

.. _`qla4_8xxx_need_qsnt_handler`:

qla4_8xxx_need_qsnt_handler
===========================

.. c:function:: void qla4_8xxx_need_qsnt_handler(struct scsi_qla_host *ha)

    Code to start qsnt

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4_8xxx_device_state_handler`:

qla4_8xxx_device_state_handler
==============================

.. c:function:: int qla4_8xxx_device_state_handler(struct scsi_qla_host *ha)

    Adapter state machine

    :param ha:
        pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4_8xxx_device_state_handler.note`:

Note
----

IDC lock must be UNLOCKED upon entry

.. _`qla4_82xx_read_optrom_data`:

qla4_82xx_read_optrom_data
==========================

.. c:function:: uint8_t *qla4_82xx_read_optrom_data(struct scsi_qla_host *ha, uint8_t *buf, uint32_t offset, uint32_t length)

    :param ha:
        *undescribed*
    :type ha: struct scsi_qla_host \*

    :param buf:
        *undescribed*
    :type buf: uint8_t \*

    :param offset:
        *undescribed*
    :type offset: uint32_t

    :param length:
        *undescribed*
    :type length: uint32_t

.. _`qla4_8xxx_stop_firmware`:

qla4_8xxx_stop_firmware
=======================

.. c:function:: int qla4_8xxx_stop_firmware(struct scsi_qla_host *ha)

    stops firmware on specified adapter instance

    :param ha:
        pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4_8xxx_stop_firmware.remarks`:

Remarks
-------

For iSCSI, throws away all I/O and AENs into bit bucket, so they will
not be available after successful return.  Driver must cleanup potential
outstanding I/O's after calling this funcion.

.. _`qla4_82xx_isp_reset`:

qla4_82xx_isp_reset
===================

.. c:function:: int qla4_82xx_isp_reset(struct scsi_qla_host *ha)

    Resets ISP and aborts all outstanding commands.

    :param ha:
        pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4_8xxx_get_sys_info`:

qla4_8xxx_get_sys_info
======================

.. c:function:: int qla4_8xxx_get_sys_info(struct scsi_qla_host *ha)

    get adapter MAC address(es) and serial number

    :param ha:
        pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. This file was automatic generated / don't edit.

