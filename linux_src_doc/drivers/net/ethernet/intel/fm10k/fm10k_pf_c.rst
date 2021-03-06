.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/fm10k/fm10k_pf.c

.. _`fm10k_reset_hw_pf`:

fm10k_reset_hw_pf
=================

.. c:function:: s32 fm10k_reset_hw_pf(struct fm10k_hw *hw)

    PF hardware reset

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_reset_hw_pf.description`:

Description
-----------

This function should return the hardware to a state similar to the
one it is in after being powered on.

.. _`fm10k_is_ari_hierarchy_pf`:

fm10k_is_ari_hierarchy_pf
=========================

.. c:function:: bool fm10k_is_ari_hierarchy_pf(struct fm10k_hw *hw)

    Indicate ARI hierarchy support

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_is_ari_hierarchy_pf.description`:

Description
-----------

Looks at the ARI hierarchy bit to determine whether ARI is supported or not.

.. _`fm10k_init_hw_pf`:

fm10k_init_hw_pf
================

.. c:function:: s32 fm10k_init_hw_pf(struct fm10k_hw *hw)

    PF hardware initialization

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_update_vlan_pf`:

fm10k_update_vlan_pf
====================

.. c:function:: s32 fm10k_update_vlan_pf(struct fm10k_hw *hw, u32 vid, u8 vsi, bool set)

    Update status of VLAN ID in VLAN filter table

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param vid:
        VLAN ID to add to table
    :type vid: u32

    :param vsi:
        Index indicating VF ID or PF ID in table
    :type vsi: u8

    :param set:
        Indicates if this is a set or clear operation
    :type set: bool

.. _`fm10k_update_vlan_pf.description`:

Description
-----------

This function adds or removes the corresponding VLAN ID from the VLAN
filter table for the corresponding function.  In addition to the
standard set/clear that supports one bit a multi-bit write is
supported to set 64 bits at a time.

.. _`fm10k_read_mac_addr_pf`:

fm10k_read_mac_addr_pf
======================

.. c:function:: s32 fm10k_read_mac_addr_pf(struct fm10k_hw *hw)

    Read device MAC address

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_read_mac_addr_pf.description`:

Description
-----------

Reads the device MAC address from the SM_AREA and stores the value.

.. _`fm10k_glort_valid_pf`:

fm10k_glort_valid_pf
====================

.. c:function:: bool fm10k_glort_valid_pf(struct fm10k_hw *hw, u16 glort)

    Validate that the provided glort is valid

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

    :param glort:
        base glort to be validated
    :type glort: u16

.. _`fm10k_glort_valid_pf.description`:

Description
-----------

This function will return an error if the provided glort is invalid

.. _`fm10k_update_xc_addr_pf`:

fm10k_update_xc_addr_pf
=======================

.. c:function:: s32 fm10k_update_xc_addr_pf(struct fm10k_hw *hw, u16 glort, const u8 *mac, u16 vid, bool add, u8 flags)

    Update device addresses

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

    :param glort:
        base resource tag for this request
    :type glort: u16

    :param mac:
        MAC address to add/remove from table
    :type mac: const u8 \*

    :param vid:
        VLAN ID to add/remove from table
    :type vid: u16

    :param add:
        Indicates if this is an add or remove operation
    :type add: bool

    :param flags:
        flags field to indicate add and secure
    :type flags: u8

.. _`fm10k_update_xc_addr_pf.description`:

Description
-----------

This function generates a message to the Switch API requesting
that the given logical port add/remove the given L2 MAC/VLAN address.

.. _`fm10k_update_uc_addr_pf`:

fm10k_update_uc_addr_pf
=======================

.. c:function:: s32 fm10k_update_uc_addr_pf(struct fm10k_hw *hw, u16 glort, const u8 *mac, u16 vid, bool add, u8 flags)

    Update device unicast addresses

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

    :param glort:
        base resource tag for this request
    :type glort: u16

    :param mac:
        MAC address to add/remove from table
    :type mac: const u8 \*

    :param vid:
        VLAN ID to add/remove from table
    :type vid: u16

    :param add:
        Indicates if this is an add or remove operation
    :type add: bool

    :param flags:
        flags field to indicate add and secure
    :type flags: u8

.. _`fm10k_update_uc_addr_pf.description`:

Description
-----------

