.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/rs.c

.. _`_rs_collect_tx_data`:

\_rs_collect_tx_data
====================

.. c:function:: int _rs_collect_tx_data(struct iwl_mvm *mvm, struct iwl_scale_tbl_info *tbl, int scale_index, int attempts, int successes, struct iwl_rate_scale_data *window)

    Update the success/failure sliding window

    :param mvm:
        *undescribed*
    :type mvm: struct iwl_mvm \*

    :param tbl:
        *undescribed*
    :type tbl: struct iwl_scale_tbl_info \*

    :param scale_index:
        *undescribed*
    :type scale_index: int

    :param attempts:
        *undescribed*
    :type attempts: int

    :param successes:
        *undescribed*
    :type successes: int

    :param window:
        *undescribed*
    :type window: struct iwl_rate_scale_data \*

.. _`_rs_collect_tx_data.description`:

Description
-----------

We keep a sliding window of the last 62 packets transmitted
at this rate.  window->data contains the bitmask of successful
packets.

.. _`rs_initialize_lq`:

rs_initialize_lq
================

.. c:function:: void rs_initialize_lq(struct iwl_mvm *mvm, struct ieee80211_sta *sta, struct iwl_lq_sta *lq_sta, enum nl80211_band band, bool update)

    Initialize a station's hardware rate table

    :param mvm:
        *undescribed*
    :type mvm: struct iwl_mvm \*

    :param sta:
        *undescribed*
    :type sta: struct ieee80211_sta \*

    :param lq_sta:
        *undescribed*
    :type lq_sta: struct iwl_lq_sta \*

    :param band:
        *undescribed*
    :type band: enum nl80211_band

    :param update:
        *undescribed*
    :type update: bool

.. _`rs_initialize_lq.description`:

Description
-----------

The uCode's station table contains a table of fallback rates
for automatic fallback during transmission.

.. _`rs_initialize_lq.note`:

NOTE
----

This sets up a default set of values.  These will be replaced later
if the driver's iwl-agn-rs rate scaling algorithm is used, instead of
rc80211_simple.

Run REPLY_ADD_STA command to set up station table entry, before
calling this function (which runs REPLY_TX_LINK_QUALITY_CMD,
which requires station table entry to exist).

.. _`rs_program_fix_rate`:

rs_program_fix_rate
===================

.. c:function:: void rs_program_fix_rate(struct iwl_mvm *mvm, struct iwl_lq_sta *lq_sta)

    This is for debugging/testing only once the device start use fixed rate, we need to reload the module to being back the normal operation.

    :param mvm:
        *undescribed*
    :type mvm: struct iwl_mvm \*

    :param lq_sta:
        *undescribed*
    :type lq_sta: struct iwl_lq_sta \*

.. _`iwl_mvm_tx_protection`:

iwl_mvm_tx_protection
=====================

.. c:function:: int iwl_mvm_tx_protection(struct iwl_mvm *mvm, struct iwl_mvm_sta *mvmsta, bool enable)

    ask FW to enable RTS/CTS protection

    :param mvm:
        *undescribed*
    :type mvm: struct iwl_mvm \*

    :param mvmsta:
        The station
    :type mvmsta: struct iwl_mvm_sta \*

    :param enable:
        Enable Tx protection?
    :type enable: bool

.. This file was automatic generated / don't edit.

