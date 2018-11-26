.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_82599.c

.. _`prot_autoc_read_82599`:

prot_autoc_read_82599
=====================

.. c:function:: s32 prot_autoc_read_82599(struct ixgbe_hw *hw, bool *locked, u32 *reg_val)

    Hides MAC differences needed for AUTOC read

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param locked:
        Return the if we locked for this read.
    :type locked: bool \*

    :param reg_val:
        Value we read from AUTOC
    :type reg_val: u32 \*

.. _`prot_autoc_read_82599.description`:

Description
-----------

For this part (82599) we need to wrap read-modify-writes with a possible
FW/SW lock.  It is assumed this lock will be freed with the next
\ :c:func:`prot_autoc_write_82599`\ .  Note, that locked can only be true in cases
where this function doesn't return an error.

.. _`prot_autoc_write_82599`:

prot_autoc_write_82599
======================

.. c:function:: s32 prot_autoc_write_82599(struct ixgbe_hw *hw, u32 autoc, bool locked)

    Hides MAC differences needed for AUTOC write

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param autoc:
        value to write to AUTOC
    :type autoc: u32

    :param locked:
        bool to indicate whether the SW/FW lock was already taken by
        previous proc_autoc_read_82599.
    :type locked: bool

.. _`prot_autoc_write_82599.description`:

Description
-----------

This part (82599) may need to hold a the SW/FW lock around all writes to
AUTOC. Likewise after a write we need to do a pipeline reset.

.. _`ixgbe_init_phy_ops_82599`:

ixgbe_init_phy_ops_82599
========================

.. c:function:: s32 ixgbe_init_phy_ops_82599(struct ixgbe_hw *hw)

    PHY/SFP specific init

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_init_phy_ops_82599.description`:

Description
-----------

Initialize any function pointers that were not able to be
set during get_invariants because the PHY/SFP type was
not known.  Perform the SFP init if necessary.

.. _`ixgbe_get_link_capabilities_82599`:

ixgbe_get_link_capabilities_82599
=================================

.. c:function:: s32 ixgbe_get_link_capabilities_82599(struct ixgbe_hw *hw, ixgbe_link_speed *speed, bool *autoneg)

    Determines link capabilities

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        pointer to link speed
    :type speed: ixgbe_link_speed \*

    :param autoneg:
        true when autoneg or autotry is enabled
    :type autoneg: bool \*

.. _`ixgbe_get_link_capabilities_82599.description`:

Description
-----------

Determines the link capabilities by reading the AUTOC register.

.. _`ixgbe_get_media_type_82599`:

ixgbe_get_media_type_82599
==========================

.. c:function:: enum ixgbe_media_type ixgbe_get_media_type_82599(struct ixgbe_hw *hw)

    Get media type

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_get_media_type_82599.description`:

Description
-----------

Returns the media type (fiber, copper, backplane)

.. _`ixgbe_stop_mac_link_on_d3_82599`:

ixgbe_stop_mac_link_on_d3_82599
===============================

.. c:function:: void ixgbe_stop_mac_link_on_d3_82599(struct ixgbe_hw *hw)

    Disables link on D3

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_stop_mac_link_on_d3_82599.description`:

Description
-----------

Disables link, should be called during D3 power down sequence.

.. _`ixgbe_start_mac_link_82599`:

ixgbe_start_mac_link_82599
==========================

.. c:function:: s32 ixgbe_start_mac_link_82599(struct ixgbe_hw *hw, bool autoneg_wait_to_complete)

    Setup MAC link settings

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param autoneg_wait_to_complete:
        true when waiting for completion is needed
    :type autoneg_wait_to_complete: bool

.. _`ixgbe_start_mac_link_82599.description`:

Description
-----------

Configures link settings based on values in the ixgbe_hw struct.
Restarts the link.  Performs autonegotiation if needed.

.. _`ixgbe_disable_tx_laser_multispeed_fiber`:

ixgbe_disable_tx_laser_multispeed_fiber
=======================================

.. c:function:: void ixgbe_disable_tx_laser_multispeed_fiber(struct ixgbe_hw *hw)

    Disable Tx laser

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_disable_tx_laser_multispeed_fiber.description`:

