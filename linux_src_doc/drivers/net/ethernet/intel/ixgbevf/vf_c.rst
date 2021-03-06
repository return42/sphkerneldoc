.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbevf/vf.c

.. _`ixgbevf_start_hw_vf`:

ixgbevf_start_hw_vf
===================

.. c:function:: s32 ixgbevf_start_hw_vf(struct ixgbe_hw *hw)

    Prepare hardware for Tx/Rx

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbevf_start_hw_vf.description`:

Description
-----------

Starts the hardware by filling the bus info structure and media type, clears
all on chip counters, initializes receive address registers, multicast
table, VLAN filter table, calls routine to set up link and flow control
settings, and leaves transmit and receive units disabled and uninitialized

.. _`ixgbevf_init_hw_vf`:

ixgbevf_init_hw_vf
==================

.. c:function:: s32 ixgbevf_init_hw_vf(struct ixgbe_hw *hw)

    virtual function hardware initialization

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbevf_init_hw_vf.description`:

Description
-----------

Initialize the hardware by resetting the hardware and then starting
the hardware

.. _`ixgbevf_reset_hw_vf`:

ixgbevf_reset_hw_vf
===================

.. c:function:: s32 ixgbevf_reset_hw_vf(struct ixgbe_hw *hw)

    Performs hardware reset

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbevf_reset_hw_vf.description`:

Description
-----------

Resets the hardware by resetting the transmit and receive units, masks and
clears all interrupts.

.. _`ixgbevf_hv_reset_hw_vf`:

ixgbevf_hv_reset_hw_vf
======================

.. c:function:: s32 ixgbevf_hv_reset_hw_vf(struct ixgbe_hw *hw)

    V variant; the VF/PF communication is through the PCI config space.

    :param hw:
        pointer to private hardware struct
    :type hw: struct ixgbe_hw \*

.. _`ixgbevf_stop_hw_vf`:

ixgbevf_stop_hw_vf
==================

.. c:function:: s32 ixgbevf_stop_hw_vf(struct ixgbe_hw *hw)

    Generic stop Tx/Rx units

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbevf_stop_hw_vf.description`:

Description
-----------

Sets the adapter_stopped flag within ixgbe_hw struct. Clears interrupts,
disables transmit and receive units. The adapter_stopped flag is used by
the shared code and drivers to determine if the adapter is in a stopped
state and should not touch the hardware.

.. _`ixgbevf_mta_vector`:

ixgbevf_mta_vector
==================

.. c:function:: s32 ixgbevf_mta_vector(struct ixgbe_hw *hw, u8 *mc_addr)

    Determines bit-vector in multicast table to set

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param mc_addr:
        the multicast address
    :type mc_addr: u8 \*

.. _`ixgbevf_mta_vector.description`:

Description
-----------

Extracts the 12 bits, from a multicast address, to determine which
bit-vector to set in the multicast table. The hardware uses 12 bits, from
incoming Rx multicast addresses, to determine the bit-vector to check in
the MTA. Which of the 4 combination, of 12-bits, the hardware uses is set
by the MO field of the MCSTCTRL. The MO field is set during initialization
to mc_filter_type.

.. _`ixgbevf_get_mac_addr_vf`:

ixgbevf_get_mac_addr_vf
=======================

.. c:function:: s32 ixgbevf_get_mac_addr_vf(struct ixgbe_hw *hw, u8 *mac_addr)

    Read device MAC address

    :param hw:
        pointer to the HW structure
    :type hw: struct ixgbe_hw \*

    :param mac_addr:
        pointer to storage for retrieved MAC address
    :type mac_addr: u8 \*

.. _`ixgbevf_get_reta_locked`:

ixgbevf_get_reta_locked
=======================

.. c:function:: int ixgbevf_get_reta_locked(struct ixgbe_hw *hw, u32 *reta, int num_rx_queues)

    get the RSS redirection table (RETA) contents.

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param reta:
        buffer to fill with RETA contents.
    :type reta: u32 \*

    :param num_rx_queues:
        Number of Rx queues configured for this port
    :type num_rx_queues: int

.. _`ixgbevf_get_reta_locked.description`:

Description
-----------

The "reta" buffer should be big enough to contain 32 registers.

.. _`ixgbevf_get_reta_locked.return`:

Return
------

0 on success.
if API doesn't support this operation - (-EOPNOTSUPP).

.. _`ixgbevf_get_rss_key_locked`:

ixgbevf_get_rss_key_locked
==========================

