.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/e1000e/mac.c

.. _`e1000e_get_bus_info_pcie`:

e1000e_get_bus_info_pcie
========================

.. c:function:: s32 e1000e_get_bus_info_pcie(struct e1000_hw *hw)

    Get PCIe bus information

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_get_bus_info_pcie.description`:

Description
-----------

Determines and stores the system bus information for a particular
network interface.  The following bus information is determined and stored:
bus speed, bus width, type (PCIe), and PCIe function.

.. _`e1000_set_lan_id_multi_port_pcie`:

e1000_set_lan_id_multi_port_pcie
================================

.. c:function:: void e1000_set_lan_id_multi_port_pcie(struct e1000_hw *hw)

    Set LAN id for PCIe multiple port devices

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_set_lan_id_multi_port_pcie.description`:

Description
-----------

Determines the LAN function id by reading memory-mapped registers
and swaps the port value if requested.

.. _`e1000_set_lan_id_single_port`:

e1000_set_lan_id_single_port
============================

.. c:function:: void e1000_set_lan_id_single_port(struct e1000_hw *hw)

    Set LAN id for a single port device

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_set_lan_id_single_port.description`:

Description
-----------

Sets the LAN function id to zero for a single port device.

.. _`e1000_clear_vfta_generic`:

e1000_clear_vfta_generic
========================

.. c:function:: void e1000_clear_vfta_generic(struct e1000_hw *hw)

    Clear VLAN filter table

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_clear_vfta_generic.description`:

Description
-----------

Clears the register array which contains the VLAN filter table by
setting all the values to 0.

.. _`e1000_write_vfta_generic`:

e1000_write_vfta_generic
========================

.. c:function:: void e1000_write_vfta_generic(struct e1000_hw *hw, u32 offset, u32 value)

    Write value to VLAN filter table

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset in VLAN filter table

    :param u32 value:
        register value written to VLAN filter table

.. _`e1000_write_vfta_generic.description`:

Description
-----------

Writes value at the given offset in the register array which stores
the VLAN filter table.

.. _`e1000e_init_rx_addrs`:

e1000e_init_rx_addrs
====================

.. c:function:: void e1000e_init_rx_addrs(struct e1000_hw *hw, u16 rar_count)

    Initialize receive address's

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 rar_count:
        receive address registers

.. _`e1000e_init_rx_addrs.description`:

Description
-----------

Setup the receive address registers by setting the base receive address
register to the devices MAC address and clearing all the other receive
address registers to 0.

.. _`e1000_check_alt_mac_addr_generic`:

e1000_check_alt_mac_addr_generic
================================

.. c:function:: s32 e1000_check_alt_mac_addr_generic(struct e1000_hw *hw)

    Check for alternate MAC addr

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_check_alt_mac_addr_generic.description`:

Description
-----------

Checks the nvm for an alternate MAC address.  An alternate MAC address
can be setup by pre-boot software and must be treated like a permanent
address and must override the actual permanent MAC address. If an
alternate MAC address is found it is programmed into RAR0, replacing
the permanent address that was installed into RAR0 by the Si on reset.
This function will return SUCCESS unless it encounters an error while
reading the EEPROM.

.. _`e1000e_rar_set_generic`:

e1000e_rar_set_generic
======================

.. c:function:: int e1000e_rar_set_generic(struct e1000_hw *hw, u8 *addr, u32 index)

    Set receive address register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u8 \*addr:
        pointer to the receive address

    :param u32 index:
        receive address array register

.. _`e1000e_rar_set_generic.description`:

Description
-----------

Sets the receive address array register at index to the address passed
in by addr.

.. _`e1000_hash_mc_addr`:

e1000_hash_mc_addr
==================

.. c:function:: u32 e1000_hash_mc_addr(struct e1000_hw *hw, u8 *mc_addr)

    Generate a multicast hash value

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u8 \*mc_addr:
        pointer to a multicast address

.. _`e1000_hash_mc_addr.description`:

Description
-----------

Generates a multicast address hash value which is used to determine
the multicast filter table array address and new table value.

.. _`e1000e_update_mc_addr_list_generic`:

e1000e_update_mc_addr_list_generic
==================================

.. c:function:: void e1000e_update_mc_addr_list_generic(struct e1000_hw *hw, u8 *mc_addr_list, u32 mc_addr_count)

    Update Multicast addresses

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u8 \*mc_addr_list:
        array of multicast addresses to program

    :param u32 mc_addr_count:
        number of multicast addresses to program

.. _`e1000e_update_mc_addr_list_generic.description`:

Description
-----------

Updates entire Multicast Table Array.
The caller must have a packed mc_addr_list of multicast addresses.

.. _`e1000e_clear_hw_cntrs_base`:

e1000e_clear_hw_cntrs_base
==========================

.. c:function:: void e1000e_clear_hw_cntrs_base(struct e1000_hw *hw)

    Clear base hardware counters

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_clear_hw_cntrs_base.description`:

Description
-----------

Clears the base hardware counters by reading the counter registers.

.. _`e1000e_check_for_copper_link`:

e1000e_check_for_copper_link
============================

.. c:function:: s32 e1000e_check_for_copper_link(struct e1000_hw *hw)

    Check for link (Copper)

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_check_for_copper_link.description`:

Description
-----------

Checks to see of the link status of the hardware has changed.  If a
change in link status has been detected, then we read the PHY registers
to get the current speed/duplex if link exists.

Returns a negative error code (-E1000_ERR\_\*) or 0 (link down) or 1 (link
up).

.. _`e1000e_check_for_fiber_link`:

e1000e_check_for_fiber_link
===========================

.. c:function:: s32 e1000e_check_for_fiber_link(struct e1000_hw *hw)

    Check for link (Fiber)

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_check_for_fiber_link.description`:

Description
-----------

Checks for link up on the hardware.  If link is not up and we have
a signal, then we need to force link up.

.. _`e1000e_check_for_serdes_link`:

e1000e_check_for_serdes_link
============================

.. c:function:: s32 e1000e_check_for_serdes_link(struct e1000_hw *hw)

    Check for link (Serdes)

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_check_for_serdes_link.description`:

Description
-----------

Checks for link up on the hardware.  If link is not up and we have
a signal, then we need to force link up.

.. _`e1000_set_default_fc_generic`:

e1000_set_default_fc_generic
============================

.. c:function:: s32 e1000_set_default_fc_generic(struct e1000_hw *hw)

    Set flow control default values

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_set_default_fc_generic.description`:

Description
-----------

Read the EEPROM for the default values for flow control and store the
values.

.. _`e1000e_setup_link_generic`:

e1000e_setup_link_generic
=========================

.. c:function:: s32 e1000e_setup_link_generic(struct e1000_hw *hw)

    Setup flow control and link settings

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_setup_link_generic.description`:

Description
-----------

Determines which flow control settings to use, then configures flow
control.  Calls the appropriate media-specific link configuration
function.  Assuming the adapter has a valid link partner, a valid link
should be established.  Assumes the hardware has previously been reset
and the transmitter and receiver are not enabled.

.. _`e1000_commit_fc_settings_generic`:

e1000_commit_fc_settings_generic
================================

.. c:function:: s32 e1000_commit_fc_settings_generic(struct e1000_hw *hw)

    Configure flow control

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_commit_fc_settings_generic.description`:

Description
-----------

Write the flow control settings to the Transmit Config Word Register (TXCW)
base on the flow control settings in e1000_mac_info.

.. _`e1000_poll_fiber_serdes_link_generic`:

e1000_poll_fiber_serdes_link_generic
====================================

.. c:function:: s32 e1000_poll_fiber_serdes_link_generic(struct e1000_hw *hw)

    Poll for link up

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_poll_fiber_serdes_link_generic.description`:

Description
-----------

Polls for link up by reading the status register, if link fails to come
up with auto-negotiation, then the link is forced if a signal is detected.

.. _`e1000e_setup_fiber_serdes_link`:

e1000e_setup_fiber_serdes_link
==============================

.. c:function:: s32 e1000e_setup_fiber_serdes_link(struct e1000_hw *hw)

    Setup link for fiber/serdes

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_setup_fiber_serdes_link.description`:

