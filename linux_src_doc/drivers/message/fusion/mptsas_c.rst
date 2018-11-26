.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/message/fusion/mptsas.c

.. _`mptsas_find_portinfo_by_sas_address`:

mptsas_find_portinfo_by_sas_address
===================================

.. c:function:: struct mptsas_portinfo *mptsas_find_portinfo_by_sas_address(MPT_ADAPTER *ioc, u64 sas_address)

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param sas_address:
        *undescribed*
    :type sas_address: u64

.. _`mptsas_find_portinfo_by_sas_address.description`:

Description
-----------

This function should be called with the sas_topology_mutex already held

.. _`mptsas_add_device_component`:

mptsas_add_device_component
===========================

.. c:function:: void mptsas_add_device_component(MPT_ADAPTER *ioc, u8 channel, u8 id, u64 sas_address, u32 device_info, u16 slot, u64 enclosure_logical_id)

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param channel:
        fw mapped id's
    :type channel: u8

    :param id:
        *undescribed*
    :type id: u8

    :param sas_address:
        *undescribed*
    :type sas_address: u64

    :param device_info:
        *undescribed*
    :type device_info: u32

    :param slot:
        *undescribed*
    :type slot: u16

    :param enclosure_logical_id:
        *undescribed*
    :type enclosure_logical_id: u64

.. _`mptsas_add_device_component_by_fw`:

mptsas_add_device_component_by_fw
=================================

.. c:function:: void mptsas_add_device_component_by_fw(MPT_ADAPTER *ioc, u8 channel, u8 id)

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param channel:
        fw mapped id's
    :type channel: u8

    :param id:
        *undescribed*
    :type id: u8

.. _`mptsas_add_device_component_starget_ir`:

mptsas_add_device_component_starget_ir
======================================

.. c:function:: void mptsas_add_device_component_starget_ir(MPT_ADAPTER *ioc, struct scsi_target *starget)

    Handle Integrated RAID, adding each individual device to list

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param starget:
        *undescribed*
    :type starget: struct scsi_target \*

.. _`mptsas_add_device_component_starget`:

mptsas_add_device_component_starget
===================================

.. c:function:: void mptsas_add_device_component_starget(MPT_ADAPTER *ioc, struct scsi_target *starget)

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param starget:
        *undescribed*
    :type starget: struct scsi_target \*

.. _`mptsas_del_device_component_by_os`:

mptsas_del_device_component_by_os
=================================

.. c:function:: void mptsas_del_device_component_by_os(MPT_ADAPTER *ioc, u8 channel, u8 id)

    Once a device has been removed, we mark the entry in the list as being cached

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param channel:
        os mapped id's
    :type channel: u8

    :param id:
        *undescribed*
    :type id: u8

.. _`mptsas_del_device_components`:

mptsas_del_device_components
============================

.. c:function:: void mptsas_del_device_components(MPT_ADAPTER *ioc)

    Cleaning the list

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

.. _`mptsas_find_vtarget`:

mptsas_find_vtarget
===================

.. c:function:: VirtTarget *mptsas_find_vtarget(MPT_ADAPTER *ioc, u8 channel, u8 id)

    :param ioc:
        *undescribed*
    :type ioc: MPT_ADAPTER \*

    :param channel:
        *undescribed*
    :type channel: u8

    :param id:
        *undescribed*
    :type id: u8

.. _`mptsas_find_vtarget.description`:

Description
-----------

\ ``ioc``\ 
\ ``volume_id``\ 
\ ``volume_bus``\ 

.. _`mptsas_target_reset`:

mptsas_target_reset
===================

.. c:function:: int mptsas_target_reset(MPT_ADAPTER *ioc, u8 channel, u8 id)

    :param ioc:
        *undescribed*
    :type ioc: MPT_ADAPTER \*

    :param channel:
        *undescribed*
    :type channel: u8

    :param id:
        *undescribed*
    :type id: u8

.. _`mptsas_target_reset.description`:

Description
-----------

Issues TARGET_RESET to end device using handshaking method

\ ``ioc``\ 
\ ``channel``\ 
\ ``id``\ 

Returns (1) success
(0) failure

.. _`mptsas_target_reset_queue`:

mptsas_target_reset_queue
=========================

