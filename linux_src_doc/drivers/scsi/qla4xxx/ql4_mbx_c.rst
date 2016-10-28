.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla4xxx/ql4_mbx.c

.. _`qla4xxx_is_intr_poll_mode`:

qla4xxx_is_intr_poll_mode
=========================

.. c:function:: int qla4xxx_is_intr_poll_mode(struct scsi_qla_host *ha)

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

.. _`qla4xxx_mailbox_command`:

qla4xxx_mailbox_command
=======================

.. c:function:: int qla4xxx_mailbox_command(struct scsi_qla_host *ha, uint8_t inCount, uint8_t outCount, uint32_t *mbx_cmd, uint32_t *mbx_sts)

    issues mailbox commands

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param uint8_t inCount:
        number of mailbox registers to load.

    :param uint8_t outCount:
        number of mailbox registers to return.

    :param uint32_t \*mbx_cmd:
        data pointer for mailbox in registers.

    :param uint32_t \*mbx_sts:
        data pointer for mailbox out registers.

.. _`qla4xxx_mailbox_command.description`:

Description
-----------

This routine issue mailbox commands and waits for completion.
If outCount is 0, this routine completes successfully WITHOUT waiting
for the mailbox command to complete.

.. _`qla4xxx_get_minidump_template`:

qla4xxx_get_minidump_template
=============================

.. c:function:: int qla4xxx_get_minidump_template(struct scsi_qla_host *ha, dma_addr_t phys_addr)

    Get the firmware template

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param dma_addr_t phys_addr:
        dma address for template

.. _`qla4xxx_get_minidump_template.description`:

Description
-----------

Obtain the minidump template from firmware during initialization
as it may not be available when minidump is desired.

.. _`qla4xxx_req_template_size`:

qla4xxx_req_template_size
=========================

.. c:function:: int qla4xxx_req_template_size(struct scsi_qla_host *ha)

    Get minidump template size from firmware.

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

.. _`qla4xxx_initialize_fw_cb`:

qla4xxx_initialize_fw_cb
========================

.. c:function:: int qla4xxx_initialize_fw_cb(struct scsi_qla_host *ha)

    initializes firmware control block.

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

.. _`qla4xxx_get_dhcp_ip_address`:

qla4xxx_get_dhcp_ip_address
===========================

.. c:function:: int qla4xxx_get_dhcp_ip_address(struct scsi_qla_host *ha)

    gets HBA ip address via DHCP

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

.. _`qla4xxx_get_firmware_state`:

qla4xxx_get_firmware_state
==========================

.. c:function:: int qla4xxx_get_firmware_state(struct scsi_qla_host *ha)

    gets firmware state of HBA

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

.. _`qla4xxx_get_firmware_status`:

qla4xxx_get_firmware_status
===========================

.. c:function:: int qla4xxx_get_firmware_status(struct scsi_qla_host *ha)

    retrieves firmware status

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

.. _`qla4xxx_get_fwddb_entry`:

qla4xxx_get_fwddb_entry
=======================

.. c:function:: int qla4xxx_get_fwddb_entry(struct scsi_qla_host *ha, uint16_t fw_ddb_index, struct dev_db_entry *fw_ddb_entry, dma_addr_t fw_ddb_entry_dma, uint32_t *num_valid_ddb_entries, uint32_t *next_ddb_index, uint32_t *fw_ddb_device_state, uint32_t *conn_err_detail, uint16_t *tcp_source_port_num, uint16_t *connection_id)

    retrieves firmware ddb entry

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param uint16_t fw_ddb_index:
        Firmware's device database index

    :param struct dev_db_entry \*fw_ddb_entry:
        Pointer to firmware's device database entry structure

    :param dma_addr_t fw_ddb_entry_dma:
        *undescribed*

    :param uint32_t \*num_valid_ddb_entries:
        Pointer to number of valid ddb entries

    :param uint32_t \*next_ddb_index:
        Pointer to next valid device database index

    :param uint32_t \*fw_ddb_device_state:
        Pointer to device state

    :param uint32_t \*conn_err_detail:
        *undescribed*

    :param uint16_t \*tcp_source_port_num:
        *undescribed*

    :param uint16_t \*connection_id:
        *undescribed*

.. _`qla4xxx_set_ddb_entry`:

qla4xxx_set_ddb_entry
=====================

.. c:function:: int qla4xxx_set_ddb_entry(struct scsi_qla_host *ha, uint16_t fw_ddb_index, dma_addr_t fw_ddb_entry_dma, uint32_t *mbx_sts)

    sets a ddb entry.

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param uint16_t fw_ddb_index:
        Firmware's device database index

    :param dma_addr_t fw_ddb_entry_dma:
        dma address of ddb entry

    :param uint32_t \*mbx_sts:
        mailbox 0 to be returned or NULL

.. _`qla4xxx_set_ddb_entry.description`:

Description
-----------

This routine initializes or updates the adapter's device database
entry for the specified device.

.. _`qla4xxx_get_crash_record`:

qla4xxx_get_crash_record
========================

.. c:function:: void qla4xxx_get_crash_record(struct scsi_qla_host *ha)

    retrieves crash record.

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

.. _`qla4xxx_get_crash_record.description`:

