.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igb/e1000_mac.c

.. _`igb_get_bus_info_pcie`:

igb_get_bus_info_pcie
=====================

.. c:function:: s32 igb_get_bus_info_pcie(struct e1000_hw *hw)

    Get PCIe bus information

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_get_bus_info_pcie.description`:

Description
-----------

Determines and stores the system bus information for a particular
network interface.  The following bus information is determined and stored:
bus speed, bus width, type (PCIe), and PCIe function.

.. _`igb_clear_vfta`:

igb_clear_vfta
==============

.. c:function:: void igb_clear_vfta(struct e1000_hw *hw)

    Clear VLAN filter table

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_clear_vfta.description`:

Description
-----------

Clears the register array which contains the VLAN filter table by
setting all the values to 0.

.. _`igb_write_vfta`:

igb_write_vfta
==============

.. c:function:: void igb_write_vfta(struct e1000_hw *hw, u32 offset, u32 value)

    Write value to VLAN filter table

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        register offset in VLAN filter table
    :type offset: u32

    :param value:
        register value written to VLAN filter table
    :type value: u32

.. _`igb_write_vfta.description`:

Description
-----------

Writes value at the given offset in the register array which stores
the VLAN filter table.

.. _`igb_init_rx_addrs`:

igb_init_rx_addrs
=================

.. c:function:: void igb_init_rx_addrs(struct e1000_hw *hw, u16 rar_count)

    Initialize receive address's

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param rar_count:
        receive address registers
    :type rar_count: u16

.. _`igb_init_rx_addrs.description`:

Description
-----------

Setups the receive address registers by setting the base receive address
register to the devices MAC address and clearing all the other receive
address registers to 0.

.. _`igb_find_vlvf_slot`:

igb_find_vlvf_slot
==================

.. c:function:: s32 igb_find_vlvf_slot(struct e1000_hw *hw, u32 vlan, bool vlvf_bypass)

    find the VLAN id or the first empty slot

    :param hw:
        pointer to hardware structure
    :type hw: struct e1000_hw \*

    :param vlan:
        VLAN id to write to VLAN filter
    :type vlan: u32

    :param vlvf_bypass:
        skip VLVF if no match is found
    :type vlvf_bypass: bool

.. _`igb_find_vlvf_slot.description`:

Description
-----------

return the VLVF index where this VLAN id should be placed

.. _`igb_vfta_set`:

igb_vfta_set
============

.. c:function:: s32 igb_vfta_set(struct e1000_hw *hw, u32 vlan, u32 vind, bool vlan_on, bool vlvf_bypass)

    enable or disable vlan in VLAN filter table

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param vlan:
        VLAN id to add or remove
    :type vlan: u32

    :param vind:
        VMDq output index that maps queue to VLAN id
    :type vind: u32

    :param vlan_on:
        if true add filter, if false remove
    :type vlan_on: bool

    :param vlvf_bypass:
        *undescribed*
    :type vlvf_bypass: bool

.. _`igb_vfta_set.description`:

Description
-----------

Sets or clears a bit in the VLAN filter table array based on VLAN id
and if we are adding or removing the filter

.. _`igb_check_alt_mac_addr`:

igb_check_alt_mac_addr
======================

.. c:function:: s32 igb_check_alt_mac_addr(struct e1000_hw *hw)

    Check for alternate MAC addr

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_check_alt_mac_addr.description`:

Description
-----------

Checks the nvm for an alternate MAC address.  An alternate MAC address
can be setup by pre-boot software and must be treated like a permanent
address and must override the actual permanent MAC address.  If an
alternate MAC address is found it is saved in the hw struct and
programmed into RAR0 and the function returns success, otherwise the
function returns an error.

.. _`igb_rar_set`:

igb_rar_set
===========

.. c:function:: void igb_rar_set(struct e1000_hw *hw, u8 *addr, u32 index)

    Set receive address register

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param addr:
        pointer to the receive address
    :type addr: u8 \*

    :param index:
        receive address array register
    :type index: u32

.. _`igb_rar_set.description`:

Description
-----------

Sets the receive address array register at index to the address passed
in by addr.

.. _`igb_mta_set`:

igb_mta_set
===========

.. c:function:: void igb_mta_set(struct e1000_hw *hw, u32 hash_value)

    Set multicast filter table address

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param hash_value:
        determines the MTA register and bit to set
    :type hash_value: u32

.. _`igb_mta_set.description`:

Description
-----------

The multicast table address is a register array of 32-bit registers.
The hash_value is used to determine what register the bit is in, the
current value is read, the new bit is OR'd in and the new value is
written back into the register.

.. _`igb_hash_mc_addr`:

igb_hash_mc_addr
================

.. c:function:: u32 igb_hash_mc_addr(struct e1000_hw *hw, u8 *mc_addr)

    Generate a multicast hash value

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param mc_addr:
        pointer to a multicast address
    :type mc_addr: u8 \*

.. _`igb_hash_mc_addr.description`:

Description
-----------

Generates a multicast address hash value which is used to determine
the multicast filter table array address and new table value.  See
\ :c:func:`igb_mta_set`\ 

.. _`igb_update_mc_addr_list`:

igb_update_mc_addr_list
=======================

.. c:function:: void igb_update_mc_addr_list(struct e1000_hw *hw, u8 *mc_addr_list, u32 mc_addr_count)

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

.. _`igb_update_mc_addr_list.description`:

Description
-----------

Updates entire Multicast Table Array.
The caller must have a packed mc_addr_list of multicast addresses.

.. _`igb_clear_hw_cntrs_base`:

igb_clear_hw_cntrs_base
=======================

.. c:function:: void igb_clear_hw_cntrs_base(struct e1000_hw *hw)

    Clear base hardware counters

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_clear_hw_cntrs_base.description`:

