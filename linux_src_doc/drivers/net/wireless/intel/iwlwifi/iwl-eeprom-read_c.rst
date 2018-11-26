.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-eeprom-read.c

.. _`iwl_read_eeprom`:

iwl_read_eeprom
===============

.. c:function:: int iwl_read_eeprom(struct iwl_trans *trans, u8 **eeprom, size_t *eeprom_size)

    read EEPROM contents

    :param trans:
        *undescribed*
    :type trans: struct iwl_trans \*

    :param eeprom:
        *undescribed*
    :type eeprom: u8 \*\*

    :param eeprom_size:
        *undescribed*
    :type eeprom_size: size_t \*

.. _`iwl_read_eeprom.description`:

Description
-----------

Load the EEPROM contents from adapter and return it
and its size.

.. _`iwl_read_eeprom.note`:

NOTE
----

This routine uses the non-debug IO access functions.

.. This file was automatic generated / don't edit.