Description
-----------

Configures collision distance and flow control for fiber and serdes
links.  Upon successful setup, poll for link.

.. _`e1000e_config_collision_dist_generic`:

e1000e_config_collision_dist_generic
====================================

.. c:function:: void e1000e_config_collision_dist_generic(struct e1000_hw *hw)

    Configure collision distance

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_config_collision_dist_generic.description`:

Description
-----------

Configures the collision distance to the default value and is used
during link setup.

.. _`e1000e_set_fc_watermarks`:

e1000e_set_fc_watermarks
========================

.. c:function:: s32 e1000e_set_fc_watermarks(struct e1000_hw *hw)

    Set flow control high/low watermarks

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_set_fc_watermarks.description`:

Description
-----------

Sets the flow control high/low threshold (watermark) registers.  If
flow control XON frame transmission is enabled, then set XON frame
transmission as well.

.. _`e1000e_force_mac_fc`:

e1000e_force_mac_fc
===================

.. c:function:: s32 e1000e_force_mac_fc(struct e1000_hw *hw)

    Force the MAC's flow control settings

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_force_mac_fc.description`:

Description
-----------

Force the MAC's flow control settings.  Sets the TFCE and RFCE bits in the
device control register to reflect the adapter settings.  TFCE and RFCE
need to be explicitly set by software when a copper PHY is used because
autonegotiation is managed by the PHY rather than the MAC.  Software must
also configure these bits when link is forced on a fiber connection.

.. _`e1000e_config_fc_after_link_up`:

e1000e_config_fc_after_link_up
==============================

.. c:function:: s32 e1000e_config_fc_after_link_up(struct e1000_hw *hw)

    Configures flow control after link

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_config_fc_after_link_up.description`:

Description
-----------

Checks the status of auto-negotiation after link up to ensure that the
speed and duplex were not forced.  If the link needed to be forced, then
flow control needs to be forced also.  If auto-negotiation is enabled
and did not fail, then we configure flow control based on our link
partner.

.. _`e1000e_get_speed_and_duplex_copper`:

e1000e_get_speed_and_duplex_copper
==================================

.. c:function:: s32 e1000e_get_speed_and_duplex_copper(struct e1000_hw *hw, u16 *speed, u16 *duplex)

    Retrieve current speed/duplex

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 \*speed:
        stores the current speed

    :param u16 \*duplex:
        stores the current duplex

.. _`e1000e_get_speed_and_duplex_copper.description`:

Description
-----------

Read the status register for the current speed/duplex and store the current
speed and duplex for copper connections.

.. _`e1000e_get_speed_and_duplex_fiber_serdes`:

e1000e_get_speed_and_duplex_fiber_serdes
========================================

.. c:function:: s32 e1000e_get_speed_and_duplex_fiber_serdes(struct e1000_hw __always_unused *hw, u16 *speed, u16 *duplex)

    Retrieve current speed/duplex

    :param struct e1000_hw __always_unused \*hw:
        pointer to the HW structure

    :param u16 \*speed:
        stores the current speed

    :param u16 \*duplex:
        stores the current duplex

.. _`e1000e_get_speed_and_duplex_fiber_serdes.description`:

Description
-----------

Sets the speed and duplex to gigabit full duplex (the only possible option)
for fiber/serdes links.

.. _`e1000e_get_hw_semaphore`:

e1000e_get_hw_semaphore
=======================

.. c:function:: s32 e1000e_get_hw_semaphore(struct e1000_hw *hw)

    Acquire hardware semaphore

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_get_hw_semaphore.description`:

Description
-----------

Acquire the HW semaphore to access the PHY or NVM

.. _`e1000e_put_hw_semaphore`:

e1000e_put_hw_semaphore
=======================

.. c:function:: void e1000e_put_hw_semaphore(struct e1000_hw *hw)

    Release hardware semaphore

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_put_hw_semaphore.description`:

Description
-----------

Release hardware semaphore used to access the PHY or NVM

.. _`e1000e_get_auto_rd_done`:

e1000e_get_auto_rd_done
=======================

