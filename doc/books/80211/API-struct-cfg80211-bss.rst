.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-cfg80211-bss:

===================
struct cfg80211_bss
===================

*man struct cfg80211_bss(9)*

*4.6.0-rc5*

BSS description


Synopsis
========

.. code-block:: c

    struct cfg80211_bss {
      struct ieee80211_channel * channel;
      enum nl80211_bss_scan_width scan_width;
      const struct cfg80211_bss_ies __rcu * ies;
      const struct cfg80211_bss_ies __rcu * beacon_ies;
      const struct cfg80211_bss_ies __rcu * proberesp_ies;
      struct cfg80211_bss * hidden_beacon_bss;
      s32 signal;
      u16 beacon_interval;
      u16 capability;
      u8 bssid[ETH_ALEN];
      u8 priv[0];
    };


Members
=======

channel
    channel this BSS is on

scan_width
    width of the control channel

ies
    the information elements (Note that there is no guarantee that these
    are well-formed!); this is a pointer to either the beacon_ies or
    proberesp_ies depending on whether Probe Response frame has been
    received. It is always non-\ ``NULL``.

beacon_ies
    the information elements from the last Beacon frame (implementation
    note: if ``hidden_beacon_bss`` is set this struct doesn't own the
    beacon_ies, but they're just pointers to the ones from the
    ``hidden_beacon_bss`` struct)

proberesp_ies
    the information elements from the last Probe Response frame

hidden_beacon_bss
    in case this BSS struct represents a probe response from a BSS that
    hides the SSID in its beacon, this points to the BSS struct that
    holds the beacon data. ``beacon_ies`` is still valid, of course, and
    points to the same data as hidden_beacon_bss->beacon_ies in that
    case.

signal
    signal strength value (type depends on the wiphy's signal_type)

beacon_interval
    the beacon interval as from the frame

capability
    the capability field in host byte order

bssid[ETH_ALEN]
    BSSID of the BSS

priv[0]
    private area for driver use, has at least wiphy->bss_priv_size
    bytes


Description
===========

This structure describes a BSS (which may also be a mesh network) for
use in scan results and similar.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