This function is used to add or remove unicast addresses for
the PF.

.. _`fm10k_update_mc_addr_pf`:

fm10k_update_mc_addr_pf
=======================

.. c:function:: s32 fm10k_update_mc_addr_pf(struct fm10k_hw *hw, u16 glort, const u8 *mac, u16 vid, bool add)

    Update device multicast addresses

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

    :param glort:
        base resource tag for this request
    :type glort: u16

    :param mac:
        MAC address to add/remove from table
    :type mac: const u8 \*

    :param vid:
        VLAN ID to add/remove from table
    :type vid: u16

    :param add:
        Indicates if this is an add or remove operation
    :type add: bool

.. _`fm10k_update_mc_addr_pf.description`:

Description
-----------

This function is used to add or remove multicast MAC addresses for
the PF.

.. _`fm10k_update_xcast_mode_pf`:

fm10k_update_xcast_mode_pf
==========================

.. c:function:: s32 fm10k_update_xcast_mode_pf(struct fm10k_hw *hw, u16 glort, u8 mode)

    Request update of multicast mode

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param glort:
        base resource tag for this request
    :type glort: u16

    :param mode:
        integer value indicating mode being requested
    :type mode: u8

.. _`fm10k_update_xcast_mode_pf.description`:

Description
-----------

This function will attempt to request a higher mode for the port
so that it can enable either multicast, multicast promiscuous, or
promiscuous mode of operation.

.. _`fm10k_update_int_moderator_pf`:

fm10k_update_int_moderator_pf
=============================

