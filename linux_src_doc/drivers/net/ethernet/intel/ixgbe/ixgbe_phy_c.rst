.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_phy.c

.. _`ixgbe_out_i2c_byte_ack`:

ixgbe_out_i2c_byte_ack
======================

.. c:function:: s32 ixgbe_out_i2c_byte_ack(struct ixgbe_hw *hw, u8 byte)

    Send I2C byte with ack

    :param struct ixgbe_hw \*hw:
        pointer to the hardware structure

    :param u8 byte:
        byte to send

.. _`ixgbe_out_i2c_byte_ack.description`:

Description
-----------

Returns an error code on error.

.. _`ixgbe_in_i2c_byte_ack`:

ixgbe_in_i2c_byte_ack
=====================

.. c:function:: s32 ixgbe_in_i2c_byte_ack(struct ixgbe_hw *hw, u8 *byte)

    Receive an I2C byte and send ack

    :param struct ixgbe_hw \*hw:
        pointer to the hardware structure

    :param u8 \*byte:
        pointer to a u8 to receive the byte

.. _`ixgbe_in_i2c_byte_ack.description`:

Description
-----------

Returns an error code on error.

.. _`ixgbe_ones_comp_byte_add`:

ixgbe_ones_comp_byte_add
========================

.. c:function:: u8 ixgbe_ones_comp_byte_add(u8 add1, u8 add2)

    Perform one's complement addition

    :param u8 add1:
        addend 1

    :param u8 add2:
        addend 2

.. _`ixgbe_ones_comp_byte_add.description`:

Description
-----------

Returns one's complement 8-bit sum.

.. _`ixgbe_read_i2c_combined_generic_int`:

ixgbe_read_i2c_combined_generic_int
===================================

.. c:function:: s32 ixgbe_read_i2c_combined_generic_int(struct ixgbe_hw *hw, u8 addr, u16 reg, u16 *val, bool lock)

    Perform I2C read combined operation

    :param struct ixgbe_hw \*hw:
        pointer to the hardware structure

    :param u8 addr:
        I2C bus address to read from

    :param u16 reg:
        I2C device register to read from

    :param u16 \*val:
        pointer to location to receive read value

    :param bool lock:
        true if to take and release semaphore

.. _`ixgbe_read_i2c_combined_generic_int.description`:

Description
-----------

Returns an error code on error.

.. _`ixgbe_write_i2c_combined_generic_int`:

ixgbe_write_i2c_combined_generic_int
====================================

.. c:function:: s32 ixgbe_write_i2c_combined_generic_int(struct ixgbe_hw *hw, u8 addr, u16 reg, u16 val, bool lock)

    Perform I2C write combined operation

    :param struct ixgbe_hw \*hw:
        pointer to the hardware structure

    :param u8 addr:
        I2C bus address to write to

    :param u16 reg:
        I2C device register to write to

    :param u16 val:
        value to write

    :param bool lock:
        true if to take and release semaphore

.. _`ixgbe_write_i2c_combined_generic_int.description`:

Description
-----------

Returns an error code on error.

.. _`ixgbe_probe_phy`:

ixgbe_probe_phy
===============

.. c:function:: bool ixgbe_probe_phy(struct ixgbe_hw *hw, u16 phy_addr)

    Probe a single address for a PHY

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 phy_addr:
        PHY address to probe

.. _`ixgbe_probe_phy.description`:

Description
-----------

Returns true if PHY found

.. _`ixgbe_identify_phy_generic`:

ixgbe_identify_phy_generic
==========================

