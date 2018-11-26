.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/dvm/sta.c

.. _`iwl_prep_station`:

iwl_prep_station
================

.. c:function:: u8 iwl_prep_station(struct iwl_priv *priv, struct iwl_rxon_context *ctx, const u8 *addr, bool is_ap, struct ieee80211_sta *sta)

    Prepare station information for addition

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param ctx:
        *undescribed*
    :type ctx: struct iwl_rxon_context \*

    :param addr:
        *undescribed*
    :type addr: const u8 \*

    :param is_ap:
        *undescribed*
    :type is_ap: bool

    :param sta:
        *undescribed*
    :type sta: struct ieee80211_sta \*

.. _`iwl_prep_station.description`:

Description
-----------

should be called with sta_lock held

.. _`iwl_add_station_common`:

iwl_add_station_common
======================

.. c:function:: int iwl_add_station_common(struct iwl_priv *priv, struct iwl_rxon_context *ctx, const u8 *addr, bool is_ap, struct ieee80211_sta *sta, u8 *sta_id_r)

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param ctx:
        *undescribed*
    :type ctx: struct iwl_rxon_context \*

    :param addr:
        *undescribed*
    :type addr: const u8 \*

    :param is_ap:
        *undescribed*
    :type is_ap: bool

    :param sta:
        *undescribed*
    :type sta: struct ieee80211_sta \*

    :param sta_id_r:
        *undescribed*
    :type sta_id_r: u8 \*

.. _`iwl_sta_ucode_deactivate`:

iwl_sta_ucode_deactivate
========================

.. c:function:: void iwl_sta_ucode_deactivate(struct iwl_priv *priv, u8 sta_id)

    deactivate ucode status for a station

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param sta_id:
        *undescribed*
    :type sta_id: u8

.. _`iwl_remove_station`:

iwl_remove_station
==================

.. c:function:: int iwl_remove_station(struct iwl_priv *priv, const u8 sta_id, const u8 *addr)

    Remove driver's knowledge of station.

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param sta_id:
        *undescribed*
    :type sta_id: const u8

    :param addr:
        *undescribed*
    :type addr: const u8 \*

.. _`iwl_clear_ucode_stations`:

iwl_clear_ucode_stations
========================

.. c:function:: void iwl_clear_ucode_stations(struct iwl_priv *priv, struct iwl_rxon_context *ctx)

    clear ucode station table bits

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param ctx:
        *undescribed*
    :type ctx: struct iwl_rxon_context \*

.. _`iwl_clear_ucode_stations.description`:

Description
-----------

This function clears all the bits in the driver indicating
which stations are active in the ucode. Call when something
other than explicit station management would cause this in
the ucode, e.g. unassociated RXON.

.. _`iwl_restore_stations`:

iwl_restore_stations
====================

.. c:function:: void iwl_restore_stations(struct iwl_priv *priv, struct iwl_rxon_context *ctx)

    Restore driver known stations to device

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param ctx:
        *undescribed*
    :type ctx: struct iwl_rxon_context \*

.. _`iwl_restore_stations.description`:

Description
-----------

All stations considered active by driver, but not present in ucode, is
restored.

Function sleeps.

.. _`is_lq_table_valid`:

is_lq_table_valid
=================

.. c:function:: bool is_lq_table_valid(struct iwl_priv *priv, struct iwl_rxon_context *ctx, struct iwl_link_quality_cmd *lq)

    Test one aspect of LQ cmd for validity

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param ctx:
        *undescribed*
    :type ctx: struct iwl_rxon_context \*

    :param lq:
        *undescribed*
    :type lq: struct iwl_link_quality_cmd \*

.. _`is_lq_table_valid.description`:

Description
-----------

It sometimes happens when a HT rate has been in use and we
loose connectivity with AP then mac80211 will first tell us that the
current channel is not HT anymore before removing the station. In such a
scenario the RXON flags will be updated to indicate we are not
communicating HT anymore, but the LQ command may still contain HT rates.
Test for this to prevent driver from sending LQ command between the time
RXON flags are updated and when LQ command is updated.

.. _`iwl_send_lq_cmd`:

iwl_send_lq_cmd
===============

.. c:function:: int iwl_send_lq_cmd(struct iwl_priv *priv, struct iwl_rxon_context *ctx, struct iwl_link_quality_cmd *lq, u8 flags, bool init)

    Send link quality command

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param ctx:
        *undescribed*
    :type ctx: struct iwl_rxon_context \*

    :param lq:
        *undescribed*
    :type lq: struct iwl_link_quality_cmd \*

    :param flags:
        *undescribed*
    :type flags: u8

    :param init:
        This command is sent as part of station initialization right
        after station has been added.
    :type init: bool

.. _`iwl_send_lq_cmd.description`:

Description
-----------

The link quality command is sent as the last step of station creation.
This is the special case in which init is set and we call a callback in
this case to clear the state indicating that station creation is in
progress.

.. _`iwlagn_alloc_bcast_station`:

iwlagn_alloc_bcast_station
==========================

.. c:function:: int iwlagn_alloc_bcast_station(struct iwl_priv *priv, struct iwl_rxon_context *ctx)

    add broadcast station into driver's station table.

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param ctx:
        *undescribed*
    :type ctx: struct iwl_rxon_context \*

.. _`iwlagn_alloc_bcast_station.description`:

Description
-----------

This adds the broadcast station into the driver's station table
and marks it driver active, so that it will be restored to the
device at the next best time.

.. _`iwl_update_bcast_station`:

iwl_update_bcast_station
========================

.. c:function:: int iwl_update_bcast_station(struct iwl_priv *priv, struct iwl_rxon_context *ctx)

    update broadcast station's LQ command

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param ctx:
        *undescribed*
    :type ctx: struct iwl_rxon_context \*

.. _`iwl_update_bcast_station.description`:

Description
-----------

Only used by iwlagn. Placed here to have all bcast station management
code together.

.. _`iwl_sta_tx_modify_enable_tid`:

iwl_sta_tx_modify_enable_tid
============================

.. c:function:: int iwl_sta_tx_modify_enable_tid(struct iwl_priv *priv, int sta_id, int tid)

    Enable Tx for this TID in station table

    :param priv:
        *undescribed*
    :type priv: struct iwl_priv \*

    :param sta_id:
        *undescribed*
    :type sta_id: int

    :param tid:
        *undescribed*
    :type tid: int

.. This file was automatic generated / don't edit.

