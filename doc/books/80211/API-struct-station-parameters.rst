
.. _API-struct-station-parameters:

=========================
struct station_parameters
=========================

*man struct station_parameters(9)*

*4.6.0-rc1*

station parameters


Synopsis
========

.. code-block:: c

    struct station_parameters {
      const u8 * supported_rates;
      struct net_device * vlan;
      u32 sta_flags_mask;
      u32 sta_flags_set;
      u32 sta_modify_mask;
      int listen_interval;
      u16 aid;
      u8 supported_rates_len;
      u8 plink_action;
      u8 plink_state;
      const struct ieee80211_ht_cap * ht_capa;
      const struct ieee80211_vht_cap * vht_capa;
      u8 uapsd_queues;
      u8 max_sp;
      enum nl80211_mesh_power_mode local_pm;
      u16 capability;
      const u8 * ext_capab;
      u8 ext_capab_len;
      const u8 * supported_channels;
      u8 supported_channels_len;
      const u8 * supported_oper_classes;
      u8 supported_oper_classes_len;
      u8 opmode_notif;
      bool opmode_notif_used;
    };


Members
=======

supported_rates
    supported rates in IEEE 802.11 format (or NULL for no change)

vlan
    vlan interface station should belong to

sta_flags_mask
    station flags that changed (bitmask of BIT(NL80211_STA_FLAG_...))

sta_flags_set
    station flags values (bitmask of BIT(NL80211_STA_FLAG_...))

sta_modify_mask
    bitmap indicating which parameters changed (for those that don't have a natural “no change” value), see ``enum`` station_parameters_apply_mask

listen_interval
    listen interval or -1 for no change

aid
    AID or zero for no change

supported_rates_len
    number of supported rates

plink_action
    plink action to take

plink_state
    set the peer link state for a station

ht_capa
    HT capabilities of station

vht_capa
    VHT capabilities of station

uapsd_queues
    bitmap of queues configured for uapsd. same format as the AC bitmap in the QoS info field

max_sp
    max Service Period. same format as the MAX_SP in the QoS info field (but already shifted down)

local_pm
    local link-specific mesh power save mode (no change when set to unknown)

capability
    station capability

ext_capab
    extended capabilities of the station

ext_capab_len
    number of extended capabilities

supported_channels
    supported channels in IEEE 802.11 format

supported_channels_len
    number of supported channels

supported_oper_classes
    supported oper classes in IEEE 802.11 format

supported_oper_classes_len
    number of supported operating classes

opmode_notif
    operating mode field from Operating Mode Notification

opmode_notif_used
    information if operating mode field is used


Description
===========

Used to change and create a new station.
