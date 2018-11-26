.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/rsi/rsi_91x_mgmt.c

.. _`rsi_set_default_parameters`:

rsi_set_default_parameters
==========================

.. c:function:: void rsi_set_default_parameters(struct rsi_common *common)

    This function sets default parameters.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

.. _`rsi_set_default_parameters.return`:

Return
------

none

.. _`rsi_set_contention_vals`:

rsi_set_contention_vals
=======================

.. c:function:: void rsi_set_contention_vals(struct rsi_common *common)

    This function sets the contention values for the backoff procedure.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

.. _`rsi_set_contention_vals.return`:

Return
------

None.

.. _`rsi_send_internal_mgmt_frame`:

rsi_send_internal_mgmt_frame
============================

.. c:function:: int rsi_send_internal_mgmt_frame(struct rsi_common *common, struct sk_buff *skb)

    This function sends management frames to firmware.Also schedules packet to queue for transmission.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param skb:
        Pointer to the socket buffer structure.
    :type skb: struct sk_buff \*

.. _`rsi_send_internal_mgmt_frame.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_load_radio_caps`:

rsi_load_radio_caps
===================

.. c:function:: int rsi_load_radio_caps(struct rsi_common *common)

    This function is used to send radio capabilities values to firmware.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

.. _`rsi_load_radio_caps.return`:

Return
------

0 on success, corresponding negative error code on failure.

.. _`rsi_mgmt_pkt_to_core`:

rsi_mgmt_pkt_to_core
====================

.. c:function:: int rsi_mgmt_pkt_to_core(struct rsi_common *common, u8 *msg, s32 msg_len)

    This function is the entry point for Mgmt module.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param msg:
        Pointer to received packet.
    :type msg: u8 \*

    :param msg_len:
        Length of the recieved packet.
    :type msg_len: s32

.. _`rsi_mgmt_pkt_to_core.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_hal_send_sta_notify_frame`:

rsi_hal_send_sta_notify_frame
=============================

.. c:function:: int rsi_hal_send_sta_notify_frame(struct rsi_common *common, enum opmode opmode, u8 notify_event, const unsigned char *bssid, u8 qos_enable, u16 aid, u16 sta_id, struct ieee80211_vif *vif)

    This function sends the station notify frame to firmware.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param opmode:
        Operating mode of device.
    :type opmode: enum opmode

    :param notify_event:
        Notification about station connection.
    :type notify_event: u8

    :param bssid:
        bssid.
    :type bssid: const unsigned char \*

    :param qos_enable:
        Qos is enabled.
    :type qos_enable: u8

    :param aid:
        Aid (unique for all STA).
    :type aid: u16

    :param sta_id:
        *undescribed*
    :type sta_id: u16

    :param vif:
        *undescribed*
    :type vif: struct ieee80211_vif \*

.. _`rsi_hal_send_sta_notify_frame.return`:

Return
------

status: 0 on success, corresponding negative error code on failure.

.. _`rsi_send_aggregation_params_frame`:

rsi_send_aggregation_params_frame
=================================

.. c:function:: int rsi_send_aggregation_params_frame(struct rsi_common *common, u16 tid, u16 ssn, u8 buf_size, u8 event, u8 sta_id)

    This function sends the ampdu indication frame to firmware.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param tid:
        traffic identifier.
    :type tid: u16

    :param ssn:
        ssn.
    :type ssn: u16

    :param buf_size:
        buffer size.
    :type buf_size: u8

    :param event:
        notification about station connection.
    :type event: u8

    :param sta_id:
        *undescribed*
    :type sta_id: u8

.. _`rsi_send_aggregation_params_frame.return`:

Return
------

0 on success, corresponding negative error code on failure.

.. _`rsi_program_bb_rf`:

rsi_program_bb_rf
=================

.. c:function:: int rsi_program_bb_rf(struct rsi_common *common)

    This function starts base band and RF programming. This is called after initial configurations are done.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

.. _`rsi_program_bb_rf.return`:

Return
------

0 on success, corresponding negative error code on failure.

