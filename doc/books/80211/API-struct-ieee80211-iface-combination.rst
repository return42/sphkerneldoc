
.. _API-struct-ieee80211-iface-combination:

==================================
struct ieee80211_iface_combination
==================================

*man struct ieee80211_iface_combination(9)*

*4.6.0-rc1*

possible interface combination


Synopsis
========

.. code-block:: c

    struct ieee80211_iface_combination {
      const struct ieee80211_iface_limit * limits;
      u32 num_different_channels;
      u16 max_interfaces;
      u8 n_limits;
      bool beacon_int_infra_match;
      u8 radar_detect_widths;
      u8 radar_detect_regions;
    };


Members
=======

limits
    limits for the given interface types

num_different_channels
    can use up to this many different channels

max_interfaces
    maximum number of interfaces in total allowed in this group

n_limits
    number of limitations

beacon_int_infra_match
    In this combination, the beacon intervals between infrastructure and AP types must match. This is required only in special cases.

radar_detect_widths
    bitmap of channel widths supported for radar detection

radar_detect_regions
    bitmap of regions supported for radar detection


Description
===========

With this structure the driver can describe which interface combinations it supports concurrently.


Examples
========


.. code-block:: c

       1. Allow #STA <= 1, #AP <= 1, matching BI, channels = 1, 2 total:

        struct ieee80211_iface_limit limits1[] = {
        { .max = 1, .types = BIT(NL80211_IFTYPE_STATION), },
        { .max = 1, .types = BIT(NL80211_IFTYPE_AP}, },
        };
        struct ieee80211_iface_combination combination1 = {
        .limits = limits1,
        .n_limits = ARRAY_SIZE(limits1),
        .max_interfaces = 2,
        .beacon_int_infra_match = true,
        };


       2. Allow #{AP, P2P-GO} <= 8, channels = 1, 8 total:

        struct ieee80211_iface_limit limits2[] = {
        { .max = 8, .types = BIT(NL80211_IFTYPE_AP) |
                     BIT(NL80211_IFTYPE_P2P_GO), },
        };
        struct ieee80211_iface_combination combination2 = {
        .limits = limits2,
        .n_limits = ARRAY_SIZE(limits2),
        .max_interfaces = 8,
        .num_different_channels = 1,
        };


       3. Allow #STA <= 1, #{P2P-client,P2P-GO} <= 3 on two channels, 4 total.

       This allows for an infrastructure connection and three P2P connections.

        struct ieee80211_iface_limit limits3[] = {
        { .max = 1, .types = BIT(NL80211_IFTYPE_STATION), },
        { .max = 3, .types = BIT(NL80211_IFTYPE_P2P_GO) |
                     BIT(NL80211_IFTYPE_P2P_CLIENT), },
        };
        struct ieee80211_iface_combination combination3 = {
        .limits = limits3,
        .n_limits = ARRAY_SIZE(limits3),
        .max_interfaces = 4,
        .num_different_channels = 2,
        };