Description
-----------

The base drivers may require better control over SFP+ module
PHY states.  This includes selectively shutting down the Tx
laser on the PHY, effectively halting physical link.

.. _`ixgbe_enable_tx_laser_multispeed_fiber`:

ixgbe_enable_tx_laser_multispeed_fiber
======================================

.. c:function:: void ixgbe_enable_tx_laser_multispeed_fiber(struct ixgbe_hw *hw)

    Enable Tx laser

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_enable_tx_laser_multispeed_fiber.description`:

Description
-----------

The base drivers may require better control over SFP+ module
PHY states.  This includes selectively turning on the Tx
laser on the PHY, effectively starting physical link.

.. _`ixgbe_flap_tx_laser_multispeed_fiber`:

ixgbe_flap_tx_laser_multispeed_fiber
====================================

.. c:function:: void ixgbe_flap_tx_laser_multispeed_fiber(struct ixgbe_hw *hw)

    Flap Tx laser

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_flap_tx_laser_multispeed_fiber.description`:

Description
-----------

When the driver changes the link speeds that it can support,
it sets autotry_restart to true to indicate that we need to
initiate a new autotry session with the link partner.  To do
so, we set the speed then disable and re-enable the tx laser, to
alert the link partner that it also needs to restart autotry on its
end.  This is consistent with true clause 37 autoneg, which also
involves a loss of signal.

.. _`ixgbe_set_hard_rate_select_speed`:

ixgbe_set_hard_rate_select_speed
================================

.. c:function:: void ixgbe_set_hard_rate_select_speed(struct ixgbe_hw *hw, ixgbe_link_speed speed)

    Set module link speed

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        link speed to set
    :type speed: ixgbe_link_speed

.. _`ixgbe_set_hard_rate_select_speed.description`:

Description
-----------

Set module link speed via RS0/RS1 rate select pins.

.. _`ixgbe_setup_mac_link_smartspeed`:

ixgbe_setup_mac_link_smartspeed
===============================

.. c:function:: s32 ixgbe_setup_mac_link_smartspeed(struct ixgbe_hw *hw, ixgbe_link_speed speed, bool autoneg_wait_to_complete)

    Set MAC link speed using SmartSpeed

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        new link speed
    :type speed: ixgbe_link_speed

    :param autoneg_wait_to_complete:
        true when waiting for completion is needed
    :type autoneg_wait_to_complete: bool

.. _`ixgbe_setup_mac_link_smartspeed.description`:

Description
-----------

Implements the Intel SmartSpeed algorithm.

.. _`ixgbe_setup_mac_link_82599`:

ixgbe_setup_mac_link_82599
==========================

.. c:function:: s32 ixgbe_setup_mac_link_82599(struct ixgbe_hw *hw, ixgbe_link_speed speed, bool autoneg_wait_to_complete)

    Set MAC link speed

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        new link speed
    :type speed: ixgbe_link_speed

    :param autoneg_wait_to_complete:
        true when waiting for completion is needed
    :type autoneg_wait_to_complete: bool

.. _`ixgbe_setup_mac_link_82599.description`:

Description
-----------

Set the link speed in the AUTOC register and restarts link.

.. _`ixgbe_setup_copper_link_82599`:

ixgbe_setup_copper_link_82599
=============================

.. c:function:: s32 ixgbe_setup_copper_link_82599(struct ixgbe_hw *hw, ixgbe_link_speed speed, bool autoneg_wait_to_complete)

    Set the PHY autoneg advertised field

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        new link speed
    :type speed: ixgbe_link_speed

    :param autoneg_wait_to_complete:
        true if waiting is needed to complete
    :type autoneg_wait_to_complete: bool

.. _`ixgbe_setup_copper_link_82599.description`:

Description
-----------

Restarts link on PHY and MAC based on settings passed in.

.. _`ixgbe_reset_hw_82599`:

ixgbe_reset_hw_82599
====================

.. c:function:: s32 ixgbe_reset_hw_82599(struct ixgbe_hw *hw)

    Perform hardware reset

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_reset_hw_82599.description`:

Description
-----------

Resets the hardware by resetting the transmit and receive units, masks
and clears all interrupts, perform a PHY reset, and perform a link (MAC)
reset.

.. _`ixgbe_fdir_check_cmd_complete`:

ixgbe_fdir_check_cmd_complete
=============================

.. c:function:: s32 ixgbe_fdir_check_cmd_complete(struct ixgbe_hw *hw, u32 *fdircmd)

    poll to check whether FDIRCMD is complete

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param fdircmd:
        current value of FDIRCMD register
    :type fdircmd: u32 \*

.. _`ixgbe_reinit_fdir_tables_82599`:

ixgbe_reinit_fdir_tables_82599
==============================

.. c:function:: s32 ixgbe_reinit_fdir_tables_82599(struct ixgbe_hw *hw)

    Reinitialize Flow Director tables.

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_fdir_enable_82599`:

ixgbe_fdir_enable_82599
=======================

.. c:function:: void ixgbe_fdir_enable_82599(struct ixgbe_hw *hw, u32 fdirctrl)

    Initialize Flow Director control registers

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param fdirctrl:
        value to write to flow director control register
    :type fdirctrl: u32

.. _`ixgbe_init_fdir_signature_82599`:

ixgbe_init_fdir_signature_82599
===============================

.. c:function:: s32 ixgbe_init_fdir_signature_82599(struct ixgbe_hw *hw, u32 fdirctrl)

    Initialize Flow Director signature filters

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param fdirctrl:
        value to write to flow director control register, initially
        contains just the value of the Rx packet buffer allocation
    :type fdirctrl: u32

.. _`ixgbe_init_fdir_perfect_82599`:

ixgbe_init_fdir_perfect_82599
=============================

.. c:function:: s32 ixgbe_init_fdir_perfect_82599(struct ixgbe_hw *hw, u32 fdirctrl)

    Initialize Flow Director perfect filters

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param fdirctrl:
        value to write to flow director control register, initially
        contains just the value of the Rx packet buffer allocation
    :type fdirctrl: u32

.. _`ixgbe_atr_compute_sig_hash_82599`:

ixgbe_atr_compute_sig_hash_82599
================================

.. c:function:: u32 ixgbe_atr_compute_sig_hash_82599(union ixgbe_atr_hash_dword input, union ixgbe_atr_hash_dword common)

    Compute the signature hash

    :param input:
        input bitstream to compute the hash on
    :type input: union ixgbe_atr_hash_dword

    :param common:
        compressed common input dword
    :type common: union ixgbe_atr_hash_dword

.. _`ixgbe_atr_compute_sig_hash_82599.description`:

Description
-----------

This function is almost identical to the function above but contains
several optimizations such as unwinding all of the loops, letting the
compiler work out all of the conditional ifs since the keys are static
defines, and computing two keys at once since the hashed dword stream
will be the same for both keys.

.. _`ixgbe_fdir_add_signature_filter_82599`:

ixgbe_fdir_add_signature_filter_82599
=====================================

.. c:function:: s32 ixgbe_fdir_add_signature_filter_82599(struct ixgbe_hw *hw, union ixgbe_atr_hash_dword input, union ixgbe_atr_hash_dword common, u8 queue)

    Adds a signature hash filter

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param input:
        unique input dword
    :type input: union ixgbe_atr_hash_dword

    :param common:
        compressed common input dword
    :type common: union ixgbe_atr_hash_dword

    :param queue:
        queue index to direct traffic to
    :type queue: u8

.. _`ixgbe_fdir_add_signature_filter_82599.description`:

Description
-----------

Note that the tunnel bit in input must not be set when the hardware
tunneling support does not exist.

.. _`ixgbe_atr_compute_perfect_hash_82599`:

ixgbe_atr_compute_perfect_hash_82599
====================================

