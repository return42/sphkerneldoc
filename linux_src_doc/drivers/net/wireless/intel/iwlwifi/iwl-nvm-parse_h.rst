.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-nvm-parse.h

.. _`iwl_nvm_sbands_flags`:

enum iwl_nvm_sbands_flags
=========================

.. c:type:: enum iwl_nvm_sbands_flags

    modification flags for the channel profiles

.. _`iwl_nvm_sbands_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_nvm_sbands_flags {
        IWL_NVM_SBANDS_FLAGS_LAR,
        IWL_NVM_SBANDS_FLAGS_NO_WIDE_IN_5GHZ
    };

.. _`iwl_nvm_sbands_flags.constants`:

Constants
---------

IWL_NVM_SBANDS_FLAGS_LAR
    LAR is enabled

IWL_NVM_SBANDS_FLAGS_NO_WIDE_IN_5GHZ
    disallow 40, 80 and 160MHz on 5GHz

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

.. _`iwl_parse_nvm_mcc_info`:

iwl_parse_nvm_mcc_info
======================

.. c:function:: struct ieee80211_regdomain *iwl_parse_nvm_mcc_info(struct device *dev, const struct iwl_cfg *cfg, int num_of_ch, __le32 *channels, u16 fw_mcc, u16 geo_info)

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

    :param u16 geo_info:
        *undescribed*

.. _`iwl_parse_nvm_mcc_info.description`:

Description
-----------

This function parses the regulatory channel data received as a
MCC_UPDATE_CMD command. It returns a newly allocation regulatory domain,
to be fed into the regulatory core. In case the geo_info is set handle
accordingly. An ERR_PTR is returned on error.
If not given to the regulatory core, the user is responsible for freeing
the regdomain returned here with kfree.

.. _`iwl_nvm_section`:

struct iwl_nvm_section
======================

.. c:type:: struct iwl_nvm_section

    describes an NVM section in memory.

.. _`iwl_nvm_section.definition`:

Definition
----------

.. code-block:: c

    struct iwl_nvm_section {
        u16 length;
        const u8 *data;
    }

.. _`iwl_nvm_section.members`:

Members
-------

length
    *undescribed*

data
    *undescribed*

.. _`iwl_nvm_section.description`:

Description
-----------

This struct holds an NVM section read from the NIC using NVM_ACCESS_CMD,
and saved for later use by the driver. Not all NVM sections are saved
this way, only the needed ones.

.. _`iwl_read_external_nvm`:

iwl_read_external_nvm
=====================

.. c:function:: int iwl_read_external_nvm(struct iwl_trans *trans, const char *nvm_file_name, struct iwl_nvm_section *nvm_sections)

    Reads external NVM from a file into nvm_sections

    :param struct iwl_trans \*trans:
        *undescribed*

    :param const char \*nvm_file_name:
        *undescribed*

    :param struct iwl_nvm_section \*nvm_sections:
        *undescribed*

.. _`iwl_get_nvm`:

iwl_get_nvm
===========

.. c:function:: struct iwl_nvm_data *iwl_get_nvm(struct iwl_trans *trans, const struct iwl_fw *fw)

    retrieve NVM data from firmware

    :param struct iwl_trans \*trans:
        *undescribed*

    :param const struct iwl_fw \*fw:
        *undescribed*

.. _`iwl_get_nvm.description`:

Description
-----------

Allocates a new iwl_nvm_data structure, fills it with
NVM data, and returns it to caller.

.. This file was automatic generated / don't edit.