.. _`rsi_set_vap_capabilities`:

rsi_set_vap_capabilities
========================

.. c:function:: int rsi_set_vap_capabilities(struct rsi_common *common, enum opmode mode, u8 *mac_addr, u8 vap_id, u8 vap_status)

    This function send vap capability to firmware.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param mode:
        *undescribed*
    :type mode: enum opmode

    :param mac_addr:
        *undescribed*
    :type mac_addr: u8 \*

    :param vap_id:
        *undescribed*
    :type vap_id: u8

    :param vap_status:
        *undescribed*
    :type vap_status: u8

.. _`rsi_set_vap_capabilities.return`:

Return
------

0 on success, corresponding negative error code on failure.

.. _`rsi_hal_load_key`:

rsi_hal_load_key
================

.. c:function:: int rsi_hal_load_key(struct rsi_common *common, u8 *data, u16 key_len, u8 key_type, u8 key_id, u32 cipher, s16 sta_id, struct ieee80211_vif *vif)

    This function is used to load keys within the firmware.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param data:
        Pointer to the key data.
    :type data: u8 \*

    :param key_len:
        Key length to be loaded.
    :type key_len: u16

    :param key_type:
        Type of key: GROUP/PAIRWISE.
    :type key_type: u8

    :param key_id:
        Key index.
    :type key_id: u8

    :param cipher:
        Type of cipher used.
    :type cipher: u32

    :param sta_id:
        *undescribed*
    :type sta_id: s16

    :param vif:
        *undescribed*
    :type vif: struct ieee80211_vif \*

.. _`rsi_hal_load_key.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_send_reset_mac`:

rsi_send_reset_mac
==================

.. c:function:: int rsi_send_reset_mac(struct rsi_common *common)

    This function prepares reset MAC request and sends an internal management frame to indicate it to firmware.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

.. _`rsi_send_reset_mac.return`:

Return
------

0 on success, corresponding error code on failure.

.. _`rsi_band_check`:

rsi_band_check
==============

.. c:function:: int rsi_band_check(struct rsi_common *common, struct ieee80211_channel *curchan)

    This function programs the band

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param curchan:
        *undescribed*
    :type curchan: struct ieee80211_channel \*

.. _`rsi_band_check.return`:

Return
------

0 on success, corresponding error code on failure.

.. _`rsi_set_channel`:

rsi_set_channel
===============

.. c:function:: int rsi_set_channel(struct rsi_common *common, struct ieee80211_channel *channel)

    This function programs the channel.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param channel:
        Channel value to be set.
    :type channel: struct ieee80211_channel \*

.. _`rsi_set_channel.return`:

Return
------

0 on success, corresponding error code on failure.

.. _`rsi_send_radio_params_update`:

rsi_send_radio_params_update
============================

.. c:function:: int rsi_send_radio_params_update(struct rsi_common *common)

    This function sends the radio parameters update to device

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

.. _`rsi_send_radio_params_update.return`:

Return
------

0 on success, corresponding error code on failure.

.. _`rsi_compare`:

rsi_compare
===========

.. c:function:: int rsi_compare(const void *a, const void *b)

    This function is used to compare two integers

    :param a:
        pointer to the first integer
    :type a: const void \*

    :param b:
        pointer to the second integer
    :type b: const void \*

.. _`rsi_compare.return`:

Return
------

0 if both are equal, -1 if the first is smaller, else 1

.. _`rsi_map_rates`:

rsi_map_rates
=============

.. c:function:: bool rsi_map_rates(u16 rate, int *offset)

    This function is used to map selected rates to hw rates.

    :param rate:
        The standard rate to be mapped.
    :type rate: u16

    :param offset:
        Offset that will be returned.
    :type offset: int \*

.. _`rsi_map_rates.return`:

Return
------

0 if it is a mcs rate, else 1

.. _`rsi_send_auto_rate_request`:

rsi_send_auto_rate_request
==========================