Description
-----------

Clears the base hardware counters by reading the counter registers.

.. _`igb_check_for_copper_link`:

igb_check_for_copper_link
=========================

.. c:function:: s32 igb_check_for_copper_link(struct e1000_hw *hw)

    Check for link (Copper)

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_check_for_copper_link.description`:

Description
-----------

Checks to see of the link status of the hardware has changed.  If a
change in link status has been detected, then we read the PHY registers
to get the current speed/duplex if link exists.

.. _`igb_setup_link`:

igb_setup_link
==============

.. c:function:: s32 igb_setup_link(struct e1000_hw *hw)

    Setup flow control and link settings

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_setup_link.description`:

Description
-----------

Determines which flow control settings to use, then configures flow
control.  Calls the appropriate media-specific link configuration
function.  Assuming the adapter has a valid link partner, a valid link
should be established.  Assumes the hardware has previously been reset
and the transmitter and receiver are not enabled.

.. _`igb_config_collision_dist`:

igb_config_collision_dist
=========================

.. c:function:: void igb_config_collision_dist(struct e1000_hw *hw)

    Configure collision distance

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_config_collision_dist.description`:

Description
-----------

Configures the collision distance to the default value and is used
during link setup. Currently no func pointer exists and all
implementations are handled in the generic version of this function.

.. _`igb_set_fc_watermarks`:

igb_set_fc_watermarks
=====================

.. c:function:: s32 igb_set_fc_watermarks(struct e1000_hw *hw)

    Set flow control high/low watermarks

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_set_fc_watermarks.description`:

Description
-----------

Sets the flow control high/low threshold (watermark) registers.  If
flow control XON frame transmission is enabled, then set XON frame
tansmission as well.

.. _`igb_set_default_fc`:

igb_set_default_fc
==================

.. c:function:: s32 igb_set_default_fc(struct e1000_hw *hw)

    Set flow control default values

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_set_default_fc.description`:

Description
-----------

Read the EEPROM for the default values for flow control and store the
values.

.. _`igb_force_mac_fc`:

igb_force_mac_fc
================

.. c:function:: s32 igb_force_mac_fc(struct e1000_hw *hw)

    Force the MAC's flow control settings

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_force_mac_fc.description`:

Description
-----------

Force the MAC's flow control settings.  Sets the TFCE and RFCE bits in the
device control register to reflect the adapter settings.  TFCE and RFCE
need to be explicitly set by software when a copper PHY is used because
autonegotiation is managed by the PHY rather than the MAC.  Software must
also configure these bits when link is forced on a fiber connection.

.. _`igb_config_fc_after_link_up`:

igb_config_fc_after_link_up
===========================

.. c:function:: s32 igb_config_fc_after_link_up(struct e1000_hw *hw)

    Configures flow control after link

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_config_fc_after_link_up.description`:

Description
-----------

Checks the status of auto-negotiation after link up to ensure that the
speed and duplex were not forced.  If the link needed to be forced, then
flow control needs to be forced also.  If auto-negotiation is enabled
and did not fail, then we configure flow control based on our link
partner.

.. _`igb_get_speed_and_duplex_copper`:

igb_get_speed_and_duplex_copper
===============================

.. c:function:: s32 igb_get_speed_and_duplex_copper(struct e1000_hw *hw, u16 *speed, u16 *duplex)

    Retrieve current speed/duplex

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param speed:
        stores the current speed
    :type speed: u16 \*

    :param duplex:
        stores the current duplex
    :type duplex: u16 \*

.. _`igb_get_speed_and_duplex_copper.description`:

Description
-----------

Read the status register for the current speed/duplex and store the current
speed and duplex for copper connections.

.. _`igb_get_hw_semaphore`:

igb_get_hw_semaphore
====================

.. c:function:: s32 igb_get_hw_semaphore(struct e1000_hw *hw)

    Acquire hardware semaphore

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_get_hw_semaphore.description`:

Description
-----------

Acquire the HW semaphore to access the PHY or NVM

.. _`igb_put_hw_semaphore`:

igb_put_hw_semaphore
====================

.. c:function:: void igb_put_hw_semaphore(struct e1000_hw *hw)

    Release hardware semaphore

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_put_hw_semaphore.description`:

Description
-----------

Release hardware semaphore used to access the PHY or NVM

.. _`igb_get_auto_rd_done`:

igb_get_auto_rd_done
====================

.. c:function:: s32 igb_get_auto_rd_done(struct e1000_hw *hw)

    Check for auto read completion

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_get_auto_rd_done.description`:

Description
-----------

Check EEPROM for Auto Read done bit.

.. _`igb_valid_led_default`:

igb_valid_led_default
=====================

.. c:function:: s32 igb_valid_led_default(struct e1000_hw *hw, u16 *data)

    Verify a valid default LED config

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param data:
        pointer to the NVM (EEPROM)
    :type data: u16 \*

.. _`igb_valid_led_default.description`:

Description
-----------

Read the EEPROM for the current default LED configuration.  If the
LED configuration is not valid, set to a valid LED configuration.

.. _`igb_id_led_init`:

igb_id_led_init
===============

.. c:function:: s32 igb_id_led_init(struct e1000_hw *hw)

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_cleanup_led`:

igb_cleanup_led
===============

.. c:function:: s32 igb_cleanup_led(struct e1000_hw *hw)

    Set LED config to default operation

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_cleanup_led.description`:

Description
-----------

Remove the current LED configuration and set the LED configuration
to the default value, saved from the EEPROM.

.. _`igb_blink_led`:

igb_blink_led
=============

.. c:function:: s32 igb_blink_led(struct e1000_hw *hw)

    Blink LED

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_blink_led.description`:

Description
-----------

Blink the led's which are set to be on.

.. _`igb_led_off`:

igb_led_off
===========

.. c:function:: s32 igb_led_off(struct e1000_hw *hw)

    Turn LED off

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_led_off.description`:

Description
-----------

Turn LED off.

.. _`igb_disable_pcie_master`:

igb_disable_pcie_master
=======================

.. c:function:: s32 igb_disable_pcie_master(struct e1000_hw *hw)

    Disables PCI-express master access

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_disable_pcie_master.description`:

Description
-----------

Returns 0 (0) if successful, else returns -10
(-E1000_ERR_MASTER_REQUESTS_PENDING) if master disable bit has not caused
the master requests to be disabled.

Disables PCI-Express master access and verifies there are no pending
requests.

.. _`igb_validate_mdi_setting`:

igb_validate_mdi_setting
========================

.. c:function:: s32 igb_validate_mdi_setting(struct e1000_hw *hw)

    Verify MDI/MDIx settings

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_validate_mdi_setting.description`:

Description
-----------

Verify that when not using auto-negotitation that MDI/MDIx is correctly
set, which is forced to MDI mode only.

.. _`igb_write_8bit_ctrl_reg`:

igb_write_8bit_ctrl_reg
=======================

.. c:function:: s32 igb_write_8bit_ctrl_reg(struct e1000_hw *hw, u32 reg, u32 offset, u8 data)

    Write a 8bit CTRL register

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param reg:
        32bit register offset such as E1000_SCTL
    :type reg: u32

    :param offset:
        register offset to write to
    :type offset: u32

    :param data:
        data to write at register offset
    :type data: u8

.. _`igb_write_8bit_ctrl_reg.description`:

Description
-----------

Writes an address/data control type register.  There are several of these
and they all have the format address << 8 \| data and bit 31 is polled for
completion.

.. _`igb_enable_mng_pass_thru`:

igb_enable_mng_pass_thru
========================

.. c:function:: bool igb_enable_mng_pass_thru(struct e1000_hw *hw)

    Enable processing of ARP's

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`igb_enable_mng_pass_thru.description`:

Description
-----------

Verifies the hardware needs to leave interface enabled so that frames can
be directed to and from the management interface.

.. This file was automatic generated / don't edit.