.. c:function:: s32 ixgbe_identify_phy_generic(struct ixgbe_hw *hw)

    Get physical layer module

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_identify_phy_generic.description`:

Description
-----------

Determines the physical layer module found on the current adapter.

.. _`ixgbe_check_reset_blocked`:

ixgbe_check_reset_blocked
=========================

.. c:function:: bool ixgbe_check_reset_blocked(struct ixgbe_hw *hw)

    check status of MNG FW veto bit

    :param struct ixgbe_hw \*hw:
        pointer to the hardware structure

.. _`ixgbe_check_reset_blocked.description`:

Description
-----------

This function checks the MMNGC.MNG_VETO bit to see if there are
any constraints on link from manageability.  For MAC's that don't
have this bit just return false since the link can not be blocked
via this method.

.. _`ixgbe_get_phy_id`:

ixgbe_get_phy_id
================

.. c:function:: s32 ixgbe_get_phy_id(struct ixgbe_hw *hw)

    Get the phy type

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_get_phy_type_from_id`:

ixgbe_get_phy_type_from_id
==========================

.. c:function:: enum ixgbe_phy_type ixgbe_get_phy_type_from_id(u32 phy_id)

    Get the phy type

    :param u32 phy_id:
        *undescribed*

.. _`ixgbe_reset_phy_generic`:

ixgbe_reset_phy_generic
=======================

.. c:function:: s32 ixgbe_reset_phy_generic(struct ixgbe_hw *hw)

    Performs a PHY reset

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_read_phy_reg_mdi`:

ixgbe_read_phy_reg_mdi
======================

.. c:function:: s32 ixgbe_read_phy_reg_mdi(struct ixgbe_hw *hw, u32 reg_addr, u32 device_type, u16 *phy_data)

    Reads a value from a specified PHY register without the SWFW lock

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 reg_addr:
        32 bit address of PHY register to read

    :param u32 device_type:
        *undescribed*

    :param u16 \*phy_data:
        Pointer to read data from PHY register

.. _`ixgbe_read_phy_reg_generic`:

ixgbe_read_phy_reg_generic
==========================

.. c:function:: s32 ixgbe_read_phy_reg_generic(struct ixgbe_hw *hw, u32 reg_addr, u32 device_type, u16 *phy_data)

    Reads a value from a specified PHY register using the SWFW lock - this function is needed in most cases

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 reg_addr:
        32 bit address of PHY register to read

    :param u32 device_type:
        *undescribed*

    :param u16 \*phy_data:
        Pointer to read data from PHY register

.. _`ixgbe_write_phy_reg_mdi`:

ixgbe_write_phy_reg_mdi
=======================

.. c:function:: s32 ixgbe_write_phy_reg_mdi(struct ixgbe_hw *hw, u32 reg_addr, u32 device_type, u16 phy_data)

    Writes a value to specified PHY register without SWFW lock

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 reg_addr:
        32 bit PHY register to write

    :param u32 device_type:
        5 bit device type

    :param u16 phy_data:
        Data to write to the PHY register

.. _`ixgbe_write_phy_reg_generic`:

ixgbe_write_phy_reg_generic
===========================

.. c:function:: s32 ixgbe_write_phy_reg_generic(struct ixgbe_hw *hw, u32 reg_addr, u32 device_type, u16 phy_data)

    Writes a value to specified PHY register using SWFW lock- this function is needed in most cases

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 reg_addr:
        32 bit PHY register to write

    :param u32 device_type:
        5 bit device type

    :param u16 phy_data:
        Data to write to the PHY register

.. _`ixgbe_setup_phy_link_generic`:

ixgbe_setup_phy_link_generic
============================

.. c:function:: s32 ixgbe_setup_phy_link_generic(struct ixgbe_hw *hw)

    Set and restart autoneg

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_setup_phy_link_generic.description`:

Description
-----------

Restart autonegotiation and PHY and waits for completion.

.. _`ixgbe_setup_phy_link_speed_generic`:

ixgbe_setup_phy_link_speed_generic
==================================

.. c:function:: s32 ixgbe_setup_phy_link_speed_generic(struct ixgbe_hw *hw, ixgbe_link_speed speed, bool autoneg_wait_to_complete)

    Sets the auto advertised capabilities

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param ixgbe_link_speed speed:
        new link speed

    :param bool autoneg_wait_to_complete:
        *undescribed*

