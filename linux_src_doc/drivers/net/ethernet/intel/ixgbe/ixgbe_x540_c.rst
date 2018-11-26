.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_x540.c

.. _`ixgbe_setup_mac_link_x540`:

ixgbe_setup_mac_link_X540
=========================

.. c:function:: s32 ixgbe_setup_mac_link_X540(struct ixgbe_hw *hw, ixgbe_link_speed speed, bool autoneg_wait_to_complete)

    Set the auto advertised capabilitires

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        new link speed
    :type speed: ixgbe_link_speed

    :param autoneg_wait_to_complete:
        true when waiting for completion is needed
    :type autoneg_wait_to_complete: bool

.. _`ixgbe_reset_hw_x540`:

ixgbe_reset_hw_X540
===================

.. c:function:: s32 ixgbe_reset_hw_X540(struct ixgbe_hw *hw)

    Perform hardware reset

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_reset_hw_x540.description`:

Description
-----------

Resets the hardware by resetting the transmit and receive units, masks
and clears all interrupts, perform a PHY reset, and perform a link (MAC)
reset.

.. _`ixgbe_start_hw_x540`:

ixgbe_start_hw_X540
===================

.. c:function:: s32 ixgbe_start_hw_X540(struct ixgbe_hw *hw)

    Prepare hardware for Tx/Rx

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_start_hw_x540.description`:

Description
-----------

Starts the hardware using the generic start_hw function
and the generation start_hw function.
Then performs revision-specific operations, if any.

.. _`ixgbe_init_eeprom_params_x540`:

ixgbe_init_eeprom_params_X540
=============================

.. c:function:: s32 ixgbe_init_eeprom_params_X540(struct ixgbe_hw *hw)

    Initialize EEPROM params

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_init_eeprom_params_x540.description`:

Description
-----------

Initializes the EEPROM parameters ixgbe_eeprom_info within the
ixgbe_hw struct in order to set up EEPROM access.

.. _`ixgbe_read_eerd_x540`:

ixgbe_read_eerd_X540
====================

.. c:function:: s32 ixgbe_read_eerd_X540(struct ixgbe_hw *hw, u16 offset, u16 *data)

    Read EEPROM word using EERD

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param offset:
        offset of  word in the EEPROM to read
    :type offset: u16

    :param data:
        word read from the EEPROM
    :type data: u16 \*

.. _`ixgbe_read_eerd_x540.description`:

Description
-----------

Reads a 16 bit word from the EEPROM using the EERD register.

.. _`ixgbe_read_eerd_buffer_x540`:

ixgbe_read_eerd_buffer_X540
===========================

.. c:function:: s32 ixgbe_read_eerd_buffer_X540(struct ixgbe_hw *hw, u16 offset, u16 words, u16 *data)

    Read EEPROM word(s) using EERD

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param offset:
        offset of  word in the EEPROM to read
    :type offset: u16

    :param words:
        number of words
    :type words: u16

    :param data:
        word(s) read from the EEPROM
    :type data: u16 \*

.. _`ixgbe_read_eerd_buffer_x540.description`:

Description
-----------

Reads a 16 bit word(s) from the EEPROM using the EERD register.

.. _`ixgbe_write_eewr_x540`:

ixgbe_write_eewr_X540
=====================

.. c:function:: s32 ixgbe_write_eewr_X540(struct ixgbe_hw *hw, u16 offset, u16 data)

    Write EEPROM word using EEWR

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param offset:
        offset of  word in the EEPROM to write
    :type offset: u16

    :param data:
        word write to the EEPROM
    :type data: u16

.. _`ixgbe_write_eewr_x540.description`:

Description
-----------

Write a 16 bit word to the EEPROM using the EEWR register.

.. _`ixgbe_write_eewr_buffer_x540`:

ixgbe_write_eewr_buffer_X540
============================

.. c:function:: s32 ixgbe_write_eewr_buffer_X540(struct ixgbe_hw *hw, u16 offset, u16 words, u16 *data)

    Write EEPROM word(s) using EEWR

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param offset:
        offset of  word in the EEPROM to write
    :type offset: u16

    :param words:
        number of words
    :type words: u16

    :param data:
        word(s) write to the EEPROM
    :type data: u16 \*

.. _`ixgbe_write_eewr_buffer_x540.description`:

Description
-----------

Write a 16 bit word(s) to the EEPROM using the EEWR register.

.. _`ixgbe_calc_eeprom_checksum_x540`:

ixgbe_calc_eeprom_checksum_X540
===============================

.. c:function:: s32 ixgbe_calc_eeprom_checksum_X540(struct ixgbe_hw *hw)

    Calculates and returns the checksum

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_calc_eeprom_checksum_x540.description`:

Description
-----------

This function does not use synchronization for EERD and EEWR. It can
be used internally by function which utilize ixgbe_acquire_swfw_sync_X540.

.. _`ixgbe_validate_eeprom_checksum_x540`:

ixgbe_validate_eeprom_checksum_X540
===================================

