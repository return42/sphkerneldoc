.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlegacy/common.c

.. _`il_eeprom_init`:

il_eeprom_init
==============

.. c:function:: int il_eeprom_init(struct il_priv *il)

    read EEPROM contents

    :param il:
        *undescribed*
    :type il: struct il_priv \*

.. _`il_eeprom_init.description`:

Description
-----------

Load the EEPROM contents from adapter into il->eeprom

.. _`il_eeprom_init.note`:

NOTE
----

This routine uses the non-debug IO access functions.

.. _`il_mod_ht40_chan_info`:

il_mod_ht40_chan_info
=====================

.. c:function:: int il_mod_ht40_chan_info(struct il_priv *il, enum nl80211_band band, u16 channel, const struct il_eeprom_channel *eeprom_ch, u8 clear_ht40_extension_channel)

    Copy ht40 channel info into driver's il.

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param band:
        *undescribed*
    :type band: enum nl80211_band

    :param channel:
        *undescribed*
    :type channel: u16

    :param eeprom_ch:
        *undescribed*
    :type eeprom_ch: const struct il_eeprom_channel \*

    :param clear_ht40_extension_channel:
        *undescribed*
    :type clear_ht40_extension_channel: u8

.. _`il_mod_ht40_chan_info.description`:

Description
-----------

Does not set up a command, or touch hardware.

.. _`il_init_channel_map`:

il_init_channel_map
===================

.. c:function:: int il_init_channel_map(struct il_priv *il)

    Set up driver's info for all possible channels

    :param il:
        *undescribed*
    :type il: struct il_priv \*

.. _`il_get_channel_info`:

il_get_channel_info
===================

.. c:function:: const struct il_channel_info *il_get_channel_info(const struct il_priv *il, enum nl80211_band band, u16 channel)

    Find driver's ilate channel info

    :param il:
        *undescribed*
    :type il: const struct il_priv \*

    :param band:
        *undescribed*
    :type band: enum nl80211_band

    :param channel:
        *undescribed*
    :type channel: u16

.. _`il_get_channel_info.description`:

Description
-----------

Based on band and channel number.

.. _`il_scan_cancel`:

il_scan_cancel
==============

.. c:function:: int il_scan_cancel(struct il_priv *il)

    Cancel any currently executing HW scan

    :param il:
        *undescribed*
    :type il: struct il_priv \*

.. _`il_scan_cancel_timeout`:

il_scan_cancel_timeout
======================

.. c:function:: int il_scan_cancel_timeout(struct il_priv *il, unsigned long ms)

    Cancel any currently executing HW scan

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param ms:
        amount of time to wait (in milliseconds) for scan to abort
    :type ms: unsigned long

.. _`il_fill_probe_req`:

il_fill_probe_req
=================

.. c:function:: u16 il_fill_probe_req(struct il_priv *il, struct ieee80211_mgmt *frame, const u8 *ta, const u8 *ies, int ie_len, int left)

    fill in all required fields and IE for probe request

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param frame:
        *undescribed*
    :type frame: struct ieee80211_mgmt \*

    :param ta:
        *undescribed*
    :type ta: const u8 \*

    :param ies:
        *undescribed*
    :type ies: const u8 \*

    :param ie_len:
        *undescribed*
    :type ie_len: int

    :param left:
        *undescribed*
    :type left: int

.. _`il_prep_station`:

il_prep_station
===============

.. c:function:: u8 il_prep_station(struct il_priv *il, const u8 *addr, bool is_ap, struct ieee80211_sta *sta)

    Prepare station information for addition

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param addr:
        *undescribed*
    :type addr: const u8 \*

    :param is_ap:
        *undescribed*
    :type is_ap: bool

    :param sta:
        *undescribed*
    :type sta: struct ieee80211_sta \*

.. _`il_prep_station.description`:

Description
-----------

should be called with sta_lock held

.. _`il_add_station_common`:

il_add_station_common
=====================

.. c:function:: int il_add_station_common(struct il_priv *il, const u8 *addr, bool is_ap, struct ieee80211_sta *sta, u8 *sta_id_r)

    :param il:
        *undescribed*
    :type il: struct il_priv \*

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

.. _`il_sta_ucode_deactivate`:

il_sta_ucode_deactivate
=======================

.. c:function:: void il_sta_ucode_deactivate(struct il_priv *il, u8 sta_id)

    deactivate ucode status for a station

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param sta_id:
        *undescribed*
    :type sta_id: u8

.. _`il_sta_ucode_deactivate.description`:

Description
-----------

il->sta_lock must be held

.. _`il_remove_station`:

il_remove_station
=================

.. c:function:: int il_remove_station(struct il_priv *il, const u8 sta_id, const u8 *addr)

    Remove driver's knowledge of station.

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param sta_id:
        *undescribed*
    :type sta_id: const u8

    :param addr:
        *undescribed*
    :type addr: const u8 \*

