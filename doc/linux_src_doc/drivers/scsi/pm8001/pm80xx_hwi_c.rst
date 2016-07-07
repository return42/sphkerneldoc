.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/pm8001/pm80xx_hwi.c

.. _`read_main_config_table`:

read_main_config_table
======================

.. c:function:: void read_main_config_table(struct pm8001_hba_info *pm8001_ha)

    read the configure table and save it.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

.. _`read_general_status_table`:

read_general_status_table
=========================

.. c:function:: void read_general_status_table(struct pm8001_hba_info *pm8001_ha)

    read the general status table and save it.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

.. _`read_phy_attr_table`:

read_phy_attr_table
===================

.. c:function:: void read_phy_attr_table(struct pm8001_hba_info *pm8001_ha)

    read the phy attribute table and save it.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

.. _`read_inbnd_queue_table`:

read_inbnd_queue_table
======================

.. c:function:: void read_inbnd_queue_table(struct pm8001_hba_info *pm8001_ha)

    read the inbound queue table and save it.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

.. _`read_outbnd_queue_table`:

read_outbnd_queue_table
=======================

.. c:function:: void read_outbnd_queue_table(struct pm8001_hba_info *pm8001_ha)

    read the outbound queue table and save it.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

.. _`init_default_table_values`:

init_default_table_values
=========================

.. c:function:: void init_default_table_values(struct pm8001_hba_info *pm8001_ha)

    init the default table.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

.. _`update_main_config_table`:

update_main_config_table
========================

.. c:function:: void update_main_config_table(struct pm8001_hba_info *pm8001_ha)

    update the main default table to the HBA.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

.. _`update_inbnd_queue_table`:

update_inbnd_queue_table
========================

.. c:function:: void update_inbnd_queue_table(struct pm8001_hba_info *pm8001_ha, int number)

    update the inbound queue table to the HBA.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param int number:
        *undescribed*

.. _`update_outbnd_queue_table`:

update_outbnd_queue_table
=========================

.. c:function:: void update_outbnd_queue_table(struct pm8001_hba_info *pm8001_ha, int number)

    update the outbound queue table to the HBA.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param int number:
        *undescribed*

.. _`mpi_init_check`:

mpi_init_check
==============

.. c:function:: int mpi_init_check(struct pm8001_hba_info *pm8001_ha)

    check firmware initialization status.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

.. _`check_fw_ready`:

check_fw_ready
==============

.. c:function:: int check_fw_ready(struct pm8001_hba_info *pm8001_ha)

    The LLDD check if the FW is ready, if not, return error.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

.. _`pm80xx_set_thermal_config`:

pm80xx_set_thermal_config
=========================

.. c:function:: int pm80xx_set_thermal_config(struct pm8001_hba_info *pm8001_ha)

    support the thermal configuration

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information.

.. _`pm80xx_set_sas_protocol_timer_config`:

pm80xx_set_sas_protocol_timer_config
====================================

.. c:function:: int pm80xx_set_sas_protocol_timer_config(struct pm8001_hba_info *pm8001_ha)

    support the SAS Protocol Timer configuration page

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information.

.. _`pm80xx_get_encrypt_info`:

pm80xx_get_encrypt_info
=======================

.. c:function:: int pm80xx_get_encrypt_info(struct pm8001_hba_info *pm8001_ha)

    Check for encryption

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information.

.. _`pm80xx_encrypt_update`:

pm80xx_encrypt_update
=====================

.. c:function:: int pm80xx_encrypt_update(struct pm8001_hba_info *pm8001_ha)

    update flash with encryption informtion

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information.

.. _`pm80xx_chip_init`:

pm80xx_chip_init
================

.. c:function:: int pm80xx_chip_init(struct pm8001_hba_info *pm8001_ha)

    the main init function that initialize whole PM8001 chip.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

.. _`pm80xx_chip_soft_rst`:

pm80xx_chip_soft_rst
====================

.. c:function:: int pm80xx_chip_soft_rst(struct pm8001_hba_info *pm8001_ha)

    soft reset the PM8001 chip, so that the clear all the FW register status to the originated status.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

.. _`pm80xx_chip_intx_interrupt_enable`:

pm80xx_chip_intx_interrupt_enable
=================================

