.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igbvf/vf.c

.. _`e1000_init_mac_params_vf`:

e1000_init_mac_params_vf
========================

.. c:function:: s32 e1000_init_mac_params_vf(struct e1000_hw *hw)

    Inits MAC params

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_init_function_pointers_vf`:

e1000_init_function_pointers_vf
===============================

.. c:function:: void e1000_init_function_pointers_vf(struct e1000_hw *hw)

    Inits function pointers

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_get_link_up_info_vf`:

e1000_get_link_up_info_vf
=========================

.. c:function:: s32 e1000_get_link_up_info_vf(struct e1000_hw *hw, u16 *speed, u16 *duplex)

    Gets link info.

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 \*speed:
        pointer to 16 bit value to store link speed.

    :param u16 \*duplex:
        pointer to 16 bit value to store duplex.

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

    :param struct e1000_hw \*hw:
        pointer to the HW structure

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

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_init_hw_vf.description`:

Description
-----------

Not much to do here except clear the PF Reset indication if there is one.

.. _`e1000_hash_mc_addr_vf`:

e1000_hash_mc_addr_vf
=====================

.. c:function:: u32 e1000_hash_mc_addr_vf(struct e1000_hw *hw, u8 *mc_addr)

    Generate a multicast hash value

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u8 \*mc_addr:
        pointer to a multicast address

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

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u8 \*mc_addr_list:
        array of multicast addresses to program

    :param u32 mc_addr_count:
        number of multicast addresses to program

    :param u32 rar_used_count:
        the first RAR register free to program

    :param u32 rar_count:
        total number of supported Receive Address Registers

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

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 vid:
        determines the vfta register and bit to set/unset

    :param bool set:
        if true then set bit, else clear bit

.. _`e1000_rlpml_set_vf`:

e1000_rlpml_set_vf
==================

.. c:function:: void e1000_rlpml_set_vf(struct e1000_hw *hw, u16 max_size)

    Set the maximum receive packet length

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 max_size:
        value to assign to max frame size

.. _`e1000_rar_set_vf`:

e1000_rar_set_vf
================

.. c:function:: void e1000_rar_set_vf(struct e1000_hw *hw, u8 *addr, u32 index)

    set device MAC address

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u8 \*addr:
        pointer to the receive address

    :param u32 index:
        receive address array register

.. _`e1000_read_mac_addr_vf`:

e1000_read_mac_addr_vf
======================

.. c:function:: s32 e1000_read_mac_addr_vf(struct e1000_hw *hw)

    Read device MAC address

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_set_uc_addr_vf`:

e1000_set_uc_addr_vf
====================

.. c:function:: s32 e1000_set_uc_addr_vf(struct e1000_hw *hw, u32 sub_cmd, u8 *addr)

    Set or clear unicast filters

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 sub_cmd:
        add or clear filters

    :param u8 \*addr:
        pointer to the filter MAC address

.. _`e1000_check_for_link_vf`:

e1000_check_for_link_vf
=======================

.. c:function:: s32 e1000_check_for_link_vf(struct e1000_hw *hw)

    Check for link for a virtual interface

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_check_for_link_vf.description`:

Description
-----------

Checks to see if the underlying PF is still talking to the VF and
if it is then it reports the link state to the hardware, otherwise
it reports link down and returns an error.

.. This file was automatic generated / don't edit.

