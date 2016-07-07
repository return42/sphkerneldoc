.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igb/e1000_nvm.c

.. _`igb_raise_eec_clk`:

igb_raise_eec_clk
=================

.. c:function:: void igb_raise_eec_clk(struct e1000_hw *hw, u32 *eecd)

    Raise EEPROM clock

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 \*eecd:
        pointer to the EEPROM

.. _`igb_raise_eec_clk.description`:

Description
-----------

Enable/Raise the EEPROM clock bit.

.. _`igb_lower_eec_clk`:

igb_lower_eec_clk
=================

.. c:function:: void igb_lower_eec_clk(struct e1000_hw *hw, u32 *eecd)

    Lower EEPROM clock

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 \*eecd:
        pointer to the EEPROM

.. _`igb_lower_eec_clk.description`:

Description
-----------

Clear/Lower the EEPROM clock bit.

.. _`igb_shift_out_eec_bits`:

igb_shift_out_eec_bits
======================

.. c:function:: void igb_shift_out_eec_bits(struct e1000_hw *hw, u16 data, u16 count)

    Shift data bits our to the EEPROM

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 data:
        data to send to the EEPROM

    :param u16 count:
        number of bits to shift out

.. _`igb_shift_out_eec_bits.description`:

Description
-----------

We need to shift 'count' bits out to the EEPROM.  So, the value in the
"data" parameter will be shifted out to the EEPROM one bit at a time.
In order to do this, "data" must be broken down into bits.

.. _`igb_shift_in_eec_bits`:

igb_shift_in_eec_bits
=====================

.. c:function:: u16 igb_shift_in_eec_bits(struct e1000_hw *hw, u16 count)

    Shift data bits in from the EEPROM

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 count:
        number of bits to shift in

.. _`igb_shift_in_eec_bits.description`:

Description
-----------

In order to read a register from the EEPROM, we need to shift 'count' bits
in from the EEPROM.  Bits are "shifted in" by raising the clock input to
the EEPROM (setting the SK bit), and then reading the value of the data out
"DO" bit.  During this "shifting in" process the data in "DI" bit should
always be clear.

.. _`igb_poll_eerd_eewr_done`:

igb_poll_eerd_eewr_done
=======================

.. c:function:: s32 igb_poll_eerd_eewr_done(struct e1000_hw *hw, int ee_reg)

    Poll for EEPROM read/write completion

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param int ee_reg:
        EEPROM flag for polling

.. _`igb_poll_eerd_eewr_done.description`:

Description
-----------

Polls the EEPROM status bit for either read or write completion based
upon the value of 'ee_reg'.

.. _`igb_acquire_nvm`:

igb_acquire_nvm
===============

.. c:function:: s32 igb_acquire_nvm(struct e1000_hw *hw)

    Generic request for access to EEPROM

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_acquire_nvm.description`:

Description
-----------

Set the EEPROM access request bit and wait for EEPROM access grant bit.
Return successful if access grant bit set, else clear the request for
EEPROM access and return -E1000_ERR_NVM (-1).

.. _`igb_standby_nvm`:

igb_standby_nvm
===============

.. c:function:: void igb_standby_nvm(struct e1000_hw *hw)

    Return EEPROM to standby state

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_standby_nvm.description`:

Description
-----------

Return the EEPROM to a standby state.

.. _`e1000_stop_nvm`:

e1000_stop_nvm
==============

.. c:function:: void e1000_stop_nvm(struct e1000_hw *hw)

    Terminate EEPROM command

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_stop_nvm.description`:

Description
-----------

Terminates the current command by inverting the EEPROM's chip select pin.

.. _`igb_release_nvm`:

igb_release_nvm
===============

.. c:function:: void igb_release_nvm(struct e1000_hw *hw)

    Release exclusive access to EEPROM

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_release_nvm.description`:

Description
-----------

Stop any current commands to the EEPROM and clear the EEPROM request bit.

.. _`igb_ready_nvm_eeprom`:

igb_ready_nvm_eeprom
====================

