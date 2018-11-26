.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/pm8001/pm8001_hwi.c

.. _`read_main_config_table`:

read_main_config_table
======================

.. c:function:: void read_main_config_table(struct pm8001_hba_info *pm8001_ha)

    read the configure table and save it.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`read_general_status_table`:

read_general_status_table
=========================

.. c:function:: void read_general_status_table(struct pm8001_hba_info *pm8001_ha)

    read the general status table and save it.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`read_inbnd_queue_table`:

read_inbnd_queue_table
======================

.. c:function:: void read_inbnd_queue_table(struct pm8001_hba_info *pm8001_ha)

    read the inbound queue table and save it.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`read_outbnd_queue_table`:

read_outbnd_queue_table
=======================

.. c:function:: void read_outbnd_queue_table(struct pm8001_hba_info *pm8001_ha)

    read the outbound queue table and save it.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`init_default_table_values`:

init_default_table_values
=========================

.. c:function:: void init_default_table_values(struct pm8001_hba_info *pm8001_ha)

    init the default table.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`update_main_config_table`:

update_main_config_table
========================

.. c:function:: void update_main_config_table(struct pm8001_hba_info *pm8001_ha)

    update the main default table to the HBA.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`update_inbnd_queue_table`:

update_inbnd_queue_table
========================

.. c:function:: void update_inbnd_queue_table(struct pm8001_hba_info *pm8001_ha, int number)

    update the inbound queue table to the HBA.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param number:
        *undescribed*
    :type number: int

.. _`update_outbnd_queue_table`:

update_outbnd_queue_table
=========================

.. c:function:: void update_outbnd_queue_table(struct pm8001_hba_info *pm8001_ha, int number)

    update the outbound queue table to the HBA.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param number:
        *undescribed*
    :type number: int

.. _`pm8001_bar4_shift`:

pm8001_bar4_shift
=================

.. c:function:: int pm8001_bar4_shift(struct pm8001_hba_info *pm8001_ha, u32 shiftValue)

    function is called to shift BAR base address

    :param pm8001_ha:
        our hba card infomation
    :type pm8001_ha: struct pm8001_hba_info \*

    :param shiftValue:
        shifting value in memory bar.
    :type shiftValue: u32

.. _`mpi_set_phys_g3_with_ssc`:

mpi_set_phys_g3_with_ssc
========================

.. c:function:: void mpi_set_phys_g3_with_ssc(struct pm8001_hba_info *pm8001_ha, u32 SSCbit)

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param SSCbit:
        set SSCbit to 0 to disable all phys ssc; 1 to enable all phys ssc.
    :type SSCbit: u32

.. _`mpi_set_open_retry_interval_reg`:

mpi_set_open_retry_interval_reg
===============================

.. c:function:: void mpi_set_open_retry_interval_reg(struct pm8001_hba_info *pm8001_ha, u32 interval)

    :param pm8001_ha:
        our hba card information
        \ ``interval``\  - interval time for each OPEN_REJECT (RETRY). The units are in 1us.
    :type pm8001_ha: struct pm8001_hba_info \*

    :param interval:
        *undescribed*
    :type interval: u32

.. _`mpi_init_check`:

mpi_init_check
==============

.. c:function:: int mpi_init_check(struct pm8001_hba_info *pm8001_ha)

    check firmware initialization status.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`check_fw_ready`:

check_fw_ready
==============

.. c:function:: int check_fw_ready(struct pm8001_hba_info *pm8001_ha)

    The LLDD check if the FW is ready, if not, return error.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`pm8001_chip_init`:

pm8001_chip_init
================

.. c:function:: int pm8001_chip_init(struct pm8001_hba_info *pm8001_ha)

    the main init function that initialize whole PM8001 chip.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`soft_reset_ready_check`:

soft_reset_ready_check
======================

.. c:function:: u32 soft_reset_ready_check(struct pm8001_hba_info *pm8001_ha)

    Function to check FW is ready for soft reset.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`pm8001_chip_soft_rst`:

pm8001_chip_soft_rst
====================

.. c:function:: int pm8001_chip_soft_rst(struct pm8001_hba_info *pm8001_ha)

    soft reset the PM8001 chip, so that the clear all the FW register status to the originated status.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`pm8001_chip_iounmap`:

pm8001_chip_iounmap
===================

.. c:function:: void pm8001_chip_iounmap(struct pm8001_hba_info *pm8001_ha)

    which maped when initialized.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`pm8001_chip_intx_interrupt_enable`:

pm8001_chip_intx_interrupt_enable
=================================

.. c:function:: void pm8001_chip_intx_interrupt_enable(struct pm8001_hba_info *pm8001_ha)

    enable PM8001 chip interrupt

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

.. _`pm8001_chip_msix_interrupt_enable`:

pm8001_chip_msix_interrupt_enable
=================================

