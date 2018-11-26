.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/pm8001/pm8001_sas.c

.. _`pm8001_find_tag`:

pm8001_find_tag
===============

.. c:function:: int pm8001_find_tag(struct sas_task *task, u32 *tag)

    from sas task to find out  tag that belongs to this task

    :param task:
        the task sent to the LLDD
    :type task: struct sas_task \*

    :param tag:
        the found tag associated with the task
    :type tag: u32 \*

.. _`pm8001_tag_free`:

pm8001_tag_free
===============

.. c:function:: void pm8001_tag_free(struct pm8001_hba_info *pm8001_ha, u32 tag)

    free the no more needed tag

    :param pm8001_ha:
        our hba struct
    :type pm8001_ha: struct pm8001_hba_info \*

    :param tag:
        the found tag associated with the task
    :type tag: u32

.. _`pm8001_tag_alloc`:

pm8001_tag_alloc
================

.. c:function:: int pm8001_tag_alloc(struct pm8001_hba_info *pm8001_ha, u32 *tag_out)

    allocate a empty tag for task used.

    :param pm8001_ha:
        our hba struct
    :type pm8001_ha: struct pm8001_hba_info \*

    :param tag_out:
        the found empty tag .
    :type tag_out: u32 \*

.. _`pm8001_find_ha_by_dev`:

pm8001_find_ha_by_dev
=====================

.. c:function:: struct pm8001_hba_info *pm8001_find_ha_by_dev(struct domain_device *dev)

    from domain device which come from sas layer to find out our hba struct.

    :param dev:
        the domain device which from sas layer.
    :type dev: struct domain_device \*

.. _`pm8001_phy_control`:

pm8001_phy_control
==================

.. c:function:: int pm8001_phy_control(struct asd_sas_phy *sas_phy, enum phy_func func, void *funcdata)

    this function should be registered to sas_domain_function_template to provide libsas used, note: this is just control the HBA phy rather than other expander phy if you want control other phy, you should use SMP command.

    :param sas_phy:
        which phy in HBA phys.
    :type sas_phy: struct asd_sas_phy \*

    :param func:
        the operation.
    :type func: enum phy_func

    :param funcdata:
        always NULL.
    :type funcdata: void \*

.. _`pm8001_scan_start`:

pm8001_scan_start
=================

.. c:function:: void pm8001_scan_start(struct Scsi_Host *shost)

    we should enable all HBA phys by sending the phy_start command to HBA.

    :param shost:
        the scsi host data.
    :type shost: struct Scsi_Host \*

.. _`pm8001_task_prep_smp`:

pm8001_task_prep_smp
====================

.. c:function:: int pm8001_task_prep_smp(struct pm8001_hba_info *pm8001_ha, struct pm8001_ccb_info *ccb)

    the dispatcher function, prepare data for smp task

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param ccb:
        the ccb which attached to smp task
    :type ccb: struct pm8001_ccb_info \*

.. _`pm8001_task_prep_ata`:

pm8001_task_prep_ata
====================

.. c:function:: int pm8001_task_prep_ata(struct pm8001_hba_info *pm8001_ha, struct pm8001_ccb_info *ccb)

    the dispatcher function, prepare data for sata task

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param ccb:
        the ccb which attached to sata task
    :type ccb: struct pm8001_ccb_info \*

.. _`pm8001_task_prep_ssp_tm`:

pm8001_task_prep_ssp_tm
=======================

.. c:function:: int pm8001_task_prep_ssp_tm(struct pm8001_hba_info *pm8001_ha, struct pm8001_ccb_info *ccb, struct pm8001_tmf_task *tmf)

    the dispatcher function, prepare task management data

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param ccb:
        the ccb which attached to TM
    :type ccb: struct pm8001_ccb_info \*

    :param tmf:
        the task management IU
    :type tmf: struct pm8001_tmf_task \*

.. _`pm8001_task_prep_ssp`:

pm8001_task_prep_ssp
====================

.. c:function:: int pm8001_task_prep_ssp(struct pm8001_hba_info *pm8001_ha, struct pm8001_ccb_info *ccb)

    the dispatcher function,prepare ssp data for ssp task

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param ccb:
        the ccb which attached to ssp task
    :type ccb: struct pm8001_ccb_info \*

.. _`dev_is_gone`:

DEV_IS_GONE
===========

.. c:function::  DEV_IS_GONE( pm8001_dev)

    queue the task(ssp, smp && ata) to the hardware.

    :param pm8001_dev:
        *undescribed*
    :type pm8001_dev: 

.. _`pm8001_queue_command`:

pm8001_queue_command
====================

.. c:function:: int pm8001_queue_command(struct sas_task *task, gfp_t gfp_flags)

    register for upper layer used, all IO commands sent to HBA are from this interface.

    :param task:
        the task to be execute.
    :type task: struct sas_task \*

    :param gfp_flags:
        gfp_flags
    :type gfp_flags: gfp_t

.. _`pm8001_ccb_task_free`:

pm8001_ccb_task_free
====================

.. c:function:: void pm8001_ccb_task_free(struct pm8001_hba_info *pm8001_ha, struct sas_task *task, struct pm8001_ccb_info *ccb, u32 ccb_idx)

    free the sg for ssp and smp command, free the ccb.

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param task:
        the task to be free.
    :type task: struct sas_task \*

    :param ccb:
        the ccb which attached to ssp task
    :type ccb: struct pm8001_ccb_info \*

    :param ccb_idx:
        ccb index.
    :type ccb_idx: u32

.. _`pm8001_find_dev`:

pm8001_find_dev
===============

.. c:function:: struct pm8001_device *pm8001_find_dev(struct pm8001_hba_info *pm8001_ha, u32 device_id)

    find a matching pm8001_device

    :param pm8001_ha:
        our hba card information
    :type pm8001_ha: struct pm8001_hba_info \*

    :param device_id:
        *undescribed*
    :type device_id: u32

.. _`pm8001_dev_found_notify`:

pm8001_dev_found_notify
=======================

.. c:function:: int pm8001_dev_found_notify(struct domain_device *dev)

    libsas notify a device is found.

    :param dev:
        the device structure which sas layer used.
    :type dev: struct domain_device \*

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

    :param dev:
        the wanted device.
    :type dev: struct domain_device \*

    :param parameter:
        ssp task parameter.
    :type parameter: void \*

    :param para_len:
        para_len.
    :type para_len: u32

    :param tmf:
        which task management wanted to be take.
    :type tmf: struct pm8001_tmf_task \*

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

    :param dev:
        the device structure which sas layer used.
    :type dev: struct domain_device \*

.. _`pm8001_i_t_nexus_reset`:

pm8001_I_T_nexus_reset
======================

.. c:function:: int pm8001_I_T_nexus_reset(struct domain_device *dev)

    SSP (type 1) , only for RECOVERY

    :param dev:
        *undescribed*
    :type dev: struct domain_device \*

.. This file was automatic generated / don't edit.

