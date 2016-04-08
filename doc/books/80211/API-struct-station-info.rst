
.. _API-struct-station-info:

===================
struct station_info
===================

*man struct station_info(9)*

*4.6.0-rc1*

station information


Synopsis
========

.. code-block:: c

    struct station_info {
      u32 filled;
      u32 connected_time;
      u32 inactive_time;
      u64 rx_bytes;
      u64 tx_bytes;
      u16 llid;
      u16 plid;
      u8 plink_state;
      s8 signal;
      s8 signal_avg;
      u8 chains;
      s8 chain_signal[IEEE80211_MAX_CHAINS];
      s8 chain_signal_avg[IEEE80211_MAX_CHAINS];
      struct rate_info txrate;
      struct rate_info rxrate;
      u32 rx_packets;
      u32 tx_packets;
      u32 tx_retries;
      u32 tx_failed;
      u32 rx_dropped_misc;
      struct sta_bss_parameters bss_param;
      struct nl80211_sta_flag_update sta_flags;
      int generation;
      const u8 * assoc_req_ies;
      size_t assoc_req_ies_len;
      u32 beacon_loss_count;
      s64 t_offset;
      enum nl80211_mesh_power_mode local_pm;
      enum nl80211_mesh_power_mode peer_pm;
      enum nl80211_mesh_power_mode nonpeer_pm;
      u32 expected_throughput;
      u64 rx_beacon;
      u8 rx_beacon_signal_avg;
      struct cfg80211_tid_stats pertid[IEEE80211_NUM_TIDS + 1];
    };


Members
=======

filled
    bitflag of flags using the bits of ``enum`` nl80211_sta_info to indicate the relevant values in this struct for them

connected_time
    time(in secs) since a station is last connected

inactive_time
    time since last station activity (tx/rx) in milliseconds

rx_bytes
    bytes (size of MPDUs) received from this station

tx_bytes
    bytes (size of MPDUs) transmitted to this station

llid
    mesh local link id

plid
    mesh peer link id

plink_state
    mesh peer link state

signal
    The signal strength, type depends on the wiphy's signal_type. For CFG80211_SIGNAL_TYPE_MBM, value is expressed in _dBm_.

signal_avg
    Average signal strength, type depends on the wiphy's signal_type. For CFG80211_SIGNAL_TYPE_MBM, value is expressed in _dBm_.

chains
    bitmask for filled values in ``chain_signal``, ``chain_signal_avg``

chain_signal[IEEE80211_MAX_CHAINS]
    per-chain signal strength of last received packet in dBm

chain_signal_avg[IEEE80211_MAX_CHAINS]
    per-chain signal strength average in dBm

txrate
    current unicast bitrate from this station

rxrate
    current unicast bitrate to this station

rx_packets
    packets (MSDUs & MMPDUs) received from this station

tx_packets
    packets (MSDUs & MMPDUs) transmitted to this station

tx_retries
    cumulative retry counts (MPDUs)

tx_failed
    number of failed transmissions (MPDUs) (retries exceeded, no ACK)

rx_dropped_misc
    Dropped for un-specified reason.

bss_param
    current BSS parameters

sta_flags
    station flags mask & values

generation
    generation number for nl80211 dumps. This number should increase every time the list of stations changes, i.e. when a station is added or removed, so that userspace can tell
    whether it got a consistent snapshot.

assoc_req_ies
    IEs from (Re)Association Request. This is used only when in AP mode with drivers that do not use user space MLME/SME implementation. The information is provided for the
    ``cfg80211_new_sta`` calls to notify user space of the IEs.

assoc_req_ies_len
    Length of assoc_req_ies buffer in octets.

beacon_loss_count
    Number of times beacon loss event has triggered.

t_offset
    Time offset of the station relative to this host.

local_pm
    local mesh STA power save mode

peer_pm
    peer mesh STA power save mode

nonpeer_pm
    non-peer mesh STA power save mode

expected_throughput
    expected throughput in kbps (including 802.11 headers) towards this station.

rx_beacon
    number of beacons received from this peer

rx_beacon_signal_avg
    signal strength average (in dBm) for beacons received from this peer

pertid[IEEE80211_NUM_TIDS + 1]
    per-TID statistics, see ``struct cfg80211_tid_stats``, using the last (IEEE80211_NUM_TIDS) index for MSDUs not encapsulated in QoS-MPDUs.


Description
===========

Station information filled by driver for ``get_station`` and dump_station.