.. c:function:: void fm10k_update_int_moderator_pf(struct fm10k_hw *hw)

    Update interrupt moderator linked list

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_update_int_moderator_pf.description`:

Description
-----------

This function walks through the MSI-X vector table to determine the
number of active interrupts and based on that information updates the
interrupt moderator linked list.

.. _`fm10k_update_lport_state_pf`:

fm10k_update_lport_state_pf
===========================

.. c:function:: s32 fm10k_update_lport_state_pf(struct fm10k_hw *hw, u16 glort, u16 count, bool enable)

    Notify the switch of a change in port state

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

    :param glort:
        base resource tag for this request
    :type glort: u16

    :param count:
        number of logical ports being updated
    :type count: u16

    :param enable:
        boolean value indicating enable or disable
    :type enable: bool

.. _`fm10k_update_lport_state_pf.description`:

Description
-----------

This function is used to add/remove a logical port from the switch.

.. _`fm10k_configure_dglort_map_pf`:

fm10k_configure_dglort_map_pf
=============================

.. c:function:: s32 fm10k_configure_dglort_map_pf(struct fm10k_hw *hw, struct fm10k_dglort_cfg *dglort)

    Configures GLORT entry and queues

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param dglort:
        pointer to dglort configuration structure
    :type dglort: struct fm10k_dglort_cfg \*

.. _`fm10k_configure_dglort_map_pf.description`:

Description
-----------

Reads the configuration structure contained in dglort_cfg and uses
that information to then populate a DGLORTMAP/DEC entry and the queues
to which it has been assigned.

.. _`fm10k_iov_assign_resources_pf`:

fm10k_iov_assign_resources_pf
=============================

.. c:function:: s32 fm10k_iov_assign_resources_pf(struct fm10k_hw *hw, u16 num_vfs, u16 num_pools)

    Assign pool resources for virtualization

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

    :param num_vfs:
        number of VFs to be allocated
    :type num_vfs: u16

    :param num_pools:
        number of virtualization pools to be allocated
    :type num_pools: u16

.. _`fm10k_iov_assign_resources_pf.description`:

Description
-----------

Allocates queues and traffic classes to virtualization entities to prepare
the PF for SR-IOV and VMDq

.. _`fm10k_iov_configure_tc_pf`:

fm10k_iov_configure_tc_pf
=========================

.. c:function:: s32 fm10k_iov_configure_tc_pf(struct fm10k_hw *hw, u16 vf_idx, int rate)

    Configure the shaping group for VF

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

    :param vf_idx:
        index of VF receiving GLORT
    :type vf_idx: u16

    :param rate:
        Rate indicated in Mb/s
    :type rate: int

.. _`fm10k_iov_configure_tc_pf.description`:

Description
-----------

Configured the TC for a given VF to allow only up to a given number
of Mb/s of outgoing Tx throughput.

.. _`fm10k_iov_assign_int_moderator_pf`:

fm10k_iov_assign_int_moderator_pf
=================================

.. c:function:: s32 fm10k_iov_assign_int_moderator_pf(struct fm10k_hw *hw, u16 vf_idx)

    Add VF interrupts to moderator list

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

    :param vf_idx:
        index of VF receiving GLORT
    :type vf_idx: u16

.. _`fm10k_iov_assign_int_moderator_pf.description`:

Description
-----------

Update the interrupt moderator linked list to include any MSI-X
interrupts which the VF has enabled in the MSI-X vector table.

.. _`fm10k_iov_assign_default_mac_vlan_pf`:

fm10k_iov_assign_default_mac_vlan_pf
====================================

.. c:function:: s32 fm10k_iov_assign_default_mac_vlan_pf(struct fm10k_hw *hw, struct fm10k_vf_info *vf_info)

    Assign a MAC and VLAN to VF

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

    :param vf_info:
        pointer to VF information structure
    :type vf_info: struct fm10k_vf_info \*

.. _`fm10k_iov_assign_default_mac_vlan_pf.description`:

Description
-----------

Assign a MAC address and default VLAN to a VF and notify it of the update

.. _`fm10k_iov_reset_resources_pf`:

fm10k_iov_reset_resources_pf
============================

.. c:function:: s32 fm10k_iov_reset_resources_pf(struct fm10k_hw *hw, struct fm10k_vf_info *vf_info)

    Reassign queues and interrupts to a VF

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

    :param vf_info:
        pointer to VF information structure
    :type vf_info: struct fm10k_vf_info \*

.. _`fm10k_iov_reset_resources_pf.description`:

Description
-----------

Reassign the interrupts and queues to a VF following an FLR

.. _`fm10k_iov_set_lport_pf`:

fm10k_iov_set_lport_pf
======================

.. c:function:: s32 fm10k_iov_set_lport_pf(struct fm10k_hw *hw, struct fm10k_vf_info *vf_info, u16 lport_idx, u8 flags)

    Assign and enable a logical port for a given VF

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param vf_info:
        pointer to VF information structure
    :type vf_info: struct fm10k_vf_info \*

    :param lport_idx:
        Logical port offset from the hardware glort
    :type lport_idx: u16

    :param flags:
        Set of capability flags to extend port beyond basic functionality
    :type flags: u8

.. _`fm10k_iov_set_lport_pf.description`:

Description
-----------

This function allows enabling a VF port by assigning it a GLORT and
setting the flags so that it can enable an Rx mode.

.. _`fm10k_iov_reset_lport_pf`:

fm10k_iov_reset_lport_pf
========================

.. c:function:: void fm10k_iov_reset_lport_pf(struct fm10k_hw *hw, struct fm10k_vf_info *vf_info)

    Disable a logical port for a given VF

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param vf_info:
        pointer to VF information structure
    :type vf_info: struct fm10k_vf_info \*

.. _`fm10k_iov_reset_lport_pf.description`:

Description
-----------

This function disables a VF port by stripping it of a GLORT and
setting the flags so that it cannot enable any Rx mode.

.. _`fm10k_iov_update_stats_pf`:

fm10k_iov_update_stats_pf
=========================

.. c:function:: void fm10k_iov_update_stats_pf(struct fm10k_hw *hw, struct fm10k_hw_stats_q *q, u16 vf_idx)

    Updates hardware related statistics for VFs

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param q:
        stats for all queues of a VF
    :type q: struct fm10k_hw_stats_q \*

    :param vf_idx:
        index of VF
    :type vf_idx: u16

.. _`fm10k_iov_update_stats_pf.description`:

Description
-----------

This function collects queue stats for VFs.

.. _`fm10k_iov_msg_msix_pf`:

fm10k_iov_msg_msix_pf
=====================

.. c:function:: s32 fm10k_iov_msg_msix_pf(struct fm10k_hw *hw, u32 **results, struct fm10k_mbx_info *mbx)

    Message handler for MSI-X request from VF

    :param hw:
        Pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param results:
        Pointer array to message, results[0] is pointer to message
    :type results: u32 \*\*

    :param mbx:
        Pointer to mailbox information structure
    :type mbx: struct fm10k_mbx_info \*

.. _`fm10k_iov_msg_msix_pf.description`:

Description
-----------

This function is a default handler for MSI-X requests from the VF.  The
assumption is that in this case it is acceptable to just directly
hand off the message from the VF to the underlying shared code.

.. _`fm10k_iov_select_vid`:

fm10k_iov_select_vid
====================

.. c:function:: s32 fm10k_iov_select_vid(struct fm10k_vf_info *vf_info, u16 vid)

    Select correct default VLAN ID

    :param vf_info:
        pointer to VF information structure
    :type vf_info: struct fm10k_vf_info \*

    :param vid:
        VLAN ID to correct
    :type vid: u16

.. _`fm10k_iov_select_vid.description`:

Description
-----------

Will report an error if the VLAN ID is out of range. For VID = 0, it will
return either the pf_vid or sw_vid depending on which one is set.

.. _`fm10k_iov_msg_mac_vlan_pf`:

fm10k_iov_msg_mac_vlan_pf
=========================

.. c:function:: s32 fm10k_iov_msg_mac_vlan_pf(struct fm10k_hw *hw, u32 **results, struct fm10k_mbx_info *mbx)

    Message handler for MAC/VLAN request from VF

    :param hw:
        Pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param results:
        Pointer array to message, results[0] is pointer to message
    :type results: u32 \*\*

    :param mbx:
        Pointer to mailbox information structure
    :type mbx: struct fm10k_mbx_info \*

.. _`fm10k_iov_msg_mac_vlan_pf.description`:

Description
-----------

This function is a default handler for MAC/VLAN requests from the VF.
The assumption is that in this case it is acceptable to just directly
hand off the message from the VF to the underlying shared code.

.. _`fm10k_iov_supported_xcast_mode_pf`:

fm10k_iov_supported_xcast_mode_pf
=================================

.. c:function:: u8 fm10k_iov_supported_xcast_mode_pf(struct fm10k_vf_info *vf_info, u8 mode)

    Determine best match for xcast mode

    :param vf_info:
        VF info structure containing capability flags
    :type vf_info: struct fm10k_vf_info \*

    :param mode:
        Requested xcast mode
    :type mode: u8

.. _`fm10k_iov_supported_xcast_mode_pf.description`:

Description
-----------

This function outputs the mode that most closely matches the requested
mode.  If not modes match it will request we disable the port

.. _`fm10k_iov_msg_lport_state_pf`:

fm10k_iov_msg_lport_state_pf
============================

.. c:function:: s32 fm10k_iov_msg_lport_state_pf(struct fm10k_hw *hw, u32 **results, struct fm10k_mbx_info *mbx)

    Message handler for port state requests

    :param hw:
        Pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param results:
        Pointer array to message, results[0] is pointer to message
    :type results: u32 \*\*

    :param mbx:
        Pointer to mailbox information structure
    :type mbx: struct fm10k_mbx_info \*

.. _`fm10k_iov_msg_lport_state_pf.description`:

Description
-----------

This function is a default handler for port state requests.  The port
state requests for now are basic and consist of enabling or disabling
the port.

.. _`fm10k_update_hw_stats_pf`:

fm10k_update_hw_stats_pf
========================

.. c:function:: void fm10k_update_hw_stats_pf(struct fm10k_hw *hw, struct fm10k_hw_stats *stats)

    Updates hardware related statistics of PF

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param stats:
        pointer to the stats structure to update
    :type stats: struct fm10k_hw_stats \*

.. _`fm10k_update_hw_stats_pf.description`:

Description
-----------

This function collects and aggregates global and per queue hardware
statistics.

.. _`fm10k_rebind_hw_stats_pf`:

fm10k_rebind_hw_stats_pf
========================

.. c:function:: void fm10k_rebind_hw_stats_pf(struct fm10k_hw *hw, struct fm10k_hw_stats *stats)

    Resets base for hardware statistics of PF

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param stats:
        pointer to the stats structure to update
    :type stats: struct fm10k_hw_stats \*

.. _`fm10k_rebind_hw_stats_pf.description`:

Description
-----------

This function resets the base for global and per queue hardware
statistics.

.. _`fm10k_set_dma_mask_pf`:

fm10k_set_dma_mask_pf
=====================

.. c:function:: void fm10k_set_dma_mask_pf(struct fm10k_hw *hw, u64 dma_mask)

    Configures PhyAddrSpace to limit DMA to system

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param dma_mask:
        64 bit DMA mask required for platform
    :type dma_mask: u64

.. _`fm10k_set_dma_mask_pf.description`:

Description
-----------

This function sets the PHYADDR.PhyAddrSpace bits for the endpoint in order
to limit the access to memory beyond what is physically in the system.

.. _`fm10k_get_fault_pf`:

fm10k_get_fault_pf
==================

.. c:function:: s32 fm10k_get_fault_pf(struct fm10k_hw *hw, int type, struct fm10k_fault *fault)

    Record a fault in one of the interface units

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param type:
        pointer to fault type register offset
    :type type: int

    :param fault:
        pointer to memory location to record the fault
    :type fault: struct fm10k_fault \*

.. _`fm10k_get_fault_pf.description`:

Description
-----------

Record the fault register contents to the fault data structure and
clear the entry from the register.

Returns ERR_PARAM if invalid register is specified or no error is present.

.. _`fm10k_request_lport_map_pf`:

fm10k_request_lport_map_pf
==========================

.. c:function:: s32 fm10k_request_lport_map_pf(struct fm10k_hw *hw)

    Request LPORT map from the switch API

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_get_host_state_pf`:

