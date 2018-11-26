.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igc/igc_nvm.c

.. _`igc_poll_eerd_eewr_done`:

igc_poll_eerd_eewr_done
=======================

.. c:function:: s32 igc_poll_eerd_eewr_done(struct igc_hw *hw, int ee_reg)

    Poll for EEPROM read/write completion

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param ee_reg:
        EEPROM flag for polling
    :type ee_reg: int

.. _`igc_poll_eerd_eewr_done.description`:

Description
-----------

Polls the EEPROM status bit for either read or write completion based
upon the value of 'ee_reg'.

.. _`igc_acquire_nvm`:

igc_acquire_nvm
===============

.. c:function:: s32 igc_acquire_nvm(struct igc_hw *hw)

    Generic request for access to EEPROM

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_acquire_nvm.description`:

Description
-----------

Set the EEPROM access request bit and wait for EEPROM access grant bit.
Return successful if access grant bit set, else clear the request for
EEPROM access and return -IGC_ERR_NVM (-1).

.. _`igc_release_nvm`:

igc_release_nvm
===============

.. c:function:: void igc_release_nvm(struct igc_hw *hw)

    Release exclusive access to EEPROM

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_release_nvm.description`:

Description
-----------

Stop any current commands to the EEPROM and clear the EEPROM request bit.

.. _`igc_read_nvm_eerd`:

igc_read_nvm_eerd
=================

.. c:function:: s32 igc_read_nvm_eerd(struct igc_hw *hw, u16 offset, u16 words, u16 *data)

    Reads EEPROM using EERD register

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param offset:
        offset of word in the EEPROM to read
    :type offset: u16

    :param words:
        number of words to read
    :type words: u16

    :param data:
        word read from the EEPROM
    :type data: u16 \*

.. _`igc_read_nvm_eerd.description`:

Description
-----------

Reads a 16 bit word from the EEPROM using the EERD register.

.. _`igc_read_mac_addr`:

igc_read_mac_addr
=================

.. c:function:: s32 igc_read_mac_addr(struct igc_hw *hw)

    Read device MAC address

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_validate_nvm_checksum`:

igc_validate_nvm_checksum
=========================

.. c:function:: s32 igc_validate_nvm_checksum(struct igc_hw *hw)

    Validate EEPROM checksum

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_validate_nvm_checksum.description`:

Description
-----------

Calculates the EEPROM checksum by reading/adding each word of the EEPROM
and then verifies that the sum of the EEPROM is equal to 0xBABA.

.. _`igc_update_nvm_checksum`:

igc_update_nvm_checksum
=======================

.. c:function:: s32 igc_update_nvm_checksum(struct igc_hw *hw)

    Update EEPROM checksum

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_update_nvm_checksum.description`:

Description
-----------

Updates the EEPROM checksum by reading/adding each word of the EEPROM
up to the checksum.  Then calculates the EEPROM checksum and writes the
value to the EEPROM.

.. This file was automatic generated / don't edit.