.. c:function:: void ixgbe_atr_compute_perfect_hash_82599(union ixgbe_atr_input *input, union ixgbe_atr_input *input_mask)

    Compute the perfect filter hash

    :param input:
        input bitstream to compute the hash on
    :type input: union ixgbe_atr_input \*

    :param input_mask:
        mask for the input bitstream
    :type input_mask: union ixgbe_atr_input \*

.. _`ixgbe_atr_compute_perfect_hash_82599.description`:

Description
-----------

This function serves two main purposes.  First it applies the input_mask
to the atr_input resulting in a cleaned up atr_input data stream.
Secondly it computes the hash and stores it in the bkt_hash field at
the end of the input byte stream.  This way it will be available for
future use without needing to recompute the hash.

.. _`ixgbe_get_fdirtcpm_82599`:

ixgbe_get_fdirtcpm_82599
========================

.. c:function:: u32 ixgbe_get_fdirtcpm_82599(union ixgbe_atr_input *input_mask)

    generate a tcp port from atr_input_masks

    :param input_mask:
        mask to be bit swapped
    :type input_mask: union ixgbe_atr_input \*

.. _`ixgbe_get_fdirtcpm_82599.description`:

Description
-----------

The source and destination port masks for flow director are bit swapped
in that bit 15 effects bit 0, 14 effects 1, 13, 2 etc.  In order to
generate a correctly swapped value we need to bit swap the mask and that
is what is accomplished by this function.

.. _`ixgbe_read_analog_reg8_82599`:

ixgbe_read_analog_reg8_82599
============================

.. c:function:: s32 ixgbe_read_analog_reg8_82599(struct ixgbe_hw *hw, u32 reg, u8 *val)

    Reads 8 bit Omer analog register

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param reg:
        analog register to read
    :type reg: u32

    :param val:
        read value
    :type val: u8 \*

.. _`ixgbe_read_analog_reg8_82599.description`:

Description
-----------

Performs read operation to Omer analog register specified.

.. _`ixgbe_write_analog_reg8_82599`:

ixgbe_write_analog_reg8_82599
=============================

.. c:function:: s32 ixgbe_write_analog_reg8_82599(struct ixgbe_hw *hw, u32 reg, u8 val)

    Writes 8 bit Omer analog register

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param reg:
        atlas register to write
    :type reg: u32

    :param val:
        value to write
    :type val: u8

.. _`ixgbe_write_analog_reg8_82599.description`:

Description
-----------

Performs write operation to Omer analog register specified.

.. _`ixgbe_start_hw_82599`:

ixgbe_start_hw_82599
====================

.. c:function:: s32 ixgbe_start_hw_82599(struct ixgbe_hw *hw)

    Prepare hardware for Tx/Rx

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_start_hw_82599.description`:

Description
-----------

Starts the hardware using the generic start_hw function
and the generation start_hw function.
Then performs revision-specific operations, if any.

.. _`ixgbe_identify_phy_82599`:

ixgbe_identify_phy_82599
========================

.. c:function:: s32 ixgbe_identify_phy_82599(struct ixgbe_hw *hw)

    Get physical layer module

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_identify_phy_82599.description`:

Description
-----------

Determines the physical layer module found on the current adapter.
If PHY already detected, maintains current PHY type in hw struct,
otherwise executes the PHY detection routine.

.. _`ixgbe_enable_rx_dma_82599`:

ixgbe_enable_rx_dma_82599
=========================

.. c:function:: s32 ixgbe_enable_rx_dma_82599(struct ixgbe_hw *hw, u32 regval)

    Enable the Rx DMA unit on 82599

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param regval:
        register value to write to RXCTRL
    :type regval: u32

.. _`ixgbe_enable_rx_dma_82599.description`:

Description
-----------

Enables the Rx DMA unit for 82599

.. _`ixgbe_verify_fw_version_82599`:

ixgbe_verify_fw_version_82599
=============================

