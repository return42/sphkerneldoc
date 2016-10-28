.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/be2iscsi/be_cmds.c

.. _`beiscsi_pci_soft_reset`:

beiscsi_pci_soft_reset
======================

.. c:function:: int beiscsi_pci_soft_reset(struct beiscsi_hba *phba)

    2015 Emulex All rights reserved.

    :param struct beiscsi_hba \*phba:
        *undescribed*

.. _`beiscsi_pci_soft_reset.description`:

Description
-----------

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License version 2
as published by the Free Software Foundation.  The full GNU General
Public License is included in this distribution in the file called COPYING.

.. _`beiscsi_pci_soft_reset.contact-information`:

Contact Information
-------------------

linux-drivers\ ``avagotech``\ .com

Emulex
3333 Susan Street
Costa Mesa, CA 92626

.. _`beiscsi_fail_session`:

beiscsi_fail_session
====================

.. c:function:: void beiscsi_fail_session(struct iscsi_cls_session *cls_session)

    Closing session with appropriate error

    :param struct iscsi_cls_session \*cls_session:
        ptr to session

.. _`be_cmd_fw_initialize`:

be_cmd_fw_initialize
====================

.. c:function:: int be_cmd_fw_initialize(struct be_ctrl_info *ctrl)

    Initialize FW

    :param struct be_ctrl_info \*ctrl:
        Pointer to function control structure

.. _`be_cmd_fw_initialize.description`:

Description
-----------

Send FW initialize pattern for the function.

return

.. _`be_cmd_fw_initialize.success`:

Success
-------

0

.. _`be_cmd_fw_initialize.failure`:

Failure
-------

Non-Zero value

.. _`be_cmd_fw_uninit`:

be_cmd_fw_uninit
================

.. c:function:: int be_cmd_fw_uninit(struct be_ctrl_info *ctrl)

    Uinitialize FW

    :param struct be_ctrl_info \*ctrl:
        Pointer to function control structure

.. _`be_cmd_fw_uninit.description`:

Description
-----------

Send FW uninitialize pattern for the function

return

.. _`be_cmd_fw_uninit.success`:

Success
-------

0

.. _`be_cmd_fw_uninit.failure`:

Failure
-------

Non-Zero value

.. _`be_cmd_create_default_pdu_queue`:

be_cmd_create_default_pdu_queue
===============================

.. c:function:: int be_cmd_create_default_pdu_queue(struct be_ctrl_info *ctrl, struct be_queue_info *cq, struct be_queue_info *dq, int length, int entry_size, uint8_t is_header, uint8_t ulp_num)

    Create DEFQ for the adapter

    :param struct be_ctrl_info \*ctrl:
        ptr to ctrl_info

    :param struct be_queue_info \*cq:
        Completion Queue

    :param struct be_queue_info \*dq:
        Default Queue

    :param int length:
        *undescribed*

    :param int entry_size:
        size of each entry in DEFQ

    :param uint8_t is_header:
        Header or Data DEFQ

    :param uint8_t ulp_num:
        Bind to which ULP

.. _`be_cmd_create_default_pdu_queue.description`:

Description
-----------

Create HDR/Data DEFQ for the passed ULP. Unsol PDU are posted
on this queue by the FW

return

.. _`be_cmd_create_default_pdu_queue.success`:

Success
-------

0

.. _`be_cmd_create_default_pdu_queue.failure`:

Failure
-------

Non-Zero Value

.. _`be_cmd_wrbq_create`:

be_cmd_wrbq_create
==================

.. c:function:: int be_cmd_wrbq_create(struct be_ctrl_info *ctrl, struct be_dma_mem *q_mem, struct be_queue_info *wrbq, struct hwi_wrb_context *pwrb_context, uint8_t ulp_num)

    Create WRBQ

    :param struct be_ctrl_info \*ctrl:
        ptr to ctrl_info

    :param struct be_dma_mem \*q_mem:
        memory details for the queue

    :param struct be_queue_info \*wrbq:
        queue info

    :param struct hwi_wrb_context \*pwrb_context:
        ptr to wrb_context

    :param uint8_t ulp_num:
        ULP on which the WRBQ is to be created

.. _`be_cmd_wrbq_create.description`:

Description
-----------

Create WRBQ on the passed ULP_NUM.

.. _`be_cmd_set_vlan`:

be_cmd_set_vlan
===============

.. c:function:: int be_cmd_set_vlan(struct beiscsi_hba *phba, uint16_t vlan_tag)

    Configure VLAN paramters on the adapter

    :param struct beiscsi_hba \*phba:
        device priv structure instance

    :param uint16_t vlan_tag:
        TAG to be set

.. _`be_cmd_set_vlan.description`:

Description
-----------

Set the VLAN_TAG for the adapter or Disable VLAN on adapter

returns
TAG for the MBX Cmd

.. This file was automatic generated / don't edit.