.. c:function:: int ixgbevf_get_rss_key_locked(struct ixgbe_hw *hw, u8 *rss_key)

    get the RSS Random Key

    :param hw:
        pointer to the HW structure
    :type hw: struct ixgbe_hw \*

    :param rss_key:
        buffer to fill with RSS Hash Key contents.
    :type rss_key: u8 \*

.. _`ixgbevf_get_rss_key_locked.description`:

Description
-----------

The "rss_key" buffer should be big enough to contain 10 registers.

.. _`ixgbevf_get_rss_key_locked.return`:

Return
------

0 on success.
if API doesn't support this operation - (-EOPNOTSUPP).

.. _`ixgbevf_set_rar_vf`:

ixgbevf_set_rar_vf
==================

.. c:function:: s32 ixgbevf_set_rar_vf(struct ixgbe_hw *hw, u32 index, u8 *addr, u32 vmdq)

    set device MAC address

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param index:
        Receive address register to write
    :type index: u32

    :param addr:
        Address to put into receive address register
    :type addr: u8 \*

    :param vmdq:
        Unused in this implementation
    :type vmdq: u32

.. _`ixgbevf_hv_set_rar_vf`:

ixgbevf_hv_set_rar_vf
=====================

.. c:function:: s32 ixgbevf_hv_set_rar_vf(struct ixgbe_hw *hw, u32 index, u8 *addr, u32 vmdq)

    set device MAC address Hyper-V variant

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param index:
        Receive address register to write
    :type index: u32

    :param addr:
        Address to put into receive address register
    :type addr: u8 \*

    :param vmdq:
        Unused in this implementation
    :type vmdq: u32

.. _`ixgbevf_hv_set_rar_vf.description`:

Description
-----------

We don't really allow setting the device MAC address. However,
if the address being set is the permanent MAC address we will
permit that.

.. _`ixgbevf_update_mc_addr_list_vf`:

ixgbevf_update_mc_addr_list_vf
==============================

.. c:function:: s32 ixgbevf_update_mc_addr_list_vf(struct ixgbe_hw *hw, struct net_device *netdev)

    Update Multicast addresses

    :param hw:
        pointer to the HW structure
    :type hw: struct ixgbe_hw \*

    :param netdev:
        pointer to net device structure
    :type netdev: struct net_device \*

.. _`ixgbevf_update_mc_addr_list_vf.description`:

Description
-----------

Updates the Multicast Table Array.

.. _`ixgbevf_hv_update_mc_addr_list_vf`:

ixgbevf_hv_update_mc_addr_list_vf
=================================

.. c:function:: s32 ixgbevf_hv_update_mc_addr_list_vf(struct ixgbe_hw *hw, struct net_device *netdev)

    V variant - just a stub.

    :param hw:
        unused
    :type hw: struct ixgbe_hw \*

    :param netdev:
        unused
    :type netdev: struct net_device \*

.. _`ixgbevf_update_xcast_mode`:

ixgbevf_update_xcast_mode
=========================

.. c:function:: s32 ixgbevf_update_xcast_mode(struct ixgbe_hw *hw, int xcast_mode)

    Update Multicast mode

    :param hw:
        pointer to the HW structure
    :type hw: struct ixgbe_hw \*

    :param xcast_mode:
        new multicast mode
    :type xcast_mode: int

.. _`ixgbevf_update_xcast_mode.description`:

Description
-----------

Updates the Multicast Mode of VF.

.. _`ixgbevf_hv_update_xcast_mode`:

ixgbevf_hv_update_xcast_mode
============================

.. c:function:: s32 ixgbevf_hv_update_xcast_mode(struct ixgbe_hw *hw, int xcast_mode)

    V variant - just a stub.

    :param hw:
        unused
    :type hw: struct ixgbe_hw \*

    :param xcast_mode:
        unused
    :type xcast_mode: int

.. _`ixgbevf_set_vfta_vf`:

ixgbevf_set_vfta_vf
===================

.. c:function:: s32 ixgbevf_set_vfta_vf(struct ixgbe_hw *hw, u32 vlan, u32 vind, bool vlan_on)

    Set/Unset VLAN filter table address

    :param hw:
        pointer to the HW structure
    :type hw: struct ixgbe_hw \*

    :param vlan:
        12 bit VLAN ID
    :type vlan: u32

    :param vind:
        unused by VF drivers
    :type vind: u32

    :param vlan_on:
        if true then set bit, else clear bit
    :type vlan_on: bool

.. _`ixgbevf_hv_set_vfta_vf`:

ixgbevf_hv_set_vfta_vf
======================

