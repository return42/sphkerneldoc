.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/e1000e/nvm.c

.. _`e1000_raise_eec_clk`:

e1000_raise_eec_clk
===================

.. c:function:: void e1000_raise_eec_clk(struct e1000_hw *hw, u32 *eecd)

    Raise EEPROM clock

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param eecd:
        pointer to the EEPROM
    :type eecd: u32 \*

.. _`e1000_raise_eec_clk.description`:

Description
-----------

Enable/Raise the EEPROM clock bit.

.. _`e1000_lower_eec_clk`:

e1000_lower_eec_clk
===================

.. c:function:: void e1000_lower_eec_clk(struct e1000_hw *hw, u32 *eecd)

    Lower EEPROM clock

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param eecd:
        pointer to the EEPROM
    :type eecd: u32 \*

.. _`e1000_lower_eec_clk.description`:

Description
-----------

Clear/Lower the EEPROM clock bit.

.. _`e1000_shift_out_eec_bits`:

e1000_shift_out_eec_bits
========================

.. c:function:: void e1000_shift_out_eec_bits(struct e1000_hw *hw, u16 data, u16 count)

    Shift data bits our to the EEPROM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param data:
        data to send to the EEPROM
    :type data: u16

    :param count:
        number of bits to shift out
    :type count: u16

.. _`e1000_shift_out_eec_bits.description`:

Description
-----------

We need to shift 'count' bits out to the EEPROM.  So, the value in the
"data" parameter will be shifted out to the EEPROM one bit at a time.
In order to do this, "data" must be broken down into bits.

.. _`e1000_shift_in_eec_bits`:

e1000_shift_in_eec_bits
=======================

.. c:function:: u16 e1000_shift_in_eec_bits(struct e1000_hw *hw, u16 count)

    Shift data bits in from the EEPROM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param count:
        number of bits to shift in
    :type count: u16

.. _`e1000_shift_in_eec_bits.description`:

Description
-----------

In order to read a register from the EEPROM, we need to shift 'count' bits
in from the EEPROM.  Bits are "shifted in" by raising the clock input to
the EEPROM (setting the SK bit), and then reading the value of the data out
"DO" bit.  During this "shifting in" process the data in "DI" bit should
always be clear.

.. _`e1000e_poll_eerd_eewr_done`:

e1000e_poll_eerd_eewr_done
==========================

.. c:function:: s32 e1000e_poll_eerd_eewr_done(struct e1000_hw *hw, int ee_reg)

    Poll for EEPROM read/write completion

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param ee_reg:
        EEPROM flag for polling
    :type ee_reg: int

.. _`e1000e_poll_eerd_eewr_done.description`:

Description
-----------

Polls the EEPROM status bit for either read or write completion based
upon the value of 'ee_reg'.

.. _`e1000e_acquire_nvm`:

e1000e_acquire_nvm
==================

.. c:function:: s32 e1000e_acquire_nvm(struct e1000_hw *hw)

    Generic request for access to EEPROM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000e_acquire_nvm.description`:

Description
-----------

Set the EEPROM access request bit and wait for EEPROM access grant bit.
Return successful if access grant bit set, else clear the request for
EEPROM access and return -E1000_ERR_NVM (-1).

.. _`e1000_standby_nvm`:

e1000_standby_nvm
=================

.. c:function:: void e1000_standby_nvm(struct e1000_hw *hw)

    Return EEPROM to standby state

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_standby_nvm.description`:

Description
-----------

Return the EEPROM to a standby state.

.. _`e1000_stop_nvm`:

e1000_stop_nvm
==============

.. c:function:: void e1000_stop_nvm(struct e1000_hw *hw)

    Terminate EEPROM command

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_stop_nvm.description`:

Description
-----------

Terminates the current command by inverting the EEPROM's chip select pin.

.. _`e1000e_release_nvm`:

e1000e_release_nvm
==================

.. c:function:: void e1000e_release_nvm(struct e1000_hw *hw)

    Release exclusive access to EEPROM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000e_release_nvm.description`:

Description
-----------

Stop any current commands to the EEPROM and clear the EEPROM request bit.