.. c:function:: void pm80xx_chip_intx_interrupt_enable(struct pm8001_hba_info *pm8001_ha)

    enable PM8001 chip interrupt

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

.. _`pm80xx_chip_intx_interrupt_disable`:

pm80xx_chip_intx_interrupt_disable
==================================

.. c:function:: void pm80xx_chip_intx_interrupt_disable(struct pm8001_hba_info *pm8001_ha)

    disable PM8001 chip interrupt

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

.. _`pm80xx_chip_interrupt_enable`:

pm80xx_chip_interrupt_enable
============================

.. c:function:: void pm80xx_chip_interrupt_enable(struct pm8001_hba_info *pm8001_ha, u8 vec)

    enable PM8001 chip interrupt

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param u8 vec:
        *undescribed*

.. _`pm80xx_chip_interrupt_disable`:

pm80xx_chip_interrupt_disable
=============================

.. c:function:: void pm80xx_chip_interrupt_disable(struct pm8001_hba_info *pm8001_ha, u8 vec)

    disable PM8001 chip interrupt

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param u8 vec:
        *undescribed*

.. _`mpi_ssp_completion`:

mpi_ssp_completion
==================

.. c:function:: void mpi_ssp_completion(struct pm8001_hba_info *pm8001_ha, void *piomb)

    process the event that FW response to the SSP request.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        the message contents of this outbound message.

.. _`mpi_ssp_completion.description`:

Description
-----------

When FW has completed a ssp request for example a IO request, after it has
filled the SG data with the data, it will trigger this event represent
that he has finished the job,please check the coresponding buffer.
So we will tell the caller who maybe waiting the result to tell upper layer
that the task has been finished.

.. _`pm80xx_hw_event_ack_req`:

pm80xx_hw_event_ack_req
=======================

.. c:function:: void pm80xx_hw_event_ack_req(struct pm8001_hba_info *pm8001_ha, u32 Qnum, u32 SEA, u32 port_id, u32 phyId, u32 param0, u32 param1)

    For PM8001,some events need to acknowage to FW.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param u32 Qnum:
        the outbound queue message number.

    :param u32 SEA:
        source of event to ack

    :param u32 port_id:
        port id.

    :param u32 phyId:
        phy id.

    :param u32 param0:
        parameter 0.

    :param u32 param1:
        parameter 1.

.. _`hw_event_sas_phy_up`:

hw_event_sas_phy_up
===================

.. c:function:: void hw_event_sas_phy_up(struct pm8001_hba_info *pm8001_ha, void *piomb)

    FW tells me a SAS phy up event.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`hw_event_sata_phy_up`:

hw_event_sata_phy_up
====================

.. c:function:: void hw_event_sata_phy_up(struct pm8001_hba_info *pm8001_ha, void *piomb)

    FW tells me a SATA phy up event.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`hw_event_phy_down`:

hw_event_phy_down
=================

.. c:function:: void hw_event_phy_down(struct pm8001_hba_info *pm8001_ha, void *piomb)

    we should notify the libsas the phy is down.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`mpi_thermal_hw_event`:

mpi_thermal_hw_event
====================

.. c:function:: int mpi_thermal_hw_event(struct pm8001_hba_info *pm8001_ha, void *piomb)

    The hw event has come.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`mpi_hw_event`:

mpi_hw_event
============

.. c:function:: int mpi_hw_event(struct pm8001_hba_info *pm8001_ha, void *piomb)

    The hw event has come.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`mpi_phy_stop_resp`:

mpi_phy_stop_resp
=================

.. c:function:: int mpi_phy_stop_resp(struct pm8001_hba_info *pm8001_ha, void *piomb)

    SPCv specific

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`mpi_set_controller_config_resp`:

mpi_set_controller_config_resp
==============================

.. c:function:: int mpi_set_controller_config_resp(struct pm8001_hba_info *pm8001_ha, void *piomb)

    SPCv specific

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`mpi_get_controller_config_resp`:

mpi_get_controller_config_resp
==============================

.. c:function:: int mpi_get_controller_config_resp(struct pm8001_hba_info *pm8001_ha, void *piomb)

    SPCv specific

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`mpi_get_phy_profile_resp`:

mpi_get_phy_profile_resp
========================

