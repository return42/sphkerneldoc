.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_virtchnl_pf.c

.. _`ice_vc_vf_broadcast`:

ice_vc_vf_broadcast
===================

.. c:function:: void ice_vc_vf_broadcast(struct ice_pf *pf, enum virtchnl_ops v_opcode, enum ice_status v_retval, u8 *msg, u16 msglen)

    Broadcast a message to all VFs on PF

    :param pf:
        pointer to the PF structure
    :type pf: struct ice_pf \*

    :param v_opcode:
        operation code
    :type v_opcode: enum virtchnl_ops

    :param v_retval:
        return value
    :type v_retval: enum ice_status

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

    :param msglen:
        msg length
    :type msglen: u16

.. _`ice_set_pfe_link`:

ice_set_pfe_link
================

.. c:function:: void ice_set_pfe_link(struct ice_vf *vf, struct virtchnl_pf_event *pfe, int ice_link_speed, bool link_up)

    Set the link speed/status of the virtchnl_pf_event

    :param vf:
        pointer to the VF structure
    :type vf: struct ice_vf \*

    :param pfe:
        pointer to the virtchnl_pf_event to set link speed/status for
    :type pfe: struct virtchnl_pf_event \*

    :param ice_link_speed:
        link speed specified by ICE_AQ_LINK_SPEED\_\*
    :type ice_link_speed: int

    :param link_up:
        whether or not to set the link up/down
    :type link_up: bool

.. _`ice_set_pfe_link_forced`:

ice_set_pfe_link_forced
=======================

.. c:function:: void ice_set_pfe_link_forced(struct ice_vf *vf, struct virtchnl_pf_event *pfe, bool link_up)

    Force the virtchnl_pf_event link speed/status

    :param vf:
        pointer to the VF structure
    :type vf: struct ice_vf \*

    :param pfe:
        pointer to the virtchnl_pf_event to set link speed/status for
    :type pfe: struct virtchnl_pf_event \*

    :param link_up:
        whether or not to set the link up/down
    :type link_up: bool

.. _`ice_vc_notify_vf_link_state`:

ice_vc_notify_vf_link_state
===========================

.. c:function:: void ice_vc_notify_vf_link_state(struct ice_vf *vf)

    Inform a VF of link status

    :param vf:
        pointer to the VF structure
    :type vf: struct ice_vf \*

.. _`ice_vc_notify_vf_link_state.description`:

Description
-----------

send a link status message to a single VF

.. _`ice_get_vf_vector`:

ice_get_vf_vector
=================

.. c:function:: u32 ice_get_vf_vector(int vf_msix, int vf_id, int i)

    get VF interrupt vector register offset

    :param vf_msix:
        number of MSIx vector per VF on a PF
    :type vf_msix: int

    :param vf_id:
        VF identifier
    :type vf_id: int

    :param i:
        index of MSIx vector
    :type i: int

.. _`ice_free_vf_res`:

ice_free_vf_res
===============

.. c:function:: void ice_free_vf_res(struct ice_vf *vf)

    Free a VF's resources

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

.. _`ice_dis_vf_mappings`:

ice_dis_vf_mappings
===================

.. c:function:: void ice_dis_vf_mappings(struct ice_vf *vf)

    :param vf:
        pointer to the VF structure
    :type vf: struct ice_vf \*

.. _`ice_free_vfs`:

ice_free_vfs
============

.. c:function:: void ice_free_vfs(struct ice_pf *pf)

    Free all VFs

    :param pf:
        pointer to the PF structure
    :type pf: struct ice_pf \*

.. _`ice_trigger_vf_reset`:

ice_trigger_vf_reset
====================

.. c:function:: void ice_trigger_vf_reset(struct ice_vf *vf, bool is_vflr)

    Reset a VF on HW

    :param vf:
        pointer to the VF structure
    :type vf: struct ice_vf \*

    :param is_vflr:
        true if VFLR was issued, false if not
    :type is_vflr: bool

.. _`ice_trigger_vf_reset.description`:

Description
-----------

Trigger hardware to start a reset for a particular VF. Expects the caller
to wait the proper amount of time to allow hardware to reset the VF before
it cleans up and restores VF functionality.