.. c:function:: s32 ixgbe_validate_eeprom_checksum_X540(struct ixgbe_hw *hw, u16 *checksum_val)

    Validate EEPROM checksum

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param checksum_val:
        calculated checksum
    :type checksum_val: u16 \*

.. _`ixgbe_validate_eeprom_checksum_x540.description`:

Description
-----------

Performs checksum calculation and validates the EEPROM checksum.  If the
caller does not need checksum_val, the value can be NULL.

.. _`ixgbe_update_eeprom_checksum_x540`:

ixgbe_update_eeprom_checksum_X540
=================================

.. c:function:: s32 ixgbe_update_eeprom_checksum_X540(struct ixgbe_hw *hw)

    Updates the EEPROM checksum and flash

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_update_eeprom_checksum_x540.description`:

Description
-----------

After writing EEPROM to shadow RAM using EEWR register, software calculates
checksum and updates the EEPROM and instructs the hardware to update
the flash.

.. _`ixgbe_update_flash_x540`:

ixgbe_update_flash_X540
=======================

.. c:function:: s32 ixgbe_update_flash_X540(struct ixgbe_hw *hw)

    Instruct HW to copy EEPROM to Flash device

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_update_flash_x540.description`:

Description
-----------

Set FLUP (bit 23) of the EEC register to instruct Hardware to copy
EEPROM from shadow RAM to the flash device.

.. _`ixgbe_poll_flash_update_done_x540`:

ixgbe_poll_flash_update_done_X540
=================================

.. c:function:: s32 ixgbe_poll_flash_update_done_X540(struct ixgbe_hw *hw)

    Poll flash update status

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_poll_flash_update_done_x540.description`:

Description
-----------

Polls the FLUDONE (bit 26) of the EEC Register to determine when the
flash update is done.

.. _`ixgbe_acquire_swfw_sync_x540`:

ixgbe_acquire_swfw_sync_X540
============================

.. c:function:: s32 ixgbe_acquire_swfw_sync_X540(struct ixgbe_hw *hw, u32 mask)

    Acquire SWFW semaphore

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param mask:
        Mask to specify which semaphore to acquire
    :type mask: u32

.. _`ixgbe_acquire_swfw_sync_x540.description`:

Description
-----------

Acquires the SWFW semaphore thought the SW_FW_SYNC register for
the specified function (CSR, PHY0, PHY1, NVM, Flash)

.. _`ixgbe_release_swfw_sync_x540`:

ixgbe_release_swfw_sync_X540
============================

.. c:function:: void ixgbe_release_swfw_sync_X540(struct ixgbe_hw *hw, u32 mask)

    Release SWFW semaphore

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param mask:
        Mask to specify which semaphore to release
    :type mask: u32

.. _`ixgbe_release_swfw_sync_x540.description`:

Description
-----------

Releases the SWFW semaphore through the SW_FW_SYNC register
for the specified function (CSR, PHY0, PHY1, EVM, Flash)

.. _`ixgbe_get_swfw_sync_semaphore`:

ixgbe_get_swfw_sync_semaphore
=============================

.. c:function:: s32 ixgbe_get_swfw_sync_semaphore(struct ixgbe_hw *hw)

    Get hardware semaphore

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_get_swfw_sync_semaphore.description`:

Description
-----------

Sets the hardware semaphores so SW/FW can gain control of shared resources

.. _`ixgbe_release_swfw_sync_semaphore`:

ixgbe_release_swfw_sync_semaphore
=================================

.. c:function:: void ixgbe_release_swfw_sync_semaphore(struct ixgbe_hw *hw)

    Release hardware semaphore

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_release_swfw_sync_semaphore.description`:

Description
-----------

This function clears hardware semaphore bits.

.. _`ixgbe_init_swfw_sync_x540`:

ixgbe_init_swfw_sync_X540
=========================

.. c:function:: void ixgbe_init_swfw_sync_X540(struct ixgbe_hw *hw)

    Release hardware semaphore

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_init_swfw_sync_x540.description`:

Description
-----------

This function reset hardware semaphore bits for a semaphore that may
have be left locked due to a catastrophic failure.

.. _`ixgbe_blink_led_start_x540`:

ixgbe_blink_led_start_X540
==========================

.. c:function:: s32 ixgbe_blink_led_start_X540(struct ixgbe_hw *hw, u32 index)

    Blink LED based on index.

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param index:
        led number to blink
    :type index: u32

.. _`ixgbe_blink_led_start_x540.devices-that-implement-the-version-2-interface`:

Devices that implement the version 2 interface
----------------------------------------------

X540

.. _`ixgbe_blink_led_stop_x540`:

ixgbe_blink_led_stop_X540
=========================

.. c:function:: s32 ixgbe_blink_led_stop_X540(struct ixgbe_hw *hw, u32 index)

    Stop blinking LED based on index.

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param index:
        led number to stop blinking
    :type index: u32

.. _`ixgbe_blink_led_stop_x540.devices-that-implement-the-version-2-interface`:

Devices that implement the version 2 interface
----------------------------------------------

X540

.. This file was automatic generated / don't edit.

