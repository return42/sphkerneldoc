.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_virtchnl_pf.c

.. _`i40e_vc_vf_broadcast`:

i40e_vc_vf_broadcast
====================

.. c:function:: void i40e_vc_vf_broadcast(struct i40e_pf *pf, enum virtchnl_ops v_opcode, i40e_status v_retval, u8 *msg, u16 msglen)

    :param pf:
        pointer to the PF structure
    :type pf: struct i40e_pf \*

    :param v_opcode:
        operation code
    :type v_opcode: enum virtchnl_ops

    :param v_retval:
        return value
    :type v_retval: i40e_status

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

    :param msglen:
        msg length
    :type msglen: u16

.. _`i40e_vc_vf_broadcast.description`:

Description
-----------

send a message to all VFs on a given PF

.. _`i40e_vc_notify_vf_link_state`:

i40e_vc_notify_vf_link_state
============================

.. c:function:: void i40e_vc_notify_vf_link_state(struct i40e_vf *vf)

    :param vf:
        pointer to the VF structure
    :type vf: struct i40e_vf \*

.. _`i40e_vc_notify_vf_link_state.description`:

Description
-----------

send a link status message to a single VF

.. _`i40e_vc_notify_link_state`:

i40e_vc_notify_link_state
=========================

.. c:function:: void i40e_vc_notify_link_state(struct i40e_pf *pf)

    :param pf:
        pointer to the PF structure
    :type pf: struct i40e_pf \*

.. _`i40e_vc_notify_link_state.description`:

Description
-----------

send a link status message to all VFs on a given PF

.. _`i40e_vc_notify_reset`:

i40e_vc_notify_reset
====================

.. c:function:: void i40e_vc_notify_reset(struct i40e_pf *pf)

    :param pf:
        pointer to the PF structure
    :type pf: struct i40e_pf \*

.. _`i40e_vc_notify_reset.description`:

Description
-----------

indicate a pending reset to all VFs on a given PF

.. _`i40e_vc_notify_vf_reset`:

i40e_vc_notify_vf_reset
=======================

.. c:function:: void i40e_vc_notify_vf_reset(struct i40e_vf *vf)

    :param vf:
        pointer to the VF structure
    :type vf: struct i40e_vf \*

.. _`i40e_vc_notify_vf_reset.description`:

Description
-----------

indicate a pending reset to the given VF

.. _`i40e_vc_disable_vf`:

i40e_vc_disable_vf
==================

.. c:function:: void i40e_vc_disable_vf(struct i40e_vf *vf)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

.. _`i40e_vc_disable_vf.description`:

Description
-----------

Disable the VF through a SW reset.

.. _`i40e_vc_isvalid_vsi_id`:

i40e_vc_isvalid_vsi_id
======================

.. c:function:: bool i40e_vc_isvalid_vsi_id(struct i40e_vf *vf, u16 vsi_id)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param vsi_id:
        VF relative VSI id
    :type vsi_id: u16

.. _`i40e_vc_isvalid_vsi_id.description`:

Description
-----------

check for the valid VSI id

.. _`i40e_vc_isvalid_queue_id`:

i40e_vc_isvalid_queue_id
========================

.. c:function:: bool i40e_vc_isvalid_queue_id(struct i40e_vf *vf, u16 vsi_id, u8 qid)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param vsi_id:
        vsi id
    :type vsi_id: u16

    :param qid:
        vsi relative queue id
    :type qid: u8

.. _`i40e_vc_isvalid_queue_id.description`:

Description
-----------

check for the valid queue id

.. _`i40e_vc_isvalid_vector_id`:

i40e_vc_isvalid_vector_id
=========================

.. c:function:: bool i40e_vc_isvalid_vector_id(struct i40e_vf *vf, u8 vector_id)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param vector_id:
        VF relative vector id
    :type vector_id: u8

.. _`i40e_vc_isvalid_vector_id.description`:

Description
-----------

check for the valid vector id

.. _`i40e_vc_get_pf_queue_id`:

i40e_vc_get_pf_queue_id
=======================

.. c:function:: u16 i40e_vc_get_pf_queue_id(struct i40e_vf *vf, u16 vsi_id, u8 vsi_queue_id)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param vsi_id:
        id of VSI as provided by the FW
    :type vsi_id: u16

    :param vsi_queue_id:
        vsi relative queue id
    :type vsi_queue_id: u8

