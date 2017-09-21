.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-nvm-parse.h

.. _`iwl_parse_nvm_data`:

iwl_parse_nvm_data
==================

.. c:function:: struct iwl_nvm_data *iwl_parse_nvm_data(struct iwl_trans *trans, const struct iwl_cfg *cfg, const __be16 *nvm_hw, const __le16 *nvm_sw, const __le16 *nvm_calib, const __le16 *regulatory, const __le16 *mac_override, const __le16 *phy_sku, u8 tx_chains, u8 rx_chains, bool lar_fw_supported)

    parse NVM data and return values

    :param struct iwl_trans \*trans:
        *undescribed*

    :param const struct iwl_cfg \*cfg:
        *undescribed*

    :param const __be16 \*nvm_hw:
        *undescribed*

    :param const __le16 \*nvm_sw:
        *undescribed*

    :param const __le16 \*nvm_calib:
        *undescribed*

    :param const __le16 \*regulatory:
        *undescribed*

    :param const __le16 \*mac_override:
        *undescribed*

    :param const __le16 \*phy_sku:
        *undescribed*

    :param u8 tx_chains:
        *undescribed*

    :param u8 rx_chains:
        *undescribed*

    :param bool lar_fw_supported:
        *undescribed*

.. _`iwl_parse_nvm_data.description`:

Description
-----------

This function parses all NVM values we need and then
returns a (newly allocated) struct containing all the
relevant values for driver use. The struct must be freed
later with \ :c:func:`iwl_free_nvm_data`\ .

.. _`iwl_set_hw_address_from_csr`:

iwl_set_hw_address_from_csr
===========================

.. c:function:: void iwl_set_hw_address_from_csr(struct iwl_trans *trans, struct iwl_nvm_data *data)

    sets HW address for 9000 devices and on

    :param struct iwl_trans \*trans:
        *undescribed*

    :param struct iwl_nvm_data \*data:
        *undescribed*

.. _`iwl_init_sbands`:

iwl_init_sbands
===============

.. c:function:: void iwl_init_sbands(struct device *dev, const struct iwl_cfg *cfg, struct iwl_nvm_data *data, const __le16 *nvm_ch_flags, u8 tx_chains, u8 rx_chains, bool lar_supported, bool no_wide_in_5ghz)

    parse and set all channel profiles

    :param struct device \*dev:
        *undescribed*

    :param const struct iwl_cfg \*cfg:
        *undescribed*

    :param struct iwl_nvm_data \*data:
        *undescribed*

    :param const __le16 \*nvm_ch_flags:
        *undescribed*

    :param u8 tx_chains:
        *undescribed*

    :param u8 rx_chains:
        *undescribed*

    :param bool lar_supported:
        *undescribed*

    :param bool no_wide_in_5ghz:
        *undescribed*

.. _`iwl_parse_nvm_mcc_info`:

iwl_parse_nvm_mcc_info
======================

.. c:function:: struct ieee80211_regdomain *iwl_parse_nvm_mcc_info(struct device *dev, const struct iwl_cfg *cfg, int num_of_ch, __le32 *channels, u16 fw_mcc)

    parse MCC (mobile country code) info coming from FW

    :param struct device \*dev:
        *undescribed*

    :param const struct iwl_cfg \*cfg:
        *undescribed*

    :param int num_of_ch:
        *undescribed*

    :param __le32 \*channels:
        *undescribed*

    :param u16 fw_mcc:
        *undescribed*

.. _`iwl_parse_nvm_mcc_info.description`:

Description
-----------

This function parses the regulatory channel data received as a
MCC_UPDATE_CMD command. It returns a newly allocation regulatory domain,
to be fed into the regulatory core. An ERR_PTR is returned on error.
If not given to the regulatory core, the user is responsible for freeing
the regdomain returned here with kfree.

.. _`iwl_get_bios_mcc`:

iwl_get_bios_mcc
================

.. c:function:: int iwl_get_bios_mcc(struct device *dev, char *mcc)

    read MCC from BIOS, if available

    :param struct device \*dev:
        the struct device

    :param char \*mcc:
        output buffer (3 bytes) that will get the MCC

.. _`iwl_get_bios_mcc.description`:

Description
-----------

This function tries to read the current MCC from ACPI if available.

.. This file was automatic generated / don't edit.

