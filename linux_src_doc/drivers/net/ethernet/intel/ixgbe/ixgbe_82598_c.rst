.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_82598.c

.. _`ixgbe_set_pcie_completion_timeout`:

ixgbe_set_pcie_completion_timeout
=================================

.. c:function:: void ixgbe_set_pcie_completion_timeout(struct ixgbe_hw *hw)

    set pci-e completion timeout

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

.. _`ixgbe_set_pcie_completion_timeout.description`:

Description
-----------

The defaults for 82598 should be in the range of 50us to 50ms,
however the hardware default for these parts is 500us to 1ms which is less
than the 10ms recommended by the pci-e spec.  To address this we need to
increase the value to either 10ms to 250ms for capability version 1 config,
or 16ms to 55ms for version 2.

.. _`ixgbe_init_phy_ops_82598`:

ixgbe_init_phy_ops_82598
========================

.. c:function:: s32 ixgbe_init_phy_ops_82598(struct ixgbe_hw *hw)

    PHY/SFP specific init

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_init_phy_ops_82598.description`:

Description
-----------

Initialize any function pointers that were not able to be
set during get_invariants because the PHY/SFP type was
not known.  Perform the SFP init if necessary.

.. _`ixgbe_start_hw_82598`:

ixgbe_start_hw_82598
====================

.. c:function:: s32 ixgbe_start_hw_82598(struct ixgbe_hw *hw)

    Prepare hardware for Tx/Rx

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_start_hw_82598.description`:

Description
-----------

Starts the hardware using the generic start_hw function.
Disables relaxed ordering for archs other than SPARC
Then set pcie completion timeout

.. _`ixgbe_get_link_capabilities_82598`:

ixgbe_get_link_capabilities_82598
=================================

.. c:function:: s32 ixgbe_get_link_capabilities_82598(struct ixgbe_hw *hw, ixgbe_link_speed *speed, bool *autoneg)

    Determines link capabilities

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param ixgbe_link_speed \*speed:
        pointer to link speed

    :param bool \*autoneg:
        boolean auto-negotiation value

.. _`ixgbe_get_link_capabilities_82598.description`:

Description
-----------

Determines the link capabilities by reading the AUTOC register.

.. _`ixgbe_get_media_type_82598`:

ixgbe_get_media_type_82598
==========================

.. c:function:: enum ixgbe_media_type ixgbe_get_media_type_82598(struct ixgbe_hw *hw)

    Determines media type

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_get_media_type_82598.description`:

Description
-----------

Returns the media type (fiber, copper, backplane)

.. _`ixgbe_fc_enable_82598`:

ixgbe_fc_enable_82598
=====================

.. c:function:: s32 ixgbe_fc_enable_82598(struct ixgbe_hw *hw)

    Enable flow control

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_fc_enable_82598.description`:

Description
-----------

Enable flow control according to the current settings.

.. _`ixgbe_start_mac_link_82598`:

ixgbe_start_mac_link_82598
==========================

.. c:function:: s32 ixgbe_start_mac_link_82598(struct ixgbe_hw *hw, bool autoneg_wait_to_complete)

    Configures MAC link settings

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param bool autoneg_wait_to_complete:
        *undescribed*

.. _`ixgbe_start_mac_link_82598.description`:

Description
-----------

Configures link settings based on values in the ixgbe_hw struct.
Restarts the link.  Performs autonegotiation if needed.

.. _`ixgbe_validate_link_ready`:

ixgbe_validate_link_ready
=========================

