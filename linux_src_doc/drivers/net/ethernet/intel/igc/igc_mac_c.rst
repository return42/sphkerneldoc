.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igc/igc_mac.c

.. _`igc_disable_pcie_master`:

igc_disable_pcie_master
=======================

.. c:function:: s32 igc_disable_pcie_master(struct igc_hw *hw)

    Disables PCI-express master access

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_disable_pcie_master.description`:

Description
-----------

Returns 0 (0) if successful, else returns -10
(-IGC_ERR_MASTER_REQUESTS_PENDING) if master disable bit has not caused
the master requests to be disabled.

Disables PCI-Express master access and verifies there are no pending
requests.

.. _`igc_init_rx_addrs`:

igc_init_rx_addrs
=================

.. c:function:: void igc_init_rx_addrs(struct igc_hw *hw, u16 rar_count)

    Initialize receive addresses

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param rar_count:
        receive address registers
    :type rar_count: u16

.. _`igc_init_rx_addrs.description`:

Description
-----------

Setup the receive address registers by setting the base receive address
register to the devices MAC address and clearing all the other receive
address registers to 0.

.. _`igc_setup_link`:

igc_setup_link
==============

.. c:function:: s32 igc_setup_link(struct igc_hw *hw)

    Setup flow control and link settings

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_setup_link.description`:

Description
-----------

Determines which flow control settings to use, then configures flow
control.  Calls the appropriate media-specific link configuration
function.  Assuming the adapter has a valid link partner, a valid link
should be established.  Assumes the hardware has previously been reset
and the transmitter and receiver are not enabled.

.. _`igc_set_default_fc`:

igc_set_default_fc
==================

.. c:function:: s32 igc_set_default_fc(struct igc_hw *hw)

    Set flow control default values

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_set_default_fc.description`:

Description
-----------

Read the EEPROM for the default values for flow control and store the
values.

.. _`igc_force_mac_fc`:

igc_force_mac_fc
================

.. c:function:: s32 igc_force_mac_fc(struct igc_hw *hw)

    Force the MAC's flow control settings

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_force_mac_fc.description`:

Description
-----------

Force the MAC's flow control settings.  Sets the TFCE and RFCE bits in the
device control register to reflect the adapter settings.  TFCE and RFCE
need to be explicitly set by software when a copper PHY is used because
autonegotiation is managed by the PHY rather than the MAC.  Software must
also configure these bits when link is forced on a fiber connection.

.. _`igc_set_fc_watermarks`:

igc_set_fc_watermarks
=====================

.. c:function:: s32 igc_set_fc_watermarks(struct igc_hw *hw)

    Set flow control high/low watermarks

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_set_fc_watermarks.description`:

Description
-----------

Sets the flow control high/low threshold (watermark) registers.  If
flow control XON frame transmission is enabled, then set XON frame
transmission as well.

.. _`igc_clear_hw_cntrs_base`:

igc_clear_hw_cntrs_base
=======================

.. c:function:: void igc_clear_hw_cntrs_base(struct igc_hw *hw)

    Clear base hardware counters

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_clear_hw_cntrs_base.description`:

Description
-----------

Clears the base hardware counters by reading the counter registers.

.. _`igc_rar_set`:

igc_rar_set
===========

.. c:function:: void igc_rar_set(struct igc_hw *hw, u8 *addr, u32 index)

    Set receive address register

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param addr:
        pointer to the receive address
    :type addr: u8 \*

    :param index:
        receive address array register
    :type index: u32

.. _`igc_rar_set.description`:

Description
-----------

Sets the receive address array register at index to the address passed
in by addr.

.. _`igc_check_for_copper_link`:

igc_check_for_copper_link
=========================

.. c:function:: s32 igc_check_for_copper_link(struct igc_hw *hw)

    Check for link (Copper)

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_check_for_copper_link.description`:

Description
-----------

Checks to see of the link status of the hardware has changed.  If a
change in link status has been detected, then we read the PHY registers
to get the current speed/duplex if link exists.

.. _`igc_config_collision_dist`:

igc_config_collision_dist
=========================

.. c:function:: void igc_config_collision_dist(struct igc_hw *hw)

    Configure collision distance

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_config_collision_dist.description`:

Description
-----------

Configures the collision distance to the default value and is used
during link setup. Currently no func pointer exists and all
implementations are handled in the generic version of this function.

.. _`igc_config_fc_after_link_up`:

igc_config_fc_after_link_up
===========================

.. c:function:: s32 igc_config_fc_after_link_up(struct igc_hw *hw)

    Configures flow control after link

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_config_fc_after_link_up.description`:

Description
-----------

Checks the status of auto-negotiation after link up to ensure that the
speed and duplex were not forced.  If the link needed to be forced, then
flow control needs to be forced also.  If auto-negotiation is enabled
and did not fail, then we configure flow control based on our link
partner.

.. _`igc_get_auto_rd_done`:

igc_get_auto_rd_done
====================

.. c:function:: s32 igc_get_auto_rd_done(struct igc_hw *hw)

    Check for auto read completion

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_get_auto_rd_done.description`:

Description
-----------

Check EEPROM for Auto Read done bit.

.. _`igc_get_speed_and_duplex_copper`:

igc_get_speed_and_duplex_copper
===============================

.. c:function:: s32 igc_get_speed_and_duplex_copper(struct igc_hw *hw, u16 *speed, u16 *duplex)

    Retrieve current speed/duplex

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param speed:
        stores the current speed
    :type speed: u16 \*

    :param duplex:
        stores the current duplex
    :type duplex: u16 \*

.. _`igc_get_speed_and_duplex_copper.description`:

Description
-----------

Read the status register for the current speed/duplex and store the current
speed and duplex for copper connections.

.. _`igc_put_hw_semaphore`:

igc_put_hw_semaphore
====================

.. c:function:: void igc_put_hw_semaphore(struct igc_hw *hw)

    Release hardware semaphore

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_put_hw_semaphore.description`:

Description
-----------

Release hardware semaphore used to access the PHY or NVM

.. _`igc_enable_mng_pass_thru`:

igc_enable_mng_pass_thru
========================

.. c:function:: bool igc_enable_mng_pass_thru(struct igc_hw *hw)

    Enable processing of ARP's

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_enable_mng_pass_thru.description`:

Description
-----------

Verifies the hardware needs to leave interface enabled so that frames can
be directed to and from the management interface.

.. This file was automatic generated / don't edit.

