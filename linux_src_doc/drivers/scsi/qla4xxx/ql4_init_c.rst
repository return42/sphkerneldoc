.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla4xxx/ql4_init.c

.. _`qla4xxx_free_ddb`:

qla4xxx_free_ddb
================

.. c:function:: void qla4xxx_free_ddb(struct scsi_qla_host *ha, struct ddb_entry *ddb_entry)

    deallocate ddb

    :param ha:
        pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

    :param ddb_entry:
        pointer to device database entry
    :type ddb_entry: struct ddb_entry \*

.. _`qla4xxx_free_ddb.description`:

Description
-----------

This routine marks a DDB entry INVALID

.. _`qla4xxx_init_response_q_entries`:

qla4xxx_init_response_q_entries
===============================

.. c:function:: void qla4xxx_init_response_q_entries(struct scsi_qla_host *ha)

    Initializes response queue entries.

    :param ha:
        HA context
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_init_response_q_entries.description`:

Description
-----------

Beginning of request ring has initialization control block already built
by nvram config routine.

.. _`qla4xxx_init_rings`:

qla4xxx_init_rings
==================

.. c:function:: int qla4xxx_init_rings(struct scsi_qla_host *ha)

    initialize hw queues

    :param ha:
        pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_init_rings.description`:

Description
-----------

This routine initializes the internal queues for the specified adapter.
The QLA4010 requires us to restart the queues at index 0.
The QLA4000 doesn't care, so just default to QLA4010's requirement.

.. _`qla4xxx_get_sys_info`:

qla4xxx_get_sys_info
====================

.. c:function:: int qla4xxx_get_sys_info(struct scsi_qla_host *ha)

    validate adapter MAC address(es)

    :param ha:
        pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_init_local_data`:

qla4xxx_init_local_data
=======================

.. c:function:: void qla4xxx_init_local_data(struct scsi_qla_host *ha)

    initialize adapter specific local data

    :param ha:
        pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_alloc_fw_dump`:

qla4xxx_alloc_fw_dump
=====================

.. c:function:: void qla4xxx_alloc_fw_dump(struct scsi_qla_host *ha)

    Allocate memory for minidump data.

    :param ha:
        pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_init_firmware`:

qla4xxx_init_firmware
=====================

.. c:function:: int qla4xxx_init_firmware(struct scsi_qla_host *ha)

    initializes the firmware.

    :param ha:
        pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4_8xxx_pci_config`:

qla4_8xxx_pci_config
====================

.. c:function:: void qla4_8xxx_pci_config(struct scsi_qla_host *ha)

    Setup ISP82xx PCI configuration registers.

    :param ha:
        HA context
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_start_firmware`:

qla4xxx_start_firmware
======================

.. c:function:: int qla4xxx_start_firmware(struct scsi_qla_host *ha)

    starts qla4xxx firmware

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_start_firmware.description`:

Description
-----------

This routine performs the necessary steps to start the firmware for
the QLA4010 adapter.

.. _`qla4xxx_free_ddb_index`:

qla4xxx_free_ddb_index
======================

.. c:function:: void qla4xxx_free_ddb_index(struct scsi_qla_host *ha)

    Free DDBs reserved by firmware

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_free_ddb_index.description`:

Description
-----------

Since firmware is not running in autoconnect mode the DDB indices should
be freed so that when login happens from user space there are free DDB
indices available.

.. _`qla4xxx_initialize_adapter`:

qla4xxx_initialize_adapter
==========================

.. c:function:: int qla4xxx_initialize_adapter(struct scsi_qla_host *ha, int is_reset)

    initiailizes hba

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

    :param is_reset:
        *undescribed*
    :type is_reset: int

.. _`qla4xxx_initialize_adapter.description`:

Description
-----------

This routine parforms all of the steps necessary to initialize the adapter.

.. _`qla4xxx_process_ddb_changed`:

qla4xxx_process_ddb_changed
===========================

.. c:function:: int qla4xxx_process_ddb_changed(struct scsi_qla_host *ha, uint32_t fw_ddb_index, uint32_t state, uint32_t conn_err)

    process ddb state change \ ``ha``\  - Pointer to host adapter structure. \ ``fw_ddb_index``\  - Firmware's device database index \ ``state``\  - Device state

    :param ha:
        *undescribed*
    :type ha: struct scsi_qla_host \*

    :param fw_ddb_index:
        *undescribed*
    :type fw_ddb_index: uint32_t

    :param state:
        *undescribed*
    :type state: uint32_t

    :param conn_err:
        *undescribed*
    :type conn_err: uint32_t

.. _`qla4xxx_process_ddb_changed.description`:

Description
-----------

This routine processes a Decive Database Changed AEN Event.

.. _`qla4xxx_login_flash_ddb`:

qla4xxx_login_flash_ddb
=======================

.. c:function:: void qla4xxx_login_flash_ddb(struct iscsi_cls_session *cls_session)

    Login to target (DDB)

    :param cls_session:
        Pointer to the session to login
    :type cls_session: struct iscsi_cls_session \*

.. _`qla4xxx_login_flash_ddb.description`:

Description
-----------

This routine logins to the target.
Issues setddb and conn open mbx

.. This file was automatic generated / don't edit.

