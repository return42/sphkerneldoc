.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/rsi/rsi_91x_mac80211.c

.. _`rsi_is_cipher_wep`:

rsi_is_cipher_wep
=================

.. c:function:: bool rsi_is_cipher_wep(struct rsi_common *common)

    This function determines if the cipher is WEP or not.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

.. _`rsi_is_cipher_wep.return`:

Return
------

If cipher type is WEP, a value of 1 is returned, else 0.

.. _`rsi_register_rates_channels`:

rsi_register_rates_channels
===========================

.. c:function:: void rsi_register_rates_channels(struct rsi_hw *adapter, int band)

    This function registers channels and rates.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param band:
        Operating band to be set.
    :type band: int

.. _`rsi_register_rates_channels.return`:

Return
------

None.

.. _`rsi_mac80211_detach`:

rsi_mac80211_detach
===================

.. c:function:: void rsi_mac80211_detach(struct rsi_hw *adapter)

    This function is used to de-initialize the Mac80211 stack.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

.. _`rsi_mac80211_detach.return`:

Return
------

None.

.. _`rsi_indicate_tx_status`:

rsi_indicate_tx_status
======================

.. c:function:: void rsi_indicate_tx_status(struct rsi_hw *adapter, struct sk_buff *skb, int status)

    This function indicates the transmit status.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param skb:
        Pointer to the socket buffer structure.
    :type skb: struct sk_buff \*

    :param status:
        Status
    :type status: int

.. _`rsi_indicate_tx_status.return`:

Return
------

None.

.. _`rsi_mac80211_tx`:

rsi_mac80211_tx
===============

.. c:function:: void rsi_mac80211_tx(struct ieee80211_hw *hw, struct ieee80211_tx_control *control, struct sk_buff *skb)

    This is the handler that 802.11 module calls for each transmitted frame.SKB contains the buffer starting from the IEEE 802.11 header.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param control:
        Pointer to the ieee80211_tx_control structure
    :type control: struct ieee80211_tx_control \*

    :param skb:
        Pointer to the socket buffer structure.
    :type skb: struct sk_buff \*

.. _`rsi_mac80211_tx.return`:

Return
------

None

.. _`rsi_mac80211_start`:

rsi_mac80211_start
==================

.. c:function:: int rsi_mac80211_start(struct ieee80211_hw *hw)

    This is first handler that 802.11 module calls, since the driver init is complete by then, just returns success.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

.. _`rsi_mac80211_start.return`:

Return
------

0 as success.

.. _`rsi_mac80211_stop`:

rsi_mac80211_stop
=================

.. c:function:: void rsi_mac80211_stop(struct ieee80211_hw *hw)

    This is the last handler that 802.11 module calls.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

.. _`rsi_mac80211_stop.return`:

Return
------

None.

.. _`rsi_mac80211_add_interface`:

rsi_mac80211_add_interface
==========================

.. c:function:: int rsi_mac80211_add_interface(struct ieee80211_hw *hw, struct ieee80211_vif *vif)

    This function is called when a netdevice attached to the hardware is enabled.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param vif:
        Pointer to the ieee80211_vif structure.
    :type vif: struct ieee80211_vif \*

.. _`rsi_mac80211_add_interface.return`:

Return
------

ret: 0 on success, negative error code on failure.

.. _`rsi_mac80211_remove_interface`:

rsi_mac80211_remove_interface
=============================

.. c:function:: void rsi_mac80211_remove_interface(struct ieee80211_hw *hw, struct ieee80211_vif *vif)

    This function notifies driver that an interface is going down.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param vif:
        Pointer to the ieee80211_vif structure.
    :type vif: struct ieee80211_vif \*

.. _`rsi_mac80211_remove_interface.return`:

Return
------

None.

.. _`rsi_channel_change`:

rsi_channel_change
==================

.. c:function:: int rsi_channel_change(struct ieee80211_hw *hw)

    This function is a performs the checks required for changing a channel and sets the channel accordingly.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

.. _`rsi_channel_change.return`:

Return
------

0 on success, negative error code on failure.

.. _`rsi_config_power`:

rsi_config_power
================

.. c:function:: int rsi_config_power(struct ieee80211_hw *hw)

    This function configures tx power to device

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

.. _`rsi_config_power.return`:

Return
------

0 on success, negative error code on failure.

.. _`rsi_mac80211_config`:

rsi_mac80211_config
===================

.. c:function:: int rsi_mac80211_config(struct ieee80211_hw *hw, u32 changed)

    This function is a handler for configuration requests. The stack calls this function to change hardware configuration, e.g., channel.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param changed:
        Changed flags set.
    :type changed: u32

.. _`rsi_mac80211_config.return`:

Return
------

0 on success, negative error code on failure.

.. _`rsi_get_connected_channel`:

rsi_get_connected_channel
=========================

.. c:function:: u16 rsi_get_connected_channel(struct ieee80211_vif *vif)

    This function is used to get the current connected channel number.

    :param vif:
        *undescribed*
    :type vif: struct ieee80211_vif \*

.. _`rsi_get_connected_channel.return`:

Return
------

Current connected AP's channel number is returned.

