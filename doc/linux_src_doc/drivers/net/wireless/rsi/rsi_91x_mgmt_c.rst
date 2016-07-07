.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/rsi/rsi_91x_mgmt.c

.. _`rsi_set_default_parameters`:

rsi_set_default_parameters
==========================

.. c:function:: void rsi_set_default_parameters(struct rsi_common *common)

    This function sets default parameters.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

.. _`rsi_set_default_parameters.return`:

Return
------

none

.. _`rsi_set_contention_vals`:

rsi_set_contention_vals
=======================

.. c:function:: void rsi_set_contention_vals(struct rsi_common *common)

    This function sets the contention values for the backoff procedure.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

.. _`rsi_set_contention_vals.return`:

Return
------

None.

.. _`rsi_send_internal_mgmt_frame`:

rsi_send_internal_mgmt_frame
============================

.. c:function:: int rsi_send_internal_mgmt_frame(struct rsi_common *common, struct sk_buff *skb)

    This function sends management frames to firmware.Also schedules packet to queue for transmission.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

    :param struct sk_buff \*skb:
        Pointer to the socket buffer structure.

.. _`rsi_send_internal_mgmt_frame.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_load_radio_caps`:

rsi_load_radio_caps
===================

.. c:function:: int rsi_load_radio_caps(struct rsi_common *common)

    This function is used to send radio capabilities values to firmware.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

.. _`rsi_load_radio_caps.return`:

Return
------

0 on success, corresponding negative error code on failure.

.. _`rsi_mgmt_pkt_to_core`:

rsi_mgmt_pkt_to_core
====================

.. c:function:: int rsi_mgmt_pkt_to_core(struct rsi_common *common, u8 *msg, s32 msg_len, u8 type)

    This function is the entry point for Mgmt module.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

    :param u8 \*msg:
        Pointer to received packet.

    :param s32 msg_len:
        Length of the recieved packet.

    :param u8 type:
        Type of recieved packet.

.. _`rsi_mgmt_pkt_to_core.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_hal_send_sta_notify_frame`:

rsi_hal_send_sta_notify_frame
=============================

.. c:function:: int rsi_hal_send_sta_notify_frame(struct rsi_common *common, u8 opmode, u8 notify_event, const unsigned char *bssid, u8 qos_enable, u16 aid)

    This function sends the station notify frame to firmware.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

    :param u8 opmode:
        Operating mode of device.

    :param u8 notify_event:
        Notification about station connection.

    :param const unsigned char \*bssid:
        bssid.

    :param u8 qos_enable:
        Qos is enabled.

    :param u16 aid:
        Aid (unique for all STA).

.. _`rsi_hal_send_sta_notify_frame.return`:

Return
------

status: 0 on success, corresponding negative error code on failure.

.. _`rsi_send_aggregation_params_frame`:

rsi_send_aggregation_params_frame
=================================

.. c:function:: int rsi_send_aggregation_params_frame(struct rsi_common *common, u16 tid, u16 ssn, u8 buf_size, u8 event)

    This function sends the ampdu indication frame to firmware.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

    :param u16 tid:
        traffic identifier.

    :param u16 ssn:
        ssn.

    :param u8 buf_size:
        buffer size.

    :param u8 event:
        notification about station connection.

.. _`rsi_send_aggregation_params_frame.return`:

Return
------

0 on success, corresponding negative error code on failure.

.. _`rsi_program_bb_rf`:

rsi_program_bb_rf
=================

.. c:function:: int rsi_program_bb_rf(struct rsi_common *common)

    This function starts base band and RF programming. This is called after initial configurations are done.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

.. _`rsi_program_bb_rf.return`:

Return
------

0 on success, corresponding negative error code on failure.

.. _`rsi_set_vap_capabilities`:

rsi_set_vap_capabilities
========================

.. c:function:: int rsi_set_vap_capabilities(struct rsi_common *common, enum opmode mode)

    This function send vap capability to firmware.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

    :param enum opmode mode:
        *undescribed*

.. _`rsi_set_vap_capabilities.return`:

Return
------

0 on success, corresponding negative error code on failure.

.. _`rsi_hal_load_key`:

rsi_hal_load_key
================

.. c:function:: int rsi_hal_load_key(struct rsi_common *common, u8 *data, u16 key_len, u8 key_type, u8 key_id, u32 cipher)

    This function is used to load keys within the firmware.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

    :param u8 \*data:
        Pointer to the key data.

    :param u16 key_len:
        Key length to be loaded.

    :param u8 key_type:
        Type of key: GROUP/PAIRWISE.

    :param u8 key_id:
        Key index.

    :param u32 cipher:
        Type of cipher used.