.. c:function:: s32 ixgbe_validate_link_ready(struct ixgbe_hw *hw)

    Function looks for phy link

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_validate_link_ready.description`:

Description
-----------

Function indicates success when phy link is available. If phy is not ready
within 5 seconds of MAC indicating link, the function returns error.

.. _`ixgbe_check_mac_link_82598`:

ixgbe_check_mac_link_82598
==========================

.. c:function:: s32 ixgbe_check_mac_link_82598(struct ixgbe_hw *hw, ixgbe_link_speed *speed, bool *link_up, bool link_up_wait_to_complete)

    Get link/speed status

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param ixgbe_link_speed \*speed:
        pointer to link speed

    :param bool \*link_up:
        true is link is up, false otherwise

    :param bool link_up_wait_to_complete:
        bool used to wait for link up or not

.. _`ixgbe_check_mac_link_82598.description`:

Description
-----------

Reads the links register to determine if link is up and the current speed

.. _`ixgbe_setup_mac_link_82598`:

ixgbe_setup_mac_link_82598
==========================

.. c:function:: s32 ixgbe_setup_mac_link_82598(struct ixgbe_hw *hw, ixgbe_link_speed speed, bool autoneg_wait_to_complete)

    Set MAC link speed

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param ixgbe_link_speed speed:
        new link speed

    :param bool autoneg_wait_to_complete:
        true when waiting for completion is needed

.. _`ixgbe_setup_mac_link_82598.description`:

Description
-----------

Set the link speed in the AUTOC register and restarts link.

.. _`ixgbe_setup_copper_link_82598`:

ixgbe_setup_copper_link_82598
=============================

.. c:function:: s32 ixgbe_setup_copper_link_82598(struct ixgbe_hw *hw, ixgbe_link_speed speed, bool autoneg_wait_to_complete)

    Set the PHY autoneg advertised field

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param ixgbe_link_speed speed:
        new link speed

    :param bool autoneg_wait_to_complete:
        true if waiting is needed to complete

.. _`ixgbe_setup_copper_link_82598.description`:

Description
-----------

Sets the link speed in the AUTOC register in the MAC and restarts link.

.. _`ixgbe_reset_hw_82598`:

ixgbe_reset_hw_82598
====================

.. c:function:: s32 ixgbe_reset_hw_82598(struct ixgbe_hw *hw)

    Performs hardware reset

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_reset_hw_82598.description`:

Description
-----------

Resets the hardware by resetting the transmit and receive units, masks and
clears all interrupts, performing a PHY reset, and performing a link (MAC)
reset.

.. _`ixgbe_set_vmdq_82598`:

ixgbe_set_vmdq_82598
====================

.. c:function:: s32 ixgbe_set_vmdq_82598(struct ixgbe_hw *hw, u32 rar, u32 vmdq)

    Associate a VMDq set index with a rx address

    :param struct ixgbe_hw \*hw:
        pointer to hardware struct

    :param u32 rar:
        receive address register index to associate with a VMDq index

    :param u32 vmdq:
        VMDq set index

.. _`ixgbe_clear_vmdq_82598`:

ixgbe_clear_vmdq_82598
======================

.. c:function:: s32 ixgbe_clear_vmdq_82598(struct ixgbe_hw *hw, u32 rar, u32 vmdq)

    Disassociate a VMDq set index from an rx address

    :param struct ixgbe_hw \*hw:
        pointer to hardware struct

    :param u32 rar:
        receive address register index to associate with a VMDq index

    :param u32 vmdq:
        VMDq clear index (not used in 82598, but elsewhere)

.. _`ixgbe_set_vfta_82598`:

ixgbe_set_vfta_82598
====================

.. c:function:: s32 ixgbe_set_vfta_82598(struct ixgbe_hw *hw, u32 vlan, u32 vind, bool vlan_on, bool vlvf_bypass)

    Set VLAN filter table

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 vlan:
        VLAN id to write to VLAN filter

    :param u32 vind:
        VMDq output index that maps queue to VLAN id in VFTA

    :param bool vlan_on:
        boolean flag to turn on/off VLAN in VFTA

    :param bool vlvf_bypass:
        boolean flag - unused

.. _`ixgbe_set_vfta_82598.description`:

Description
-----------

Turn on/off specified VLAN in the VLAN filter table.

.. _`ixgbe_clear_vfta_82598`:

ixgbe_clear_vfta_82598
======================