.. c:function:: void pm8001_chip_msix_interrupt_enable(struct pm8001_hba_info *pm8001_ha, u32 int_vec_idx)

    enable PM8001 chip interrupt

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param int_vec_idx:
        *undescribed*
    :type int_vec_idx: u32

.. _`pm8001_chip_msix_interrupt_disable`:

pm8001_chip_msix_interrupt_disable
==================================

.. c:function:: void pm8001_chip_msix_interrupt_disable(struct pm8001_hba_info *pm8001_ha, u32 int_vec_idx)

    disable PM8001 chip interrupt

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param int_vec_idx:
        *undescribed*
    :type int_vec_idx: u32

.. _`pm8001_chip_interrupt_enable`:

pm8001_chip_interrupt_enable
============================

.. c:function:: void pm8001_chip_interrupt_enable(struct pm8001_hba_info *pm8001_ha, u8 vec)

    enable PM8001 chip interrupt

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param vec:
        *undescribed*
    :type vec: u8

.. _`pm8001_chip_interrupt_disable`:

pm8001_chip_interrupt_disable
=============================

.. c:function:: void pm8001_chip_interrupt_disable(struct pm8001_hba_info *pm8001_ha, u8 vec)

    disable PM8001 chip interrupt

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param vec:
        *undescribed*
    :type vec: u8

.. _`pm8001_mpi_msg_free_get`:

pm8001_mpi_msg_free_get
=======================

.. c:function:: int pm8001_mpi_msg_free_get(struct inbound_queue_table *circularQ, u16 messageSize, void **messagePtr)

    get the free message buffer for transfer inbound queue.

    :param circularQ:
        the inbound queue  we want to transfer to HBA.
    :type circularQ: struct inbound_queue_table \*

    :param messageSize:
        the message size of this transfer, normally it is 64 bytes
    :type messageSize: u16

    :param messagePtr:
        the pointer to message.
    :type messagePtr: void \*\*

.. _`pm8001_mpi_build_cmd`:

pm8001_mpi_build_cmd
====================

.. c:function:: int pm8001_mpi_build_cmd(struct pm8001_hba_info *pm8001_ha, struct inbound_queue_table *circularQ, u32 opCode, void *payload, u32 responseQueue)

    build the message queue for transfer, update the PI to FW to tell the fw to get this message from IOMB.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param circularQ:
        the inbound queue we want to transfer to HBA.
    :type circularQ: struct inbound_queue_table \*

    :param opCode:
        the operation code represents commands which LLDD and fw recognized.
    :type opCode: u32

    :param payload:
        the command payload of each operation command.
    :type payload: void \*

    :param responseQueue:
        *undescribed*
    :type responseQueue: u32

.. _`pm8001_mpi_msg_consume`:

pm8001_mpi_msg_consume
======================

.. c:function:: u32 pm8001_mpi_msg_consume(struct pm8001_hba_info *pm8001_ha, struct outbound_queue_table *circularQ, void **messagePtr1, u8 *pBC)

    get the MPI message from outbound queue message table.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param circularQ:
        the outbound queue  table.
    :type circularQ: struct outbound_queue_table \*

    :param messagePtr1:
        the message contents of this outbound message.
    :type messagePtr1: void \*\*

    :param pBC:
        the message size.
    :type pBC: u8 \*

.. _`mpi_ssp_completion`:

mpi_ssp_completion
==================

.. c:function:: void mpi_ssp_completion(struct pm8001_hba_info *pm8001_ha, void *piomb)

    process the event that FW response to the SSP request.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param piomb:
        the message contents of this outbound message.
    :type piomb: void \*

.. _`mpi_ssp_completion.description`:

Description
-----------

When FW has completed a ssp request for example a IO request, after it has
filled the SG data with the data, it will trigger this event represent
that he has finished the job,please check the coresponding buffer.
So we will tell the caller who maybe waiting the result to tell upper layer
that the task has been finished.

.. _`pm8001_bytes_dmaed`:

pm8001_bytes_dmaed
==================

.. c:function:: void pm8001_bytes_dmaed(struct pm8001_hba_info *pm8001_ha, int i)

    one of the interface function communication with libsas

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param i:
        which phy that received the event.
    :type i: int

.. _`pm8001_bytes_dmaed.description`:

Description
-----------

when HBA driver received the identify done event or initiate FIS received
event(for SATA), it will invoke this function to notify the sas layer that
the sas toplogy has formed, please discover the the whole sas domain,
while receive a broadcast(change) primitive just tell the sas
layer to discover the changed domain rather than the whole domain.

.. _`pm8001_get_attached_sas_addr`:

pm8001_get_attached_sas_addr
============================