Description
-----------

This routine retrieves a crash record from the QLA4010 after an 8002h aen.

.. _`qla4xxx_get_conn_event_log`:

qla4xxx_get_conn_event_log
==========================

.. c:function:: void qla4xxx_get_conn_event_log(struct scsi_qla_host *ha)

    retrieves connection event log

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

.. _`qla4xxx_abort_task`:

qla4xxx_abort_task
==================

.. c:function:: int qla4xxx_abort_task(struct scsi_qla_host *ha, struct srb *srb)

    issues Abort Task

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param struct srb \*srb:
        Pointer to srb entry

.. _`qla4xxx_abort_task.description`:

Description
-----------

This routine performs a LUN RESET on the specified target/lun.
The caller must ensure that the ddb_entry and lun_entry pointers
are valid before calling this routine.

.. _`qla4xxx_reset_lun`:

qla4xxx_reset_lun
=================

.. c:function:: int qla4xxx_reset_lun(struct scsi_qla_host *ha, struct ddb_entry *ddb_entry, uint64_t lun)

    issues LUN Reset

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param struct ddb_entry \*ddb_entry:
        Pointer to device database entry

    :param uint64_t lun:
        lun number

.. _`qla4xxx_reset_lun.description`:

Description
-----------

This routine performs a LUN RESET on the specified target/lun.
The caller must ensure that the ddb_entry and lun_entry pointers
are valid before calling this routine.

.. _`qla4xxx_reset_target`:

qla4xxx_reset_target
====================

.. c:function:: int qla4xxx_reset_target(struct scsi_qla_host *ha, struct ddb_entry *ddb_entry)

    issues target Reset

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param struct ddb_entry \*ddb_entry:
        *undescribed*

.. _`qla4xxx_reset_target.description`:

Description
-----------

This routine performs a TARGET RESET on the specified target.
The caller must ensure that the ddb_entry pointers
are valid before calling this routine.

.. _`qla4xxx_about_firmware`:

qla4xxx_about_firmware
======================

.. c:function:: int qla4xxx_about_firmware(struct scsi_qla_host *ha)

    gets FW, iscsi draft and boot loader version

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

.. _`qla4xxx_about_firmware.description`:

Description
-----------

Retrieves the FW version, iSCSI draft version & bootloader version of HBA.
Mailboxes 2 & 3 may hold an address for data. Make sure that we write 0 to
those mailboxes, if unused.

.. _`qla4xxx_set_chap`:

qla4xxx_set_chap
================

.. c:function:: int qla4xxx_set_chap(struct scsi_qla_host *ha, char *username, char *password, uint16_t idx, int bidi)

    Make a chap entry at the given index

    :param struct scsi_qla_host \*ha:
        pointer to adapter structure

    :param char \*username:
        CHAP username to set

    :param char \*password:
        CHAP password to set

    :param uint16_t idx:
        CHAP index at which to make the entry

    :param int bidi:
        type of chap entry (chap_in or chap_out)

.. _`qla4xxx_set_chap.description`:

Description
-----------

Create chap entry at the given index with the information provided.

.. _`qla4xxx_set_chap.note`:

Note
----

Caller should acquire the chap lock before getting here.

.. _`qla4xxx_get_chap_index`:

qla4xxx_get_chap_index
======================

.. c:function:: int qla4xxx_get_chap_index(struct scsi_qla_host *ha, char *username, char *password, int bidi, uint16_t *chap_index)

    Get chap index given username and secret

    :param struct scsi_qla_host \*ha:
        pointer to adapter structure

    :param char \*username:
        CHAP username to be searched

    :param char \*password:
        CHAP password to be searched

    :param int bidi:
        Is this a BIDI CHAP

    :param uint16_t \*chap_index:
        CHAP index to be returned

.. _`qla4xxx_get_chap_index.description`:

Description
-----------

Match the username and password in the chap_list, return the index if a
match is found. If a match is not found then add the entry in FLASH and
return the index at which entry is written in the FLASH.

.. _`qla4_84xx_extend_idc_tmo`:

qla4_84xx_extend_idc_tmo
========================

.. c:function:: int qla4_84xx_extend_idc_tmo(struct scsi_qla_host *ha, uint32_t ext_tmo)

    Extend IDC Timeout.

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param uint32_t ext_tmo:
        idc timeout value

.. _`qla4_84xx_extend_idc_tmo.description`:

Description
-----------

Requests firmware to extend the idc timeout value.

.. _`qla4_8xxx_set_param`:

qla4_8xxx_set_param
===================

.. c:function:: int qla4_8xxx_set_param(struct scsi_qla_host *ha, int param)

    set driver version in firmware.

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

    :param int param:
        Parameter to set i.e driver version

.. _`qla4_83xx_post_idc_ack`:

qla4_83xx_post_idc_ack
======================

.. c:function:: int qla4_83xx_post_idc_ack(struct scsi_qla_host *ha)

    post IDC ACK

    :param struct scsi_qla_host \*ha:
        Pointer to host adapter structure.

.. _`qla4_83xx_post_idc_ack.description`:

Description
-----------

Posts IDC ACK for IDC Request Notification AEN.

.. This file was automatic generated / don't edit.