.. _`ixgbe_get_copper_speeds_supported`:

ixgbe_get_copper_speeds_supported
=================================

.. c:function:: s32 ixgbe_get_copper_speeds_supported(struct ixgbe_hw *hw)

    Get copper link speed from phy

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_get_copper_speeds_supported.description`:

Description
-----------

Determines the supported link capabilities by reading the PHY auto
negotiation register.

.. _`ixgbe_get_copper_link_capabilities_generic`:

ixgbe_get_copper_link_capabilities_generic
==========================================

.. c:function:: s32 ixgbe_get_copper_link_capabilities_generic(struct ixgbe_hw *hw, ixgbe_link_speed *speed, bool *autoneg)

    Determines link capabilities

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param ixgbe_link_speed \*speed:
        pointer to link speed

    :param bool \*autoneg:
        boolean auto-negotiation value

.. _`ixgbe_check_phy_link_tnx`:

ixgbe_check_phy_link_tnx
========================

.. c:function:: s32 ixgbe_check_phy_link_tnx(struct ixgbe_hw *hw, ixgbe_link_speed *speed, bool *link_up)

    Determine link and speed status

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param ixgbe_link_speed \*speed:
        *undescribed*

    :param bool \*link_up:
        *undescribed*

.. _`ixgbe_check_phy_link_tnx.description`:

Description
-----------

Reads the VS1 register to determine if link is up and the current speed for
the PHY.

.. _`ixgbe_setup_phy_link_tnx`:

ixgbe_setup_phy_link_tnx
========================

.. c:function:: s32 ixgbe_setup_phy_link_tnx(struct ixgbe_hw *hw)

    Set and restart autoneg

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_setup_phy_link_tnx.description`:

Description
-----------

Restart autonegotiation and PHY and waits for completion.
This function always returns success, this is nessary since
it is called via a function pointer that could call other
functions that could return an error.

.. _`ixgbe_reset_phy_nl`:

ixgbe_reset_phy_nl
==================

.. c:function:: s32 ixgbe_reset_phy_nl(struct ixgbe_hw *hw)

    Performs a PHY reset

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_identify_module_generic`:

ixgbe_identify_module_generic
=============================

.. c:function:: s32 ixgbe_identify_module_generic(struct ixgbe_hw *hw)

    Identifies module type

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_identify_module_generic.description`:

Description
-----------

Determines HW type and calls appropriate function.

.. _`ixgbe_identify_sfp_module_generic`:

ixgbe_identify_sfp_module_generic
=================================

.. c:function:: s32 ixgbe_identify_sfp_module_generic(struct ixgbe_hw *hw)

    Identifies SFP modules

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_identify_sfp_module_generic.description`:

Description
-----------

Searches for and identifies the SFP module and assigns appropriate PHY type.

.. _`ixgbe_identify_qsfp_module_generic`:

ixgbe_identify_qsfp_module_generic
==================================

.. c:function:: s32 ixgbe_identify_qsfp_module_generic(struct ixgbe_hw *hw)

    Identifies QSFP modules

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_identify_qsfp_module_generic.description`:

Description
-----------

Searches for and identifies the QSFP module and assigns appropriate PHY type

.. _`ixgbe_get_sfp_init_sequence_offsets`:

ixgbe_get_sfp_init_sequence_offsets
===================================

.. c:function:: s32 ixgbe_get_sfp_init_sequence_offsets(struct ixgbe_hw *hw, u16 *list_offset, u16 *data_offset)

    Provides offset of PHY init sequence

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 \*list_offset:
        offset to the SFP ID list

    :param u16 \*data_offset:
        offset to the SFP data block

.. _`ixgbe_get_sfp_init_sequence_offsets.description`:

Description
-----------

Checks the MAC's EEPROM to see if it supports a given SFP+ module type, if
so it returns the offsets to the phy init sequence block.

.. _`ixgbe_read_i2c_eeprom_generic`:

