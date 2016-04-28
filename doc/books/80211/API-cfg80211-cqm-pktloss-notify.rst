.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-cqm-pktloss-notify:

===========================
cfg80211_cqm_pktloss_notify
===========================

*man cfg80211_cqm_pktloss_notify(9)*

*4.6.0-rc5*

notify userspace about packetloss to peer


Synopsis
========

.. c:function:: void cfg80211_cqm_pktloss_notify( struct net_device * dev, const u8 * peer, u32 num_packets, gfp_t gfp )

Arguments
=========

``dev``
    network device

``peer``
    peer's MAC address

``num_packets``
    how many packets were lost -- should be a fixed threshold but
    probably no less than maybe 50, or maybe a throughput dependent
    threshold (to account for temporary interference)

``gfp``
    context flags


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
