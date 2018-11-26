.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/tx.c

.. _`ieee80211_build_hdr`:

ieee80211_build_hdr
===================

.. c:function:: struct sk_buff *ieee80211_build_hdr(struct ieee80211_sub_if_data *sdata, struct sk_buff *skb, u32 info_flags, struct sta_info *sta)

    build 802.11 header in the given frame

    :param sdata:
        virtual interface to build the header for
    :type sdata: struct ieee80211_sub_if_data \*

    :param skb:
        the skb to build the header in
    :type skb: struct sk_buff \*

    :param info_flags:
        skb flags to set
    :type info_flags: u32

    :param sta:
        *undescribed*
    :type sta: struct sta_info \*

.. _`ieee80211_build_hdr.description`:

Description
-----------

This function takes the skb with 802.3 header and reformats the header to
the appropriate IEEE 802.11 header based on which interface the packet is
being transmitted on.

Note that this function also takes care of the TX status request and
potential unsharing of the SKB - this needs to be interleaved with the
header building.

The function requires the read-side RCU lock held

.. _`ieee80211_build_hdr.return`:

Return
------

the (possibly reallocated) skb or an \ :c:func:`ERR_PTR`\  code

.. _`ieee80211_subif_start_xmit`:

ieee80211_subif_start_xmit
==========================

.. c:function:: netdev_tx_t ieee80211_subif_start_xmit(struct sk_buff *skb, struct net_device *dev)

    netif start_xmit function for 802.3 vifs

    :param skb:
        packet to be sent
    :type skb: struct sk_buff \*

    :param dev:
        incoming interface
    :type dev: struct net_device \*

.. _`ieee80211_subif_start_xmit.description`:

Description
-----------

On failure skb will be freed.

.. This file was automatic generated / don't edit.

