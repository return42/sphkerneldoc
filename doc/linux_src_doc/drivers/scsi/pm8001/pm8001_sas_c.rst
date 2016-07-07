.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/pm8001/pm8001_sas.c

.. _`pm8001_find_tag`:

pm8001_find_tag
===============

.. c:function:: int pm8001_find_tag(struct sas_task *task, u32 *tag)

    from sas task to find out  tag that belongs to this task

    :param struct sas_task \*task:
        the task sent to the LLDD

    :param u32 \*tag:
        the found tag associated with the task

.. _`pm8001_tag_free`:

pm8001_tag_free
===============

.. c:function:: void pm8001_tag_free(struct pm8001_hba_info *pm8001_ha, u32 tag)

    free the no more needed tag

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba struct

    :param u32 tag:
        the found tag associated with the task

.. _`pm8001_tag_alloc`:

pm8001_tag_alloc
================

.. c:function:: int pm8001_tag_alloc(struct pm8001_hba_info *pm8001_ha, u32 *tag_out)

    allocate a empty tag for task used.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba struct

    :param u32 \*tag_out:
        the found empty tag .

.. _`pm8001_find_ha_by_dev`:

pm8001_find_ha_by_dev
=====================

.. c:function:: struct pm8001_hba_info *pm8001_find_ha_by_dev(struct domain_device *dev)

    from domain device which come from sas layer to find out our hba struct.

    :param struct domain_device \*dev:
        the domain device which from sas layer.

.. _`pm8001_phy_control`:

pm8001_phy_control
==================

.. c:function:: int pm8001_phy_control(struct asd_sas_phy *sas_phy, enum phy_func func, void *funcdata)

    this function should be registered to sas_domain_function_template to provide libsas used, note: this is just control the HBA phy rather than other expander phy if you want control other phy, you should use SMP command.

    :param struct asd_sas_phy \*sas_phy:
        which phy in HBA phys.

    :param enum phy_func func:
        the operation.

    :param void \*funcdata:
        always NULL.

.. _`pm8001_scan_start`:

pm8001_scan_start
=================

.. c:function:: void pm8001_scan_start(struct Scsi_Host *shost)

    we should enable all HBA phys by sending the phy_start command to HBA.

    :param struct Scsi_Host \*shost:
        the scsi host data.

.. _`pm8001_task_prep_smp`:

pm8001_task_prep_smp
====================

.. c:function:: int pm8001_task_prep_smp(struct pm8001_hba_info *pm8001_ha, struct pm8001_ccb_info *ccb)

    the dispatcher function, prepare data for smp task

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param struct pm8001_ccb_info \*ccb:
        the ccb which attached to smp task

.. _`pm8001_task_prep_ata`:

pm8001_task_prep_ata
====================

.. c:function:: int pm8001_task_prep_ata(struct pm8001_hba_info *pm8001_ha, struct pm8001_ccb_info *ccb)

    the dispatcher function, prepare data for sata task

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param struct pm8001_ccb_info \*ccb:
        the ccb which attached to sata task

.. _`pm8001_task_prep_ssp_tm`:

pm8001_task_prep_ssp_tm
=======================

.. c:function:: int pm8001_task_prep_ssp_tm(struct pm8001_hba_info *pm8001_ha, struct pm8001_ccb_info *ccb, struct pm8001_tmf_task *tmf)

    the dispatcher function, prepare task management data

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param struct pm8001_ccb_info \*ccb:
        the ccb which attached to TM

    :param struct pm8001_tmf_task \*tmf:
        the task management IU

.. _`pm8001_task_prep_ssp`:

pm8001_task_prep_ssp
====================

.. c:function:: int pm8001_task_prep_ssp(struct pm8001_hba_info *pm8001_ha, struct pm8001_ccb_info *ccb)

    the dispatcher function,prepare ssp data for ssp task

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param struct pm8001_ccb_info \*ccb:
        the ccb which attached to ssp task

.. _`dev_is_gone`:

DEV_IS_GONE
===========

.. c:function::  DEV_IS_GONE( pm8001_dev)

    queue the task(ssp, smp && ata) to the hardware.

    :param  pm8001_dev:
        *undescribed*

.. _`pm8001_queue_command`:

pm8001_queue_command
====================

.. c:function:: int pm8001_queue_command(struct sas_task *task, gfp_t gfp_flags)

    register for upper layer used, all IO commands sent to HBA are from this interface.

    :param struct sas_task \*task:
        the task to be execute.

    :param gfp_t gfp_flags:
        gfp_flags

.. _`pm8001_ccb_task_free`:

pm8001_ccb_task_free
====================

.. c:function:: void pm8001_ccb_task_free(struct pm8001_hba_info *pm8001_ha, struct sas_task *task, struct pm8001_ccb_info *ccb, u32 ccb_idx)

    free the sg for ssp and smp command, free the ccb.

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param struct sas_task \*task:
        the task to be free.

    :param struct pm8001_ccb_info \*ccb:
        the ccb which attached to ssp task

    :param u32 ccb_idx:
        ccb index.

.. _`pm8001_find_dev`:

pm8001_find_dev
===============

.. c:function:: struct pm8001_device *pm8001_find_dev(struct pm8001_hba_info *pm8001_ha, u32 device_id)

    find a matching pm8001_device

    :param struct pm8001_hba_info \*pm8001_ha:
        our hba card information

    :param u32 device_id:
        *undescribed*

.. _`pm8001_dev_found_notify`:

pm8001_dev_found_notify
=======================

.. c:function:: int pm8001_dev_found_notify(struct domain_device *dev)

    libsas notify a device is found.

    :param struct domain_device \*dev:
        the device structure which sas layer used.

.. _`pm8001_dev_found_notify.description`:

Description
-----------

when libsas find a sas domain device, it should tell the LLDD that
device is found, and then LLDD register this device to HBA firmware
by the command "OPC_INB_REG_DEV", after that the HBA will assign a
device ID(according to device's sas address) and returned it to LLDD. From
now on, we communicate with HBA FW with the device ID which HBA assigned
rather than sas address. it is the necessary step for our HBA but it is
the optional for other HBA driver.

.. _`pm8001_exec_internal_tmf_task`:

pm8001_exec_internal_tmf_task
=============================

.. c:function:: int pm8001_exec_internal_tmf_task(struct domain_device *dev, void *parameter, u32 para_len, struct pm8001_tmf_task *tmf)

    execute some task management commands.

    :param struct domain_device \*dev:
        the wanted device.

    :param void \*parameter:
        ssp task parameter.

    :param u32 para_len:
        para_len.

    :param struct pm8001_tmf_task \*tmf:
        which task management wanted to be take.

.. _`pm8001_exec_internal_tmf_task.description`:

Description
-----------

when errors or exception happened, we may want to do something, for example
abort the issued task which result in this execption, it is done by calling
this function, note it is also with the task execute interface.

.. _`pm8001_dev_gone_notify`:

pm8001_dev_gone_notify
======================

.. c:function:: void pm8001_dev_gone_notify(struct domain_device *dev)

    see the comments for "pm8001_dev_found_notify"

    :param struct domain_device \*dev:
        the device structure which sas layer used.

.. _`pm8001_i_t_nexus_reset`:

pm8001_I_T_nexus_reset
======================

.. c:function:: int pm8001_I_T_nexus_reset(struct domain_device *dev)

    SSP (type 1) , only for RECOVERY

    :param struct domain_device \*dev:
        *undescribed*

.. This file was automatic generated / don't edit.

