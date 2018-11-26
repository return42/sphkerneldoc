.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/dvm/rxon.c

.. _`iwl_set_rxon_channel`:

iwl_set_rxon_channel
====================

.. c:function:: void iwl_set_rxon_channel(struct iwl_priv *priv, struct ieee80211_channel *ch, struct iwl_rxon_context *ctx)

    Set the band and channel values in staging RXON

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param ch:
        requested channel as a pointer to struct ieee80211_channel
    :type ch: struct ieee80211_channel \*

    :param ctx:
        *undescribed*
    :type ctx: struct iwl_rxon_context \*

.. _`iwl_set_rxon_channel.note`:

NOTE
----

Does not commit to the hardware; it sets appropriate bit fields
in the staging RXON flag structure based on the ch->band

.. _`iwl_full_rxon_required`:

iwl_full_rxon_required
======================

.. c:function:: int iwl_full_rxon_required(struct iwl_priv *priv, struct iwl_rxon_context *ctx)

    check if full RXON (vs RXON_ASSOC) cmd is needed

    :param priv:
        staging_rxon is compared to active_rxon
    :type priv: struct iwl_priv \*

    :param ctx:
        *undescribed*
    :type ctx: struct iwl_rxon_context \*

.. _`iwl_full_rxon_required.description`:

Description
-----------

If the RXON structure is changing enough to require a new tune,
or is clearing the RXON_FILTER_ASSOC_MSK, then return 1 to indicate that
a new tune (full RXON command, rather than RXON_ASSOC cmd) is required.

.. _`iwlagn_commit_rxon`:

iwlagn_commit_rxon
==================

.. c:function:: int iwlagn_commit_rxon(struct iwl_priv *priv, struct iwl_rxon_context *ctx)

    commit staging_rxon to hardware

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param ctx:
        *undescribed*
    :type ctx: struct iwl_rxon_context \*

.. _`iwlagn_commit_rxon.description`:

Description
-----------

The RXON command in staging_rxon is committed to the hardware and
the active_rxon structure is updated with the new data.  This
function correctly transitions out of the RXON_ASSOC_MSK state if
a HW tune is required based on the RXON structure changes.

The connect/disconnect flow should be as the following:

1. make sure send RXON command with association bit unset if not connect
this should include the channel and the band for the candidate
to be connected to
2. Add Station before RXON association with the AP
3. RXON_timing has to send before RXON for connection
4. full RXON command - associated bit set
5. use RXON_ASSOC command to update any flags changes

.. This file was automatic generated / don't edit.