ixgbe_read_i2c_eeprom_generic
=============================

.. c:function:: s32 ixgbe_read_i2c_eeprom_generic(struct ixgbe_hw *hw, u8 byte_offset, u8 *eeprom_data)

    Reads 8 bit EEPROM word over I2C interface

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 byte_offset:
        EEPROM byte offset to read

    :param u8 \*eeprom_data:
        value read

.. _`ixgbe_read_i2c_eeprom_generic.description`:

Description
-----------

Performs byte read operation to SFP module's EEPROM over I2C interface.

.. _`ixgbe_read_i2c_sff8472_generic`:

ixgbe_read_i2c_sff8472_generic
==============================

.. c:function:: s32 ixgbe_read_i2c_sff8472_generic(struct ixgbe_hw *hw, u8 byte_offset, u8 *sff8472_data)

    Reads 8 bit word over I2C interface

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 byte_offset:
        byte offset at address 0xA2

    :param u8 \*sff8472_data:
        *undescribed*

.. _`ixgbe_read_i2c_sff8472_generic.description`:

Description
-----------

Performs byte read operation to SFP module's SFF-8472 data over I2C

.. _`ixgbe_write_i2c_eeprom_generic`:

ixgbe_write_i2c_eeprom_generic
==============================

.. c:function:: s32 ixgbe_write_i2c_eeprom_generic(struct ixgbe_hw *hw, u8 byte_offset, u8 eeprom_data)

    Writes 8 bit EEPROM word over I2C interface

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 byte_offset:
        EEPROM byte offset to write

    :param u8 eeprom_data:
        value to write

.. _`ixgbe_write_i2c_eeprom_generic.description`:

Description
-----------

Performs byte write operation to SFP module's EEPROM over I2C interface.

.. _`ixgbe_is_sfp_probe`:

ixgbe_is_sfp_probe
==================

.. c:function:: bool ixgbe_is_sfp_probe(struct ixgbe_hw *hw, u8 offset, u8 addr)

    Returns true if SFP is being detected

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 offset:
        eeprom offset to be read

    :param u8 addr:
        I2C address to be read

.. _`ixgbe_read_i2c_byte_generic_int`:

ixgbe_read_i2c_byte_generic_int
===============================

.. c:function:: s32 ixgbe_read_i2c_byte_generic_int(struct ixgbe_hw *hw, u8 byte_offset, u8 dev_addr, u8 *data, bool lock)

    Reads 8 bit word over I2C

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 byte_offset:
        byte offset to read

    :param u8 dev_addr:
        *undescribed*

    :param u8 \*data:
        value read

    :param bool lock:
        true if to take and release semaphore

.. _`ixgbe_read_i2c_byte_generic_int.description`:

Description
-----------

Performs byte read operation to SFP module's EEPROM over I2C interface at
a specified device address.

.. _`ixgbe_read_i2c_byte_generic`:

ixgbe_read_i2c_byte_generic
===========================

.. c:function:: s32 ixgbe_read_i2c_byte_generic(struct ixgbe_hw *hw, u8 byte_offset, u8 dev_addr, u8 *data)

    Reads 8 bit word over I2C

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 byte_offset:
        byte offset to read

    :param u8 dev_addr:
        *undescribed*

    :param u8 \*data:
        value read

.. _`ixgbe_read_i2c_byte_generic.description`:

Description
-----------

Performs byte read operation to SFP module's EEPROM over I2C interface at
a specified device address.

.. _`ixgbe_read_i2c_byte_generic_unlocked`:

ixgbe_read_i2c_byte_generic_unlocked
====================================

.. c:function:: s32 ixgbe_read_i2c_byte_generic_unlocked(struct ixgbe_hw *hw, u8 byte_offset, u8 dev_addr, u8 *data)

    Reads 8 bit word over I2C

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 byte_offset:
        byte offset to read

    :param u8 dev_addr:
        *undescribed*

    :param u8 \*data:
        value read

