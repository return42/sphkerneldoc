.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/fm10k/fm10k_vf.c

.. _`fm10k_stop_hw_vf`:

fm10k_stop_hw_vf
================

.. c:function:: s32 fm10k_stop_hw_vf(struct fm10k_hw *hw)

    Stop Tx/Rx units

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_reset_hw_vf`:

fm10k_reset_hw_vf
=================

.. c:function:: s32 fm10k_reset_hw_vf(struct fm10k_hw *hw)

    VF hardware reset

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_reset_hw_vf.description`:

Description
-----------

This function should return the hardware to a state similar to the
one it is in after just being initialized.

.. _`fm10k_init_hw_vf`:

fm10k_init_hw_vf
================

.. c:function:: s32 fm10k_init_hw_vf(struct fm10k_hw *hw)

    VF hardware initialization

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_update_vlan_vf`:

fm10k_update_vlan_vf
====================

.. c:function:: s32 fm10k_update_vlan_vf(struct fm10k_hw *hw, u32 vid, u8 vsi, bool set)

    Update status of VLAN ID in VLAN filter table

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param vid:
        VLAN ID to add to table
    :type vid: u32

    :param vsi:
        Reserved, should always be 0
    :type vsi: u8

    :param set:
        Indicates if this is a set or clear operation
    :type set: bool

.. _`fm10k_update_vlan_vf.description`:

Description
-----------

This function adds or removes the corresponding VLAN ID from the VLAN
filter table for this VF.

.. _`fm10k_msg_mac_vlan_vf`:

fm10k_msg_mac_vlan_vf
=====================

.. c:function:: s32 fm10k_msg_mac_vlan_vf(struct fm10k_hw *hw, u32 **results, struct fm10k_mbx_info *mbx)

    Read device MAC address from mailbox message

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

    :param results:
        Attributes for message
    :type results: u32 \*\*

    :param mbx:
        unused mailbox data
    :type mbx: struct fm10k_mbx_info \*

.. _`fm10k_msg_mac_vlan_vf.description`:

Description
-----------

This function should determine the MAC address for the VF

.. _`fm10k_read_mac_addr_vf`:

fm10k_read_mac_addr_vf
======================

.. c:function:: s32 fm10k_read_mac_addr_vf(struct fm10k_hw *hw)

    Read device MAC address

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_read_mac_addr_vf.description`:

Description
-----------

This function should determine the MAC address for the VF

.. _`fm10k_update_uc_addr_vf`:

fm10k_update_uc_addr_vf
=======================

.. c:function:: s32 fm10k_update_uc_addr_vf(struct fm10k_hw *hw, u16 glort, const u8 *mac, u16 vid, bool add, u8 flags)

    Update device unicast addresses

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

    :param glort:
        unused
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
        flags field to indicate add and secure - unused
    :type flags: u8

.. _`fm10k_update_uc_addr_vf.description`:

Description
-----------

This function is used to add or remove unicast MAC addresses for
the VF.

.. _`fm10k_update_mc_addr_vf`:

fm10k_update_mc_addr_vf
=======================

.. c:function:: s32 fm10k_update_mc_addr_vf(struct fm10k_hw *hw, u16 glort, const u8 *mac, u16 vid, bool add)

    Update device multicast addresses

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

    :param glort:
        unused
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

.. _`fm10k_update_mc_addr_vf.description`:

Description
-----------

This function is used to add or remove multicast MAC addresses for
the VF.

.. _`fm10k_update_int_moderator_vf`:

fm10k_update_int_moderator_vf
=============================

.. c:function:: void fm10k_update_int_moderator_vf(struct fm10k_hw *hw)

    Request update of interrupt moderator list

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

.. _`fm10k_update_int_moderator_vf.description`:

Description
-----------

This function will issue a request to the PF to rescan our MSI-X table
and to update the interrupt moderator linked list.

.. _`fm10k_msg_lport_state_vf`:

fm10k_msg_lport_state_vf
========================

.. c:function:: s32 fm10k_msg_lport_state_vf(struct fm10k_hw *hw, u32 **results, struct fm10k_mbx_info *mbx)

    Message handler for lport_state message from PF

    :param hw:
        Pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param results:
        pointer array containing parsed data
    :type results: u32 \*\*

    :param mbx:
        Pointer to mailbox information structure
    :type mbx: struct fm10k_mbx_info \*

.. _`fm10k_msg_lport_state_vf.description`:

Description
-----------

This handler is meant to capture the indication from the PF that we
are ready to bring up the interface.

.. _`fm10k_update_lport_state_vf`:

fm10k_update_lport_state_vf
===========================

.. c:function:: s32 fm10k_update_lport_state_vf(struct fm10k_hw *hw, u16 glort, u16 count, bool enable)

    Update device state in lower device

    :param hw:
        pointer to the HW structure
    :type hw: struct fm10k_hw \*

    :param glort:
        unused
    :type glort: u16

    :param count:
        number of logical ports to enable - unused (always 1)
    :type count: u16

    :param enable:
        boolean value indicating if this is an enable or disable request
    :type enable: bool

.. _`fm10k_update_lport_state_vf.description`:

Description
-----------

Notify the lower device of a state change.  If the lower device is
enabled we can add filters, if it is disabled all filters for this
logical port are flushed.

.. _`fm10k_update_xcast_mode_vf`:

fm10k_update_xcast_mode_vf
==========================

.. c:function:: s32 fm10k_update_xcast_mode_vf(struct fm10k_hw *hw, u16 glort, u8 mode)

    Request update of multicast mode

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param glort:
        unused
    :type glort: u16

    :param mode:
        integer value indicating mode being requested
    :type mode: u8

.. _`fm10k_update_xcast_mode_vf.description`:

Description
-----------

This function will attempt to request a higher mode for the port
so that it can enable either multicast, multicast promiscuous, or
promiscuous mode of operation.

.. _`fm10k_update_hw_stats_vf`:

fm10k_update_hw_stats_vf
========================

.. c:function:: void fm10k_update_hw_stats_vf(struct fm10k_hw *hw, struct fm10k_hw_stats *stats)

    Updates hardware related statistics of VF

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param stats:
        pointer to statistics structure
    :type stats: struct fm10k_hw_stats \*

.. _`fm10k_update_hw_stats_vf.description`:

Description
-----------

This function collects and aggregates per queue hardware statistics.

.. _`fm10k_rebind_hw_stats_vf`:

fm10k_rebind_hw_stats_vf
========================

.. c:function:: void fm10k_rebind_hw_stats_vf(struct fm10k_hw *hw, struct fm10k_hw_stats *stats)

    Resets base for hardware statistics of VF

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param stats:
        pointer to the stats structure to update
    :type stats: struct fm10k_hw_stats \*

.. _`fm10k_rebind_hw_stats_vf.description`:

Description
-----------

This function resets the base for queue hardware statistics.

.. _`fm10k_configure_dglort_map_vf`:

fm10k_configure_dglort_map_vf
=============================

.. c:function:: s32 fm10k_configure_dglort_map_vf(struct fm10k_hw *hw, struct fm10k_dglort_cfg *dglort)

    Configures GLORT entry and queues

    :param hw:
        pointer to hardware structure
    :type hw: struct fm10k_hw \*

    :param dglort:
        pointer to dglort configuration structure
    :type dglort: struct fm10k_dglort_cfg \*

.. _`fm10k_configure_dglort_map_vf.description`:

Description
-----------

Reads the configuration structure contained in dglort_cfg and uses
that information to then populate a DGLORTMAP/DEC entry and the queues
to which it has been assigned.

.. This file was automatic generated / don't edit.

