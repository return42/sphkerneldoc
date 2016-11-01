.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/zydas/zd1211rw/zd_mac.c

.. _`zd_mac_tx_status`:

zd_mac_tx_status
================

.. c:function:: void zd_mac_tx_status(struct ieee80211_hw *hw, struct sk_buff *skb, int ackssi, struct tx_status *tx_status)

    reports tx status of a packet if required \ ``hw``\  - a \ :c:type:`struct ieee80211_hw <ieee80211_hw>`\  pointer \ ``skb``\  - a sk-buffer

    :param struct ieee80211_hw \*hw:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

    :param int ackssi:
        ACK signal strength
        \ ``success``\  - True for successful transmission of the frame

    :param struct tx_status \*tx_status:
        *undescribed*

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

    :param struct urb \*urb:
        *undescribed*

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

    :param struct sk_buff \*skb:
        a \ :c:type:`struct sk_buff <sk_buff>`\  pointer

    :param int error:
        error value, 0 if transmission successful

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

    :param struct ieee80211_hw \*hw:
        *undescribed*

    :param struct ieee80211_tx_control \*control:
        the control structure

    :param struct sk_buff \*skb:
        socket buffer

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

    :param struct ieee80211_hw \*hw:
        *undescribed*

    :param struct ieee80211_hdr \*rx_hdr:
        received header

    :param struct ieee80211_rx_status \*stats:
        the status for the received packet

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