.. c:function:: void pm8001_get_attached_sas_addr(struct pm8001_phy *phy, u8 *sas_addr)

    - extract/generate attached SAS address

    :param phy:
        pointer to asd_phy
    :type phy: struct pm8001_phy \*

    :param sas_addr:
        pointer to buffer where the SAS address is to be written
    :type sas_addr: u8 \*

.. _`pm8001_get_attached_sas_addr.description`:

Description
-----------

This function extracts the SAS address from an IDENTIFY frame
received.  If OOB is SATA, then a SAS address is generated from the
HA tables.

.. _`pm8001_get_attached_sas_addr.locking`:

LOCKING
-------

the frame_rcvd_lock needs to be held since this parses the frame
buffer.

.. _`pm8001_hw_event_ack_req`:

pm8001_hw_event_ack_req
=======================

.. c:function:: void pm8001_hw_event_ack_req(struct pm8001_hba_info *pm8001_ha, u32 Qnum, u32 SEA, u32 port_id, u32 phyId, u32 param0, u32 param1)

    For PM8001,some events need to acknowage to FW.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param Qnum:
        the outbound queue message number.
    :type Qnum: u32

    :param SEA:
        source of event to ack
    :type SEA: u32

    :param port_id:
        port id.
    :type port_id: u32

    :param phyId:
        phy id.
    :type phyId: u32

    :param param0:
        parameter 0.
    :type param0: u32

    :param param1:
        parameter 1.
    :type param1: u32

.. _`hw_event_sas_phy_up`:

hw_event_sas_phy_up
===================

.. c:function:: void hw_event_sas_phy_up(struct pm8001_hba_info *pm8001_ha, void *piomb)

    FW tells me a SAS phy up event.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param piomb:
        IO message buffer
    :type piomb: void \*

.. _`hw_event_sata_phy_up`:

hw_event_sata_phy_up
====================

.. c:function:: void hw_event_sata_phy_up(struct pm8001_hba_info *pm8001_ha, void *piomb)

    FW tells me a SATA phy up event.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param piomb:
        IO message buffer
    :type piomb: void \*

.. _`hw_event_phy_down`:

hw_event_phy_down
=================

.. c:function:: void hw_event_phy_down(struct pm8001_hba_info *pm8001_ha, void *piomb)

    we should notify the libsas the phy is down.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param piomb:
        IO message buffer
    :type piomb: void \*

.. _`pm8001_mpi_reg_resp`:

pm8001_mpi_reg_resp
===================

.. c:function:: int pm8001_mpi_reg_resp(struct pm8001_hba_info *pm8001_ha, void *piomb)

    process register device ID response.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param piomb:
        IO message buffer
    :type piomb: void \*

.. _`pm8001_mpi_reg_resp.description`:

Description
-----------

when sas layer find a device it will notify LLDD, then the driver register
the domain device to FW, this event is the return device ID which the FW
has assigned, from now,inter-communication with FW is no longer using the
SAS address, use device ID which FW assigned.

.. _`pm8001_mpi_fw_flash_update_resp`:

pm8001_mpi_fw_flash_update_resp
===============================

.. c:function:: int pm8001_mpi_fw_flash_update_resp(struct pm8001_hba_info *pm8001_ha, void *piomb)

    Response from FW for flash update command.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param piomb:
        IO message buffer
    :type piomb: void \*

.. _`mpi_hw_event`:

mpi_hw_event
============

.. c:function:: int mpi_hw_event(struct pm8001_hba_info *pm8001_ha, void* piomb)

    The hw event has come.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param piomb:
        IO message buffer
    :type piomb: void\*

.. _`process_one_iomb`:

process_one_iomb
================

.. c:function:: void process_one_iomb(struct pm8001_hba_info *pm8001_ha, void *piomb)

    process one outbound Queue memory block

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param piomb:
        IO message buffer
    :type piomb: void \*

.. _`pm8001_chip_smp_req`:

pm8001_chip_smp_req
===================

.. c:function:: int pm8001_chip_smp_req(struct pm8001_hba_info *pm8001_ha, struct pm8001_ccb_info *ccb)

    send a SMP task to FW

    :param pm8001_ha:
        our hba card information.
    :type pm8001_ha: struct pm8001_hba_info \*

    :param ccb:
        the ccb information this request used.
    :type ccb: struct pm8001_ccb_info \*

.. _`pm8001_chip_ssp_io_req`:

pm8001_chip_ssp_io_req
======================

.. c:function:: int pm8001_chip_ssp_io_req(struct pm8001_hba_info *pm8001_ha, struct pm8001_ccb_info *ccb)

    send a SSP task to FW

    :param pm8001_ha:
        our hba card information.
    :type pm8001_ha: struct pm8001_hba_info \*

    :param ccb:
        the ccb information this request used.
    :type ccb: struct pm8001_ccb_info \*

.. _`pm8001_chip_phy_start_req`:

pm8001_chip_phy_start_req
=========================