.. c:function:: void mptsas_target_reset_queue(MPT_ADAPTER *ioc, EVENT_DATA_SAS_DEVICE_STATUS_CHANGE *sas_event_data)

    :param ioc:
        *undescribed*
    :type ioc: MPT_ADAPTER \*

    :param sas_event_data:
        *undescribed*
    :type sas_event_data: EVENT_DATA_SAS_DEVICE_STATUS_CHANGE \*

.. _`mptsas_target_reset_queue.description`:

Description
-----------

Receive request for TARGET_RESET after receiving an firmware
event NOT_RESPONDING_EVENT, then put command in link list
and queue if task_queue already in use.

\ ``ioc``\ 
\ ``sas_event_data``\ 

.. _`mptsas_schedule_target_reset`:

mptsas_schedule_target_reset
============================

.. c:function:: void mptsas_schedule_target_reset(void *iocp)

    send pending target reset

    :param iocp:
        per adapter object
    :type iocp: void \*

.. _`mptsas_schedule_target_reset.description`:

Description
-----------

This function will delete scheduled target reset from the list and
try to send next target reset. This will be called from completion
context of any Task management command.

.. _`mptsas_taskmgmt_complete`:

mptsas_taskmgmt_complete
========================

.. c:function:: int mptsas_taskmgmt_complete(MPT_ADAPTER *ioc, MPT_FRAME_HDR *mf, MPT_FRAME_HDR *mr)

    complete SAS task management function

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param mf:
        *undescribed*
    :type mf: MPT_FRAME_HDR \*

    :param mr:
        *undescribed*
    :type mr: MPT_FRAME_HDR \*

.. _`mptsas_taskmgmt_complete.description`:

Description
-----------

Completion for TARGET_RESET after NOT_RESPONDING_EVENT, enable work
queue to finish off removing device from upper layers. then send next
TARGET_RESET in the queue.

.. _`mptsas_ioc_reset`:

mptsas_ioc_reset
================

.. c:function:: int mptsas_ioc_reset(MPT_ADAPTER *ioc, int reset_phase)

    :param ioc:
        *undescribed*
    :type ioc: MPT_ADAPTER \*

    :param reset_phase:
        *undescribed*
    :type reset_phase: int

.. _`mptsas_ioc_reset.description`:

Description
-----------

\ ``ioc``\ 
\ ``reset_phase``\ 

.. _`device_state`:

enum device_state
=================

.. c:type:: enum device_state


.. _`device_state.definition`:

Definition
----------

.. code-block:: c

    enum device_state {
        DEVICE_RETRY,
        DEVICE_ERROR,
        DEVICE_READY
    };

.. _`device_state.constants`:

Constants
---------

DEVICE_RETRY
    need to retry the TUR

DEVICE_ERROR
    TUR return error, don't add device

DEVICE_READY
    device can be added

.. _`mptsas_add_end_device`:

mptsas_add_end_device
=====================

.. c:function:: int mptsas_add_end_device(MPT_ADAPTER *ioc, struct mptsas_phyinfo *phy_info)

    report a new end device to sas transport layer

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param phy_info:
        describes attached device
    :type phy_info: struct mptsas_phyinfo \*

.. _`mptsas_add_end_device.description`:

Description
-----------

return (0) success (1) failure

.. _`mptsas_del_end_device`:

mptsas_del_end_device
=====================

.. c:function:: void mptsas_del_end_device(MPT_ADAPTER *ioc, struct mptsas_phyinfo *phy_info)

    report a deleted end device to sas transport layer

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param phy_info:
        describes attached device
    :type phy_info: struct mptsas_phyinfo \*

.. _`mptsas_firmware_event_work`:

mptsas_firmware_event_work
==========================

.. c:function:: void mptsas_firmware_event_work(struct work_struct *work)

    work thread for processing fw events

    :param work:
        work queue payload containing info describing the event
    :type work: struct work_struct \*

.. _`mptsas_firmware_event_work.context`:

Context
-------

user

.. _`mptsas_eh_timed_out`:

mptsas_eh_timed_out
===================

.. c:function:: enum blk_eh_timer_return mptsas_eh_timed_out(struct scsi_cmnd *sc)

    resets the scsi_cmnd timeout if the device under question is currently in the device removal delay.

    :param sc:
        scsi command that the midlayer is about to time out
    :type sc: struct scsi_cmnd \*

.. _`mptsas_exp_repmanufacture_info`:

mptsas_exp_repmanufacture_info
==============================

