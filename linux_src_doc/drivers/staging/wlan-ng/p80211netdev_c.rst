.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/wlan-ng/p80211netdev.c

.. _`p80211_convert_to_ether`:

p80211_convert_to_ether
=======================

.. c:function:: int p80211_convert_to_ether(struct wlandevice *wlandev, struct sk_buff *skb)

    conversion from 802.11 frame to ethernet frame

    :param struct wlandevice \*wlandev:
        pointer to WLAN device

    :param struct sk_buff \*skb:
        pointer to socket buffer

.. _`p80211_convert_to_ether.return`:

Return
------

0 if conversion succeeded
CONV_TO_ETHER_FAILED if conversion failed
CONV_TO_ETHER_SKIPPED if frame is ignored

.. _`p80211netdev_rx_bh`:

p80211netdev_rx_bh
==================

.. c:function:: void p80211netdev_rx_bh(unsigned long arg)

    deferred processing of all received frames

    :param unsigned long arg:
        pointer to WLAN network device structure (cast to unsigned long)

.. This file was automatic generated / don't edit.