.. c:function:: s32 igb_ready_nvm_eeprom(struct e1000_hw *hw)

    Prepares EEPROM for read/write

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_ready_nvm_eeprom.description`:

Description
-----------

Setups the EEPROM for reading and writing.

.. _`igb_read_nvm_spi`:

igb_read_nvm_spi
================

.. c:function:: s32 igb_read_nvm_spi(struct e1000_hw *hw, u16 offset, u16 words, u16 *data)

    Read EEPROM's using SPI

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 offset:
        offset of word in the EEPROM to read

    :param u16 words:
        number of words to read

    :param u16 \*data:
        word read from the EEPROM

.. _`igb_read_nvm_spi.description`:

Description
-----------

Reads a 16 bit word from the EEPROM.

.. _`igb_read_nvm_eerd`:

igb_read_nvm_eerd
=================

.. c:function:: s32 igb_read_nvm_eerd(struct e1000_hw *hw, u16 offset, u16 words, u16 *data)

    Reads EEPROM using EERD register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 offset:
        offset of word in the EEPROM to read

    :param u16 words:
        number of words to read

    :param u16 \*data:
        word read from the EEPROM

.. _`igb_read_nvm_eerd.description`:

Description
-----------

Reads a 16 bit word from the EEPROM using the EERD register.

.. _`igb_write_nvm_spi`:

igb_write_nvm_spi
=================

.. c:function:: s32 igb_write_nvm_spi(struct e1000_hw *hw, u16 offset, u16 words, u16 *data)

    Write to EEPROM using SPI

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 offset:
        offset within the EEPROM to be written to

    :param u16 words:
        number of words to write

    :param u16 \*data:
        16 bit word(s) to be written to the EEPROM

.. _`igb_write_nvm_spi.description`:

Description
-----------

Writes data to EEPROM at offset using SPI interface.

If e1000_update_nvm_checksum is not called after this function , the
EEPROM will most likley contain an invalid checksum.

.. _`igb_read_part_string`:

igb_read_part_string
====================

.. c:function:: s32 igb_read_part_string(struct e1000_hw *hw, u8 *part_num, u32 part_num_size)

    Read device part number

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u8 \*part_num:
        pointer to device part number

    :param u32 part_num_size:
        size of part number buffer

.. _`igb_read_part_string.description`:

Description
-----------

Reads the product board assembly (PBA) number from the EEPROM and stores
the value in part_num.

.. _`igb_read_mac_addr`:

igb_read_mac_addr
=================

.. c:function:: s32 igb_read_mac_addr(struct e1000_hw *hw)

    Read device MAC address

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_read_mac_addr.description`:

Description
-----------

Reads the device MAC address from the EEPROM and stores the value.
Since devices with two ports use the same EEPROM, we increment the
last bit in the MAC address for the second port.

.. _`igb_validate_nvm_checksum`:

igb_validate_nvm_checksum
=========================

.. c:function:: s32 igb_validate_nvm_checksum(struct e1000_hw *hw)

    Validate EEPROM checksum

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_validate_nvm_checksum.description`:

Description
-----------

Calculates the EEPROM checksum by reading/adding each word of the EEPROM
and then verifies that the sum of the EEPROM is equal to 0xBABA.

.. _`igb_update_nvm_checksum`:

igb_update_nvm_checksum
=======================

.. c:function:: s32 igb_update_nvm_checksum(struct e1000_hw *hw)

    Update EEPROM checksum

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_update_nvm_checksum.description`:

Description
-----------

Updates the EEPROM checksum by reading/adding each word of the EEPROM
up to the checksum.  Then calculates the EEPROM checksum and writes the
value to the EEPROM.

.. _`igb_get_fw_version`:

igb_get_fw_version
==================

.. c:function:: void igb_get_fw_version(struct e1000_hw *hw, struct e1000_fw_version *fw_vers)

    Get firmware version information

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param struct e1000_fw_version \*fw_vers:
        pointer to output structure

.. _`igb_get_fw_version.description`:

Description
-----------

unsupported MAC types will return all 0 version structure

.. This file was automatic generated / don't edit.