.. c:function:: s32 ixgbe_verify_fw_version_82599(struct ixgbe_hw *hw)

    verify fw version for 82599

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_verify_fw_version_82599.description`:

Description
-----------

Verifies that installed the firmware version is 0.6 or higher
for SFI devices. All 82599 SFI devices should have version 0.6 or higher.

Returns IXGBE_ERR_EEPROM_VERSION if the FW is not present or
if the FW version is not supported.

.. _`ixgbe_verify_lesm_fw_enabled_82599`:

ixgbe_verify_lesm_fw_enabled_82599
==================================

.. c:function:: bool ixgbe_verify_lesm_fw_enabled_82599(struct ixgbe_hw *hw)

    Checks LESM FW module state.

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_verify_lesm_fw_enabled_82599.description`:

Description
-----------

Returns true if the LESM FW module is present and enabled. Otherwise
returns false. Smart Speed must be disabled if LESM FW module is enabled.

.. _`ixgbe_read_eeprom_buffer_82599`:

ixgbe_read_eeprom_buffer_82599
==============================

.. c:function:: s32 ixgbe_read_eeprom_buffer_82599(struct ixgbe_hw *hw, u16 offset, u16 words, u16 *data)

    Read EEPROM word(s) using fastest available method

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param offset:
        offset of  word in EEPROM to read
    :type offset: u16

    :param words:
        number of words
    :type words: u16

    :param data:
        word(s) read from the EEPROM
    :type data: u16 \*

.. _`ixgbe_read_eeprom_buffer_82599.description`:

Description
-----------

Retrieves 16 bit word(s) read from EEPROM

.. _`ixgbe_read_eeprom_82599`:

ixgbe_read_eeprom_82599
=======================

.. c:function:: s32 ixgbe_read_eeprom_82599(struct ixgbe_hw *hw, u16 offset, u16 *data)

    Read EEPROM word using fastest available method

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param offset:
        offset of  word in the EEPROM to read
    :type offset: u16

    :param data:
        word read from the EEPROM
    :type data: u16 \*

.. _`ixgbe_read_eeprom_82599.description`:

Description
-----------

Reads a 16 bit word from the EEPROM

.. _`ixgbe_reset_pipeline_82599`:

ixgbe_reset_pipeline_82599
==========================

.. c:function:: s32 ixgbe_reset_pipeline_82599(struct ixgbe_hw *hw)

    perform pipeline reset

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_reset_pipeline_82599.description`:

Description
-----------

Reset pipeline by asserting Restart_AN together with LMS change to ensure
full pipeline reset.  Note - We must hold the SW/FW semaphore before writing
to AUTOC, so this function assumes the semaphore is held.

.. _`ixgbe_read_i2c_byte_82599`:

ixgbe_read_i2c_byte_82599
=========================

.. c:function:: s32 ixgbe_read_i2c_byte_82599(struct ixgbe_hw *hw, u8 byte_offset, u8 dev_addr, u8 *data)

    Reads 8 bit word over I2C

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param byte_offset:
        byte offset to read
    :type byte_offset: u8

    :param dev_addr:
        address to read from
    :type dev_addr: u8

    :param data:
        value read
    :type data: u8 \*

.. _`ixgbe_read_i2c_byte_82599.description`:

Description
-----------

Performs byte read operation to SFP module's EEPROM over I2C interface at
a specified device address.

.. _`ixgbe_write_i2c_byte_82599`:

ixgbe_write_i2c_byte_82599
==========================

.. c:function:: s32 ixgbe_write_i2c_byte_82599(struct ixgbe_hw *hw, u8 byte_offset, u8 dev_addr, u8 data)

    Writes 8 bit word over I2C

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param byte_offset:
        byte offset to write
    :type byte_offset: u8

    :param dev_addr:
        address to write to
    :type dev_addr: u8

    :param data:
        value to write
    :type data: u8

.. _`ixgbe_write_i2c_byte_82599.description`:

Description
-----------

Performs byte write operation to SFP module's EEPROM over I2C interface at
a specified device address.

.. This file was automatic generated / don't edit.

