.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ieee80211-tx-rate-control:

================================
struct ieee80211_tx_rate_control
================================

*man struct ieee80211_tx_rate_control(9)*

*4.6.0-rc5*

rate control information for/from RC algo


Synopsis
========

.. code-block:: c

    struct ieee80211_tx_rate_control {
      struct ieee80211_hw * hw;
      struct ieee80211_supported_band * sband;
      struct ieee80211_bss_conf * bss_conf;
      struct sk_buff * skb;
      struct ieee80211_tx_rate reported_rate;
      bool rts;
      bool short_preamble;
      u8 max_rate_idx;
      u32 rate_idx_mask;
      u8 * rate_idx_mcs_mask;
      bool bss;
    };


Members
=======

hw
    The hardware the algorithm is invoked for.

sband
    The band this frame is being transmitted on.

bss_conf
    the current BSS configuration

skb
    the skb that will be transmitted, the control information in it
    needs to be filled in

reported_rate
    The rate control algorithm can fill this in to indicate which rate
    should be reported to userspace as the current rate and used for
    rate calculations in the mesh network.

rts
    whether RTS will be used for this frame because it is longer than
    the RTS threshold

short_preamble
    whether mac80211 will request short-preamble transmission if the
    selected rate supports it

max_rate_idx
    user-requested maximum (legacy) rate (deprecated; this will be
    removed once drivers get updated to use rate_idx_mask)

rate_idx_mask
    user-requested (legacy) rate mask

rate_idx_mcs_mask
    user-requested MCS rate mask (NULL if not in use)

bss
    whether this frame is sent out in AP or IBSS mode


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