.. _`il_clear_ucode_stations`:

il_clear_ucode_stations
=======================

.. c:function:: void il_clear_ucode_stations(struct il_priv *il)

    clear ucode station table bits

    :param il:
        *undescribed*
    :type il: struct il_priv \*

.. _`il_clear_ucode_stations.description`:

Description
-----------

This function clears all the bits in the driver indicating
which stations are active in the ucode. Call when something
other than explicit station management would cause this in
the ucode, e.g. unassociated RXON.

.. _`il_restore_stations`:

il_restore_stations
===================

.. c:function:: void il_restore_stations(struct il_priv *il)

    Restore driver known stations to device

    :param il:
        *undescribed*
    :type il: struct il_priv \*

.. _`il_restore_stations.description`:

Description
-----------

All stations considered active by driver, but not present in ucode, is
restored.

Function sleeps.

.. _`il_is_lq_table_valid`:

il_is_lq_table_valid
====================

.. c:function:: bool il_is_lq_table_valid(struct il_priv *il, struct il_link_quality_cmd *lq)

    Test one aspect of LQ cmd for validity

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param lq:
        *undescribed*
    :type lq: struct il_link_quality_cmd \*

.. _`il_is_lq_table_valid.description`:

Description
-----------

It sometimes happens when a HT rate has been in use and we
loose connectivity with AP then mac80211 will first tell us that the
current channel is not HT anymore before removing the station. In such a
scenario the RXON flags will be updated to indicate we are not
communicating HT anymore, but the LQ command may still contain HT rates.
Test for this to prevent driver from sending LQ command between the time
RXON flags are updated and when LQ command is updated.

.. _`il_send_lq_cmd`:

il_send_lq_cmd
==============

.. c:function:: int il_send_lq_cmd(struct il_priv *il, struct il_link_quality_cmd *lq, u8 flags, bool init)

    Send link quality command

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param lq:
        *undescribed*
    :type lq: struct il_link_quality_cmd \*

    :param flags:
        *undescribed*
    :type flags: u8

    :param init:
        This command is sent as part of station initialization right
        after station has been added.
    :type init: bool

.. _`il_send_lq_cmd.description`:

Description
-----------

The link quality command is sent as the last step of station creation.
This is the special case in which init is set and we call a callback in
this case to clear the state indicating that station creation is in
progress.

.. _`il_rx_queue_space`:

il_rx_queue_space
=================

.. c:function:: int il_rx_queue_space(const struct il_rx_queue *q)

    Return number of free slots available in queue.

    :param q:
        *undescribed*
    :type q: const struct il_rx_queue \*

.. _`il_rx_queue_update_write_ptr`:

il_rx_queue_update_write_ptr
============================

.. c:function:: void il_rx_queue_update_write_ptr(struct il_priv *il, struct il_rx_queue *q)

    Update the write pointer for the RX queue

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param q:
        *undescribed*
    :type q: struct il_rx_queue \*

.. _`il_txq_update_write_ptr`:

il_txq_update_write_ptr
=======================

.. c:function:: void il_txq_update_write_ptr(struct il_priv *il, struct il_tx_queue *txq)

    Send new write idx to hardware

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param txq:
        *undescribed*
    :type txq: struct il_tx_queue \*

.. _`il_tx_queue_unmap`:

il_tx_queue_unmap
=================

.. c:function:: void il_tx_queue_unmap(struct il_priv *il, int txq_id)

    Unmap any remaining DMA mappings and free skb's

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param txq_id:
        *undescribed*
    :type txq_id: int

.. _`il_tx_queue_free`:

il_tx_queue_free
================

.. c:function:: void il_tx_queue_free(struct il_priv *il, int txq_id)

    Deallocate DMA queue.

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param txq_id:
        *undescribed*
    :type txq_id: int

.. _`il_tx_queue_free.description`:

Description
-----------

Empty queue by removing and destroying all BD's.
Free all buffers.
0-fill, but do not free "txq" descriptor structure.

.. _`il_cmd_queue_unmap`:

il_cmd_queue_unmap
==================

.. c:function:: void il_cmd_queue_unmap(struct il_priv *il)

    Unmap any remaining DMA mappings from command queue

    :param il:
        *undescribed*
    :type il: struct il_priv \*

.. _`il_cmd_queue_free`:

il_cmd_queue_free
=================

.. c:function:: void il_cmd_queue_free(struct il_priv *il)

    Deallocate DMA queue.

    :param il:
        *undescribed*
    :type il: struct il_priv \*

.. _`il_cmd_queue_free.description`:

Description
-----------

Empty queue by removing and destroying all BD's.
Free all buffers.
0-fill, but do not free "txq" descriptor structure.

.. _`il_queue_init`:

il_queue_init
=============