.. _`ixgbe_read_i2c_byte_generic_unlocked.description`:

Description
-----------

Performs byte read operation to SFP module's EEPROM over I2C interface at
a specified device address.

.. _`ixgbe_write_i2c_byte_generic_int`:

ixgbe_write_i2c_byte_generic_int
================================

.. c:function:: s32 ixgbe_write_i2c_byte_generic_int(struct ixgbe_hw *hw, u8 byte_offset, u8 dev_addr, u8 data, bool lock)

    Writes 8 bit word over I2C

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 byte_offset:
        byte offset to write

    :param u8 dev_addr:
        *undescribed*

    :param u8 data:
        value to write

    :param bool lock:
        true if to take and release semaphore

.. _`ixgbe_write_i2c_byte_generic_int.description`:

Description
-----------

Performs byte write operation to SFP module's EEPROM over I2C interface at
a specified device address.

.. _`ixgbe_write_i2c_byte_generic`:

ixgbe_write_i2c_byte_generic
============================

.. c:function:: s32 ixgbe_write_i2c_byte_generic(struct ixgbe_hw *hw, u8 byte_offset, u8 dev_addr, u8 data)

    Writes 8 bit word over I2C

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 byte_offset:
        byte offset to write

    :param u8 dev_addr:
        *undescribed*

    :param u8 data:
        value to write

.. _`ixgbe_write_i2c_byte_generic.description`:

Description
-----------

Performs byte write operation to SFP module's EEPROM over I2C interface at
a specified device address.

.. _`ixgbe_write_i2c_byte_generic_unlocked`:

ixgbe_write_i2c_byte_generic_unlocked
=====================================

.. c:function:: s32 ixgbe_write_i2c_byte_generic_unlocked(struct ixgbe_hw *hw, u8 byte_offset, u8 dev_addr, u8 data)

    Writes 8 bit word over I2C

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 byte_offset:
        byte offset to write

    :param u8 dev_addr:
        *undescribed*

    :param u8 data:
        value to write

.. _`ixgbe_write_i2c_byte_generic_unlocked.description`:

Description
-----------

Performs byte write operation to SFP module's EEPROM over I2C interface at
a specified device address.

.. _`ixgbe_i2c_start`:

ixgbe_i2c_start
===============

.. c:function:: void ixgbe_i2c_start(struct ixgbe_hw *hw)

    Sets I2C start condition

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_i2c_start.description`:

Description
-----------

Sets I2C start condition (High -> Low on SDA while SCL is High)
Set bit-bang mode on X550 hardware.

.. _`ixgbe_i2c_stop`:

ixgbe_i2c_stop
==============

.. c:function:: void ixgbe_i2c_stop(struct ixgbe_hw *hw)

    Sets I2C stop condition

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_i2c_stop.description`:

Description
-----------

Sets I2C stop condition (Low -> High on SDA while SCL is High)
Disables bit-bang mode and negates data output enable on X550
hardware.

.. _`ixgbe_clock_in_i2c_byte`:

ixgbe_clock_in_i2c_byte
=======================

.. c:function:: s32 ixgbe_clock_in_i2c_byte(struct ixgbe_hw *hw, u8 *data)

    Clocks in one byte via I2C

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 \*data:
        data byte to clock in

.. _`ixgbe_clock_in_i2c_byte.description`:

Description
-----------

Clocks in one byte data via I2C data/clock

.. _`ixgbe_clock_out_i2c_byte`:

ixgbe_clock_out_i2c_byte
========================

.. c:function:: s32 ixgbe_clock_out_i2c_byte(struct ixgbe_hw *hw, u8 data)

    Clocks out one byte via I2C

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 data:
        data byte clocked out

.. _`ixgbe_clock_out_i2c_byte.description`:

Description
-----------

Clocks out one byte data via I2C data/clock

.. _`ixgbe_get_i2c_ack`:

ixgbe_get_i2c_ack
=================