fm10k_get_host_state_pf
=======================

.. c:function:: s32 fm10k_get_host_state_pf(struct fm10k_hw *hw, bool *switch_ready)

    Returns the state of the switch and mailbox

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param switch_ready:
        pointer to boolean value that will record switch state
    :type switch_ready: bool \*

.. _`fm10k_get_host_state_pf.description`:

Description
-----------

This function will check the DMA_CTRL2 register and mailbox in order
to determine if the switch is ready for the PF to begin requesting
addresses and mapping traffic to the local interface.

.. _`fm10k_msg_lport_map_pf`:

fm10k_msg_lport_map_pf
======================

.. c:function:: s32 fm10k_msg_lport_map_pf(struct fm10k_hw *hw, u32 **results, struct fm10k_mbx_info *mbx)

    Message handler for lport_map message from SM

    :param hw:
        Pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param results:
        pointer array containing parsed data
    :type results: u32 \*\*

    :param mbx:
        Pointer to mailbox information structure
    :type mbx: struct fm10k_mbx_info \*

.. _`fm10k_msg_lport_map_pf.description`:

Description
-----------

This handler configures the lport mapping based on the reply from the
switch API.

.. _`fm10k_msg_update_pvid_pf`:

fm10k_msg_update_pvid_pf
========================

.. c:function:: s32 fm10k_msg_update_pvid_pf(struct fm10k_hw *hw, u32 **results, struct fm10k_mbx_info *mbx)

    Message handler for port VLAN message from SM

    :param hw:
        Pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param results:
        pointer array containing parsed data
    :type results: u32 \*\*

    :param mbx:
        Pointer to mailbox information structure
    :type mbx: struct fm10k_mbx_info \*