.. _`e1000_ready_nvm_eeprom`:

e1000_ready_nvm_eeprom
======================

.. c:function:: s32 e1000_ready_nvm_eeprom(struct e1000_hw *hw)

    Prepares EEPROM for read/write

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_ready_nvm_eeprom.description`:

Description
-----------

Setups the EEPROM for reading and writing.

.. _`e1000e_read_nvm_eerd`:

e1000e_read_nvm_eerd
====================

.. c:function:: s32 e1000e_read_nvm_eerd(struct e1000_hw *hw, u16 offset, u16 words, u16 *data)

    Reads EEPROM using EERD register

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        offset of word in the EEPROM to read
    :type offset: u16

    :param words:
        number of words to read
    :type words: u16

    :param data:
        word read from the EEPROM
    :type data: u16 \*

.. _`e1000e_read_nvm_eerd.description`:

Description
-----------

Reads a 16 bit word from the EEPROM using the EERD register.

.. _`e1000e_write_nvm_spi`:

e1000e_write_nvm_spi
====================

.. c:function:: s32 e1000e_write_nvm_spi(struct e1000_hw *hw, u16 offset, u16 words, u16 *data)

    Write to EEPROM using SPI

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        offset within the EEPROM to be written to
    :type offset: u16

    :param words:
        number of words to write
    :type words: u16

    :param data:
        16 bit word(s) to be written to the EEPROM
    :type data: u16 \*

.. _`e1000e_write_nvm_spi.description`:

Description
-----------

Writes data to EEPROM at offset using SPI interface.

If e1000e_update_nvm_checksum is not called after this function , the
EEPROM will most likely contain an invalid checksum.

.. _`e1000_read_pba_string_generic`:

e1000_read_pba_string_generic
=============================

.. c:function:: s32 e1000_read_pba_string_generic(struct e1000_hw *hw, u8 *pba_num, u32 pba_num_size)

    Read device part number

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param pba_num:
        pointer to device part number
    :type pba_num: u8 \*

    :param pba_num_size:
        size of part number buffer
    :type pba_num_size: u32

.. _`e1000_read_pba_string_generic.description`:

Description
-----------

Reads the product board assembly (PBA) number from the EEPROM and stores
the value in pba_num.

.. _`e1000_read_mac_addr_generic`:

e1000_read_mac_addr_generic
===========================

.. c:function:: s32 e1000_read_mac_addr_generic(struct e1000_hw *hw)

    Read device MAC address

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_read_mac_addr_generic.description`:

Description
-----------

Reads the device MAC address from the EEPROM and stores the value.
Since devices with two ports use the same EEPROM, we increment the
last bit in the MAC address for the second port.

.. _`e1000e_validate_nvm_checksum_generic`:

e1000e_validate_nvm_checksum_generic
====================================

.. c:function:: s32 e1000e_validate_nvm_checksum_generic(struct e1000_hw *hw)

    Validate EEPROM checksum

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000e_validate_nvm_checksum_generic.description`:

Description
-----------

Calculates the EEPROM checksum by reading/adding each word of the EEPROM
and then verifies that the sum of the EEPROM is equal to 0xBABA.

.. _`e1000e_update_nvm_checksum_generic`:

e1000e_update_nvm_checksum_generic
==================================

.. c:function:: s32 e1000e_update_nvm_checksum_generic(struct e1000_hw *hw)

    Update EEPROM checksum

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000e_update_nvm_checksum_generic.description`:

Description
-----------

Updates the EEPROM checksum by reading/adding each word of the EEPROM
up to the checksum.  Then calculates the EEPROM checksum and writes the
value to the EEPROM.

.. _`e1000e_reload_nvm_generic`:

e1000e_reload_nvm_generic
=========================

.. c:function:: void e1000e_reload_nvm_generic(struct e1000_hw *hw)

    Reloads EEPROM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000e_reload_nvm_generic.description`:

Description
-----------

Reloads the EEPROM by setting the "Reinitialize from EEPROM" bit in the
extended control register.

.. This file was automatic generated / don't edit.

