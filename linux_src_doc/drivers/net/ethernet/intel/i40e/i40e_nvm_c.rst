.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_nvm.c

.. _`i40e_init_nvm`:

i40e_init_nvm
=============

.. c:function:: i40e_status i40e_init_nvm(struct i40e_hw *hw)

    Initialize NVM function pointers

    :param struct i40e_hw \*hw:
        pointer to the HW structure

.. _`i40e_init_nvm.description`:

Description
-----------

Setup the function pointers and the NVM info structure. Should be called
once per NVM initialization, e.g. inside the \ :c:func:`i40e_init_shared_code`\ .
Please notice that the NVM term is used here (& in all methods covered
in this file) as an equivalent of the FLASH part mapped into the SR.
We are accessing FLASH always thru the Shadow RAM.

.. _`i40e_acquire_nvm`:

i40e_acquire_nvm
================

.. c:function:: i40e_status i40e_acquire_nvm(struct i40e_hw *hw, enum i40e_aq_resource_access_type access)

    Generic request for acquiring the NVM ownership

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param enum i40e_aq_resource_access_type access:
        NVM access type (read or write)

.. _`i40e_acquire_nvm.description`:

Description
-----------

This function will request NVM ownership for reading
via the proper Admin Command.

.. _`i40e_release_nvm`:

i40e_release_nvm
================

.. c:function:: void i40e_release_nvm(struct i40e_hw *hw)

    Generic request for releasing the NVM ownership

    :param struct i40e_hw \*hw:
        pointer to the HW structure

.. _`i40e_release_nvm.description`:

Description
-----------

This function will release NVM resource via the proper Admin Command.

.. _`i40e_poll_sr_srctl_done_bit`:

i40e_poll_sr_srctl_done_bit
===========================

.. c:function:: i40e_status i40e_poll_sr_srctl_done_bit(struct i40e_hw *hw)

    Polls the GLNVM_SRCTL done bit

    :param struct i40e_hw \*hw:
        pointer to the HW structure

.. _`i40e_poll_sr_srctl_done_bit.description`:

Description
-----------

Polls the SRCTL Shadow RAM register done bit.

.. _`i40e_read_nvm_word_srctl`:

i40e_read_nvm_word_srctl
========================

.. c:function:: i40e_status i40e_read_nvm_word_srctl(struct i40e_hw *hw, u16 offset, u16 *data)

    Reads Shadow RAM via SRCTL register

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param u16 offset:
        offset of the Shadow RAM word to read (0x000000 - 0x001FFF)

    :param u16 \*data:
        word read from the Shadow RAM

.. _`i40e_read_nvm_word_srctl.description`:

Description
-----------

Reads one 16 bit word from the Shadow RAM using the GLNVM_SRCTL register.

.. _`i40e_read_nvm_aq`:

i40e_read_nvm_aq
================

.. c:function:: i40e_status i40e_read_nvm_aq(struct i40e_hw *hw, u8 module_pointer, u32 offset, u16 words, void *data, bool last_command)

    Read Shadow RAM.

    :param struct i40e_hw \*hw:
        pointer to the HW structure.

    :param u8 module_pointer:
        module pointer location in words from the NVM beginning

    :param u32 offset:
        offset in words from module start

    :param u16 words:
        number of words to write

    :param void \*data:
        buffer with words to write to the Shadow RAM

    :param bool last_command:
        tells the AdminQ that this is the last command

.. _`i40e_read_nvm_aq.description`:

Description
-----------

Writes a 16 bit words buffer to the Shadow RAM using the admin command.

.. _`i40e_read_nvm_word_aq`:

i40e_read_nvm_word_aq
=====================

.. c:function:: i40e_status i40e_read_nvm_word_aq(struct i40e_hw *hw, u16 offset, u16 *data)

    Reads Shadow RAM via AQ

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param u16 offset:
        offset of the Shadow RAM word to read (0x000000 - 0x001FFF)

    :param u16 \*data:
        word read from the Shadow RAM

.. _`i40e_read_nvm_word_aq.description`:

Description
-----------

Reads one 16 bit word from the Shadow RAM using the AdminQ

.. _`__i40e_read_nvm_word`:

__i40e_read_nvm_word
====================

.. c:function:: i40e_status __i40e_read_nvm_word(struct i40e_hw *hw, u16 offset, u16 *data)

    Reads nvm word, assumes caller does the locking

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param u16 offset:
        offset of the Shadow RAM word to read (0x000000 - 0x001FFF)

    :param u16 \*data:
        word read from the Shadow RAM