.. _`ice_vsi_set_pvid`:

ice_vsi_set_pvid
================

.. c:function:: int ice_vsi_set_pvid(struct ice_vsi *vsi, u16 vid)

    Set port VLAN id for the VSI

    :param vsi:
        the VSI being changed
    :type vsi: struct ice_vsi \*

    :param vid:
        the VLAN id to set as a PVID
    :type vid: u16

.. _`ice_vsi_kill_pvid`:

ice_vsi_kill_pvid
=================

.. c:function:: int ice_vsi_kill_pvid(struct ice_vsi *vsi)

    Remove port VLAN id from the VSI

    :param vsi:
        the VSI being changed
    :type vsi: struct ice_vsi \*

.. _`ice_vf_vsi_setup`:

ice_vf_vsi_setup
================

.. c:function:: struct ice_vsi *ice_vf_vsi_setup(struct ice_pf *pf, struct ice_port_info *pi, u16 vf_id)

    Set up a VF VSI

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

    :param pi:
        pointer to the port_info instance
    :type pi: struct ice_port_info \*

    :param vf_id:
        defines VF id to which this VSI connects.
    :type vf_id: u16

.. _`ice_vf_vsi_setup.description`:

Description
-----------

Returns pointer to the successfully allocated VSI struct on success,
otherwise returns NULL on failure.

.. _`ice_alloc_vsi_res`:

ice_alloc_vsi_res
=================

.. c:function:: int ice_alloc_vsi_res(struct ice_vf *vf)

    Setup VF VSI and its resources

    :param vf:
        pointer to the VF structure
    :type vf: struct ice_vf \*

.. _`ice_alloc_vsi_res.description`:

Description
-----------

Returns 0 on success, negative value on failure

.. _`ice_alloc_vf_res`:

ice_alloc_vf_res
================

.. c:function:: int ice_alloc_vf_res(struct ice_vf *vf)

    Allocate VF resources

    :param vf:
        pointer to the VF structure
    :type vf: struct ice_vf \*

.. _`ice_ena_vf_mappings`:

ice_ena_vf_mappings
===================

.. c:function:: void ice_ena_vf_mappings(struct ice_vf *vf)

    :param vf:
        pointer to the VF structure
    :type vf: struct ice_vf \*

.. _`ice_ena_vf_mappings.description`:

Description
-----------

Enable VF vectors and queues allocation by writing the details into
respective registers.

.. _`ice_determine_res`:

ice_determine_res
=================

.. c:function:: int ice_determine_res(struct ice_pf *pf, u16 avail_res, u16 max_res, u16 min_res)

    :param pf:
        pointer to the PF structure
    :type pf: struct ice_pf \*

    :param avail_res:
        available resources in the PF structure
    :type avail_res: u16

    :param max_res:
        maximum resources that can be given per VF
    :type max_res: u16

    :param min_res:
        minimum resources that can be given per VF
    :type min_res: u16

.. _`ice_determine_res.description`:

Description
-----------

Returns non-zero value if resources (queues/vectors) are available or
returns zero if PF cannot accommodate for all num_alloc_vfs.

.. _`ice_check_avail_res`:

ice_check_avail_res
===================

.. c:function:: int ice_check_avail_res(struct ice_pf *pf)

    check if vectors and queues are available

    :param pf:
        pointer to the PF structure
    :type pf: struct ice_pf \*

.. _`ice_check_avail_res.description`:

Description
-----------

This function is where we calculate actual number of resources for VF VSIs,
we don't reserve ahead of time during probe. Returns success if vectors and
queues resources are available, otherwise returns error code

.. _`ice_cleanup_and_realloc_vf`:

ice_cleanup_and_realloc_vf
==========================

.. c:function:: void ice_cleanup_and_realloc_vf(struct ice_vf *vf)

    Clean up VF and reallocate resources after reset

    :param vf:
        pointer to the VF structure
    :type vf: struct ice_vf \*

.. _`ice_cleanup_and_realloc_vf.description`:

Description
-----------

Cleanup a VF after the hardware reset is finished. Expects the caller to
have verified whether the reset is finished properly, and ensure the
minimum amount of wait time has passed. Reallocate VF resources back to make
VF state active

