.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/dvm/rs.c

.. _`rs_program_fix_rate`:

rs_program_fix_rate
===================

.. c:function:: void rs_program_fix_rate(struct iwl_priv *priv, struct iwl_lq_sta *lq_sta)

    This is for debugging/testing only once the device start use fixed rate, we need to reload the module to being back the normal operation.

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param lq_sta:
        *undescribed*
    :type lq_sta: struct iwl_lq_sta \*

.. _`rs_collect_tx_data`:

rs_collect_tx_data
==================

.. c:function:: int rs_collect_tx_data(struct iwl_scale_tbl_info *tbl, int scale_index, int attempts, int successes)

    Update the success/failure sliding window

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

.. _`rs_collect_tx_data.description`:

Description
-----------

We keep a sliding window of the last 62 packets transmitted
at this rate.  window->data contains the bitmask of successful
packets.

.. _`rs_use_green`:

rs_use_green
============

.. c:function:: bool rs_use_green(struct ieee80211_sta *sta)

    field mode is valid if the station supports it and there are no non-GF stations present in the BSS.

    :param sta:
        *undescribed*
    :type sta: struct ieee80211_sta \*

.. _`rs_get_supported_rates`:

rs_get_supported_rates
======================

.. c:function:: u16 rs_get_supported_rates(struct iwl_lq_sta *lq_sta, struct ieee80211_hdr *hdr, enum iwl_table_type rate_type)

    get the available rates

    :param lq_sta:
        *undescribed*
    :type lq_sta: struct iwl_lq_sta \*

    :param hdr:
        *undescribed*
    :type hdr: struct ieee80211_hdr \*

    :param rate_type:
        *undescribed*
    :type rate_type: enum iwl_table_type

.. _`rs_get_supported_rates.description`:

Description
-----------

if management frame or broadcast frame only return
basic available rates.

.. _`rs_initialize_lq`:

rs_initialize_lq
================

.. c:function:: void rs_initialize_lq(struct iwl_priv *priv, struct ieee80211_sta *sta, struct iwl_lq_sta *lq_sta)

    Initialize a station's hardware rate table

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param sta:
        *undescribed*
    :type sta: struct ieee80211_sta \*

    :param lq_sta:
        *undescribed*
    :type lq_sta: struct iwl_lq_sta \*

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

.. This file was automatic generated / don't edit.