.. _`__i40e_read_nvm_word.description`:

Description
-----------

Reads one 16 bit word from the Shadow RAM.

Do not use this function except in cases where the nvm lock is already
taken via \ :c:func:`i40e_acquire_nvm`\ .

.. _`i40e_read_nvm_word`:

i40e_read_nvm_word
==================

.. c:function:: i40e_status i40e_read_nvm_word(struct i40e_hw *hw, u16 offset, u16 *data)

    Reads nvm word and acquire lock if necessary

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param u16 offset:
        offset of the Shadow RAM word to read (0x000000 - 0x001FFF)

    :param u16 \*data:
        word read from the Shadow RAM

.. _`i40e_read_nvm_word.description`:

Description
-----------

Reads one 16 bit word from the Shadow RAM.

.. _`i40e_read_nvm_buffer_srctl`:

i40e_read_nvm_buffer_srctl
==========================

.. c:function:: i40e_status i40e_read_nvm_buffer_srctl(struct i40e_hw *hw, u16 offset, u16 *words, u16 *data)

    Reads Shadow RAM buffer via SRCTL register

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param u16 offset:
        offset of the Shadow RAM word to read (0x000000 - 0x001FFF).

    :param u16 \*words:
        (in) number of words to read; (out) number of words actually read

    :param u16 \*data:
        words read from the Shadow RAM

.. _`i40e_read_nvm_buffer_srctl.description`:

Description
-----------

Reads 16 bit words (data buffer) from the SR using the \ :c:func:`i40e_read_nvm_srrd`\ 
method. The buffer read is preceded by the NVM ownership take
and followed by the release.

.. _`i40e_read_nvm_buffer_aq`:

i40e_read_nvm_buffer_aq
=======================

.. c:function:: i40e_status i40e_read_nvm_buffer_aq(struct i40e_hw *hw, u16 offset, u16 *words, u16 *data)

    Reads Shadow RAM buffer via AQ

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param u16 offset:
        offset of the Shadow RAM word to read (0x000000 - 0x001FFF).

    :param u16 \*words:
        (in) number of words to read; (out) number of words actually read

    :param u16 \*data:
        words read from the Shadow RAM

.. _`i40e_read_nvm_buffer_aq.description`:

Description
-----------

Reads 16 bit words (data buffer) from the SR using the \ :c:func:`i40e_read_nvm_aq`\ 
method. The buffer read is preceded by the NVM ownership take
and followed by the release.

.. _`__i40e_read_nvm_buffer`:

__i40e_read_nvm_buffer
======================

.. c:function:: i40e_status __i40e_read_nvm_buffer(struct i40e_hw *hw, u16 offset, u16 *words, u16 *data)

    Reads nvm buffer, caller must acquire lock

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param u16 offset:
        offset of the Shadow RAM word to read (0x000000 - 0x001FFF).

    :param u16 \*words:
        (in) number of words to read; (out) number of words actually read

    :param u16 \*data:
        words read from the Shadow RAM

.. _`__i40e_read_nvm_buffer.description`:

Description
-----------

Reads 16 bit words (data buffer) from the SR using the \ :c:func:`i40e_read_nvm_srrd`\ 
method.

.. _`i40e_write_nvm_aq`:

i40e_write_nvm_aq
=================

.. c:function:: i40e_status i40e_write_nvm_aq(struct i40e_hw *hw, u8 module_pointer, u32 offset, u16 words, void *data, bool last_command)

    Writes Shadow RAM.

    :param struct i40e_hw \*hw:
        pointer to the HW structure.

    :param u8 module_pointer:
        module pointer location in words from the NVM beginning

    :param u32 offset:
        offset in words from module start

    :param u16 words:
        number of words to write

    :param void \*data:
        buffer with words to write to the Shadow RAM

    :param bool last_command:
        tells the AdminQ that this is the last command

.. _`i40e_write_nvm_aq.description`:

Description
-----------

Writes a 16 bit words buffer to the Shadow RAM using the admin command.

.. _`i40e_calc_nvm_checksum`:

i40e_calc_nvm_checksum
======================

.. c:function:: i40e_status i40e_calc_nvm_checksum(struct i40e_hw *hw, u16 *checksum)

    Calculates and returns the checksum

    :param struct i40e_hw \*hw:
        pointer to hardware structure

    :param u16 \*checksum:
        pointer to the checksum

