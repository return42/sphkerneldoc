.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/zydas/zd1211rw/zd_mac.c

.. _`zd_mac_tx_status`:

zd_mac_tx_status
================

.. c:function:: void zd_mac_tx_status(struct ieee80211_hw *hw, struct sk_buff *skb, int ackssi, struct tx_status *tx_status)

    reports tx status of a packet if required \ ``hw``\  - a \ :c:type:`struct ieee80211_hw <ieee80211_hw>`\  pointer \ ``skb``\  - a sk-buffer

    :param hw:
        *undescribed*
    :type hw: struct ieee80211_hw \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param ackssi:
        ACK signal strength
        \ ``success``\  - True for successful transmission of the frame
    :type ackssi: int

    :param tx_status:
        *undescribed*
    :type tx_status: struct tx_status \*

.. _`zd_mac_tx_status.description`:

Description
-----------

This information calls \ :c:func:`ieee80211_tx_status_irqsafe`\  if required by the
control information. It copies the control information into the status
information.

If no status information has been requested, the skb is freed.

.. _`zd_mac_tx_failed`:

zd_mac_tx_failed
================

.. c:function:: void zd_mac_tx_failed(struct urb *urb)

    callback for failed frames

    :param urb:
        *undescribed*
    :type urb: struct urb \*

.. _`zd_mac_tx_failed.description`:

Description
-----------

This function is called if a frame couldn't be successfully
transferred. The first frame from the tx queue, will be selected and
reported as error to the upper layers.

.. _`zd_mac_tx_to_dev`:

zd_mac_tx_to_dev
================

.. c:function:: void zd_mac_tx_to_dev(struct sk_buff *skb, int error)

    callback for USB layer

    :param skb:
        a \ :c:type:`struct sk_buff <sk_buff>`\  pointer
    :type skb: struct sk_buff \*

    :param error:
        error value, 0 if transmission successful
    :type error: int

.. _`zd_mac_tx_to_dev.description`:

Description
-----------

Informs the MAC layer that the frame has successfully transferred to the
device. If an ACK is required and the transfer to the device has been
successful, the packets are put on the \ ``ack_wait_queue``\  with
the control set removed.

.. _`zd_op_tx`:

zd_op_tx
========

.. c:function:: void zd_op_tx(struct ieee80211_hw *hw, struct ieee80211_tx_control *control, struct sk_buff *skb)

    transmits a network frame to the device

    :param hw:
        *undescribed*
    :type hw: struct ieee80211_hw \*

    :param control:
        the control structure
    :type control: struct ieee80211_tx_control \*

    :param skb:
        socket buffer
    :type skb: struct sk_buff \*

.. _`zd_op_tx.description`:

Description
-----------

This function transmit an IEEE 802.11 network frame to the device. The
control block of the skbuff will be initialized. If necessary the incoming
mac80211 queues will be stopped.

.. _`filter_ack`:

filter_ack
==========

.. c:function:: int filter_ack(struct ieee80211_hw *hw, struct ieee80211_hdr *rx_hdr, struct ieee80211_rx_status *stats)

    filters incoming packets for acknowledgements

    :param hw:
        *undescribed*
    :type hw: struct ieee80211_hw \*

    :param rx_hdr:
        received header
    :type rx_hdr: struct ieee80211_hdr \*

    :param stats:
        the status for the received packet
    :type stats: struct ieee80211_rx_status \*

.. _`filter_ack.description`:

Description
-----------

This functions looks for ACK packets and tries to match them with the
frames in the tx queue. If a match is found the frame will be dequeued and
the upper layers is informed about the successful transmission. If
mac80211 queues have been stopped and the number of frames still to be
transmitted is low the queues will be opened again.

Returns 1 if the frame was an ACK, 0 if it was ignored.

.. This file was automatic generated / don't edit.