.. c:function:: int il_queue_init(struct il_priv *il, struct il_queue *q, int slots, u32 id)

    Initialize queue's high/low-water and read/write idxes

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param q:
        *undescribed*
    :type q: struct il_queue \*

    :param slots:
        *undescribed*
    :type slots: int

    :param id:
        *undescribed*
    :type id: u32

.. _`il_tx_queue_alloc`:

il_tx_queue_alloc
=================

.. c:function:: int il_tx_queue_alloc(struct il_priv *il, struct il_tx_queue *txq, u32 id)

    Alloc driver data and TFD CB for one Tx/cmd queue

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param txq:
        *undescribed*
    :type txq: struct il_tx_queue \*

    :param id:
        *undescribed*
    :type id: u32

.. _`il_tx_queue_init`:

il_tx_queue_init
================

.. c:function:: int il_tx_queue_init(struct il_priv *il, u32 txq_id)

    Allocate and initialize one tx/cmd queue

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param txq_id:
        *undescribed*
    :type txq_id: u32

.. _`il_enqueue_hcmd`:

il_enqueue_hcmd
===============

.. c:function:: int il_enqueue_hcmd(struct il_priv *il, struct il_host_cmd *cmd)

    enqueue a uCode command

    :param il:
        device ilate data point
    :type il: struct il_priv \*

    :param cmd:
        a point to the ucode command structure
    :type cmd: struct il_host_cmd \*

.. _`il_enqueue_hcmd.description`:

Description
-----------

The function returns < 0 values to indicate the operation is
failed. On success, it turns the idx (> 0) of command in the
command queue.

.. _`il_hcmd_queue_reclaim`:

il_hcmd_queue_reclaim
=====================

.. c:function:: void il_hcmd_queue_reclaim(struct il_priv *il, int txq_id, int idx, int cmd_idx)

    Reclaim TX command queue entries already Tx'd

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param txq_id:
        *undescribed*
    :type txq_id: int

    :param idx:
        *undescribed*
    :type idx: int

    :param cmd_idx:
        *undescribed*
    :type cmd_idx: int

.. _`il_hcmd_queue_reclaim.description`:

Description
-----------

When FW advances 'R' idx, all entries between old and new 'R' idx
need to be reclaimed. As result, some free space forms.  If there is
enough free space (> low mark), wake the stack that feeds us.

.. _`il_tx_cmd_complete`:

il_tx_cmd_complete
==================

.. c:function:: void il_tx_cmd_complete(struct il_priv *il, struct il_rx_buf *rxb)

    Pull unused buffers off the queue and reclaim them

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param rxb:
        Rx buffer to reclaim
    :type rxb: struct il_rx_buf \*

.. _`il_tx_cmd_complete.description`:

Description
-----------

If an Rx buffer has an async callback associated with it the callback
will be executed.  The attached skb (if present) will only be freed
if the callback returns 1

.. _`il_init_geos`:

il_init_geos
============

.. c:function:: int il_init_geos(struct il_priv *il)

    Initialize mac80211's geo/channel info based from eeprom

    :param il:
        *undescribed*
    :type il: struct il_priv \*

.. _`il_full_rxon_required`:

il_full_rxon_required
=====================

.. c:function:: int il_full_rxon_required(struct il_priv *il)

    check if full RXON (vs RXON_ASSOC) cmd is needed

    :param il:
        staging_rxon is compared to active_rxon
    :type il: struct il_priv \*

.. _`il_full_rxon_required.description`:

Description
-----------

If the RXON structure is changing enough to require a new tune,
or is clearing the RXON_FILTER_ASSOC_MSK, then return 1 to indicate that
a new tune (full RXON command, rather than RXON_ASSOC cmd) is required.

.. _`il_set_rxon_channel`:

il_set_rxon_channel
===================

.. c:function:: int il_set_rxon_channel(struct il_priv *il, struct ieee80211_channel *ch)

    Set the band and channel values in staging RXON

    :param il:
        *undescribed*
    :type il: struct il_priv \*

    :param ch:
        requested channel as a pointer to struct ieee80211_channel
    :type ch: struct ieee80211_channel \*

.. _`il_set_rxon_channel.note`:

NOTE
----

Does not commit to the hardware; it sets appropriate bit fields
in the staging RXON flag structure based on the ch->band

.. _`il_irq_handle_error`:

il_irq_handle_error
===================

.. c:function:: void il_irq_handle_error(struct il_priv *il)

    called for HW or SW error interrupt from card

    :param il:
        *undescribed*
    :type il: struct il_priv \*

.. _`il_mac_config`:

il_mac_config
=============

.. c:function:: int il_mac_config(struct ieee80211_hw *hw, u32 changed)

    mac80211 config callback

    :param hw:
        *undescribed*
    :type hw: struct ieee80211_hw \*

    :param changed:
        *undescribed*
    :type changed: u32

.. This file was automatic generated / don't edit.

