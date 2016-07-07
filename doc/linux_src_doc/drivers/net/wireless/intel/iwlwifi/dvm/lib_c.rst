.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/dvm/lib.c

.. _`iwlagn_txfifo_flush`:

iwlagn_txfifo_flush
===================

.. c:function:: int iwlagn_txfifo_flush(struct iwl_priv *priv, u32 scd_q_msk)

    send REPLY_TXFIFO_FLUSH command to uCode

    :param struct iwl_priv \*priv:
        *undescribed*

    :param u32 scd_q_msk:
        *undescribed*

.. _`iwlagn_txfifo_flush.description`:

Description
-----------

pre-requirements:
1. acquire mutex before calling
2. make sure rf is on and not in exit state

.. _`iwlagn_set_rxon_chain`:

iwlagn_set_rxon_chain
=====================

.. c:function:: void iwlagn_set_rxon_chain(struct iwl_priv *priv, struct iwl_rxon_context *ctx)

    Set up Rx chain usage in "staging" RXON image

    :param struct iwl_priv \*priv:
        *undescribed*

    :param struct iwl_rxon_context \*ctx:
        *undescribed*

.. _`iwlagn_set_rxon_chain.description`:

Description
-----------

Selects how many and which Rx receivers/antennas/chains to use.
This should not be used for scan command ... it puts data in wrong place.

.. This file was automatic generated / don't edit.

