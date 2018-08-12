.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_nvm.c

.. _`ice_aq_read_nvm`:

ice_aq_read_nvm
===============

.. c:function:: enum ice_status ice_aq_read_nvm(struct ice_hw *hw, u16 module_typeid, u32 offset, u16 length, void *data, bool last_command, struct ice_sq_cd *cd)

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u16 module_typeid:
        module pointer location in words from the NVM beginning

    :param u32 offset:
        byte offset from the module beginning

    :param u16 length:
        length of the section to be read (in bytes from the offset)

    :param void \*data:
        command buffer (size [bytes] = length)

    :param bool last_command:
        tells if this is the last command in a series

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_read_nvm.description`:

Description
-----------

Read the NVM using the admin queue commands (0x0701)

.. _`ice_check_sr_access_params`:

ice_check_sr_access_params
==========================

.. c:function:: enum ice_status ice_check_sr_access_params(struct ice_hw *hw, u32 offset, u16 words)

    verify params for Shadow RAM R/W operations.

    :param struct ice_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        offset in words from module start

    :param u16 words:
        number of words to access

.. _`ice_read_sr_aq`:

ice_read_sr_aq
==============

.. c:function:: enum ice_status ice_read_sr_aq(struct ice_hw *hw, u32 offset, u16 words, u16 *data, bool last_command)

    Read Shadow RAM.

    :param struct ice_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        offset in words from module start

    :param u16 words:
        number of words to read

    :param u16 \*data:
        buffer for words reads from Shadow RAM

    :param bool last_command:
        tells the AdminQ that this is the last command

.. _`ice_read_sr_aq.description`:

Description
-----------

Reads 16-bit word buffers from the Shadow RAM using the admin command.

.. _`ice_read_sr_word_aq`:

ice_read_sr_word_aq
===================

.. c:function:: enum ice_status ice_read_sr_word_aq(struct ice_hw *hw, u16 offset, u16 *data)

    Reads Shadow RAM via AQ

    :param struct ice_hw \*hw:
        pointer to the HW structure

    :param u16 offset:
        offset of the Shadow RAM word to read (0x000000 - 0x001FFF)

    :param u16 \*data:
        word read from the Shadow RAM

.. _`ice_read_sr_word_aq.description`:

Description
-----------

Reads one 16 bit word from the Shadow RAM using the ice_read_sr_aq method.

.. _`ice_acquire_nvm`:

ice_acquire_nvm
===============

.. c:function:: enum ice_status ice_acquire_nvm(struct ice_hw *hw, enum ice_aq_res_access_type access)

    Generic request for acquiring the NVM ownership

    :param struct ice_hw \*hw:
        pointer to the HW structure

    :param enum ice_aq_res_access_type access:
        NVM access type (read or write)

.. _`ice_acquire_nvm.description`:

Description
-----------

This function will request NVM ownership.

.. _`ice_release_nvm`:

ice_release_nvm
===============

.. c:function:: void ice_release_nvm(struct ice_hw *hw)

    Generic request for releasing the NVM ownership

    :param struct ice_hw \*hw:
        pointer to the HW structure

.. _`ice_release_nvm.description`:

Description
-----------

This function will release NVM ownership.

.. _`ice_read_sr_word`:

ice_read_sr_word
================

.. c:function:: enum ice_status ice_read_sr_word(struct ice_hw *hw, u16 offset, u16 *data)

    Reads Shadow RAM word and acquire NVM if necessary

    :param struct ice_hw \*hw:
        pointer to the HW structure

    :param u16 offset:
        offset of the Shadow RAM word to read (0x000000 - 0x001FFF)

    :param u16 \*data:
        word read from the Shadow RAM

.. _`ice_read_sr_word.description`:

Description
-----------

Reads one 16 bit word from the Shadow RAM using the ice_read_sr_word_aq.

.. _`ice_init_nvm`:

ice_init_nvm
============

.. c:function:: enum ice_status ice_init_nvm(struct ice_hw *hw)

    initializes NVM setting

    :param struct ice_hw \*hw:
        pointer to the hw struct

.. _`ice_init_nvm.description`:

Description
-----------

This function reads and populates NVM settings such as Shadow RAM size,
max_timeout, and blank_nvm_mode

.. This file was automatic generated / don't edit.

