.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/be2iscsi/be_cmds.c

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

.. _`beiscsi_get_fw_config`:

beiscsi_get_fw_config
=====================

.. c:function:: int beiscsi_get_fw_config(struct be_ctrl_info *ctrl, struct beiscsi_hba *phba)

    Get the FW config for the function

    :param struct be_ctrl_info \*ctrl:
        ptr to Ctrl Info

    :param struct beiscsi_hba \*phba:
        ptr to the dev priv structure

.. _`beiscsi_get_fw_config.description`:

Description
-----------

Get the FW config and resources available for the function.
The resources are created based on the count received here.

return

.. _`beiscsi_get_fw_config.success`:

Success
-------

0

.. _`beiscsi_get_fw_config.failure`:

Failure
-------

Non-Zero Value

.. _`beiscsi_get_port_name`:

beiscsi_get_port_name
=====================

.. c:function:: int beiscsi_get_port_name(struct be_ctrl_info *ctrl, struct beiscsi_hba *phba)

    Get port name for the function

    :param struct be_ctrl_info \*ctrl:
        ptr to Ctrl Info

    :param struct beiscsi_hba \*phba:
        ptr to the dev priv structure

.. _`beiscsi_get_port_name.description`:

Description
-----------

Get the alphanumeric character for port

.. _`beiscsi_cmd_iscsi_cleanup`:

beiscsi_cmd_iscsi_cleanup
=========================

.. c:function:: int beiscsi_cmd_iscsi_cleanup(struct beiscsi_hba *phba, unsigned short ulp)

    Inform FW to cleanup EP data structures.

    :param struct beiscsi_hba \*phba:
        pointer to dev priv structure

    :param unsigned short ulp:
        ULP number.

.. _`beiscsi_cmd_iscsi_cleanup.description`:

Description
-----------

return

.. _`beiscsi_cmd_iscsi_cleanup.success`:

Success
-------

0

.. _`beiscsi_cmd_iscsi_cleanup.failure`:

Failure
-------

Non-Zero Value

.. This file was automatic generated / don't edit.

