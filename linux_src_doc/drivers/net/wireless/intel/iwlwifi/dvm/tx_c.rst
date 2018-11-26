.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/dvm/tx.c

.. _`iwl_sta_id_or_broadcast`:

iwl_sta_id_or_broadcast
=======================

.. c:function:: int iwl_sta_id_or_broadcast(struct iwl_rxon_context *context, struct ieee80211_sta *sta)

    return sta_id or broadcast sta

    :param context:
        the current context
    :type context: struct iwl_rxon_context \*

    :param sta:
        mac80211 station
    :type sta: struct ieee80211_sta \*

.. _`iwl_sta_id_or_broadcast.description`:

Description
-----------

In certain circumstances mac80211 passes a station pointer
that may be \ ``NULL``\ , for example during TX or key setup. In
that case, we need to use the broadcast station, so this
inline wraps that pattern.

.. _`iwlagn_hwrate_to_tx_control`:

iwlagn_hwrate_to_tx_control
===========================

.. c:function:: void iwlagn_hwrate_to_tx_control(struct iwl_priv *priv, u32 rate_n_flags, struct ieee80211_tx_info *info)

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param rate_n_flags:
        *undescribed*
    :type rate_n_flags: u32

    :param info:
        *undescribed*
    :type info: struct ieee80211_tx_info \*

.. _`iwlagn_rx_reply_compressed_ba`:

iwlagn_rx_reply_compressed_ba
=============================

.. c:function:: void iwlagn_rx_reply_compressed_ba(struct iwl_priv *priv, struct iwl_rx_cmd_buffer *rxb)

    Handler for REPLY_COMPRESSED_BA

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param rxb:
        *undescribed*
    :type rxb: struct iwl_rx_cmd_buffer \*

.. _`iwlagn_rx_reply_compressed_ba.description`:

Description
-----------

Handles block-acknowledge notification from device, which reports success
of frames sent via aggregation.

.. This file was automatic generated / don't edit.

