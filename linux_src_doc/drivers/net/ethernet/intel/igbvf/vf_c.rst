.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igbvf/vf.c

.. _`e1000_init_mac_params_vf`:

e1000_init_mac_params_vf
========================

.. c:function:: s32 e1000_init_mac_params_vf(struct e1000_hw *hw)

    Inits MAC params

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_init_function_pointers_vf`:

e1000_init_function_pointers_vf
===============================

.. c:function:: void e1000_init_function_pointers_vf(struct e1000_hw *hw)

    Inits function pointers

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_get_link_up_info_vf`:

e1000_get_link_up_info_vf
=========================

.. c:function:: s32 e1000_get_link_up_info_vf(struct e1000_hw *hw, u16 *speed, u16 *duplex)

    Gets link info.

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param speed:
        pointer to 16 bit value to store link speed.
    :type speed: u16 \*

    :param duplex:
        pointer to 16 bit value to store duplex.
    :type duplex: u16 \*

.. _`e1000_get_link_up_info_vf.description`:

Description
-----------

Since we cannot read the PHY and get accurate link info, we must rely upon
the status register's data which is often stale and inaccurate.

.. _`e1000_reset_hw_vf`:

e1000_reset_hw_vf
=================

.. c:function:: s32 e1000_reset_hw_vf(struct e1000_hw *hw)

    Resets the HW

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_reset_hw_vf.description`:

Description
-----------

VF's provide a function level reset. This is done using bit 26 of ctrl_reg.
This is all the reset we can perform on a VF.

.. _`e1000_init_hw_vf`:

e1000_init_hw_vf
================

.. c:function:: s32 e1000_init_hw_vf(struct e1000_hw *hw)

    Inits the HW

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_init_hw_vf.description`:

Description
-----------

Not much to do here except clear the PF Reset indication if there is one.

.. _`e1000_hash_mc_addr_vf`:

e1000_hash_mc_addr_vf
=====================

.. c:function:: u32 e1000_hash_mc_addr_vf(struct e1000_hw *hw, u8 *mc_addr)

    Generate a multicast hash value

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param mc_addr:
        pointer to a multicast address
    :type mc_addr: u8 \*

.. _`e1000_hash_mc_addr_vf.description`:

Description
-----------

Generates a multicast address hash value which is used to determine
the multicast filter table array address and new table value.  See
\ :c:func:`e1000_mta_set_generic`\ 

.. _`e1000_update_mc_addr_list_vf`:

e1000_update_mc_addr_list_vf
============================

.. c:function:: void e1000_update_mc_addr_list_vf(struct e1000_hw *hw, u8 *mc_addr_list, u32 mc_addr_count, u32 rar_used_count, u32 rar_count)

    Update Multicast addresses

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param mc_addr_list:
        array of multicast addresses to program
    :type mc_addr_list: u8 \*

    :param mc_addr_count:
        number of multicast addresses to program
    :type mc_addr_count: u32

    :param rar_used_count:
        the first RAR register free to program
    :type rar_used_count: u32

    :param rar_count:
        total number of supported Receive Address Registers
    :type rar_count: u32

.. _`e1000_update_mc_addr_list_vf.description`:

Description
-----------

Updates the Receive Address Registers and Multicast Table Array.
The caller must have a packed mc_addr_list of multicast addresses.
The parameter rar_count will usually be hw->mac.rar_entry_count
unless there are workarounds that change this.

.. _`e1000_set_vfta_vf`:

e1000_set_vfta_vf
=================

.. c:function:: s32 e1000_set_vfta_vf(struct e1000_hw *hw, u16 vid, bool set)

    Set/Unset vlan filter table address

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param vid:
        determines the vfta register and bit to set/unset
    :type vid: u16

    :param set:
        if true then set bit, else clear bit
    :type set: bool

.. _`e1000_rlpml_set_vf`:

e1000_rlpml_set_vf
==================

.. c:function:: void e1000_rlpml_set_vf(struct e1000_hw *hw, u16 max_size)

    Set the maximum receive packet length

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param max_size:
        value to assign to max frame size
    :type max_size: u16

.. _`e1000_rar_set_vf`:

e1000_rar_set_vf
================

.. c:function:: void e1000_rar_set_vf(struct e1000_hw *hw, u8 *addr, u32 index)

    set device MAC address

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param addr:
        pointer to the receive address
    :type addr: u8 \*

    :param index:
        receive address array register
    :type index: u32

.. _`e1000_read_mac_addr_vf`:

e1000_read_mac_addr_vf
======================

.. c:function:: s32 e1000_read_mac_addr_vf(struct e1000_hw *hw)

    Read device MAC address

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_set_uc_addr_vf`:

e1000_set_uc_addr_vf
====================

.. c:function:: s32 e1000_set_uc_addr_vf(struct e1000_hw *hw, u32 sub_cmd, u8 *addr)

    Set or clear unicast filters

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param sub_cmd:
        add or clear filters
    :type sub_cmd: u32

    :param addr:
        pointer to the filter MAC address
    :type addr: u8 \*

.. _`e1000_check_for_link_vf`:

e1000_check_for_link_vf
=======================

.. c:function:: s32 e1000_check_for_link_vf(struct e1000_hw *hw)

    Check for link for a virtual interface

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_check_for_link_vf.description`:

Description
-----------

Checks to see if the underlying PF is still talking to the VF and
if it is then it reports the link state to the hardware, otherwise
it reports link down and returns an error.

.. This file was automatic generated / don't edit.

