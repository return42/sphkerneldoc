.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_virtchnl_pf.c

.. _`i40e_vc_vf_broadcast`:

i40e_vc_vf_broadcast
====================

.. c:function:: void i40e_vc_vf_broadcast(struct i40e_pf *pf, enum virtchnl_ops v_opcode, i40e_status v_retval, u8 *msg, u16 msglen)

    :param struct i40e_pf \*pf:
        pointer to the PF structure

    :param enum virtchnl_ops v_opcode:
        *undescribed*

    :param i40e_status v_retval:
        *undescribed*

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_vf_broadcast.description`:

Description
-----------

send a message to all VFs on a given PF

.. _`i40e_vc_notify_vf_link_state`:

i40e_vc_notify_vf_link_state
============================

.. c:function:: void i40e_vc_notify_vf_link_state(struct i40e_vf *vf)

    :param struct i40e_vf \*vf:
        pointer to the VF structure

.. _`i40e_vc_notify_vf_link_state.description`:

Description
-----------

send a link status message to a single VF

.. _`i40e_vc_notify_link_state`:

i40e_vc_notify_link_state
=========================

.. c:function:: void i40e_vc_notify_link_state(struct i40e_pf *pf)

    :param struct i40e_pf \*pf:
        pointer to the PF structure

.. _`i40e_vc_notify_link_state.description`:

Description
-----------

send a link status message to all VFs on a given PF

.. _`i40e_vc_notify_reset`:

i40e_vc_notify_reset
====================

.. c:function:: void i40e_vc_notify_reset(struct i40e_pf *pf)

    :param struct i40e_pf \*pf:
        pointer to the PF structure

.. _`i40e_vc_notify_reset.description`:

Description
-----------

indicate a pending reset to all VFs on a given PF

.. _`i40e_vc_notify_vf_reset`:

i40e_vc_notify_vf_reset
=======================

.. c:function:: void i40e_vc_notify_vf_reset(struct i40e_vf *vf)

    :param struct i40e_vf \*vf:
        pointer to the VF structure

.. _`i40e_vc_notify_vf_reset.description`:

Description
-----------

indicate a pending reset to the given VF

.. _`i40e_vc_disable_vf`:

i40e_vc_disable_vf
==================

.. c:function:: void i40e_vc_disable_vf(struct i40e_pf *pf, struct i40e_vf *vf)

    :param struct i40e_pf \*pf:
        pointer to the PF info

    :param struct i40e_vf \*vf:
        pointer to the VF info

.. _`i40e_vc_disable_vf.description`:

Description
-----------

Disable the VF through a SW reset

.. _`i40e_vc_isvalid_vsi_id`:

i40e_vc_isvalid_vsi_id
======================

.. c:function:: bool i40e_vc_isvalid_vsi_id(struct i40e_vf *vf, u16 vsi_id)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u16 vsi_id:
        VF relative VSI id

.. _`i40e_vc_isvalid_vsi_id.description`:

Description
-----------

check for the valid VSI id

.. _`i40e_vc_isvalid_queue_id`:

i40e_vc_isvalid_queue_id
========================

.. c:function:: bool i40e_vc_isvalid_queue_id(struct i40e_vf *vf, u16 vsi_id, u8 qid)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u16 vsi_id:
        vsi id

    :param u8 qid:
        vsi relative queue id

.. _`i40e_vc_isvalid_queue_id.description`:

Description
-----------

check for the valid queue id

.. _`i40e_vc_isvalid_vector_id`:

i40e_vc_isvalid_vector_id
=========================

.. c:function:: bool i40e_vc_isvalid_vector_id(struct i40e_vf *vf, u8 vector_id)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 vector_id:
        VF relative vector id

.. _`i40e_vc_isvalid_vector_id.description`:

Description
-----------

check for the valid vector id

.. _`i40e_vc_get_pf_queue_id`:

i40e_vc_get_pf_queue_id
=======================

.. c:function:: u16 i40e_vc_get_pf_queue_id(struct i40e_vf *vf, u16 vsi_id, u8 vsi_queue_id)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u16 vsi_id:
        id of VSI as provided by the FW

    :param u8 vsi_queue_id:
        vsi relative queue id

.. _`i40e_vc_get_pf_queue_id.description`:

Description
-----------

return PF relative queue id

.. _`i40e_config_irq_link_list`:

i40e_config_irq_link_list
=========================

.. c:function:: void i40e_config_irq_link_list(struct i40e_vf *vf, u16 vsi_id, struct virtchnl_vector_map *vecmap)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u16 vsi_id:
        id of VSI as given by the FW

    :param struct virtchnl_vector_map \*vecmap:
        irq map info

.. _`i40e_config_irq_link_list.description`:

Description
-----------

configure irq link list from the map

.. _`i40e_release_iwarp_qvlist`:

i40e_release_iwarp_qvlist
=========================

.. c:function:: void i40e_release_iwarp_qvlist(struct i40e_vf *vf)

    :param struct i40e_vf \*vf:
        pointer to the VF.

.. _`i40e_config_iwarp_qvlist`:

i40e_config_iwarp_qvlist
========================

.. c:function:: int i40e_config_iwarp_qvlist(struct i40e_vf *vf, struct virtchnl_iwarp_qvlist_info *qvlist_info)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param struct virtchnl_iwarp_qvlist_info \*qvlist_info:
        queue and vector list

.. _`i40e_config_iwarp_qvlist.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`i40e_config_vsi_tx_queue`:

i40e_config_vsi_tx_queue
========================

.. c:function:: int i40e_config_vsi_tx_queue(struct i40e_vf *vf, u16 vsi_id, u16 vsi_queue_id, struct virtchnl_txq_info *info)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u16 vsi_id:
        id of VSI as provided by the FW

    :param u16 vsi_queue_id:
        vsi relative queue index

    :param struct virtchnl_txq_info \*info:
        config. info

.. _`i40e_config_vsi_tx_queue.description`:

Description
-----------

configure tx queue

.. _`i40e_config_vsi_rx_queue`:

i40e_config_vsi_rx_queue
========================

.. c:function:: int i40e_config_vsi_rx_queue(struct i40e_vf *vf, u16 vsi_id, u16 vsi_queue_id, struct virtchnl_rxq_info *info)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u16 vsi_id:
        id of VSI  as provided by the FW

    :param u16 vsi_queue_id:
        vsi relative queue index

    :param struct virtchnl_rxq_info \*info:
        config. info

.. _`i40e_config_vsi_rx_queue.description`:

Description
-----------

configure rx queue

.. _`i40e_alloc_vsi_res`:

i40e_alloc_vsi_res
==================

.. c:function:: int i40e_alloc_vsi_res(struct i40e_vf *vf, enum i40e_vsi_type type)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param enum i40e_vsi_type type:
        type of VSI to allocate

.. _`i40e_alloc_vsi_res.description`:

Description
-----------

alloc VF vsi context & resources

.. _`i40e_enable_vf_mappings`:

i40e_enable_vf_mappings
=======================

.. c:function:: void i40e_enable_vf_mappings(struct i40e_vf *vf)

    :param struct i40e_vf \*vf:
        pointer to the VF info

.. _`i40e_enable_vf_mappings.description`:

Description
-----------

enable VF mappings

.. _`i40e_disable_vf_mappings`:

i40e_disable_vf_mappings
========================

.. c:function:: void i40e_disable_vf_mappings(struct i40e_vf *vf)

    :param struct i40e_vf \*vf:
        pointer to the VF info

.. _`i40e_disable_vf_mappings.description`:

Description
-----------

disable VF mappings

.. _`i40e_free_vf_res`:

i40e_free_vf_res
================

.. c:function:: void i40e_free_vf_res(struct i40e_vf *vf)

    :param struct i40e_vf \*vf:
        pointer to the VF info

.. _`i40e_free_vf_res.description`:

Description
-----------

free VF resources

.. _`i40e_alloc_vf_res`:

i40e_alloc_vf_res
=================