.. _`ice_reset_all_vfs`:

ice_reset_all_vfs
=================

.. c:function:: bool ice_reset_all_vfs(struct ice_pf *pf, bool is_vflr)

    reset all allocated VFs in one go

    :param pf:
        pointer to the PF structure
    :type pf: struct ice_pf \*

    :param is_vflr:
        true if VFLR was issued, false if not
    :type is_vflr: bool

.. _`ice_reset_all_vfs.description`:

Description
-----------

First, tell the hardware to reset each VF, then do all the waiting in one
chunk, and finally finish restoring each VF after the wait. This is useful
during PF routines which need to reset all VFs, as otherwise it must perform
these resets in a serialized fashion.

Returns true if any VFs were reset, and false otherwise.

.. _`ice_reset_vf`:

ice_reset_vf
============

.. c:function:: bool ice_reset_vf(struct ice_vf *vf, bool is_vflr)

    Reset a particular VF

    :param vf:
        pointer to the VF structure
    :type vf: struct ice_vf \*

    :param is_vflr:
        true if VFLR was issued, false if not
    :type is_vflr: bool

.. _`ice_reset_vf.description`:

Description
-----------

Returns true if the VF is reset, false otherwise.

.. _`ice_vc_notify_link_state`:

ice_vc_notify_link_state
========================

.. c:function:: void ice_vc_notify_link_state(struct ice_pf *pf)

    Inform all VFs on a PF of link status

    :param pf:
        pointer to the PF structure
    :type pf: struct ice_pf \*

.. _`ice_vc_notify_reset`:

ice_vc_notify_reset
===================

.. c:function:: void ice_vc_notify_reset(struct ice_pf *pf)

    Send pending reset message to all VFs

    :param pf:
        pointer to the PF structure
    :type pf: struct ice_pf \*

.. _`ice_vc_notify_reset.description`:

Description
-----------

indicate a pending reset to all VFs on a given PF

.. _`ice_vc_notify_vf_reset`:

ice_vc_notify_vf_reset
======================

.. c:function:: void ice_vc_notify_vf_reset(struct ice_vf *vf)

    Notify VF of a reset event

    :param vf:
        pointer to the VF structure
    :type vf: struct ice_vf \*

.. _`ice_alloc_vfs`:

ice_alloc_vfs
=============

.. c:function:: int ice_alloc_vfs(struct ice_pf *pf, u16 num_alloc_vfs)

    Allocate and set up VFs resources

    :param pf:
        pointer to the PF structure
    :type pf: struct ice_pf \*

    :param num_alloc_vfs:
        number of VFs to allocate
    :type num_alloc_vfs: u16

.. _`ice_pf_state_is_nominal`:

ice_pf_state_is_nominal
=======================

.. c:function:: bool ice_pf_state_is_nominal(struct ice_pf *pf)

    checks the pf for nominal state

    :param pf:
        pointer to pf to check
    :type pf: struct ice_pf \*

.. _`ice_pf_state_is_nominal.description`:

Description
-----------

Check the PF's state for a collection of bits that would indicate
the PF is in a state that would inhibit normal operation for
driver functionality.

Returns true if PF is in a nominal state.
Returns false otherwise

.. _`ice_pci_sriov_ena`:

ice_pci_sriov_ena
=================

.. c:function:: int ice_pci_sriov_ena(struct ice_pf *pf, int num_vfs)

    Enable or change number of VFs

    :param pf:
        pointer to the PF structure
    :type pf: struct ice_pf \*

    :param num_vfs:
        number of VFs to allocate
    :type num_vfs: int

.. _`ice_sriov_configure`:

ice_sriov_configure
===================

.. c:function:: int ice_sriov_configure(struct pci_dev *pdev, int num_vfs)

    Enable or change number of VFs via sysfs

    :param pdev:
        pointer to a pci_dev structure
    :type pdev: struct pci_dev \*

    :param num_vfs:
        number of VFs to allocate
    :type num_vfs: int

.. _`ice_sriov_configure.description`:

Description
-----------

This function is called when the user updates the number of VFs in sysfs.

.. _`ice_process_vflr_event`:

ice_process_vflr_event
======================

