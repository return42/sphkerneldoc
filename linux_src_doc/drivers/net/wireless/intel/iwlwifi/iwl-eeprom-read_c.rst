.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-eeprom-read.c

.. _`iwl_read_eeprom`:

iwl_read_eeprom
===============

.. c:function:: int iwl_read_eeprom(struct iwl_trans *trans, u8 **eeprom, size_t *eeprom_size)

    read EEPROM contents

    :param struct iwl_trans \*trans:
        *undescribed*

    :param u8 \*\*eeprom:
        *undescribed*

    :param size_t \*eeprom_size:
        *undescribed*

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