.. c:function:: int i40e_alloc_vf_res(struct i40e_vf *vf)

    :param struct i40e_vf \*vf:
        pointer to the VF info

.. _`i40e_alloc_vf_res.description`:

Description
-----------

allocate VF resources

.. _`i40e_quiesce_vf_pci`:

i40e_quiesce_vf_pci
===================

.. c:function:: int i40e_quiesce_vf_pci(struct i40e_vf *vf)

    :param struct i40e_vf \*vf:
        pointer to the VF structure

.. _`i40e_quiesce_vf_pci.description`:

Description
-----------

Wait for VF PCI transactions to be cleared after reset. Returns -EIO
if the transactions never clear.

.. _`i40e_trigger_vf_reset`:

i40e_trigger_vf_reset
=====================

.. c:function:: void i40e_trigger_vf_reset(struct i40e_vf *vf, bool flr)

    :param struct i40e_vf \*vf:
        pointer to the VF structure

    :param bool flr:
        VFLR was issued or not

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

    :param struct i40e_vf \*vf:
        pointer to the VF structure

.. _`i40e_cleanup_reset_vf.description`:

Description
-----------

Cleanup a VF after the hardware reset is finished. Expects the caller to
have verified whether the reset is finished properly, and ensure the
minimum amount of wait time has passed.

.. _`i40e_reset_vf`:

i40e_reset_vf
=============

.. c:function:: void i40e_reset_vf(struct i40e_vf *vf, bool flr)

    :param struct i40e_vf \*vf:
        pointer to the VF structure

    :param bool flr:
        VFLR was issued or not

.. _`i40e_reset_vf.description`:

Description
-----------

reset the VF

.. _`i40e_reset_all_vfs`:

i40e_reset_all_vfs
==================

.. c:function:: void i40e_reset_all_vfs(struct i40e_pf *pf, bool flr)

    :param struct i40e_pf \*pf:
        pointer to the PF structure

    :param bool flr:
        VFLR was issued or not

.. _`i40e_reset_all_vfs.description`:

Description
-----------

Reset all allocated VFs in one go. First, tell the hardware to reset each
VF, then do all the waiting in one chunk, and finally finish restoring each
VF after the wait. This is useful during PF routines which need to reset
all VFs, as otherwise it must perform these resets in a serialized fashion.

.. _`i40e_free_vfs`:

i40e_free_vfs
=============

.. c:function:: void i40e_free_vfs(struct i40e_pf *pf)

    :param struct i40e_pf \*pf:
        pointer to the PF structure

.. _`i40e_free_vfs.description`:

Description
-----------

free VF resources

.. _`i40e_alloc_vfs`:

i40e_alloc_vfs
==============

.. c:function:: int i40e_alloc_vfs(struct i40e_pf *pf, u16 num_alloc_vfs)

    :param struct i40e_pf \*pf:
        pointer to the PF structure

    :param u16 num_alloc_vfs:
        number of VFs to allocate

.. _`i40e_alloc_vfs.description`:

Description
-----------

allocate VF resources

.. _`i40e_pci_sriov_enable`:

i40e_pci_sriov_enable
=====================

.. c:function:: int i40e_pci_sriov_enable(struct pci_dev *pdev, int num_vfs)

    :param struct pci_dev \*pdev:
        pointer to a pci_dev structure

    :param int num_vfs:
        number of VFs to allocate

.. _`i40e_pci_sriov_enable.description`:

Description
-----------

Enable or change the number of VFs

.. _`i40e_pci_sriov_configure`:

i40e_pci_sriov_configure
========================

.. c:function:: int i40e_pci_sriov_configure(struct pci_dev *pdev, int num_vfs)

    :param struct pci_dev \*pdev:
        pointer to a pci_dev structure

    :param int num_vfs:
        number of VFs to allocate

.. _`i40e_pci_sriov_configure.description`:

Description
-----------

Enable or change the number of VFs. Called when the user updates the number
of VFs in sysfs.

.. _`i40e_vc_send_msg_to_vf`:

i40e_vc_send_msg_to_vf
======================

