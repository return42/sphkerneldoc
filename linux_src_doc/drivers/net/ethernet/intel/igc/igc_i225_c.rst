.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igc/igc_i225.c

.. _`igc_acquire_nvm_i225`:

igc_acquire_nvm_i225
====================

.. c:function:: s32 igc_acquire_nvm_i225(struct igc_hw *hw)

    Acquire hardware semaphore

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_acquire_nvm_i225.description`:

Description
-----------

Acquire the necessary semaphores for exclusive access to the EEPROM.
Set the EEPROM access request bit and wait for EEPROM access grant bit.
Return successful if access grant bit set, else clear the request for
EEPROM access and return -IGC_ERR_NVM (-1).

.. _`igc_release_nvm_i225`:

igc_release_nvm_i225
====================

.. c:function:: void igc_release_nvm_i225(struct igc_hw *hw)

    Release exclusive access to EEPROM

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_release_nvm_i225.description`:

Description
-----------

Stop any current commands to the EEPROM and clear the EEPROM request bit,
then release the semaphores acquired.

.. _`igc_get_hw_semaphore_i225`:

igc_get_hw_semaphore_i225
=========================

.. c:function:: s32 igc_get_hw_semaphore_i225(struct igc_hw *hw)

    Acquire hardware semaphore

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_get_hw_semaphore_i225.description`:

Description
-----------

Acquire the HW semaphore to access the PHY or NVM

.. _`igc_acquire_swfw_sync_i225`:

igc_acquire_swfw_sync_i225
==========================

.. c:function:: s32 igc_acquire_swfw_sync_i225(struct igc_hw *hw, u16 mask)

    Acquire SW/FW semaphore

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param mask:
        specifies which semaphore to acquire
    :type mask: u16

.. _`igc_acquire_swfw_sync_i225.description`:

Description
-----------

Acquire the SW/FW semaphore to access the PHY or NVM.  The mask
will also specify which port we're acquiring the lock for.

.. _`igc_release_swfw_sync_i225`:

igc_release_swfw_sync_i225
==========================

.. c:function:: void igc_release_swfw_sync_i225(struct igc_hw *hw, u16 mask)

    Release SW/FW semaphore

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param mask:
        specifies which semaphore to acquire
    :type mask: u16

.. _`igc_release_swfw_sync_i225.description`:

Description
-----------

Release the SW/FW semaphore used to access the PHY or NVM.  The mask
will also specify which port we're releasing the lock for.

.. _`igc_read_nvm_srrd_i225`:

igc_read_nvm_srrd_i225
======================

.. c:function:: s32 igc_read_nvm_srrd_i225(struct igc_hw *hw, u16 offset, u16 words, u16 *data)

    Reads Shadow Ram using EERD register

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param offset:
        offset of word in the Shadow Ram to read
    :type offset: u16

    :param words:
        number of words to read
    :type words: u16

    :param data:
        word read from the Shadow Ram
    :type data: u16 \*

.. _`igc_read_nvm_srrd_i225.description`:

Description
-----------

Reads a 16 bit word from the Shadow Ram using the EERD register.
Uses necessary synchronization semaphores.

.. _`igc_write_nvm_srwr`:

igc_write_nvm_srwr
==================

.. c:function:: s32 igc_write_nvm_srwr(struct igc_hw *hw, u16 offset, u16 words, u16 *data)

    Write to Shadow Ram using EEWR

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param offset:
        offset within the Shadow Ram to be written to
    :type offset: u16

    :param words:
        number of words to write
    :type words: u16

    :param data:
        16 bit word(s) to be written to the Shadow Ram
    :type data: u16 \*

.. _`igc_write_nvm_srwr.description`:

Description
-----------

Writes data to Shadow Ram at offset using EEWR register.

If igc_update_nvm_checksum is not called after this function , the
Shadow Ram will most likely contain an invalid checksum.

.. _`igc_write_nvm_srwr_i225`:

igc_write_nvm_srwr_i225
=======================

.. c:function:: s32 igc_write_nvm_srwr_i225(struct igc_hw *hw, u16 offset, u16 words, u16 *data)

    Write to Shadow RAM using EEWR

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param offset:
        offset within the Shadow RAM to be written to
    :type offset: u16

    :param words:
        number of words to write
    :type words: u16

    :param data:
        16 bit word(s) to be written to the Shadow RAM
    :type data: u16 \*

.. _`igc_write_nvm_srwr_i225.description`:

Description
-----------

Writes data to Shadow RAM at offset using EEWR register.

If igc_update_nvm_checksum is not called after this function , the
data will not be committed to FLASH and also Shadow RAM will most likely
contain an invalid checksum.

If error code is returned, data and Shadow RAM may be inconsistent - buffer
partially written.

.. _`igc_validate_nvm_checksum_i225`:

igc_validate_nvm_checksum_i225
==============================

.. c:function:: s32 igc_validate_nvm_checksum_i225(struct igc_hw *hw)

    Validate EEPROM checksum

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_validate_nvm_checksum_i225.description`:

Description
-----------

Calculates the EEPROM checksum by reading/adding each word of the EEPROM
and then verifies that the sum of the EEPROM is equal to 0xBABA.

.. _`igc_pool_flash_update_done_i225`:

igc_pool_flash_update_done_i225
===============================

.. c:function:: s32 igc_pool_flash_update_done_i225(struct igc_hw *hw)

    Pool FLUDONE status

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_update_flash_i225`:

igc_update_flash_i225
=====================

.. c:function:: s32 igc_update_flash_i225(struct igc_hw *hw)

    Commit EEPROM to the flash

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_update_nvm_checksum_i225`:

igc_update_nvm_checksum_i225
============================

.. c:function:: s32 igc_update_nvm_checksum_i225(struct igc_hw *hw)

    Update EEPROM checksum

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_update_nvm_checksum_i225.description`:

Description
-----------

Updates the EEPROM checksum by reading/adding each word of the EEPROM
up to the checksum.  Then calculates the EEPROM checksum and writes the
value to the EEPROM. Next commit EEPROM data onto the Flash.

.. _`igc_get_flash_presence_i225`:

igc_get_flash_presence_i225
===========================

.. c:function:: bool igc_get_flash_presence_i225(struct igc_hw *hw)

    Check if flash device is detected

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_init_nvm_params_i225`:

igc_init_nvm_params_i225
========================

.. c:function:: s32 igc_init_nvm_params_i225(struct igc_hw *hw)

    Init NVM func ptrs.

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. This file was automatic generated / don't edit.