.. _`rsi_mac80211_bss_info_changed`:

rsi_mac80211_bss_info_changed
=============================

.. c:function:: void rsi_mac80211_bss_info_changed(struct ieee80211_hw *hw, struct ieee80211_vif *vif, struct ieee80211_bss_conf *bss_conf, u32 changed)

    This function is a handler for config requests related to BSS parameters that may vary during BSS's lifespan.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param vif:
        Pointer to the ieee80211_vif structure.
    :type vif: struct ieee80211_vif \*

    :param bss_conf:
        Pointer to the ieee80211_bss_conf structure.
    :type bss_conf: struct ieee80211_bss_conf \*

    :param changed:
        Changed flags set.
    :type changed: u32

.. _`rsi_mac80211_bss_info_changed.return`:

Return
------

None.

.. _`rsi_mac80211_conf_filter`:

rsi_mac80211_conf_filter
========================

.. c:function:: void rsi_mac80211_conf_filter(struct ieee80211_hw *hw, u32 changed_flags, u32 *total_flags, u64 multicast)

    This function configure the device's RX filter.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param changed_flags:
        *undescribed*
    :type changed_flags: u32

    :param total_flags:
        Total initial flags set.
    :type total_flags: u32 \*

    :param multicast:
        Multicast.
    :type multicast: u64

.. _`rsi_mac80211_conf_filter.return`:

Return
------

None.

.. _`rsi_mac80211_conf_tx`:

rsi_mac80211_conf_tx
====================

.. c:function:: int rsi_mac80211_conf_tx(struct ieee80211_hw *hw, struct ieee80211_vif *vif, u16 queue, const struct ieee80211_tx_queue_params *params)

    This function configures TX queue parameters (EDCF (aifs, cw_min, cw_max), bursting) for a hardware TX queue.

    :param hw:
        Pointer to the ieee80211_hw structure
    :type hw: struct ieee80211_hw \*

    :param vif:
        Pointer to the ieee80211_vif structure.
    :type vif: struct ieee80211_vif \*

    :param queue:
        Queue number.
    :type queue: u16

    :param params:
        Pointer to ieee80211_tx_queue_params structure.
    :type params: const struct ieee80211_tx_queue_params \*

.. _`rsi_mac80211_conf_tx.return`:

Return
------

0 on success, negative error code on failure.

.. _`rsi_hal_key_config`:

rsi_hal_key_config
==================

.. c:function:: int rsi_hal_key_config(struct ieee80211_hw *hw, struct ieee80211_vif *vif, struct ieee80211_key_conf *key, struct ieee80211_sta *sta)

    This function loads the keys into the firmware.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param vif:
        Pointer to the ieee80211_vif structure.
    :type vif: struct ieee80211_vif \*

    :param key:
        Pointer to the ieee80211_key_conf structure.
    :type key: struct ieee80211_key_conf \*

    :param sta:
        *undescribed*
    :type sta: struct ieee80211_sta \*

.. _`rsi_hal_key_config.return`:

Return
------

status: 0 on success, negative error codes on failure.

.. _`rsi_mac80211_set_key`:

rsi_mac80211_set_key
====================

.. c:function:: int rsi_mac80211_set_key(struct ieee80211_hw *hw, enum set_key_cmd cmd, struct ieee80211_vif *vif, struct ieee80211_sta *sta, struct ieee80211_key_conf *key)

    This function sets type of key to be loaded.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param cmd:
        enum set_key_cmd.
    :type cmd: enum set_key_cmd

    :param vif:
        Pointer to the ieee80211_vif structure.
    :type vif: struct ieee80211_vif \*

    :param sta:
        Pointer to the ieee80211_sta structure.
    :type sta: struct ieee80211_sta \*

    :param key:
        Pointer to the ieee80211_key_conf structure.
    :type key: struct ieee80211_key_conf \*

.. _`rsi_mac80211_set_key.return`:

Return
------

status: 0 on success, negative error code on failure.

.. _`rsi_mac80211_ampdu_action`:

rsi_mac80211_ampdu_action
=========================

.. c:function:: int rsi_mac80211_ampdu_action(struct ieee80211_hw *hw, struct ieee80211_vif *vif, struct ieee80211_ampdu_params *params)

    This function selects the AMPDU action for the corresponding mlme_action flag and informs the f/w regarding this.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param vif:
        Pointer to the ieee80211_vif structure.
    :type vif: struct ieee80211_vif \*

    :param params:
        Pointer to A-MPDU action parameters
    :type params: struct ieee80211_ampdu_params \*

.. _`rsi_mac80211_ampdu_action.return`:

Return
------

status: 0 on success, negative error code on failure.

.. _`rsi_mac80211_set_rts_threshold`:

rsi_mac80211_set_rts_threshold
==============================

.. c:function:: int rsi_mac80211_set_rts_threshold(struct ieee80211_hw *hw, u32 value)

    This function sets rts threshold value.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param value:
        Rts threshold value.
    :type value: u32

.. _`rsi_mac80211_set_rts_threshold.return`:

Return
------

0 on success.

.. _`rsi_mac80211_set_rate_mask`:

rsi_mac80211_set_rate_mask
==========================

