.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-eeprom-parse.h

.. _`iwl_parse_eeprom_data`:

iwl_parse_eeprom_data
=====================

.. c:function:: struct iwl_nvm_data *iwl_parse_eeprom_data(struct device *dev, const struct iwl_cfg *cfg, const u8 *eeprom, size_t eeprom_size)

    parse EEPROM data and return values

    :param struct device \*dev:
        device pointer we're parsing for, for debug only

    :param const struct iwl_cfg \*cfg:
        device configuration for parsing and overrides

    :param const u8 \*eeprom:
        the EEPROM data

    :param size_t eeprom_size:
        length of the EEPROM data

.. _`iwl_parse_eeprom_data.description`:

Description
-----------

This function parses all EEPROM values we need and then
returns a (newly allocated) struct containing all the
relevant values for driver use. The struct must be freed
later with \ :c:func:`iwl_free_nvm_data`\ .

.. This file was automatic generated / don't edit.