.. c:function:: s32 ixgbe_clear_vfta_82598(struct ixgbe_hw *hw)

    Clear VLAN filter table

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_clear_vfta_82598.description`:

Description
-----------

Clears the VLAN filer table, and the VMDq index associated with the filter

.. _`ixgbe_read_analog_reg8_82598`:

ixgbe_read_analog_reg8_82598
============================

.. c:function:: s32 ixgbe_read_analog_reg8_82598(struct ixgbe_hw *hw, u32 reg, u8 *val)

    Reads 8 bit Atlas analog register

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 reg:
        analog register to read

    :param u8 \*val:
        read value

.. _`ixgbe_read_analog_reg8_82598.description`:

Description
-----------

Performs read operation to Atlas analog register specified.

.. _`ixgbe_write_analog_reg8_82598`:

ixgbe_write_analog_reg8_82598
=============================

.. c:function:: s32 ixgbe_write_analog_reg8_82598(struct ixgbe_hw *hw, u32 reg, u8 val)

    Writes 8 bit Atlas analog register

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 reg:
        atlas register to write

    :param u8 val:
        value to write

.. _`ixgbe_write_analog_reg8_82598.description`:

Description
-----------

Performs write operation to Atlas analog register specified.

.. _`ixgbe_read_i2c_phy_82598`:

ixgbe_read_i2c_phy_82598
========================

.. c:function:: s32 ixgbe_read_i2c_phy_82598(struct ixgbe_hw *hw, u8 dev_addr, u8 byte_offset, u8 *eeprom_data)

    Reads 8 bit word over I2C interface.

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 dev_addr:
        address to read from

    :param u8 byte_offset:
        byte offset to read from dev_addr

    :param u8 \*eeprom_data:
        value read

.. _`ixgbe_read_i2c_phy_82598.description`:

Description
-----------

Performs 8 byte read operation to SFP module's data over I2C interface.

.. _`ixgbe_read_i2c_eeprom_82598`:

ixgbe_read_i2c_eeprom_82598
===========================

.. c:function:: s32 ixgbe_read_i2c_eeprom_82598(struct ixgbe_hw *hw, u8 byte_offset, u8 *eeprom_data)

    Reads 8 bit word over I2C interface.

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 byte_offset:
        EEPROM byte offset to read

    :param u8 \*eeprom_data:
        value read

.. _`ixgbe_read_i2c_eeprom_82598.description`:

Description
-----------

Performs 8 byte read operation to SFP module's EEPROM over I2C interface.

.. _`ixgbe_read_i2c_sff8472_82598`:

ixgbe_read_i2c_sff8472_82598
============================

.. c:function:: s32 ixgbe_read_i2c_sff8472_82598(struct ixgbe_hw *hw, u8 byte_offset, u8 *sff8472_data)

    Reads 8 bit word over I2C interface.

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 byte_offset:
        byte offset at address 0xA2

    :param u8 \*sff8472_data:
        *undescribed*

.. _`ixgbe_read_i2c_sff8472_82598.description`:

Description
-----------

Performs 8 byte read operation to SFP module's SFF-8472 data over I2C

.. _`ixgbe_set_lan_id_multi_port_pcie_82598`:

ixgbe_set_lan_id_multi_port_pcie_82598
======================================

.. c:function:: void ixgbe_set_lan_id_multi_port_pcie_82598(struct ixgbe_hw *hw)

    Set LAN id for PCIe multiple port devices.

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

.. _`ixgbe_set_lan_id_multi_port_pcie_82598.description`:

Description
-----------

Calls common function and corrects issue with some single port devices
that enable LAN1 but not LAN0.

.. _`ixgbe_set_rxpba_82598`:

ixgbe_set_rxpba_82598
=====================

.. c:function:: void ixgbe_set_rxpba_82598(struct ixgbe_hw *hw, int num_pb, u32 headroom, int strategy)

    Initialize RX packet buffer

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param int num_pb:
        number of packet buffers to allocate

    :param u32 headroom:
        reserve n KB of headroom

    :param int strategy:
        packet buffer allocation strategy

.. This file was automatic generated / don't edit.

