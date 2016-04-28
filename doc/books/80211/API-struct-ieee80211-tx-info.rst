.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ieee80211-tx-info:

========================
struct ieee80211_tx_info
========================

*man struct ieee80211_tx_info(9)*

*4.6.0-rc5*

skb transmit information


Synopsis
========

.. code-block:: c

    struct ieee80211_tx_info {
      u32 flags;
      u8 band;
      u8 hw_queue;
      u16 ack_frame_id;
      union {unnamed_union};
    };


Members
=======

flags
    transmit info flags, defined above

band
    the band to transmit on (use for checking for races)

hw_queue
    HW queue to put the frame on, ``skb_get_queue_mapping`` gives the AC

ack_frame_id
    internal frame ID for TX status, used internally

{unnamed_union}
    anonymous


Description
===========

This structure is placed in skb->cb for three uses: (1) mac80211 TX
control - mac80211 tells the driver what to do (2) driver internal use
(if applicable) (3) TX status information - driver tells mac80211 what
happened


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
