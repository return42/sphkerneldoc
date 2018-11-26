.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/dvm/rx.c

.. _`iwlagn_good_plcp_health`:

iwlagn_good_plcp_health
=======================

.. c:function:: bool iwlagn_good_plcp_health(struct iwl_priv *priv, struct statistics_rx_phy *cur_ofdm, struct statistics_rx_ht_phy *cur_ofdm_ht, unsigned int msecs)

    checks for plcp error.

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param cur_ofdm:
        *undescribed*
    :type cur_ofdm: struct statistics_rx_phy \*

    :param cur_ofdm_ht:
        *undescribed*
    :type cur_ofdm_ht: struct statistics_rx_ht_phy \*

    :param msecs:
        *undescribed*
    :type msecs: unsigned int

.. _`iwlagn_good_plcp_health.description`:

Description
-----------

When the plcp error is exceeding the thresholds, reset the radio
to improve the throughput.

.. _`iwl_setup_rx_handlers`:

iwl_setup_rx_handlers
=====================

.. c:function:: void iwl_setup_rx_handlers(struct iwl_priv *priv)

    Initialize Rx handler callbacks

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

.. _`iwl_setup_rx_handlers.description`:

Description
-----------

Setup the RX handlers for each of the reply types sent from the uCode
to the host.

.. This file was automatic generated / don't edit.