.. _`i40e_vc_get_pf_queue_id.description`:

Description
-----------

return PF relative queue id

.. _`i40e_get_real_pf_qid`:

i40e_get_real_pf_qid
====================

.. c:function:: u16 i40e_get_real_pf_qid(struct i40e_vf *vf, u16 vsi_id, u16 queue_id)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param vsi_id:
        vsi id
    :type vsi_id: u16

    :param queue_id:
        queue number
    :type queue_id: u16

.. _`i40e_get_real_pf_qid.description`:

Description
-----------

wrapper function to get pf_queue_id handling ADq code as well

.. _`i40e_config_irq_link_list`:

i40e_config_irq_link_list
=========================

.. c:function:: void i40e_config_irq_link_list(struct i40e_vf *vf, u16 vsi_id, struct virtchnl_vector_map *vecmap)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param vsi_id:
        id of VSI as given by the FW
    :type vsi_id: u16

    :param vecmap:
        irq map info
    :type vecmap: struct virtchnl_vector_map \*

.. _`i40e_config_irq_link_list.description`:

Description
-----------

configure irq link list from the map

.. _`i40e_release_iwarp_qvlist`:

i40e_release_iwarp_qvlist
=========================

.. c:function:: void i40e_release_iwarp_qvlist(struct i40e_vf *vf)

    :param vf:
        pointer to the VF.
    :type vf: struct i40e_vf \*

.. _`i40e_config_iwarp_qvlist`:

i40e_config_iwarp_qvlist
========================

.. c:function:: int i40e_config_iwarp_qvlist(struct i40e_vf *vf, struct virtchnl_iwarp_qvlist_info *qvlist_info)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param qvlist_info:
        queue and vector list
    :type qvlist_info: struct virtchnl_iwarp_qvlist_info \*