.. c:function:: s32 ixgbe_get_i2c_ack(struct ixgbe_hw *hw)

    Polls for I2C ACK

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_get_i2c_ack.description`:

Description
-----------

Clocks in/out one bit via I2C data/clock

.. _`ixgbe_clock_in_i2c_bit`:

ixgbe_clock_in_i2c_bit
======================

.. c:function:: s32 ixgbe_clock_in_i2c_bit(struct ixgbe_hw *hw, bool *data)

    Clocks in one bit via I2C data/clock

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param bool \*data:
        read data value

.. _`ixgbe_clock_in_i2c_bit.description`:

Description
-----------

Clocks in one bit via I2C data/clock

.. _`ixgbe_clock_out_i2c_bit`:

ixgbe_clock_out_i2c_bit
=======================

.. c:function:: s32 ixgbe_clock_out_i2c_bit(struct ixgbe_hw *hw, bool data)

    Clocks in/out one bit via I2C data/clock

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param bool data:
        data value to write

.. _`ixgbe_clock_out_i2c_bit.description`:

Description
-----------

Clocks out one bit via I2C data/clock

.. _`ixgbe_raise_i2c_clk`:

ixgbe_raise_i2c_clk
===================

.. c:function:: void ixgbe_raise_i2c_clk(struct ixgbe_hw *hw, u32 *i2cctl)

    Raises the I2C SCL clock

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 \*i2cctl:
        Current value of I2CCTL register

.. _`ixgbe_raise_i2c_clk.description`:

Description
-----------

Raises the I2C clock line '0'->'1'
Negates the I2C clock output enable on X550 hardware.

.. _`ixgbe_lower_i2c_clk`:

ixgbe_lower_i2c_clk
===================

.. c:function:: void ixgbe_lower_i2c_clk(struct ixgbe_hw *hw, u32 *i2cctl)

    Lowers the I2C SCL clock

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 \*i2cctl:
        Current value of I2CCTL register

.. _`ixgbe_lower_i2c_clk.description`:

Description
-----------

Lowers the I2C clock line '1'->'0'
Asserts the I2C clock output enable on X550 hardware.

.. _`ixgbe_set_i2c_data`:

ixgbe_set_i2c_data
==================

.. c:function:: s32 ixgbe_set_i2c_data(struct ixgbe_hw *hw, u32 *i2cctl, bool data)

    Sets the I2C data bit

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 \*i2cctl:
        Current value of I2CCTL register

    :param bool data:
        I2C data value (0 or 1) to set

.. _`ixgbe_set_i2c_data.description`:

Description
-----------

Sets the I2C data bit
Asserts the I2C data output enable on X550 hardware.

.. _`ixgbe_get_i2c_data`:

ixgbe_get_i2c_data
==================

.. c:function:: bool ixgbe_get_i2c_data(struct ixgbe_hw *hw, u32 *i2cctl)

    Reads the I2C SDA data bit

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 \*i2cctl:
        Current value of I2CCTL register

.. _`ixgbe_get_i2c_data.description`:

Description
-----------

Returns the I2C data bit value
Negates the I2C data output enable on X550 hardware.

.. _`ixgbe_i2c_bus_clear`:

ixgbe_i2c_bus_clear
===================

.. c:function:: void ixgbe_i2c_bus_clear(struct ixgbe_hw *hw)

    Clears the I2C bus

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_i2c_bus_clear.description`:

Description
-----------

Clears the I2C bus by sending nine clock pulses.
Used when data line is stuck low.

.. _`ixgbe_tn_check_overtemp`:

ixgbe_tn_check_overtemp
=======================

.. c:function:: s32 ixgbe_tn_check_overtemp(struct ixgbe_hw *hw)

    Checks if an overtemp occurred.

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_tn_check_overtemp.description`:

Description
-----------

Checks if the LASI temp alarm status was triggered due to overtemp

.. This file was automatic generated / don't edit.