.. _`i40e_calc_nvm_checksum.description`:

Description
-----------

This function calculates SW Checksum that covers the whole 64kB shadow RAM
except the VPD and PCIe ALT Auto-load modules. The structure and size of VPD
is customer specific and unknown. Therefore, this function skips all maximum
possible size of VPD (1kB).

.. _`i40e_update_nvm_checksum`:

i40e_update_nvm_checksum
========================

.. c:function:: i40e_status i40e_update_nvm_checksum(struct i40e_hw *hw)

    Updates the NVM checksum

    :param struct i40e_hw \*hw:
        pointer to hardware structure

.. _`i40e_update_nvm_checksum.description`:

Description
-----------

NVM ownership must be acquired before calling this function and released
on ARQ completion event reception by caller.
This function will commit SR to NVM.

.. _`i40e_validate_nvm_checksum`:

i40e_validate_nvm_checksum
==========================

.. c:function:: i40e_status i40e_validate_nvm_checksum(struct i40e_hw *hw, u16 *checksum)

    Validate EEPROM checksum

    :param struct i40e_hw \*hw:
        pointer to hardware structure

    :param u16 \*checksum:
        calculated checksum

.. _`i40e_validate_nvm_checksum.description`:

Description
-----------

Performs checksum calculation and validates the NVM SW checksum. If the
caller does not need checksum, the value can be NULL.

.. _`i40e_nvmupd_command`:

i40e_nvmupd_command
===================

.. c:function:: i40e_status i40e_nvmupd_command(struct i40e_hw *hw, struct i40e_nvm_access *cmd, u8 *bytes, int *perrno)

    Process an NVM update command

    :param struct i40e_hw \*hw:
        pointer to hardware structure

    :param struct i40e_nvm_access \*cmd:
        pointer to nvm update command

    :param u8 \*bytes:
        pointer to the data buffer

    :param int \*perrno:
        pointer to return error code

.. _`i40e_nvmupd_command.description`:

Description
-----------

Dispatches command depending on what update state is current

.. _`i40e_nvmupd_state_init`:

i40e_nvmupd_state_init
======================

.. c:function:: i40e_status i40e_nvmupd_state_init(struct i40e_hw *hw, struct i40e_nvm_access *cmd, u8 *bytes, int *perrno)

    Handle NVM update state Init

    :param struct i40e_hw \*hw:
        pointer to hardware structure

    :param struct i40e_nvm_access \*cmd:
        pointer to nvm update command buffer

    :param u8 \*bytes:
        pointer to the data buffer

    :param int \*perrno:
        pointer to return error code

.. _`i40e_nvmupd_state_init.description`:

Description
-----------

Process legitimate commands of the Init state and conditionally set next
state. Reject all other commands.

.. _`i40e_nvmupd_state_reading`:

i40e_nvmupd_state_reading
=========================

.. c:function:: i40e_status i40e_nvmupd_state_reading(struct i40e_hw *hw, struct i40e_nvm_access *cmd, u8 *bytes, int *perrno)

    Handle NVM update state Reading

    :param struct i40e_hw \*hw:
        pointer to hardware structure

    :param struct i40e_nvm_access \*cmd:
        pointer to nvm update command buffer

    :param u8 \*bytes:
        pointer to the data buffer

    :param int \*perrno:
        pointer to return error code

.. _`i40e_nvmupd_state_reading.description`:

Description
-----------

NVM ownership is already held.  Process legitimate commands and set any
change in state; reject all other commands.

.. _`i40e_nvmupd_state_writing`:

i40e_nvmupd_state_writing
=========================

.. c:function:: i40e_status i40e_nvmupd_state_writing(struct i40e_hw *hw, struct i40e_nvm_access *cmd, u8 *bytes, int *perrno)

    Handle NVM update state Writing

    :param struct i40e_hw \*hw:
        pointer to hardware structure

    :param struct i40e_nvm_access \*cmd:
        pointer to nvm update command buffer

    :param u8 \*bytes:
        pointer to the data buffer

    :param int \*perrno:
        pointer to return error code

.. _`i40e_nvmupd_state_writing.description`:

Description
-----------

NVM ownership is already held.  Process legitimate commands and set any
change in state; reject all other commands

.. _`i40e_nvmupd_check_wait_event`:

i40e_nvmupd_check_wait_event
============================