.. c:function:: int mptsas_exp_repmanufacture_info(MPT_ADAPTER *ioc, u64 sas_address, struct sas_expander_device *edev)

    :param ioc:
        per adapter object
    :type ioc: MPT_ADAPTER \*

    :param sas_address:
        expander sas address
    :type sas_address: u64

    :param edev:
        the sas_expander_device object
    :type edev: struct sas_expander_device \*

.. _`mptsas_exp_repmanufacture_info.description`:

Description
-----------

Fills in the sas_expander_device object when SMP port is created.

Returns 0 for success, non-zero for failure.

.. _`mptsas_delete_expander_siblings`:

mptsas_delete_expander_siblings
===============================

.. c:function:: void mptsas_delete_expander_siblings(MPT_ADAPTER *ioc, struct mptsas_portinfo *parent, struct mptsas_portinfo *expander)

    remove siblings attached to expander

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param parent:
        the parent port_info object
    :type parent: struct mptsas_portinfo \*

    :param expander:
        the expander port_info object
    :type expander: struct mptsas_portinfo \*

.. _`mptsas_expander_delete`:

mptsas_expander_delete
======================

.. c:function:: void mptsas_expander_delete(MPT_ADAPTER *ioc, struct mptsas_portinfo *port_info, u8 force)

    remove this expander

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param port_info:
        expander port_info struct
    :type port_info: struct mptsas_portinfo \*

    :param force:
        Flag to forcefully delete the expander
    :type force: u8

.. _`mptsas_send_expander_event`:

mptsas_send_expander_event
==========================

.. c:function:: void mptsas_send_expander_event(struct fw_event_work *fw_event)

    expanders events

    :param fw_event:
        *undescribed*
    :type fw_event: struct fw_event_work \*

.. _`mptsas_send_expander_event.description`:

Description
-----------


This function handles adding, removing, and refreshing
device handles within the expander objects.

.. _`mptsas_expander_add`:

mptsas_expander_add
===================

.. c:function:: struct mptsas_portinfo *mptsas_expander_add(MPT_ADAPTER *ioc, u16 handle)

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param handle:
        *undescribed*
    :type handle: u16

.. _`mptsas_probe_expanders`:

mptsas_probe_expanders
======================

.. c:function:: void mptsas_probe_expanders(MPT_ADAPTER *ioc)

    adding expanders

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

.. _`mptsas_scan_sas_topology`:

mptsas_scan_sas_topology
========================

.. c:function:: void mptsas_scan_sas_topology(MPT_ADAPTER *ioc)

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

.. _`mptsas_find_phyinfo_by_phys_disk_num`:

mptsas_find_phyinfo_by_phys_disk_num
====================================

.. c:function:: struct mptsas_phyinfo *mptsas_find_phyinfo_by_phys_disk_num(MPT_ADAPTER *ioc, u8 phys_disk_num, u8 channel, u8 id)

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param phys_disk_num:
        *undescribed*
    :type phys_disk_num: u8

    :param channel:
        *undescribed*
    :type channel: u8

    :param id:
        *undescribed*
    :type id: u8

.. _`mptsas_issue_tm`:

mptsas_issue_tm
===============

.. c:function:: int mptsas_issue_tm(MPT_ADAPTER *ioc, u8 type, u8 channel, u8 id, u64 lun, int task_context, ulong timeout, u8 *issue_reset)

    send mptsas internal tm request

    :param ioc:
        Pointer to MPT_ADAPTER structure
    :type ioc: MPT_ADAPTER \*

    :param type:
        Task Management type
    :type type: u8

    :param channel:
        channel number for task management
    :type channel: u8

    :param id:
        Logical Target ID for reset (if appropriate)
    :type id: u8

    :param lun:
        Logical unit for reset (if appropriate)
    :type lun: u64

    :param task_context:
        Context for the task to be aborted
    :type task_context: int

    :param timeout:
        timeout for task management control
    :type timeout: ulong

    :param issue_reset:
        *undescribed*
    :type issue_reset: u8 \*

.. _`mptsas_issue_tm.description`:

Description
-----------

return 0 on success and -1 on failure:

.. _`mptsas_broadcast_primitive_work`:

mptsas_broadcast_primitive_work
===============================

.. c:function:: void mptsas_broadcast_primitive_work(struct fw_event_work *fw_event)

    Handle broadcast primitives

    :param fw_event:
        *undescribed*
    :type fw_event: struct fw_event_work \*

.. _`mptsas_broadcast_primitive_work.description`:

Description
-----------

this will be handled in workqueue context.

.. This file was automatic generated / don't edit.

