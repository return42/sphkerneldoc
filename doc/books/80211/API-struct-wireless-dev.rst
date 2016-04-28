.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-wireless-dev:

===================
struct wireless_dev
===================

*man struct wireless_dev(9)*

*4.6.0-rc5*

wireless device state


Synopsis
========

.. code-block:: c

    struct wireless_dev {
      struct wiphy * wiphy;
      enum nl80211_iftype iftype;
      struct list_head list;
      struct net_device * netdev;
      u32 identifier;
      struct list_head mgmt_registrations;
      spinlock_t mgmt_registrations_lock;
      struct mutex mtx;
      bool use_4addr;
      bool p2p_started;
      u8 address[ETH_ALEN];
      u8 ssid[IEEE80211_MAX_SSID_LEN];
      u8 ssid_len;
      u8 mesh_id_len;
      u8 mesh_id_up_len;
      struct cfg80211_conn * conn;
      struct cfg80211_cached_keys * connect_keys;
      enum ieee80211_bss_type conn_bss_type;
      struct list_head event_list;
      spinlock_t event_lock;
      struct cfg80211_internal_bss * current_bss;
      struct cfg80211_chan_def preset_chandef;
      struct cfg80211_chan_def chandef;
      bool ibss_fixed;
      bool ibss_dfs_possible;
      bool ps;
      int ps_timeout;
      int beacon_interval;
      u32 ap_unexpected_nlportid;
      bool cac_started;
      unsigned long cac_start_time;
      unsigned int cac_time_ms;
      u32 owner_nlportid;
    #ifdef CONFIG_CFG80211_WEXT
      struct wext;
    #endif
    };


Members
=======

wiphy
    pointer to hardware description

iftype
    interface type

list
    (private) Used to collect the interfaces

netdev
    (private) Used to reference back to the netdev, may be ``NULL``

identifier
    (private) Identifier used in nl80211 to identify this wireless
    device if it has no netdev

mgmt_registrations
    list of registrations for management frames

mgmt_registrations_lock
    lock for the list

mtx
    mutex used to lock data in this struct, may be used by drivers and
    some API functions require it held

use_4addr
    indicates 4addr mode is used on this interface, must be set by
    driver (if supported) on add_interface BEFORE registering the
    netdev and may otherwise be used by driver read-only, will be update
    by cfg80211 on change_interface

p2p_started
    true if this is a P2P Device that has been started

address[ETH_ALEN]
    The address for this device, valid only if ``netdev`` is ``NULL``

ssid[IEEE80211_MAX_SSID_LEN]
    (private) Used by the internal configuration code

ssid_len
    (private) Used by the internal configuration code

mesh_id_len
    (private) Used by the internal configuration code

mesh_id_up_len
    (private) Used by the internal configuration code

conn
    (private) cfg80211 software SME connection state machine data

connect_keys
    (private) keys to set after connection is established

conn_bss_type
    connecting/connected BSS type

event_list
    (private) list for internal event processing

event_lock
    (private) lock for event list

current_bss
    (private) Used by the internal configuration code

preset_chandef
    (private) Used by the internal configuration code to track the
    channel to be used for AP later

chandef
    (private) Used by the internal configuration code to track the
    user-set channel definition.

ibss_fixed
    (private) IBSS is using fixed BSSID

ibss_dfs_possible
    (private) IBSS may change to a DFS channel

ps
    powersave mode is enabled

ps_timeout
    dynamic powersave timeout

beacon_interval
    beacon interval used on this device for transmitting beacons, 0 when
    not valid

ap_unexpected_nlportid
    (private) netlink port ID of application registered for unexpected
    class 3 frames (AP mode)

cac_started
    true if DFS channel availability check has been started

cac_start_time
    timestamp (jiffies) when the dfs state was entered.

cac_time_ms
    CAC time in ms

owner_nlportid
    (private) owner socket port ID

wext
    (private) Used by the internal wireless extensions compat code


Description
===========

For netdevs, this structure must be allocated by the driver that uses
the ieee80211_ptr field in struct net_device (this is intentional so
it can be allocated along with the netdev.) It need not be registered
then as netdev registration will be intercepted by cfg80211 to see the
new wireless device.

For non-netdev uses, it must also be allocated by the driver in response
to the cfg80211 callbacks that require it, as there's no netdev
registration in that case it may not be allocated outside of callback
operations that return it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