.. c:function:: void i40e_nvmupd_check_wait_event(struct i40e_hw *hw, u16 opcode)

    handle NVM update operation events

    :param struct i40e_hw \*hw:
        pointer to the hardware structure

    :param u16 opcode:
        the event that just happened

.. _`i40e_nvmupd_validate_command`:

i40e_nvmupd_validate_command
============================

.. c:function:: enum i40e_nvmupd_cmd i40e_nvmupd_validate_command(struct i40e_hw *hw, struct i40e_nvm_access *cmd, int *perrno)

    Validate given command

    :param struct i40e_hw \*hw:
        pointer to hardware structure

    :param struct i40e_nvm_access \*cmd:
        pointer to nvm update command buffer

    :param int \*perrno:
        pointer to return error code

.. _`i40e_nvmupd_validate_command.description`:

Description
-----------

Return one of the valid command types or I40E_NVMUPD_INVALID

.. _`i40e_nvmupd_exec_aq`:

i40e_nvmupd_exec_aq
===================

.. c:function:: i40e_status i40e_nvmupd_exec_aq(struct i40e_hw *hw, struct i40e_nvm_access *cmd, u8 *bytes, int *perrno)

    Run an AQ command

    :param struct i40e_hw \*hw:
        pointer to hardware structure

    :param struct i40e_nvm_access \*cmd:
        pointer to nvm update command buffer

    :param u8 \*bytes:
        pointer to the data buffer

    :param int \*perrno:
        pointer to return error code

.. _`i40e_nvmupd_exec_aq.description`:

Description
-----------

cmd structure contains identifiers and data buffer

.. _`i40e_nvmupd_get_aq_result`:

i40e_nvmupd_get_aq_result
=========================

.. c:function:: i40e_status i40e_nvmupd_get_aq_result(struct i40e_hw *hw, struct i40e_nvm_access *cmd, u8 *bytes, int *perrno)

    Get the results from the previous exec_aq

    :param struct i40e_hw \*hw:
        pointer to hardware structure

    :param struct i40e_nvm_access \*cmd:
        pointer to nvm update command buffer

    :param u8 \*bytes:
        pointer to the data buffer

    :param int \*perrno:
        pointer to return error code

.. _`i40e_nvmupd_get_aq_result.description`:

Description
-----------

cmd structure contains identifiers and data buffer

.. _`i40e_nvmupd_nvm_read`:

i40e_nvmupd_nvm_read
====================

.. c:function:: i40e_status i40e_nvmupd_nvm_read(struct i40e_hw *hw, struct i40e_nvm_access *cmd, u8 *bytes, int *perrno)

    Read NVM

    :param struct i40e_hw \*hw:
        pointer to hardware structure

    :param struct i40e_nvm_access \*cmd:
        pointer to nvm update command buffer

    :param u8 \*bytes:
        pointer to the data buffer

    :param int \*perrno:
        pointer to return error code

.. _`i40e_nvmupd_nvm_read.description`:

Description
-----------

cmd structure contains identifiers and data buffer

.. _`i40e_nvmupd_nvm_erase`:

i40e_nvmupd_nvm_erase
=====================

.. c:function:: i40e_status i40e_nvmupd_nvm_erase(struct i40e_hw *hw, struct i40e_nvm_access *cmd, int *perrno)

    Erase an NVM module

    :param struct i40e_hw \*hw:
        pointer to hardware structure

    :param struct i40e_nvm_access \*cmd:
        pointer to nvm update command buffer

    :param int \*perrno:
        pointer to return error code

.. _`i40e_nvmupd_nvm_erase.description`:

Description
-----------

module, offset, data_size and data are in cmd structure

.. _`i40e_nvmupd_nvm_write`:

i40e_nvmupd_nvm_write
=====================

.. c:function:: i40e_status i40e_nvmupd_nvm_write(struct i40e_hw *hw, struct i40e_nvm_access *cmd, u8 *bytes, int *perrno)

    Write NVM

    :param struct i40e_hw \*hw:
        pointer to hardware structure

    :param struct i40e_nvm_access \*cmd:
        pointer to nvm update command buffer

    :param u8 \*bytes:
        pointer to the data buffer

    :param int \*perrno:
        pointer to return error code

.. _`i40e_nvmupd_nvm_write.description`:

Description
-----------

module, offset, data_size and data are in cmd structure

.. This file was automatic generated / don't edit.