.. c:function:: int i40e_vc_send_msg_to_vf(struct i40e_vf *vf, u32 v_opcode, u32 v_retval, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u32 v_opcode:
        virtual channel opcode

    :param u32 v_retval:
        virtual channel return value

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_send_msg_to_vf.description`:

Description
-----------

send msg to VF

.. _`i40e_vc_send_resp_to_vf`:

i40e_vc_send_resp_to_vf
=======================

.. c:function:: int i40e_vc_send_resp_to_vf(struct i40e_vf *vf, enum virtchnl_ops opcode, i40e_status retval)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param enum virtchnl_ops opcode:
        operation code

    :param i40e_status retval:
        return value

.. _`i40e_vc_send_resp_to_vf.description`:

Description
-----------

send resp msg to VF

.. _`i40e_vc_get_version_msg`:

i40e_vc_get_version_msg
=======================

.. c:function:: int i40e_vc_get_version_msg(struct i40e_vf *vf, u8 *msg)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        *undescribed*

.. _`i40e_vc_get_version_msg.description`:

Description
-----------

called from the VF to request the API version used by the PF

.. _`i40e_vc_get_vf_resources_msg`:

i40e_vc_get_vf_resources_msg
============================

.. c:function:: int i40e_vc_get_vf_resources_msg(struct i40e_vf *vf, u8 *msg)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

.. _`i40e_vc_get_vf_resources_msg.description`:

Description
-----------

called from the VF to request its resources

.. _`i40e_vc_reset_vf_msg`:

i40e_vc_reset_vf_msg
====================

.. c:function:: void i40e_vc_reset_vf_msg(struct i40e_vf *vf)

    :param struct i40e_vf \*vf:
        pointer to the VF info

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

    :param struct i40e_vsi \*vsi:
        pointer to the vsi

.. _`i40e_getnum_vf_vsi_vlan_filters.description`:

Description
-----------

called to get the number of VLANs offloaded on this VF

.. _`i40e_vc_config_promiscuous_mode_msg`:

i40e_vc_config_promiscuous_mode_msg
===================================

.. c:function:: int i40e_vc_config_promiscuous_mode_msg(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_config_promiscuous_mode_msg.description`:

Description
-----------

called from the VF to configure the promiscuous mode of
VF vsis

.. _`i40e_vc_config_queues_msg`:

i40e_vc_config_queues_msg
=========================

.. c:function:: int i40e_vc_config_queues_msg(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_config_queues_msg.description`:

Description
-----------

called from the VF to configure the rx/tx
queues

.. _`i40e_vc_config_irq_map_msg`:

i40e_vc_config_irq_map_msg
==========================

.. c:function:: int i40e_vc_config_irq_map_msg(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_config_irq_map_msg.description`:

Description
-----------

called from the VF to configure the irq to
queue map

.. _`i40e_vc_enable_queues_msg`:

i40e_vc_enable_queues_msg
=========================

.. c:function:: int i40e_vc_enable_queues_msg(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_enable_queues_msg.description`:

Description
-----------

called from the VF to enable all or specific queue(s)

.. _`i40e_vc_disable_queues_msg`:

i40e_vc_disable_queues_msg
==========================

.. c:function:: int i40e_vc_disable_queues_msg(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_disable_queues_msg.description`:

Description
-----------

called from the VF to disable all or specific
queue(s)

.. _`i40e_vc_get_stats_msg`:

i40e_vc_get_stats_msg
=====================

.. c:function:: int i40e_vc_get_stats_msg(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_get_stats_msg.description`:

Description
-----------

called from the VF to get vsi stats

.. _`i40e_check_vf_permission`:

i40e_check_vf_permission
========================

.. c:function:: int i40e_check_vf_permission(struct i40e_vf *vf, u8 *macaddr)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*macaddr:
        pointer to the MAC Address being checked

.. _`i40e_check_vf_permission.description`:

Description
-----------

Check if the VF has permission to add or delete unicast MAC address
filters and return error code -EPERM if not.  Then check if the
address filter requested is broadcast or zero and if so return
an invalid MAC address error code.

.. _`i40e_vc_add_mac_addr_msg`:

i40e_vc_add_mac_addr_msg
========================

.. c:function:: int i40e_vc_add_mac_addr_msg(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_add_mac_addr_msg.description`:

Description
-----------

add guest mac address filter

.. _`i40e_vc_del_mac_addr_msg`:

i40e_vc_del_mac_addr_msg
========================

.. c:function:: int i40e_vc_del_mac_addr_msg(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_del_mac_addr_msg.description`:

Description
-----------

remove guest mac address filter

.. _`i40e_vc_add_vlan_msg`:

i40e_vc_add_vlan_msg
====================

.. c:function:: int i40e_vc_add_vlan_msg(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_add_vlan_msg.description`:

Description
-----------

program guest vlan id

.. _`i40e_vc_remove_vlan_msg`:

i40e_vc_remove_vlan_msg
=======================

.. c:function:: int i40e_vc_remove_vlan_msg(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_remove_vlan_msg.description`:

Description
-----------

remove programmed guest vlan id

.. _`i40e_vc_iwarp_msg`:

i40e_vc_iwarp_msg
=================

.. c:function:: int i40e_vc_iwarp_msg(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_iwarp_msg.description`:

Description
-----------

called from the VF for the iwarp msgs

.. _`i40e_vc_iwarp_qvmap_msg`:

i40e_vc_iwarp_qvmap_msg
=======================

.. c:function:: int i40e_vc_iwarp_qvmap_msg(struct i40e_vf *vf, u8 *msg, u16 msglen, bool config)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

    :param bool config:
        config qvmap or release it

.. _`i40e_vc_iwarp_qvmap_msg.description`:

Description
-----------

called from the VF for the iwarp msgs

.. _`i40e_vc_config_rss_key`:

i40e_vc_config_rss_key
======================

.. c:function:: int i40e_vc_config_rss_key(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_config_rss_key.description`:

Description
-----------

Configure the VF's RSS key

.. _`i40e_vc_config_rss_lut`:

i40e_vc_config_rss_lut
======================

.. c:function:: int i40e_vc_config_rss_lut(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_config_rss_lut.description`:

Description
-----------

Configure the VF's RSS LUT

.. _`i40e_vc_get_rss_hena`:

i40e_vc_get_rss_hena
====================

.. c:function:: int i40e_vc_get_rss_hena(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_get_rss_hena.description`:

Description
-----------

Return the RSS HENA bits allowed by the hardware

.. _`i40e_vc_set_rss_hena`:

i40e_vc_set_rss_hena
====================

.. c:function:: int i40e_vc_set_rss_hena(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_set_rss_hena.description`:

Description
-----------

Set the RSS HENA bits for the VF

.. _`i40e_vc_enable_vlan_stripping`:

i40e_vc_enable_vlan_stripping
=============================

.. c:function:: int i40e_vc_enable_vlan_stripping(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_enable_vlan_stripping.description`:

Description
-----------

Enable vlan header stripping for the VF

.. _`i40e_vc_disable_vlan_stripping`:

i40e_vc_disable_vlan_stripping
==============================

.. c:function:: int i40e_vc_disable_vlan_stripping(struct i40e_vf *vf, u8 *msg, u16 msglen)

    :param struct i40e_vf \*vf:
        pointer to the VF info

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_disable_vlan_stripping.description`:

Description
-----------

Disable vlan header stripping for the VF

.. _`i40e_vc_process_vf_msg`:

i40e_vc_process_vf_msg
======================

.. c:function:: int i40e_vc_process_vf_msg(struct i40e_pf *pf, s16 vf_id, u32 v_opcode, u32 v_retval, u8 *msg, u16 msglen)

    :param struct i40e_pf \*pf:
        pointer to the PF structure

    :param s16 vf_id:
        source VF id

    :param u32 v_opcode:
        *undescribed*

    :param u32 v_retval:
        *undescribed*

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

.. _`i40e_vc_process_vf_msg.description`:

Description
-----------

called from the common aeq/arq handler to
process request from VF

.. _`i40e_vc_process_vflr_event`:

i40e_vc_process_vflr_event
==========================

.. c:function:: int i40e_vc_process_vflr_event(struct i40e_pf *pf)

    :param struct i40e_pf \*pf:
        pointer to the PF structure

.. _`i40e_vc_process_vflr_event.description`:

Description
-----------

called from the vlfr irq handler to
free up VF resources and state variables

.. _`i40e_ndo_set_vf_mac`:

i40e_ndo_set_vf_mac
===================

.. c:function:: int i40e_ndo_set_vf_mac(struct net_device *netdev, int vf_id, u8 *mac)

    :param struct net_device \*netdev:
        network interface device structure

    :param int vf_id:
        VF identifier

    :param u8 \*mac:
        mac address

.. _`i40e_ndo_set_vf_mac.description`:

Description
-----------

program VF mac address

.. _`i40e_ndo_set_vf_port_vlan`:

i40e_ndo_set_vf_port_vlan
=========================

.. c:function:: int i40e_ndo_set_vf_port_vlan(struct net_device *netdev, int vf_id, u16 vlan_id, u8 qos, __be16 vlan_proto)

    :param struct net_device \*netdev:
        network interface device structure

    :param int vf_id:
        VF identifier

    :param u16 vlan_id:
        mac address

    :param u8 qos:
        priority setting

    :param __be16 vlan_proto:
        vlan protocol

.. _`i40e_ndo_set_vf_port_vlan.description`:

Description
-----------

program VF vlan id and/or qos

.. _`i40e_ndo_set_vf_bw`:

i40e_ndo_set_vf_bw
==================

.. c:function:: int i40e_ndo_set_vf_bw(struct net_device *netdev, int vf_id, int min_tx_rate, int max_tx_rate)

    :param struct net_device \*netdev:
        network interface device structure

    :param int vf_id:
        VF identifier

    :param int min_tx_rate:
        *undescribed*

    :param int max_tx_rate:
        *undescribed*

.. _`i40e_ndo_set_vf_bw.description`:

Description
-----------

configure VF Tx rate

.. _`i40e_ndo_get_vf_config`:

i40e_ndo_get_vf_config
======================

.. c:function:: int i40e_ndo_get_vf_config(struct net_device *netdev, int vf_id, struct ifla_vf_info *ivi)

    :param struct net_device \*netdev:
        network interface device structure

    :param int vf_id:
        VF identifier

    :param struct ifla_vf_info \*ivi:
        VF configuration structure

.. _`i40e_ndo_get_vf_config.description`:

Description
-----------

return VF configuration

.. _`i40e_ndo_set_vf_link_state`:

i40e_ndo_set_vf_link_state
==========================

.. c:function:: int i40e_ndo_set_vf_link_state(struct net_device *netdev, int vf_id, int link)

    :param struct net_device \*netdev:
        network interface device structure

    :param int vf_id:
        VF identifier

    :param int link:
        required link state

.. _`i40e_ndo_set_vf_link_state.description`:

Description
-----------

Set the link state of a specified VF, regardless of physical link state

.. _`i40e_ndo_set_vf_spoofchk`:

i40e_ndo_set_vf_spoofchk
========================

.. c:function:: int i40e_ndo_set_vf_spoofchk(struct net_device *netdev, int vf_id, bool enable)

    :param struct net_device \*netdev:
        network interface device structure

    :param int vf_id:
        VF identifier

    :param bool enable:
        flag to enable or disable feature

.. _`i40e_ndo_set_vf_spoofchk.description`:

Description
-----------

Enable or disable VF spoof checking

.. _`i40e_ndo_set_vf_trust`:

i40e_ndo_set_vf_trust
=====================

.. c:function:: int i40e_ndo_set_vf_trust(struct net_device *netdev, int vf_id, bool setting)

    :param struct net_device \*netdev:
        network interface device structure of the pf

    :param int vf_id:
        VF identifier

    :param bool setting:
        trust setting

.. _`i40e_ndo_set_vf_trust.description`:

Description
-----------

Enable or disable VF trust setting

.. This file was automatic generated / don't edit.