.. c:function:: int pm8001_chip_phy_start_req(struct pm8001_hba_info *pm8001_ha, u8 phy_id)

    start phy via PHY_START COMMAND

    :param pm8001_ha:
        our hba card information.
    :type pm8001_ha: struct pm8001_hba_info \*

    :param phy_id:
        the phy id which we wanted to start up.
    :type phy_id: u8

.. _`pm8001_chip_phy_stop_req`:

pm8001_chip_phy_stop_req
========================

.. c:function:: int pm8001_chip_phy_stop_req(struct pm8001_hba_info *pm8001_ha, u8 phy_id)

    start phy via PHY_STOP COMMAND

    :param pm8001_ha:
        our hba card information.
    :type pm8001_ha: struct pm8001_hba_info \*

    :param phy_id:
        the phy id which we wanted to start up.
    :type phy_id: u8

.. _`pm8001_chip_reg_dev_req`:

pm8001_chip_reg_dev_req
=======================

.. c:function:: int pm8001_chip_reg_dev_req(struct pm8001_hba_info *pm8001_ha, struct pm8001_device *pm8001_dev, u32 flag)

    :param pm8001_ha:
        *undescribed*
    :type pm8001_ha: struct pm8001_hba_info \*

    :param pm8001_dev:
        *undescribed*
    :type pm8001_dev: struct pm8001_device \*

    :param flag:
        *undescribed*
    :type flag: u32

.. _`pm8001_chip_dereg_dev_req`:

pm8001_chip_dereg_dev_req
=========================

.. c:function:: int pm8001_chip_dereg_dev_req(struct pm8001_hba_info *pm8001_ha, u32 device_id)

    :param pm8001_ha:
        *undescribed*
    :type pm8001_ha: struct pm8001_hba_info \*

    :param device_id:
        *undescribed*
    :type device_id: u32

.. _`pm8001_chip_phy_ctl_req`:

pm8001_chip_phy_ctl_req
=======================

.. c:function:: int pm8001_chip_phy_ctl_req(struct pm8001_hba_info *pm8001_ha, u32 phyId, u32 phy_op)

    support the local phy operation

    :param pm8001_ha:
        our hba card information.
    :type pm8001_ha: struct pm8001_hba_info \*

    :param phyId:
        *undescribed*
    :type phyId: u32

    :param phy_op:
        *undescribed*
    :type phy_op: u32

.. _`pm8001_chip_isr`:

pm8001_chip_isr
===============

.. c:function:: irqreturn_t pm8001_chip_isr(struct pm8001_hba_info *pm8001_ha, u8 vec)

    PM8001 isr handler.

    :param pm8001_ha:
        our hba card information.
    :type pm8001_ha: struct pm8001_hba_info \*

    :param vec:
        *undescribed*
    :type vec: u8

.. _`pm8001_chip_abort_task`:

pm8001_chip_abort_task
======================

.. c:function:: int pm8001_chip_abort_task(struct pm8001_hba_info *pm8001_ha, struct pm8001_device *pm8001_dev, u8 flag, u32 task_tag, u32 cmd_tag)

    SAS abort task when error or exception happened.

    :param pm8001_ha:
        *undescribed*
    :type pm8001_ha: struct pm8001_hba_info \*

    :param pm8001_dev:
        *undescribed*
    :type pm8001_dev: struct pm8001_device \*

    :param flag:
        the abort flag.
    :type flag: u8

    :param task_tag:
        *undescribed*
    :type task_tag: u32

    :param cmd_tag:
        *undescribed*
    :type cmd_tag: u32

.. _`pm8001_chip_ssp_tm_req`:

pm8001_chip_ssp_tm_req
======================

.. c:function:: int pm8001_chip_ssp_tm_req(struct pm8001_hba_info *pm8001_ha, struct pm8001_ccb_info *ccb, struct pm8001_tmf_task *tmf)

    built the task management command.

    :param pm8001_ha:
        our hba card information.
    :type pm8001_ha: struct pm8001_hba_info \*

    :param ccb:
        the ccb information.
    :type ccb: struct pm8001_ccb_info \*

    :param tmf:
        task management function.
    :type tmf: struct pm8001_tmf_task \*

.. _`pm8001_chip_fw_flash_update_build`:

pm8001_chip_fw_flash_update_build
=================================

.. c:function:: int pm8001_chip_fw_flash_update_build(struct pm8001_hba_info *pm8001_ha, void *fw_flash_updata_info, u32 tag)

    support the firmware update operation

    :param pm8001_ha:
        our hba card information.
    :type pm8001_ha: struct pm8001_hba_info \*

    :param fw_flash_updata_info:
        firmware flash update param
    :type fw_flash_updata_info: void \*

    :param tag:
        *undescribed*
    :type tag: u32

.. This file was automatic generated / don't edit.