.. _`fm10k_msg_update_pvid_pf.description`:

Description
-----------

This handler configures the default VLAN for the PF

.. _`fm10k_record_global_table_data`:

fm10k_record_global_table_data
==============================

.. c:function:: void fm10k_record_global_table_data(struct fm10k_global_table_data *from, struct fm10k_swapi_table_info *to)

    Move global table data to swapi table info

    :param from:
        pointer to source table data structure
    :type from: struct fm10k_global_table_data \*

    :param to:
        pointer to destination table info structure
    :type to: struct fm10k_swapi_table_info \*

.. _`fm10k_record_global_table_data.description`:

Description
-----------

This function is will copy table_data to the table_info contained in
the hw struct.

.. _`fm10k_msg_err_pf`:

fm10k_msg_err_pf
================

.. c:function:: s32 fm10k_msg_err_pf(struct fm10k_hw *hw, u32 **results, struct fm10k_mbx_info *mbx)

    Message handler for error reply

    :param hw:
        Pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param results:
        pointer array containing parsed data
    :type results: u32 \*\*

    :param mbx:
        Pointer to mailbox information structure
    :type mbx: struct fm10k_mbx_info \*

.. _`fm10k_msg_err_pf.description`:

Description
-----------

This handler will capture the data for any error replies to previous
messages that the PF has sent.

.. This file was automatic generated / don't edit.

