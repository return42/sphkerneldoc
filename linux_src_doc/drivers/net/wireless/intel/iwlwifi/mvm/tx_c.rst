.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/tx.c

.. _`iwl_mvm_hwrate_to_tx_status`:

iwl_mvm_hwrate_to_tx_status
===========================

.. c:function:: void iwl_mvm_hwrate_to_tx_status(u32 rate_n_flags, struct ieee80211_tx_info *info)

    :param rate_n_flags:
        *undescribed*
    :type rate_n_flags: u32

    :param info:
        *undescribed*
    :type info: struct ieee80211_tx_info \*

.. _`iwl_mvm_get_scd_ssn`:

iwl_mvm_get_scd_ssn
===================

.. c:function:: u32 iwl_mvm_get_scd_ssn(struct iwl_mvm *mvm, struct iwl_mvm_tx_resp *tx_resp)

    returns the SSN of the SCD

    :param mvm:
        *undescribed*
    :type mvm: struct iwl_mvm \*

    :param tx_resp:
        the Tx response from the fw (agg or non-agg)
    :type tx_resp: struct iwl_mvm_tx_resp \*

.. _`iwl_mvm_get_scd_ssn.description`:

Description
-----------

When the fw sends an AMPDU, it fetches the MPDUs one after the other. Since
it can't know that everything will go well until the end of the AMPDU, it
can't know in advance the number of MPDUs that will be sent in the current
batch. This is why it writes the agg Tx response while it fetches the MPDUs.
Hence, it can't know in advance what the SSN of the SCD will be at the end
of the batch. This is why the SSN of the SCD is written at the end of the
whole struct at a variable offset. This function knows how to cope with the
variable offset and returns the SSN of the SCD.

.. This file was automatic generated / don't edit.

