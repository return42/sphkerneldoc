.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_nvm.c

.. _`ice_aq_read_nvm`:

ice_aq_read_nvm
===============

.. c:function:: enum ice_status ice_aq_read_nvm(struct ice_hw *hw, u16 module_typeid, u32 offset, u16 length, void *data, bool last_command, struct ice_sq_cd *cd)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param module_typeid:
        module pointer location in words from the NVM beginning
    :type module_typeid: u16

    :param offset:
        byte offset from the module beginning
    :type offset: u32

    :param length:
        length of the section to be read (in bytes from the offset)
    :type length: u16

    :param data:
        command buffer (size [bytes] = length)
    :type data: void \*

    :param last_command:
        tells if this is the last command in a series
    :type last_command: bool

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_read_nvm.description`:

Description
-----------

Read the NVM using the admin queue commands (0x0701)

.. _`ice_check_sr_access_params`:

ice_check_sr_access_params
==========================

.. c:function:: enum ice_status ice_check_sr_access_params(struct ice_hw *hw, u32 offset, u16 words)

    verify params for Shadow RAM R/W operations.

    :param hw:
        pointer to the HW structure
    :type hw: struct ice_hw \*

    :param offset:
        offset in words from module start
    :type offset: u32

    :param words:
        number of words to access
    :type words: u16

.. _`ice_read_sr_aq`:

ice_read_sr_aq
==============

.. c:function:: enum ice_status ice_read_sr_aq(struct ice_hw *hw, u32 offset, u16 words, u16 *data, bool last_command)

    Read Shadow RAM.

    :param hw:
        pointer to the HW structure
    :type hw: struct ice_hw \*

    :param offset:
        offset in words from module start
    :type offset: u32

    :param words:
        number of words to read
    :type words: u16

    :param data:
        buffer for words reads from Shadow RAM
    :type data: u16 \*

    :param last_command:
        tells the AdminQ that this is the last command
    :type last_command: bool

.. _`ice_read_sr_aq.description`:

Description
-----------

Reads 16-bit word buffers from the Shadow RAM using the admin command.

.. _`ice_read_sr_word_aq`:

ice_read_sr_word_aq
===================

.. c:function:: enum ice_status ice_read_sr_word_aq(struct ice_hw *hw, u16 offset, u16 *data)

    Reads Shadow RAM via AQ

    :param hw:
        pointer to the HW structure
    :type hw: struct ice_hw \*

    :param offset:
        offset of the Shadow RAM word to read (0x000000 - 0x001FFF)
    :type offset: u16

    :param data:
        word read from the Shadow RAM
    :type data: u16 \*

.. _`ice_read_sr_word_aq.description`:

Description
-----------

Reads one 16 bit word from the Shadow RAM using the ice_read_sr_aq method.

.. _`ice_acquire_nvm`:

ice_acquire_nvm
===============

.. c:function:: enum ice_status ice_acquire_nvm(struct ice_hw *hw, enum ice_aq_res_access_type access)

    Generic request for acquiring the NVM ownership

    :param hw:
        pointer to the HW structure
    :type hw: struct ice_hw \*

    :param access:
        NVM access type (read or write)
    :type access: enum ice_aq_res_access_type

.. _`ice_acquire_nvm.description`:

Description
-----------

This function will request NVM ownership.

.. _`ice_release_nvm`:

ice_release_nvm
===============

.. c:function:: void ice_release_nvm(struct ice_hw *hw)

    Generic request for releasing the NVM ownership

    :param hw:
        pointer to the HW structure
    :type hw: struct ice_hw \*

.. _`ice_release_nvm.description`:

Description
-----------

This function will release NVM ownership.

.. _`ice_read_sr_word`:

ice_read_sr_word
================

.. c:function:: enum ice_status ice_read_sr_word(struct ice_hw *hw, u16 offset, u16 *data)

    Reads Shadow RAM word and acquire NVM if necessary

    :param hw:
        pointer to the HW structure
    :type hw: struct ice_hw \*

    :param offset:
        offset of the Shadow RAM word to read (0x000000 - 0x001FFF)
    :type offset: u16

    :param data:
        word read from the Shadow RAM
    :type data: u16 \*

.. _`ice_read_sr_word.description`:

Description
-----------

Reads one 16 bit word from the Shadow RAM using the ice_read_sr_word_aq.

.. _`ice_init_nvm`:

ice_init_nvm
============

.. c:function:: enum ice_status ice_init_nvm(struct ice_hw *hw)

    initializes NVM setting

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_init_nvm.description`:

Description
-----------

This function reads and populates NVM settings such as Shadow RAM size,
max_timeout, and blank_nvm_mode

.. This file was automatic generated / don't edit.