.. c:function:: s32 e1000e_get_auto_rd_done(struct e1000_hw *hw)

    Check for auto read completion

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_get_auto_rd_done.description`:

Description
-----------

Check EEPROM for Auto Read done bit.

.. _`e1000e_valid_led_default`:

e1000e_valid_led_default
========================

.. c:function:: s32 e1000e_valid_led_default(struct e1000_hw *hw, u16 *data)

    Verify a valid default LED config

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 \*data:
        pointer to the NVM (EEPROM)

.. _`e1000e_valid_led_default.description`:

Description
-----------

Read the EEPROM for the current default LED configuration.  If the
LED configuration is not valid, set to a valid LED configuration.

.. _`e1000e_id_led_init_generic`:

e1000e_id_led_init_generic
==========================

.. c:function:: s32 e1000e_id_led_init_generic(struct e1000_hw *hw)

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_setup_led_generic`:

e1000e_setup_led_generic
========================

.. c:function:: s32 e1000e_setup_led_generic(struct e1000_hw *hw)

    Configures SW controllable LED

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_setup_led_generic.description`:

Description
-----------

This prepares the SW controllable LED for use and saves the current state
of the LED so it can be later restored.

.. _`e1000e_cleanup_led_generic`:

e1000e_cleanup_led_generic
==========================

.. c:function:: s32 e1000e_cleanup_led_generic(struct e1000_hw *hw)

    Set LED config to default operation

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_cleanup_led_generic.description`:

Description
-----------

Remove the current LED configuration and set the LED configuration
to the default value, saved from the EEPROM.

.. _`e1000e_blink_led_generic`:

e1000e_blink_led_generic
========================

.. c:function:: s32 e1000e_blink_led_generic(struct e1000_hw *hw)

    Blink LED

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_blink_led_generic.description`:

Description
-----------

Blink the LEDs which are set to be on.

.. _`e1000e_led_on_generic`:

e1000e_led_on_generic
=====================

.. c:function:: s32 e1000e_led_on_generic(struct e1000_hw *hw)

    Turn LED on

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_led_on_generic.description`:

Description
-----------

Turn LED on.

.. _`e1000e_led_off_generic`:

e1000e_led_off_generic
======================

.. c:function:: s32 e1000e_led_off_generic(struct e1000_hw *hw)

    Turn LED off

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_led_off_generic.description`:

Description
-----------

Turn LED off.

.. _`e1000e_set_pcie_no_snoop`:

e1000e_set_pcie_no_snoop
========================

.. c:function:: void e1000e_set_pcie_no_snoop(struct e1000_hw *hw, u32 no_snoop)

    Set PCI-express capabilities

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 no_snoop:
        bitmap of snoop events

.. _`e1000e_set_pcie_no_snoop.description`:

Description
-----------

Set the PCI-express register to snoop for events enabled in 'no_snoop'.

.. _`e1000e_disable_pcie_master`:

e1000e_disable_pcie_master
==========================

.. c:function:: s32 e1000e_disable_pcie_master(struct e1000_hw *hw)

    Disables PCI-express master access

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_disable_pcie_master.description`:

Description
-----------

Returns 0 if successful, else returns -10
(-E1000_ERR_MASTER_REQUESTS_PENDING) if master disable bit has not caused
the master requests to be disabled.

Disables PCI-Express master access and verifies there are no pending
requests.

.. _`e1000e_reset_adaptive`:

e1000e_reset_adaptive
=====================

.. c:function:: void e1000e_reset_adaptive(struct e1000_hw *hw)

    Reset Adaptive Interframe Spacing

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_reset_adaptive.description`:

Description
-----------

Reset the Adaptive Interframe Spacing throttle to default values.

.. _`e1000e_update_adaptive`:

e1000e_update_adaptive
======================

.. c:function:: void e1000e_update_adaptive(struct e1000_hw *hw)

    Update Adaptive Interframe Spacing

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_update_adaptive.description`:

Description
-----------

Update the Adaptive Interframe Spacing Throttle value based on the
time between transmitted packets and time between collisions.

.. This file was automatic generated / don't edit.