.. c:function:: int rsi_mac80211_set_rate_mask(struct ieee80211_hw *hw, struct ieee80211_vif *vif, const struct cfg80211_bitrate_mask *mask)

    This function sets bitrate_mask to be used.

    :param hw:
        Pointer to the ieee80211_hw structure
    :type hw: struct ieee80211_hw \*

    :param vif:
        Pointer to the ieee80211_vif structure.
    :type vif: struct ieee80211_vif \*

    :param mask:
        Pointer to the cfg80211_bitrate_mask structure.
    :type mask: const struct cfg80211_bitrate_mask \*

.. _`rsi_mac80211_set_rate_mask.return`:

Return
------

0 on success.

.. _`rsi_perform_cqm`:

rsi_perform_cqm
===============

.. c:function:: void rsi_perform_cqm(struct rsi_common *common, u8 *bssid, s8 rssi, struct ieee80211_vif *vif)

    This function performs cqm.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param bssid:
        pointer to the bssid.
    :type bssid: u8 \*

    :param rssi:
        RSSI value.
    :type rssi: s8

    :param vif:
        *undescribed*
    :type vif: struct ieee80211_vif \*

.. _`rsi_fill_rx_status`:

rsi_fill_rx_status
==================

.. c:function:: void rsi_fill_rx_status(struct ieee80211_hw *hw, struct sk_buff *skb, struct rsi_common *common, struct ieee80211_rx_status *rxs)

    This function fills rx status in ieee80211_rx_status structure.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param skb:
        Pointer to the socket buffer structure.
    :type skb: struct sk_buff \*

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param rxs:
        Pointer to the ieee80211_rx_status structure.
    :type rxs: struct ieee80211_rx_status \*

.. _`rsi_fill_rx_status.return`:

Return
------

None.

.. _`rsi_indicate_pkt_to_os`:

rsi_indicate_pkt_to_os
======================

.. c:function:: void rsi_indicate_pkt_to_os(struct rsi_common *common, struct sk_buff *skb)

    This function sends recieved packet to mac80211.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param skb:
        Pointer to the socket buffer structure.
    :type skb: struct sk_buff \*

.. _`rsi_indicate_pkt_to_os.return`:

Return
------

None.

.. _`rsi_mac80211_sta_add`:

rsi_mac80211_sta_add
====================

.. c:function:: int rsi_mac80211_sta_add(struct ieee80211_hw *hw, struct ieee80211_vif *vif, struct ieee80211_sta *sta)

    This function notifies driver about a peer getting connected.

    :param hw:
        pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param vif:
        Pointer to the ieee80211_vif structure.
    :type vif: struct ieee80211_vif \*

    :param sta:
        Pointer to the ieee80211_sta structure.
    :type sta: struct ieee80211_sta \*

.. _`rsi_mac80211_sta_add.return`:

Return
------

0 on success, negative error codes on failure.

.. _`rsi_mac80211_sta_remove`:

rsi_mac80211_sta_remove
=======================

.. c:function:: int rsi_mac80211_sta_remove(struct ieee80211_hw *hw, struct ieee80211_vif *vif, struct ieee80211_sta *sta)

    This function notifies driver about a peer getting disconnected.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param vif:
        Pointer to the ieee80211_vif structure.
    :type vif: struct ieee80211_vif \*

    :param sta:
        Pointer to the ieee80211_sta structure.
    :type sta: struct ieee80211_sta \*

.. _`rsi_mac80211_sta_remove.return`:

Return
------

0 on success, negative error codes on failure.

.. _`rsi_mac80211_set_antenna`:

rsi_mac80211_set_antenna
========================

.. c:function:: int rsi_mac80211_set_antenna(struct ieee80211_hw *hw, u32 tx_ant, u32 rx_ant)

    This function is used to configure tx and rx antennas.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param tx_ant:
        Bitmap for tx antenna
    :type tx_ant: u32

    :param rx_ant:
        Bitmap for rx antenna
    :type rx_ant: u32

.. _`rsi_mac80211_set_antenna.return`:

Return
------

0 on success, Negative error code on failure.

.. _`rsi_mac80211_get_antenna`:

rsi_mac80211_get_antenna
========================

.. c:function:: int rsi_mac80211_get_antenna(struct ieee80211_hw *hw, u32 *tx_ant, u32 *rx_ant)

    This function is used to configure tx and rx antennas.

    :param hw:
        Pointer to the ieee80211_hw structure.
    :type hw: struct ieee80211_hw \*

    :param tx_ant:
        Bitmap for tx antenna
    :type tx_ant: u32 \*

    :param rx_ant:
        Bitmap for rx antenna
    :type rx_ant: u32 \*

.. _`rsi_mac80211_get_antenna.return`:

Return
------

0 on success, negative error codes on failure.

.. _`rsi_mac80211_attach`:

rsi_mac80211_attach
===================

.. c:function:: int rsi_mac80211_attach(struct rsi_common *common)

    This function is used to initialize Mac80211 stack.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

.. _`rsi_mac80211_attach.return`:

Return
------

0 on success, negative error codes on failure.

.. This file was automatic generated / don't edit.