.. c:function:: void ice_process_vflr_event(struct ice_pf *pf)

    Free VF resources via IRQ calls

    :param pf:
        pointer to the PF structure
    :type pf: struct ice_pf \*

.. _`ice_process_vflr_event.description`:

Description
-----------

called from the VLFR IRQ handler to
free up VF resources and state variables

.. _`ice_vc_dis_vf`:

ice_vc_dis_vf
=============

.. c:function:: void ice_vc_dis_vf(struct ice_vf *vf)

    Disable a given VF via SW reset

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

.. _`ice_vc_dis_vf.description`:

Description
-----------

Disable the VF through a SW reset

.. _`ice_vc_send_msg_to_vf`:

ice_vc_send_msg_to_vf
=====================

.. c:function:: int ice_vc_send_msg_to_vf(struct ice_vf *vf, u32 v_opcode, enum ice_status v_retval, u8 *msg, u16 msglen)

    Send message to VF

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param v_opcode:
        virtual channel opcode
    :type v_opcode: u32

    :param v_retval:
        virtual channel return value
    :type v_retval: enum ice_status

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

    :param msglen:
        msg length
    :type msglen: u16

.. _`ice_vc_send_msg_to_vf.description`:

Description
-----------

send msg to VF

.. _`ice_vc_get_ver_msg`:

ice_vc_get_ver_msg
==================