.. _`rsi_hal_load_key.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_send_reset_mac`:

rsi_send_reset_mac
==================

.. c:function:: int rsi_send_reset_mac(struct rsi_common *common)

    This function prepares reset MAC request and sends an internal management frame to indicate it to firmware.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

.. _`rsi_send_reset_mac.return`:

Return
------

0 on success, corresponding error code on failure.

.. _`rsi_band_check`:

rsi_band_check
==============

.. c:function:: int rsi_band_check(struct rsi_common *common)

    This function programs the band

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

.. _`rsi_band_check.return`:

Return
------

0 on success, corresponding error code on failure.

.. _`rsi_set_channel`:

rsi_set_channel
===============

.. c:function:: int rsi_set_channel(struct rsi_common *common, u16 channel)

    This function programs the channel.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

    :param u16 channel:
        Channel value to be set.

.. _`rsi_set_channel.return`:

Return
------

0 on success, corresponding error code on failure.

.. _`rsi_compare`:

rsi_compare
===========

.. c:function:: int rsi_compare(const void *a, const void *b)

    This function is used to compare two integers

    :param const void \*a:
        pointer to the first integer

    :param const void \*b:
        pointer to the second integer

.. _`rsi_compare.return`:

Return
------

0 if both are equal, -1 if the first is smaller, else 1

.. _`rsi_map_rates`:

rsi_map_rates
=============

.. c:function:: bool rsi_map_rates(u16 rate, int *offset)

    This function is used to map selected rates to hw rates.

    :param u16 rate:
        The standard rate to be mapped.

    :param int \*offset:
        Offset that will be returned.

.. _`rsi_map_rates.return`:

Return
------

0 if it is a mcs rate, else 1

.. _`rsi_send_auto_rate_request`:

rsi_send_auto_rate_request
==========================

.. c:function:: int rsi_send_auto_rate_request(struct rsi_common *common)

    This function is to set rates for connection and send autorate request to firmware.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

.. _`rsi_send_auto_rate_request.return`:

Return
------

0 on success, corresponding error code on failure.

.. _`rsi_inform_bss_status`:

rsi_inform_bss_status
=====================

.. c:function:: void rsi_inform_bss_status(struct rsi_common *common, u8 status, const unsigned char *bssid, u8 qos_enable, u16 aid)

    This function informs about bss status with the help of sta notify params by sending an internal management frame to firmware.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

    :param u8 status:
        Bss status type.

    :param const unsigned char \*bssid:
        Bssid.

    :param u8 qos_enable:
        Qos is enabled.

    :param u16 aid:
        Aid (unique for all STAs).

.. _`rsi_inform_bss_status.return`:

Return
------

None.

.. _`rsi_eeprom_read`:

rsi_eeprom_read
===============

.. c:function:: int rsi_eeprom_read(struct rsi_common *common)

    This function sends a frame to read the mac address from the eeprom.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

.. _`rsi_eeprom_read.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_send_block_unblock_frame`:

rsi_send_block_unblock_frame
============================

.. c:function:: int rsi_send_block_unblock_frame(struct rsi_common *common, bool block_event)

    data queues in the firmware

    :param struct rsi_common \*common:
        *undescribed*

    :param bool block_event:
        *undescribed*

.. _`rsi_send_block_unblock_frame.description`:

Description
-----------

\ ``param``\  common Pointer to the driver private structure.
\ ``param``\  block event - block if true, unblock if false
\ ``return``\  0 on success, -1 on failure.

.. _`rsi_handle_ta_confirm_type`:

rsi_handle_ta_confirm_type
==========================

.. c:function:: int rsi_handle_ta_confirm_type(struct rsi_common *common, u8 *msg)

    This function handles the confirm frames.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

    :param u8 \*msg:
        Pointer to received packet.

.. _`rsi_handle_ta_confirm_type.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_mgmt_pkt_recv`:

rsi_mgmt_pkt_recv
=================

.. c:function:: int rsi_mgmt_pkt_recv(struct rsi_common *common, u8 *msg)

    This function processes the management packets recieved from the hardware.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

    :param u8 \*msg:
        Pointer to the received packet.

.. _`rsi_mgmt_pkt_recv.return`:

Return
------

0 on success, -1 on failure.

.. This file was automatic generated / don't edit.