.. c:function:: int rsi_send_auto_rate_request(struct rsi_common *common, struct ieee80211_sta *sta, u16 sta_id, struct ieee80211_vif *vif)

    This function is to set rates for connection and send autorate request to firmware.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param sta:
        *undescribed*
    :type sta: struct ieee80211_sta \*

    :param sta_id:
        *undescribed*
    :type sta_id: u16

    :param vif:
        *undescribed*
    :type vif: struct ieee80211_vif \*

.. _`rsi_send_auto_rate_request.return`:

Return
------

0 on success, corresponding error code on failure.

.. _`rsi_inform_bss_status`:

rsi_inform_bss_status
=====================

.. c:function:: void rsi_inform_bss_status(struct rsi_common *common, enum opmode opmode, u8 status, const u8 *addr, u8 qos_enable, u16 aid, struct ieee80211_sta *sta, u16 sta_id, u16 assoc_cap, struct ieee80211_vif *vif)

    This function informs about bss status with the help of sta notify params by sending an internal management frame to firmware.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param opmode:
        *undescribed*
    :type opmode: enum opmode

    :param status:
        Bss status type.
    :type status: u8

    :param addr:
        *undescribed*
    :type addr: const u8 \*

    :param qos_enable:
        Qos is enabled.
    :type qos_enable: u8

    :param aid:
        Aid (unique for all STAs).
    :type aid: u16

    :param sta:
        *undescribed*
    :type sta: struct ieee80211_sta \*

    :param sta_id:
        *undescribed*
    :type sta_id: u16

    :param assoc_cap:
        *undescribed*
    :type assoc_cap: u16

    :param vif:
        *undescribed*
    :type vif: struct ieee80211_vif \*

.. _`rsi_inform_bss_status.return`:

Return
------

None.

.. _`rsi_eeprom_read`:

rsi_eeprom_read
===============

.. c:function:: int rsi_eeprom_read(struct rsi_common *common)

    This function sends a frame to read the mac address from the eeprom.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

.. _`rsi_eeprom_read.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_send_block_unblock_frame`:

rsi_send_block_unblock_frame
============================

.. c:function:: int rsi_send_block_unblock_frame(struct rsi_common *common, bool block_event)

    data queues in the firmware

    :param common:
        *undescribed*
    :type common: struct rsi_common \*

    :param block_event:
        *undescribed*
    :type block_event: bool

.. _`rsi_send_block_unblock_frame.description`:

Description
-----------

\ ``param``\  common Pointer to the driver private structure.
\ ``param``\  block event - block if true, unblock if false
\ ``return``\  0 on success, -1 on failure.

.. _`rsi_send_rx_filter_frame`:

rsi_send_rx_filter_frame
========================

.. c:function:: int rsi_send_rx_filter_frame(struct rsi_common *common, u16 rx_filter_word)

    Sends a frame to filter the RX packets

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param rx_filter_word:
        Flags of filter packets
    :type rx_filter_word: u16

.. _`rsi_set_antenna`:

rsi_set_antenna
===============

.. c:function:: int rsi_set_antenna(struct rsi_common *common, u8 antenna)

    This fuction send antenna configuration request to device

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param antenna:
        bitmap for tx antenna selection
    :type antenna: u8

.. _`rsi_set_antenna.return`:

Return
------

0 on Success, negative error code on failure

.. _`rsi_handle_ta_confirm_type`:

rsi_handle_ta_confirm_type
==========================

.. c:function:: int rsi_handle_ta_confirm_type(struct rsi_common *common, u8 *msg)

    This function handles the confirm frames.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param msg:
        Pointer to received packet.
    :type msg: u8 \*

.. _`rsi_handle_ta_confirm_type.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_mgmt_pkt_recv`:

rsi_mgmt_pkt_recv
=================

.. c:function:: int rsi_mgmt_pkt_recv(struct rsi_common *common, u8 *msg)

    This function processes the management packets recieved from the hardware.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param msg:
        Pointer to the received packet.
    :type msg: u8 \*

.. _`rsi_mgmt_pkt_recv.return`:

Return
------

0 on success, -1 on failure.

.. This file was automatic generated / don't edit.