.. _`i40e_config_iwarp_qvlist.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`i40e_config_vsi_tx_queue`:

i40e_config_vsi_tx_queue
========================

.. c:function:: int i40e_config_vsi_tx_queue(struct i40e_vf *vf, u16 vsi_id, u16 vsi_queue_id, struct virtchnl_txq_info *info)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param vsi_id:
        id of VSI as provided by the FW
    :type vsi_id: u16

    :param vsi_queue_id:
        vsi relative queue index
    :type vsi_queue_id: u16

    :param info:
        config. info
    :type info: struct virtchnl_txq_info \*

.. _`i40e_config_vsi_tx_queue.description`:

Description
-----------

configure tx queue

.. _`i40e_config_vsi_rx_queue`:

i40e_config_vsi_rx_queue
========================

.. c:function:: int i40e_config_vsi_rx_queue(struct i40e_vf *vf, u16 vsi_id, u16 vsi_queue_id, struct virtchnl_rxq_info *info)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param vsi_id:
        id of VSI  as provided by the FW
    :type vsi_id: u16

    :param vsi_queue_id:
        vsi relative queue index
    :type vsi_queue_id: u16

    :param info:
        config. info
    :type info: struct virtchnl_rxq_info \*

.. _`i40e_config_vsi_rx_queue.description`:

Description
-----------

configure rx queue

.. _`i40e_alloc_vsi_res`:

i40e_alloc_vsi_res
==================

.. c:function:: int i40e_alloc_vsi_res(struct i40e_vf *vf, u8 idx)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param idx:
        VSI index, applies only for ADq mode, zero otherwise
    :type idx: u8

.. _`i40e_alloc_vsi_res.description`:

Description
-----------

alloc VF vsi context & resources

.. _`i40e_map_pf_queues_to_vsi`:

i40e_map_pf_queues_to_vsi
=========================

.. c:function:: void i40e_map_pf_queues_to_vsi(struct i40e_vf *vf)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

.. _`i40e_map_pf_queues_to_vsi.description`:

Description
-----------

PF maps LQPs to a VF by programming VSILAN_QTABLE & VPLAN_QTABLE. This
function takes care of first part VSILAN_QTABLE, mapping pf queues to VSI.

.. _`i40e_map_pf_to_vf_queues`:

i40e_map_pf_to_vf_queues
========================

.. c:function:: void i40e_map_pf_to_vf_queues(struct i40e_vf *vf)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

.. _`i40e_map_pf_to_vf_queues.description`:

Description
-----------

PF maps LQPs to a VF by programming VSILAN_QTABLE & VPLAN_QTABLE. This
function takes care of the second part VPLAN_QTABLE & completes VF mappings.

.. _`i40e_enable_vf_mappings`:

i40e_enable_vf_mappings
=======================

.. c:function:: void i40e_enable_vf_mappings(struct i40e_vf *vf)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

.. _`i40e_enable_vf_mappings.description`:

Description
-----------

enable VF mappings

.. _`i40e_disable_vf_mappings`:

i40e_disable_vf_mappings
========================

.. c:function:: void i40e_disable_vf_mappings(struct i40e_vf *vf)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

.. _`i40e_disable_vf_mappings.description`:

Description
-----------

disable VF mappings

.. _`i40e_free_vf_res`:

i40e_free_vf_res
================

.. c:function:: void i40e_free_vf_res(struct i40e_vf *vf)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

.. _`i40e_free_vf_res.description`:

Description
-----------

free VF resources

.. _`i40e_alloc_vf_res`:

i40e_alloc_vf_res
=================

.. c:function:: int i40e_alloc_vf_res(struct i40e_vf *vf)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

.. _`i40e_alloc_vf_res.description`:

Description
-----------

allocate VF resources

.. _`i40e_quiesce_vf_pci`:

i40e_quiesce_vf_pci
===================

.. c:function:: int i40e_quiesce_vf_pci(struct i40e_vf *vf)

    :param vf:
        pointer to the VF structure
    :type vf: struct i40e_vf \*

.. _`i40e_quiesce_vf_pci.description`:

Description
-----------

Wait for VF PCI transactions to be cleared after reset. Returns -EIO
if the transactions never clear.

.. _`i40e_config_vf_promiscuous_mode`:

i40e_config_vf_promiscuous_mode
===============================

.. c:function:: i40e_status i40e_config_vf_promiscuous_mode(struct i40e_vf *vf, u16 vsi_id, bool allmulti, bool alluni)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param vsi_id:
        VSI id
    :type vsi_id: u16

    :param allmulti:
        set MAC L2 layer multicast promiscuous enable/disable
    :type allmulti: bool

    :param alluni:
        set MAC L2 layer unicast promiscuous enable/disable
    :type alluni: bool

.. _`i40e_config_vf_promiscuous_mode.description`:

Description
-----------

Called from the VF to configure the promiscuous mode of
VF vsis and from the VF reset path to reset promiscuous mode.

.. _`i40e_trigger_vf_reset`:

i40e_trigger_vf_reset
=====================

.. c:function:: void i40e_trigger_vf_reset(struct i40e_vf *vf, bool flr)

    :param vf:
        pointer to the VF structure
    :type vf: struct i40e_vf \*

    :param flr:
        VFLR was issued or not
    :type flr: bool

.. _`i40e_trigger_vf_reset.description`:

Description
-----------

Trigger hardware to start a reset for a particular VF. Expects the caller
to wait the proper amount of time to allow hardware to reset the VF before
it cleans up and restores VF functionality.

.. _`i40e_cleanup_reset_vf`:

i40e_cleanup_reset_vf
=====================

.. c:function:: void i40e_cleanup_reset_vf(struct i40e_vf *vf)

    :param vf:
        pointer to the VF structure
    :type vf: struct i40e_vf \*

.. _`i40e_cleanup_reset_vf.description`:

Description
-----------

Cleanup a VF after the hardware reset is finished. Expects the caller to
have verified whether the reset is finished properly, and ensure the
minimum amount of wait time has passed.

.. _`i40e_reset_vf`:

i40e_reset_vf
=============

.. c:function:: bool i40e_reset_vf(struct i40e_vf *vf, bool flr)

    :param vf:
        pointer to the VF structure
    :type vf: struct i40e_vf \*

    :param flr:
        VFLR was issued or not
    :type flr: bool

.. _`i40e_reset_vf.description`:

Description
-----------

Returns true if the VF is reset, false otherwise.

.. _`i40e_reset_all_vfs`:

i40e_reset_all_vfs
==================

.. c:function:: bool i40e_reset_all_vfs(struct i40e_pf *pf, bool flr)

    :param pf:
        pointer to the PF structure
    :type pf: struct i40e_pf \*

    :param flr:
        VFLR was issued or not
    :type flr: bool

.. _`i40e_reset_all_vfs.description`:

Description
-----------

Reset all allocated VFs in one go. First, tell the hardware to reset each
VF, then do all the waiting in one chunk, and finally finish restoring each
VF after the wait. This is useful during PF routines which need to reset
all VFs, as otherwise it must perform these resets in a serialized fashion.

Returns true if any VFs were reset, and false otherwise.

.. _`i40e_free_vfs`:

i40e_free_vfs
=============

.. c:function:: void i40e_free_vfs(struct i40e_pf *pf)

    :param pf:
        pointer to the PF structure
    :type pf: struct i40e_pf \*

.. _`i40e_free_vfs.description`:

Description
-----------

free VF resources

.. _`i40e_alloc_vfs`:

i40e_alloc_vfs
==============

.. c:function:: int i40e_alloc_vfs(struct i40e_pf *pf, u16 num_alloc_vfs)

    :param pf:
        pointer to the PF structure
    :type pf: struct i40e_pf \*

    :param num_alloc_vfs:
        number of VFs to allocate
    :type num_alloc_vfs: u16

.. _`i40e_alloc_vfs.description`:

Description
-----------

allocate VF resources

.. _`i40e_pci_sriov_enable`:

i40e_pci_sriov_enable
=====================

.. c:function:: int i40e_pci_sriov_enable(struct pci_dev *pdev, int num_vfs)

    :param pdev:
        pointer to a pci_dev structure
    :type pdev: struct pci_dev \*

    :param num_vfs:
        number of VFs to allocate
    :type num_vfs: int

.. _`i40e_pci_sriov_enable.description`:

Description
-----------

Enable or change the number of VFs

.. _`i40e_pci_sriov_configure`:

i40e_pci_sriov_configure
========================

.. c:function:: int i40e_pci_sriov_configure(struct pci_dev *pdev, int num_vfs)

    :param pdev:
        pointer to a pci_dev structure
    :type pdev: struct pci_dev \*

    :param num_vfs:
        number of VFs to allocate
    :type num_vfs: int

.. _`i40e_pci_sriov_configure.description`:

Description
-----------

Enable or change the number of VFs. Called when the user updates the number
of VFs in sysfs.

.. _`i40e_vc_send_msg_to_vf`:

i40e_vc_send_msg_to_vf
======================

.. c:function:: int i40e_vc_send_msg_to_vf(struct i40e_vf *vf, u32 v_opcode, u32 v_retval, u8 *msg, u16 msglen)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param v_opcode:
        virtual channel opcode
    :type v_opcode: u32

    :param v_retval:
        virtual channel return value
    :type v_retval: u32

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

    :param msglen:
        msg length
    :type msglen: u16

.. _`i40e_vc_send_msg_to_vf.description`:

Description
-----------

send msg to VF

.. _`i40e_vc_send_resp_to_vf`:

i40e_vc_send_resp_to_vf
=======================

.. c:function:: int i40e_vc_send_resp_to_vf(struct i40e_vf *vf, enum virtchnl_ops opcode, i40e_status retval)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param opcode:
        operation code
    :type opcode: enum virtchnl_ops

    :param retval:
        return value
    :type retval: i40e_status

.. _`i40e_vc_send_resp_to_vf.description`:

Description
-----------

send resp msg to VF

.. _`i40e_vc_get_version_msg`:

i40e_vc_get_version_msg
=======================

.. c:function:: int i40e_vc_get_version_msg(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_get_version_msg.description`:

Description
-----------

called from the VF to request the API version used by the PF

.. _`i40e_del_qch`:

i40e_del_qch
============

.. c:function:: void i40e_del_qch(struct i40e_vf *vf)

    delete all the additional VSIs created as a part of ADq

    :param vf:
        pointer to VF structure
    :type vf: struct i40e_vf \*

.. _`i40e_vc_get_vf_resources_msg`:

i40e_vc_get_vf_resources_msg
============================

.. c:function:: int i40e_vc_get_vf_resources_msg(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_get_vf_resources_msg.description`:

Description
-----------

called from the VF to request its resources

.. _`i40e_vc_reset_vf_msg`:

i40e_vc_reset_vf_msg
====================

.. c:function:: void i40e_vc_reset_vf_msg(struct i40e_vf *vf)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

.. _`i40e_vc_reset_vf_msg.description`:

Description
-----------

called from the VF to reset itself,
unlike other virtchnl messages, PF driver
doesn't send the response back to the VF

.. _`i40e_getnum_vf_vsi_vlan_filters`:

i40e_getnum_vf_vsi_vlan_filters
===============================

.. c:function:: int i40e_getnum_vf_vsi_vlan_filters(struct i40e_vsi *vsi)

    :param vsi:
        pointer to the vsi
    :type vsi: struct i40e_vsi \*

.. _`i40e_getnum_vf_vsi_vlan_filters.description`:

Description
-----------

called to get the number of VLANs offloaded on this VF

.. _`i40e_vc_config_promiscuous_mode_msg`:

i40e_vc_config_promiscuous_mode_msg
===================================

.. c:function:: int i40e_vc_config_promiscuous_mode_msg(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_config_promiscuous_mode_msg.description`:

Description
-----------

called from the VF to configure the promiscuous mode of
VF vsis

.. _`i40e_vc_config_queues_msg`:

i40e_vc_config_queues_msg
=========================

.. c:function:: int i40e_vc_config_queues_msg(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_config_queues_msg.description`:

Description
-----------

called from the VF to configure the rx/tx
queues

.. _`i40e_validate_queue_map`:

i40e_validate_queue_map
=======================

.. c:function:: int i40e_validate_queue_map(struct i40e_vf *vf, u16 vsi_id, unsigned long queuemap)

    :param vf:
        *undescribed*
    :type vf: struct i40e_vf \*

    :param vsi_id:
        vsi id
    :type vsi_id: u16

    :param queuemap:
        Tx or Rx queue map
    :type queuemap: unsigned long

.. _`i40e_validate_queue_map.description`:

Description
-----------

check if Tx or Rx queue map is valid

.. _`i40e_vc_config_irq_map_msg`:

i40e_vc_config_irq_map_msg
==========================

.. c:function:: int i40e_vc_config_irq_map_msg(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_config_irq_map_msg.description`:

Description
-----------

called from the VF to configure the irq to
queue map

.. _`i40e_ctrl_vf_tx_rings`:

i40e_ctrl_vf_tx_rings
=====================

.. c:function:: int i40e_ctrl_vf_tx_rings(struct i40e_vsi *vsi, unsigned long q_map, bool enable)

    :param vsi:
        the SRIOV VSI being configured
    :type vsi: struct i40e_vsi \*

    :param q_map:
        bit map of the queues to be enabled
    :type q_map: unsigned long

    :param enable:
        start or stop the queue
    :type enable: bool

.. _`i40e_ctrl_vf_rx_rings`:

i40e_ctrl_vf_rx_rings
=====================

.. c:function:: int i40e_ctrl_vf_rx_rings(struct i40e_vsi *vsi, unsigned long q_map, bool enable)

    :param vsi:
        the SRIOV VSI being configured
    :type vsi: struct i40e_vsi \*

    :param q_map:
        bit map of the queues to be enabled
    :type q_map: unsigned long

    :param enable:
        start or stop the queue
    :type enable: bool

.. _`i40e_vc_enable_queues_msg`:

i40e_vc_enable_queues_msg
=========================

.. c:function:: int i40e_vc_enable_queues_msg(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_enable_queues_msg.description`:

Description
-----------

called from the VF to enable all or specific queue(s)

.. _`i40e_vc_disable_queues_msg`:

i40e_vc_disable_queues_msg
==========================

.. c:function:: int i40e_vc_disable_queues_msg(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_disable_queues_msg.description`:

Description
-----------

called from the VF to disable all or specific
queue(s)

.. _`i40e_vc_request_queues_msg`:

i40e_vc_request_queues_msg
==========================

.. c:function:: int i40e_vc_request_queues_msg(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_request_queues_msg.description`:

Description
-----------

VFs get a default number of queues but can use this message to request a
different number.  If the request is successful, PF will reset the VF and
return 0.  If unsuccessful, PF will send message informing VF of number of
available queues and return result of sending VF a message.

.. _`i40e_vc_get_stats_msg`:

i40e_vc_get_stats_msg
=====================

.. c:function:: int i40e_vc_get_stats_msg(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_get_stats_msg.description`:

Description
-----------

called from the VF to get vsi stats

.. _`i40e_check_vf_permission`:

i40e_check_vf_permission
========================

.. c:function:: int i40e_check_vf_permission(struct i40e_vf *vf, struct virtchnl_ether_addr_list *al)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param al:
        MAC address list from virtchnl
    :type al: struct virtchnl_ether_addr_list \*

.. _`i40e_check_vf_permission.description`:

Description
-----------

Check that the given list of MAC addresses is allowed. Will return -EPERM
if any address in the list is not valid. Checks the following conditions:

1) broadcast and zero addresses are never valid
2) unicast addresses are not allowed if the VMM has administratively set
the VF MAC address, unless the VF is marked as privileged.
3) There is enough space to add all the addresses.

Note that to guarantee consistency, it is expected this function be called
while holding the mac_filter_hash_lock, as otherwise the current number of
addresses might not be accurate.

.. _`i40e_vc_add_mac_addr_msg`:

i40e_vc_add_mac_addr_msg
========================

.. c:function:: int i40e_vc_add_mac_addr_msg(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_add_mac_addr_msg.description`:

Description
-----------

add guest mac address filter

.. _`i40e_vc_del_mac_addr_msg`:

i40e_vc_del_mac_addr_msg
========================

.. c:function:: int i40e_vc_del_mac_addr_msg(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_del_mac_addr_msg.description`:

Description
-----------

remove guest mac address filter

.. _`i40e_vc_add_vlan_msg`:

i40e_vc_add_vlan_msg
====================

.. c:function:: int i40e_vc_add_vlan_msg(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_add_vlan_msg.description`:

Description
-----------

program guest vlan id

.. _`i40e_vc_remove_vlan_msg`:

i40e_vc_remove_vlan_msg
=======================

.. c:function:: int i40e_vc_remove_vlan_msg(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_remove_vlan_msg.description`:

Description
-----------

remove programmed guest vlan id

.. _`i40e_vc_iwarp_msg`:

i40e_vc_iwarp_msg
=================

.. c:function:: int i40e_vc_iwarp_msg(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

    :param msglen:
        msg length
    :type msglen: u16

.. _`i40e_vc_iwarp_msg.description`:

Description
-----------

called from the VF for the iwarp msgs

.. _`i40e_vc_iwarp_qvmap_msg`:

i40e_vc_iwarp_qvmap_msg
=======================

.. c:function:: int i40e_vc_iwarp_qvmap_msg(struct i40e_vf *vf, u8 *msg, bool config)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

    :param config:
        config qvmap or release it
    :type config: bool

.. _`i40e_vc_iwarp_qvmap_msg.description`:

Description
-----------

called from the VF for the iwarp msgs

.. _`i40e_vc_config_rss_key`:

i40e_vc_config_rss_key
======================

.. c:function:: int i40e_vc_config_rss_key(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_config_rss_key.description`:

Description
-----------

Configure the VF's RSS key

.. _`i40e_vc_config_rss_lut`:

i40e_vc_config_rss_lut
======================

.. c:function:: int i40e_vc_config_rss_lut(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_config_rss_lut.description`:

Description
-----------

Configure the VF's RSS LUT

.. _`i40e_vc_get_rss_hena`:

i40e_vc_get_rss_hena
====================

.. c:function:: int i40e_vc_get_rss_hena(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_get_rss_hena.description`:

Description
-----------

Return the RSS HENA bits allowed by the hardware

.. _`i40e_vc_set_rss_hena`:

i40e_vc_set_rss_hena
====================

.. c:function:: int i40e_vc_set_rss_hena(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_set_rss_hena.description`:

Description
-----------

Set the RSS HENA bits for the VF

.. _`i40e_vc_enable_vlan_stripping`:

i40e_vc_enable_vlan_stripping
=============================

.. c:function:: int i40e_vc_enable_vlan_stripping(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_enable_vlan_stripping.description`:

Description
-----------

Enable vlan header stripping for the VF

.. _`i40e_vc_disable_vlan_stripping`:

i40e_vc_disable_vlan_stripping
==============================

.. c:function:: int i40e_vc_disable_vlan_stripping(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_disable_vlan_stripping.description`:

Description
-----------

Disable vlan header stripping for the VF

.. _`i40e_validate_cloud_filter`:

i40e_validate_cloud_filter
==========================

.. c:function:: int i40e_validate_cloud_filter(struct i40e_vf *vf, struct virtchnl_filter *tc_filter)

    :param vf:
        *undescribed*
    :type vf: struct i40e_vf \*

    :param tc_filter:
        *undescribed*
    :type tc_filter: struct virtchnl_filter \*

.. _`i40e_validate_cloud_filter.description`:

Description
-----------

This function validates cloud filter programmed as TC filter for ADq

.. _`i40e_find_vsi_from_seid`:

i40e_find_vsi_from_seid
=======================

.. c:function:: struct i40e_vsi *i40e_find_vsi_from_seid(struct i40e_vf *vf, u16 seid)

    searches for the vsi with the given seid

    :param vf:
        pointer to the VF info
        \ ``seid``\  - seid of the vsi it is searching for
    :type vf: struct i40e_vf \*

    :param seid:
        *undescribed*
    :type seid: u16

.. _`i40e_del_all_cloud_filters`:

i40e_del_all_cloud_filters
==========================

.. c:function:: void i40e_del_all_cloud_filters(struct i40e_vf *vf)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

.. _`i40e_del_all_cloud_filters.description`:

Description
-----------

This function deletes all cloud filters

.. _`i40e_vc_del_cloud_filter`:

i40e_vc_del_cloud_filter
========================

.. c:function:: int i40e_vc_del_cloud_filter(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_del_cloud_filter.description`:

Description
-----------

This function deletes a cloud filter programmed as TC filter for ADq

.. _`i40e_vc_add_cloud_filter`:

i40e_vc_add_cloud_filter
========================

.. c:function:: int i40e_vc_add_cloud_filter(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_add_cloud_filter.description`:

Description
-----------

This function adds a cloud filter programmed as TC filter for ADq

.. _`i40e_vc_add_qch_msg`:

i40e_vc_add_qch_msg
===================

.. c:function:: int i40e_vc_add_qch_msg(struct i40e_vf *vf, u8 *msg)

    Add queue channel and enable ADq

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_del_qch_msg`:

i40e_vc_del_qch_msg
===================

.. c:function:: int i40e_vc_del_qch_msg(struct i40e_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct i40e_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`i40e_vc_process_vf_msg`:

i40e_vc_process_vf_msg
======================

.. c:function:: int i40e_vc_process_vf_msg(struct i40e_pf *pf, s16 vf_id, u32 v_opcode, u32 __always_unused v_retval, u8 *msg, u16 msglen)

    :param pf:
        pointer to the PF structure
    :type pf: struct i40e_pf \*

    :param vf_id:
        source VF id
    :type vf_id: s16

    :param v_opcode:
        operation code
    :type v_opcode: u32

    :param v_retval:
        unused return value code
    :type v_retval: u32 __always_unused

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

    :param msglen:
        msg length
    :type msglen: u16

.. _`i40e_vc_process_vf_msg.description`:

Description
-----------

called from the common aeq/arq handler to
process request from VF

.. _`i40e_vc_process_vflr_event`:

i40e_vc_process_vflr_event
==========================

.. c:function:: int i40e_vc_process_vflr_event(struct i40e_pf *pf)

    :param pf:
        pointer to the PF structure
    :type pf: struct i40e_pf \*

.. _`i40e_vc_process_vflr_event.description`:

Description
-----------

called from the vlfr irq handler to
free up VF resources and state variables

.. _`i40e_validate_vf`:

i40e_validate_vf
================

.. c:function:: int i40e_validate_vf(struct i40e_pf *pf, int vf_id)

    :param pf:
        the physical function
    :type pf: struct i40e_pf \*

    :param vf_id:
        VF identifier
    :type vf_id: int

.. _`i40e_validate_vf.description`:

Description
-----------

Check that the VF is enabled and the VSI exists.

Returns 0 on success, negative on failure

.. _`i40e_ndo_set_vf_mac`:

i40e_ndo_set_vf_mac
===================

.. c:function:: int i40e_ndo_set_vf_mac(struct net_device *netdev, int vf_id, u8 *mac)

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param vf_id:
        VF identifier
    :type vf_id: int

    :param mac:
        mac address
    :type mac: u8 \*

.. _`i40e_ndo_set_vf_mac.description`:

Description
-----------

program VF mac address

.. _`i40e_vsi_has_vlans`:

i40e_vsi_has_vlans
==================

.. c:function:: bool i40e_vsi_has_vlans(struct i40e_vsi *vsi)

    True if VSI has configured VLANs

    :param vsi:
        pointer to the vsi
    :type vsi: struct i40e_vsi \*

.. _`i40e_vsi_has_vlans.description`:

Description
-----------

Check if a VSI has configured any VLANs. False if we have a port VLAN or if
we have no configured VLANs. Do not call while holding the
mac_filter_hash_lock.

.. _`i40e_ndo_set_vf_port_vlan`:

i40e_ndo_set_vf_port_vlan
=========================

.. c:function:: int i40e_ndo_set_vf_port_vlan(struct net_device *netdev, int vf_id, u16 vlan_id, u8 qos, __be16 vlan_proto)

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param vf_id:
        VF identifier
    :type vf_id: int

    :param vlan_id:
        mac address
    :type vlan_id: u16

    :param qos:
        priority setting
    :type qos: u8

    :param vlan_proto:
        vlan protocol
    :type vlan_proto: __be16

.. _`i40e_ndo_set_vf_port_vlan.description`:

Description
-----------

program VF vlan id and/or qos

.. _`i40e_ndo_set_vf_bw`:

i40e_ndo_set_vf_bw
==================

.. c:function:: int i40e_ndo_set_vf_bw(struct net_device *netdev, int vf_id, int min_tx_rate, int max_tx_rate)

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param vf_id:
        VF identifier
    :type vf_id: int

    :param min_tx_rate:
        Minimum Tx rate
    :type min_tx_rate: int

    :param max_tx_rate:
        Maximum Tx rate
    :type max_tx_rate: int

.. _`i40e_ndo_set_vf_bw.description`:

Description
-----------

configure VF Tx rate

.. _`i40e_ndo_get_vf_config`:

i40e_ndo_get_vf_config
======================

.. c:function:: int i40e_ndo_get_vf_config(struct net_device *netdev, int vf_id, struct ifla_vf_info *ivi)

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param vf_id:
        VF identifier
    :type vf_id: int

    :param ivi:
        VF configuration structure
    :type ivi: struct ifla_vf_info \*

.. _`i40e_ndo_get_vf_config.description`:

Description
-----------

return VF configuration

.. _`i40e_ndo_set_vf_link_state`:

i40e_ndo_set_vf_link_state
==========================

.. c:function:: int i40e_ndo_set_vf_link_state(struct net_device *netdev, int vf_id, int link)

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param vf_id:
        VF identifier
    :type vf_id: int

    :param link:
        required link state
    :type link: int

.. _`i40e_ndo_set_vf_link_state.description`:

Description
-----------

Set the link state of a specified VF, regardless of physical link state

.. _`i40e_ndo_set_vf_spoofchk`:

i40e_ndo_set_vf_spoofchk
========================

.. c:function:: int i40e_ndo_set_vf_spoofchk(struct net_device *netdev, int vf_id, bool enable)

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param vf_id:
        VF identifier
    :type vf_id: int

    :param enable:
        flag to enable or disable feature
    :type enable: bool

.. _`i40e_ndo_set_vf_spoofchk.description`:

Description
-----------

Enable or disable VF spoof checking

.. _`i40e_ndo_set_vf_trust`:

i40e_ndo_set_vf_trust
=====================

.. c:function:: int i40e_ndo_set_vf_trust(struct net_device *netdev, int vf_id, bool setting)

    :param netdev:
        network interface device structure of the pf
    :type netdev: struct net_device \*

    :param vf_id:
        VF identifier
    :type vf_id: int

    :param setting:
        trust setting
    :type setting: bool

.. _`i40e_ndo_set_vf_trust.description`:

Description
-----------

Enable or disable VF trust setting

.. This file was automatic generated / don't edit.

