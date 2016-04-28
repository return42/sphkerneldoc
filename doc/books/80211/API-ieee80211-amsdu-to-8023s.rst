.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-amsdu-to-8023s:

========================
ieee80211_amsdu_to_8023s
========================

*man ieee80211_amsdu_to_8023s(9)*

*4.6.0-rc5*

decode an IEEE 802.11n A-MSDU frame


Synopsis
========

.. c:function:: void ieee80211_amsdu_to_8023s( struct sk_buff * skb, struct sk_buff_head * list, const u8 * addr, enum nl80211_iftype iftype, const unsigned int extra_headroom, bool has_80211_header )

Arguments
=========

``skb``
    The input IEEE 802.11n A-MSDU frame.

``list``
    The output list of 802.3 frames. It must be allocated and
    initialized by by the caller.

``addr``
    The device MAC address.

``iftype``
    The device interface type.

``extra_headroom``
    The hardware extra headroom for SKBs in the ``list``.

``has_80211_header``
    Set it true if SKB is with IEEE 802.11 header.


Description
===========

Decode an IEEE 802.11n A-MSDU frame and convert it to a list of 802.3
frames. The ``list`` will be empty if the decode fails. The ``skb`` is
consumed after the function returns.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