.. c:function:: int ice_vc_get_ver_msg(struct ice_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`ice_vc_get_ver_msg.description`:

Description
-----------

called from the VF to request the API version used by the PF

.. _`ice_vc_get_vf_res_msg`:

ice_vc_get_vf_res_msg
=====================

.. c:function:: int ice_vc_get_vf_res_msg(struct ice_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`ice_vc_get_vf_res_msg.description`:

Description
-----------

called from the VF to request its resources

.. _`ice_vc_reset_vf_msg`:

ice_vc_reset_vf_msg
===================

.. c:function:: void ice_vc_reset_vf_msg(struct ice_vf *vf)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

.. _`ice_vc_reset_vf_msg.description`:

Description
-----------

called from the VF to reset itself,
unlike other virtchnl messages, PF driver
doesn't send the response back to the VF

.. _`ice_find_vsi_from_id`:

ice_find_vsi_from_id
====================

.. c:function:: struct ice_vsi *ice_find_vsi_from_id(struct ice_pf *pf, u16 id)

    :param pf:
        the pf structure to search for the VSI
    :type pf: struct ice_pf \*

    :param id:
        id of the VSI it is searching for
    :type id: u16

.. _`ice_find_vsi_from_id.description`:

Description
-----------

searches for the VSI with the given id

.. _`ice_vc_isvalid_vsi_id`:

ice_vc_isvalid_vsi_id
=====================

.. c:function:: bool ice_vc_isvalid_vsi_id(struct ice_vf *vf, u16 vsi_id)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param vsi_id:
        VF relative VSI id
    :type vsi_id: u16

.. _`ice_vc_isvalid_vsi_id.description`:

Description
-----------

check for the valid VSI id

.. _`ice_vc_isvalid_q_id`:

ice_vc_isvalid_q_id
===================

.. c:function:: bool ice_vc_isvalid_q_id(struct ice_vf *vf, u16 vsi_id, u8 qid)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param vsi_id:
        VSI id
    :type vsi_id: u16

    :param qid:
        VSI relative queue id
    :type qid: u8

.. _`ice_vc_isvalid_q_id.description`:

Description
-----------

check for the valid queue id

.. _`ice_vc_config_rss_key`:

ice_vc_config_rss_key
=====================

.. c:function:: int ice_vc_config_rss_key(struct ice_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`ice_vc_config_rss_key.description`:

Description
-----------

Configure the VF's RSS key

.. _`ice_vc_config_rss_lut`:

ice_vc_config_rss_lut
=====================

.. c:function:: int ice_vc_config_rss_lut(struct ice_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`ice_vc_config_rss_lut.description`:

Description
-----------

Configure the VF's RSS LUT

.. _`ice_vc_get_stats_msg`:

ice_vc_get_stats_msg
====================

.. c:function:: int ice_vc_get_stats_msg(struct ice_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`ice_vc_get_stats_msg.description`:

Description
-----------

called from the VF to get VSI stats

.. _`ice_vc_ena_qs_msg`:

ice_vc_ena_qs_msg
=================

.. c:function:: int ice_vc_ena_qs_msg(struct ice_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`ice_vc_ena_qs_msg.description`:

Description
-----------

called from the VF to enable all or specific queue(s)

.. _`ice_vc_dis_qs_msg`:

ice_vc_dis_qs_msg
=================

.. c:function:: int ice_vc_dis_qs_msg(struct ice_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`ice_vc_dis_qs_msg.description`:

Description
-----------

called from the VF to disable all or specific
queue(s)

.. _`ice_vc_cfg_irq_map_msg`:

ice_vc_cfg_irq_map_msg
======================

.. c:function:: int ice_vc_cfg_irq_map_msg(struct ice_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`ice_vc_cfg_irq_map_msg.description`:

Description
-----------

called from the VF to configure the IRQ to queue map

.. _`ice_vc_cfg_qs_msg`:

ice_vc_cfg_qs_msg
=================

.. c:function:: int ice_vc_cfg_qs_msg(struct ice_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`ice_vc_cfg_qs_msg.description`:

Description
-----------

called from the VF to configure the Rx/Tx queues

.. _`ice_is_vf_trusted`:

ice_is_vf_trusted
=================

.. c:function:: bool ice_is_vf_trusted(struct ice_vf *vf)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

.. _`ice_can_vf_change_mac`:

ice_can_vf_change_mac
=====================

.. c:function:: bool ice_can_vf_change_mac(struct ice_vf *vf)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

.. _`ice_can_vf_change_mac.description`:

Description
-----------

Return true if the VF is allowed to change its MAC filters, false otherwise

.. _`ice_vc_handle_mac_addr_msg`:

ice_vc_handle_mac_addr_msg
==========================

.. c:function:: int ice_vc_handle_mac_addr_msg(struct ice_vf *vf, u8 *msg, bool set)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

    :param set:
        true if mac filters are being set, false otherwise
    :type set: bool

.. _`ice_vc_handle_mac_addr_msg.description`:

Description
-----------

add guest mac address filter

.. _`ice_vc_add_mac_addr_msg`:

ice_vc_add_mac_addr_msg
=======================

.. c:function:: int ice_vc_add_mac_addr_msg(struct ice_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`ice_vc_add_mac_addr_msg.description`:

Description
-----------

add guest MAC address filter

.. _`ice_vc_del_mac_addr_msg`:

ice_vc_del_mac_addr_msg
=======================

.. c:function:: int ice_vc_del_mac_addr_msg(struct ice_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`ice_vc_del_mac_addr_msg.description`:

Description
-----------

remove guest MAC address filter

.. _`ice_vc_request_qs_msg`:

ice_vc_request_qs_msg
=====================

.. c:function:: int ice_vc_request_qs_msg(struct ice_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`ice_vc_request_qs_msg.description`:

Description
-----------

VFs get a default number of queues but can use this message to request a
different number.  If the request is successful, PF will reset the VF and
return 0. If unsuccessful, PF will send message informing VF of number of
available queue pairs via virtchnl message response to VF.

.. _`ice_set_vf_port_vlan`:

ice_set_vf_port_vlan
====================

.. c:function:: int ice_set_vf_port_vlan(struct net_device *netdev, int vf_id, u16 vlan_id, u8 qos, __be16 vlan_proto)

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param vf_id:
        VF identifier
    :type vf_id: int

    :param vlan_id:
        VLAN id being set
    :type vlan_id: u16

    :param qos:
        priority setting
    :type qos: u8

    :param vlan_proto:
        VLAN protocol
    :type vlan_proto: __be16

.. _`ice_set_vf_port_vlan.description`:

Description
-----------

program VF Port VLAN id and/or qos

.. _`ice_vc_process_vlan_msg`:

ice_vc_process_vlan_msg
=======================

.. c:function:: int ice_vc_process_vlan_msg(struct ice_vf *vf, u8 *msg, bool add_v)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

    :param add_v:
        Add VLAN if true, otherwise delete VLAN
    :type add_v: bool

.. _`ice_vc_process_vlan_msg.description`:

Description
-----------

Process virtchnl op to add or remove programmed guest VLAN id

.. _`ice_vc_add_vlan_msg`:

ice_vc_add_vlan_msg
===================

.. c:function:: int ice_vc_add_vlan_msg(struct ice_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`ice_vc_add_vlan_msg.description`:

Description
-----------

Add and program guest VLAN id

.. _`ice_vc_remove_vlan_msg`:

ice_vc_remove_vlan_msg
======================

.. c:function:: int ice_vc_remove_vlan_msg(struct ice_vf *vf, u8 *msg)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

.. _`ice_vc_remove_vlan_msg.description`:

Description
-----------

remove programmed guest VLAN id

.. _`ice_vc_ena_vlan_stripping`:

ice_vc_ena_vlan_stripping
=========================

.. c:function:: int ice_vc_ena_vlan_stripping(struct ice_vf *vf)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

.. _`ice_vc_ena_vlan_stripping.description`:

Description
-----------

Enable VLAN header stripping for a given VF

.. _`ice_vc_dis_vlan_stripping`:

ice_vc_dis_vlan_stripping
=========================

.. c:function:: int ice_vc_dis_vlan_stripping(struct ice_vf *vf)

    :param vf:
        pointer to the VF info
    :type vf: struct ice_vf \*

.. _`ice_vc_dis_vlan_stripping.description`:

Description
-----------

Disable VLAN header stripping for a given VF

.. _`ice_vc_process_vf_msg`:

ice_vc_process_vf_msg
=====================

.. c:function:: void ice_vc_process_vf_msg(struct ice_pf *pf, struct ice_rq_event_info *event)

    Process request from VF

    :param pf:
        pointer to the PF structure
    :type pf: struct ice_pf \*

    :param event:
        pointer to the AQ event
    :type event: struct ice_rq_event_info \*

.. _`ice_vc_process_vf_msg.description`:

Description
-----------

called from the common asq/arq handler to
process request from VF

.. _`ice_get_vf_cfg`:

ice_get_vf_cfg
==============

.. c:function:: int ice_get_vf_cfg(struct net_device *netdev, int vf_id, struct ifla_vf_info *ivi)

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param vf_id:
        VF identifier
    :type vf_id: int

    :param ivi:
        VF configuration structure
    :type ivi: struct ifla_vf_info \*

.. _`ice_get_vf_cfg.description`:

Description
-----------

return VF configuration

.. _`ice_set_vf_spoofchk`:

ice_set_vf_spoofchk
===================

.. c:function:: int ice_set_vf_spoofchk(struct net_device *netdev, int vf_id, bool ena)

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param vf_id:
        VF identifier
    :type vf_id: int

    :param ena:
        flag to enable or disable feature
    :type ena: bool

.. _`ice_set_vf_spoofchk.description`:

Description
-----------

Enable or disable VF spoof checking

.. _`ice_set_vf_mac`:

ice_set_vf_mac
==============

.. c:function:: int ice_set_vf_mac(struct net_device *netdev, int vf_id, u8 *mac)

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param vf_id:
        VF identifier
    :type vf_id: int

    :param mac:
        mac address
    :type mac: u8 \*

.. _`ice_set_vf_mac.description`:

Description
-----------

program VF mac address

.. _`ice_set_vf_trust`:

ice_set_vf_trust
================

.. c:function:: int ice_set_vf_trust(struct net_device *netdev, int vf_id, bool trusted)

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param vf_id:
        VF identifier
    :type vf_id: int

    :param trusted:
        Boolean value to enable/disable trusted VF
    :type trusted: bool

.. _`ice_set_vf_trust.description`:

Description
-----------

Enable or disable a given VF as trusted

.. _`ice_set_vf_link_state`:

ice_set_vf_link_state
=====================

.. c:function:: int ice_set_vf_link_state(struct net_device *netdev, int vf_id, int link_state)

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param vf_id:
        VF identifier
    :type vf_id: int

    :param link_state:
        required link state
    :type link_state: int

.. _`ice_set_vf_link_state.description`:

Description
-----------

Set VF's link state, irrespective of physical link state status

.. This file was automatic generated / don't edit.