.. c:function:: int mpi_get_phy_profile_resp(struct pm8001_hba_info *pm8001_ha, void *piomb)

    SPCv specific

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`mpi_flash_op_ext_resp`:

mpi_flash_op_ext_resp
=====================

.. c:function:: int mpi_flash_op_ext_resp(struct pm8001_hba_info *pm8001_ha, void *piomb)

    SPCv specific

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`mpi_set_phy_profile_resp`:

mpi_set_phy_profile_resp
========================

.. c:function:: int mpi_set_phy_profile_resp(struct pm8001_hba_info *pm8001_ha, void *piomb)

    SPCv specific

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`mpi_kek_management_resp`:

mpi_kek_management_resp
=======================

.. c:function:: int mpi_kek_management_resp(struct pm8001_hba_info *pm8001_ha, void *piomb)

    SPCv specific

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`mpi_dek_management_resp`:

mpi_dek_management_resp
=======================

.. c:function:: int mpi_dek_management_resp(struct pm8001_hba_info *pm8001_ha, void *piomb)

    SPCv specific

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`ssp_coalesced_comp_resp`:

ssp_coalesced_comp_resp
=======================

.. c:function:: int ssp_coalesced_comp_resp(struct pm8001_hba_info *pm8001_ha, void *piomb)

    SPCv specific

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`process_one_iomb`:

process_one_iomb
================

.. c:function:: void process_one_iomb(struct pm8001_hba_info *pm8001_ha, void *piomb)

    process one outbound Queue memory block

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param void \*piomb:
        IO message buffer

.. _`pm80xx_chip_smp_req`:

pm80xx_chip_smp_req
===================

.. c:function:: int pm80xx_chip_smp_req(struct pm8001_hba_info *pm8001_ha, struct pm8001_ccb_info *ccb)

    send a SMP task to FW

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information.

    :param struct pm8001_ccb_info \*ccb:
        the ccb information this request used.

.. _`pm80xx_chip_ssp_io_req`:

pm80xx_chip_ssp_io_req
======================

.. c:function:: int pm80xx_chip_ssp_io_req(struct pm8001_hba_info *pm8001_ha, struct pm8001_ccb_info *ccb)

    send a SSP task to FW

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information.

    :param struct pm8001_ccb_info \*ccb:
        the ccb information this request used.

.. _`pm80xx_chip_phy_start_req`:

pm80xx_chip_phy_start_req
=========================

.. c:function:: int pm80xx_chip_phy_start_req(struct pm8001_hba_info *pm8001_ha, u8 phy_id)

    start phy via PHY_START COMMAND

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information.

    :param u8 phy_id:
        the phy id which we wanted to start up.

.. _`pm80xx_chip_phy_stop_req`:

pm80xx_chip_phy_stop_req
========================

.. c:function:: int pm80xx_chip_phy_stop_req(struct pm8001_hba_info *pm8001_ha, u8 phy_id)

    start phy via PHY_STOP COMMAND

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information.

    :param u8 phy_id:
        the phy id which we wanted to start up.

.. _`pm80xx_chip_reg_dev_req`:

pm80xx_chip_reg_dev_req
=======================

.. c:function:: int pm80xx_chip_reg_dev_req(struct pm8001_hba_info *pm8001_ha, struct pm8001_device *pm8001_dev, u32 flag)

    :param struct pm8001_hba_info \*pm8001_ha:
        *undescribed*

    :param struct pm8001_device \*pm8001_dev:
        *undescribed*

    :param u32 flag:
        *undescribed*

.. _`pm80xx_chip_phy_ctl_req`:

pm80xx_chip_phy_ctl_req
=======================

.. c:function:: int pm80xx_chip_phy_ctl_req(struct pm8001_hba_info *pm8001_ha, u32 phyId, u32 phy_op)

    support the local phy operation

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information.

    :param u32 phyId:
        *undescribed*

    :param u32 phy_op:
        *undescribed*

.. _`pm80xx_chip_isr`:

pm80xx_chip_isr
===============

.. c:function:: irqreturn_t pm80xx_chip_isr(struct pm8001_hba_info *pm8001_ha, u8 vec)

    PM8001 isr handler.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information.

    :param u8 vec:
        *undescribed*

.. This file was automatic generated / don't edit.