.. c:function:: s32 ixgbevf_hv_set_vfta_vf(struct ixgbe_hw *hw, u32 vlan, u32 vind, bool vlan_on)

    V variant - just a stub.

    :param hw:
        unused
    :type hw: struct ixgbe_hw \*

    :param vlan:
        unused
    :type vlan: u32

    :param vind:
        unused
    :type vind: u32

    :param vlan_on:
        unused
    :type vlan_on: bool

.. _`ixgbevf_setup_mac_link_vf`:

ixgbevf_setup_mac_link_vf
=========================

.. c:function:: s32 ixgbevf_setup_mac_link_vf(struct ixgbe_hw *hw, ixgbe_link_speed speed, bool autoneg, bool autoneg_wait_to_complete)

    Setup MAC link settings

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        Unused in this implementation
    :type speed: ixgbe_link_speed

    :param autoneg:
        Unused in this implementation
    :type autoneg: bool

    :param autoneg_wait_to_complete:
        Unused in this implementation
    :type autoneg_wait_to_complete: bool

.. _`ixgbevf_setup_mac_link_vf.description`:

Description
-----------

Do nothing and return success.  VF drivers are not allowed to change
global settings.  Maintained for driver compatibility.

.. _`ixgbevf_check_mac_link_vf`:

ixgbevf_check_mac_link_vf
=========================

.. c:function:: s32 ixgbevf_check_mac_link_vf(struct ixgbe_hw *hw, ixgbe_link_speed *speed, bool *link_up, bool autoneg_wait_to_complete)

    Get link/speed status

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        pointer to link speed
    :type speed: ixgbe_link_speed \*

    :param link_up:
        true is link is up, false otherwise
    :type link_up: bool \*

    :param autoneg_wait_to_complete:
        unused
    :type autoneg_wait_to_complete: bool

.. _`ixgbevf_check_mac_link_vf.description`:

Description
-----------

Reads the links register to determine if link is up and the current speed

.. _`ixgbevf_hv_check_mac_link_vf`:

ixgbevf_hv_check_mac_link_vf
============================

.. c:function:: s32 ixgbevf_hv_check_mac_link_vf(struct ixgbe_hw *hw, ixgbe_link_speed *speed, bool *link_up, bool autoneg_wait_to_complete)

    V variant; there is no mailbox communication.

    :param hw:
        pointer to private hardware struct
    :type hw: struct ixgbe_hw \*

    :param speed:
        pointer to link speed
    :type speed: ixgbe_link_speed \*

    :param link_up:
        true is link is up, false otherwise
    :type link_up: bool \*

    :param autoneg_wait_to_complete:
        unused
    :type autoneg_wait_to_complete: bool

.. _`ixgbevf_set_rlpml_vf`:

ixgbevf_set_rlpml_vf
====================

.. c:function:: s32 ixgbevf_set_rlpml_vf(struct ixgbe_hw *hw, u16 max_size)

    Set the maximum receive packet length

    :param hw:
        pointer to the HW structure
    :type hw: struct ixgbe_hw \*

    :param max_size:
        value to assign to max frame size
    :type max_size: u16

.. _`ixgbevf_hv_set_rlpml_vf`:

ixgbevf_hv_set_rlpml_vf
=======================

.. c:function:: s32 ixgbevf_hv_set_rlpml_vf(struct ixgbe_hw *hw, u16 max_size)

    Set the maximum receive packet length

    :param hw:
        pointer to the HW structure
    :type hw: struct ixgbe_hw \*

    :param max_size:
        value to assign to max frame size
        Hyper-V variant.
    :type max_size: u16

.. _`ixgbevf_negotiate_api_version_vf`:

ixgbevf_negotiate_api_version_vf
================================

.. c:function:: int ixgbevf_negotiate_api_version_vf(struct ixgbe_hw *hw, int api)

    Negotiate supported API version

    :param hw:
        pointer to the HW structure
    :type hw: struct ixgbe_hw \*

    :param api:
        integer containing requested API version
    :type api: int

.. _`ixgbevf_hv_negotiate_api_version_vf`:

ixgbevf_hv_negotiate_api_version_vf
===================================

.. c:function:: int ixgbevf_hv_negotiate_api_version_vf(struct ixgbe_hw *hw, int api)

    Negotiate supported API version

    :param hw:
        pointer to the HW structure
    :type hw: struct ixgbe_hw \*

    :param api:
        integer containing requested API version
        Hyper-V version - only ixgbe_mbox_api_10 supported.
    :type api: int

.. This file was automatic generated / don't edit.

