
.. _API-struct-wiphy:

============
struct wiphy
============

*man struct wiphy(9)*

*4.6.0-rc1*

wireless hardware description


Synopsis
========

.. code-block:: c

    struct wiphy {
      u8 perm_addr[ETH_ALEN];
      u8 addr_mask[ETH_ALEN];
      struct mac_address * addresses;
      const struct ieee80211_txrx_stypes * mgmt_stypes;
      const struct ieee80211_iface_combination * iface_combinations;
      int n_iface_combinations;
      u16 software_iftypes;
      u16 n_addresses;
      u16 interface_modes;
      u16 max_acl_mac_addrs;
      u32 flags;
      u32 regulatory_flags;
      u32 features;
      u8 ext_features[DIV_ROUND_UP(NUM_NL80211_EXT_FEATURES# 8)];
      u32 ap_sme_capa;
      enum cfg80211_signal_type signal_type;
      int bss_priv_size;
      u8 max_scan_ssids;
      u8 max_sched_scan_ssids;
      u8 max_match_sets;
      u16 max_scan_ie_len;
      u16 max_sched_scan_ie_len;
      u32 max_sched_scan_plans;
      u32 max_sched_scan_plan_interval;
      u32 max_sched_scan_plan_iterations;
      int n_cipher_suites;
      const u32 * cipher_suites;
      u8 retry_short;
      u8 retry_long;
      u32 frag_threshold;
      u32 rts_threshold;
      u8 coverage_class;
      char fw_version[ETHTOOL_FWVERS_LEN];
      u32 hw_version;
    #ifdef CONFIG_PM
      const struct wiphy_wowlan_support * wowlan;
      struct cfg80211_wowlan * wowlan_config;
    #endif
      u16 max_remain_on_channel_duration;
      u8 max_num_pmkids;
      u32 available_antennas_tx;
      u32 available_antennas_rx;
      u32 probe_resp_offload;
      const u8 * extended_capabilities;
      const u8 * extended_capabilities_mask;
      u8 extended_capabilities_len;
      const void * privid;
      struct ieee80211_supported_band * bands[IEEE80211_NUM_BANDS];
      void (* reg_notifier) (struct wiphy *wiphy,struct regulatory_request *request);
      const struct ieee80211_regdomain __rcu * regd;
      struct device dev;
      bool registered;
      struct dentry * debugfsdir;
      const struct ieee80211_ht_cap * ht_capa_mod_mask;
      const struct ieee80211_vht_cap * vht_capa_mod_mask;
      possible_net_t _net;
    #ifdef CONFIG_CFG80211_WEXT
      const struct iw_handler_def * wext;
    #endif
      const struct wiphy_coalesce_support * coalesce;
      const struct wiphy_vendor_command * vendor_commands;
      const struct nl80211_vendor_cmd_info * vendor_events;
      int n_vendor_commands;
      int n_vendor_events;
      u16 max_ap_assoc_sta;
      u8 max_num_csa_counters;
      u8 max_adj_channel_rssi_comp;
      char priv[0];
    };


Members
=======

perm_addr[ETH_ALEN]
    permanent MAC address of this device

addr_mask[ETH_ALEN]
    If the device supports multiple MAC addresses by masking, set this to a mask with variable bits set to 1, e.g. if the last four bits are variable then set it to
    00-00-00-00-00-0f. The actual variable bits shall be determined by the interfaces added, with interfaces not matching the mask being rejected to be brought up.

addresses
    If the device has more than one address, set this pointer to a list of addresses (6 bytes each). The first one will be used by default for perm_addr. In this case, the mask
    should be set to all-zeroes. In this case it is assumed that the device can handle the same number of arbitrary MAC addresses.

mgmt_stypes
    bitmasks of frame subtypes that can be subscribed to or transmitted through nl80211, points to an array indexed by interface type

iface_combinations
    Valid interface combinations array, should not list single interface types.

n_iface_combinations
    number of entries in ``iface_combinations`` array.

software_iftypes
    bitmask of software interface types, these are not subject to any restrictions since they are purely managed in SW.

n_addresses
    number of addresses in ``addresses``.

interface_modes
    bitmask of interfaces types valid for this wiphy, must be set by driver

max_acl_mac_addrs
    Maximum number of MAC addresses that the device supports for ACL.

flags
    wiphy flags, see ``enum`` wiphy_flags

regulatory_flags
    wiphy regulatory flags, see ``enum`` ieee80211_regulatory_flags

features
    features advertised to nl80211, see ``enum`` nl80211_feature_flags.

ext_features[DIV_ROUND_UP(NUM_NL80211_EXT_FEATURES# 8)]
    extended features advertised to nl80211, see ``enum`` nl80211_ext_feature_index.

ap_sme_capa
    AP SME capabilities, flags from ``enum`` nl80211_ap_sme_features.

signal_type
    signal type reported in ``struct cfg80211_bss``.

bss_priv_size
    each BSS struct has private data allocated with it, this variable determines its size

max_scan_ssids
    maximum number of SSIDs the device can scan for in any given scan

max_sched_scan_ssids
    maximum number of SSIDs the device can scan for in any given scheduled scan

max_match_sets
    maximum number of match sets the device can handle when performing a scheduled scan, 0 if filtering is not supported.

max_scan_ie_len
    maximum length of user-controlled IEs device can add to probe request frames transmitted during a scan, must not include fixed IEs like supported rates

max_sched_scan_ie_len
    same as max_scan_ie_len, but for scheduled scans

max_sched_scan_plans
    maximum number of scan plans (scan interval and number of iterations) for scheduled scan supported by the device.

max_sched_scan_plan_interval
    maximum interval (in seconds) for a single scan plan supported by the device.

max_sched_scan_plan_iterations
    maximum number of iterations for a single scan plan supported by the device.

n_cipher_suites
    number of supported cipher suites

cipher_suites
    supported cipher suites

retry_short
    Retry limit for short frames (dot11ShortRetryLimit)

retry_long
    Retry limit for long frames (dot11LongRetryLimit)

frag_threshold
    Fragmentation threshold (dot11FragmentationThreshold); -1 = fragmentation disabled, only odd values >= 256 used

rts_threshold
    RTS threshold (dot11RTSThreshold); -1 = RTS/CTS disabled

coverage_class
    current coverage class

fw_version[ETHTOOL_FWVERS_LEN]
    firmware version for ethtool reporting

hw_version
    hardware version for ethtool reporting

wowlan
    WoWLAN support information

wowlan_config
    current WoWLAN configuration; this should usually not be used since access to it is necessarily racy, use the parameter passed to the ``suspend`` operation instead.

max_remain_on_channel_duration
    Maximum time a remain-on-channel operation may request, if implemented.

max_num_pmkids
    maximum number of PMKIDs supported by device

available_antennas_tx
    bitmap of antennas which are available to be configured as TX antennas. Antenna configuration commands will be rejected unless this or ``available_antennas_rx`` is set.

available_antennas_rx
    bitmap of antennas which are available to be configured as RX antennas. Antenna configuration commands will be rejected unless this or ``available_antennas_tx`` is set.

probe_resp_offload
    Bitmap of supported protocols for probe response offloading. See ``enum`` nl80211_probe_resp_offload_support_attr. Only valid when the wiphy flag
    ``WIPHY_FLAG_AP_PROBE_RESP_OFFLOAD`` is set.

extended_capabilities
    extended capabilities supported by the driver, additional capabilities might be supported by userspace; these are the 802.11 extended capabilities (“Extended Capabilities
    element”) and are in the same format as in the information element. See 802.11-2012 8.4.2.29 for the defined fields.

extended_capabilities_mask
    mask of the valid values

extended_capabilities_len
    length of the extended capabilities

privid
    a pointer that drivers can use to identify if an arbitrary wiphy is theirs, e.g. in global notifiers

bands[IEEE80211_NUM_BANDS]
    information about bands/channels supported by this device

reg_notifier
    the driver's regulatory notification callback, note that if your driver uses ``wiphy_apply_custom_regulatory`` the reg_notifier's request can be passed as NULL

regd
    the driver's regulatory domain, if one was requested via the ``regulatory_hint`` API. This can be used by the driver on the ``reg_notifier`` if it chooses to ignore future
    regulatory domain changes caused by other drivers.

dev
    (virtual) struct device for this wiphy

registered
    helps synchronize suspend/resume with wiphy unregister

debugfsdir
    debugfs directory used for this wiphy, will be renamed automatically on wiphy renames

ht_capa_mod_mask
    Specify what ht_cap values can be over-ridden. If null, then none can be over-ridden.

vht_capa_mod_mask
    Specify what VHT capabilities can be over-ridden. If null, then none can be over-ridden.

_net
    the network namespace this wiphy currently lives in

wext
    wireless extension handlers

coalesce
    packet coalescing support information

vendor_commands
    array of vendor commands supported by the hardware

vendor_events
    array of vendor events supported by the hardware

n_vendor_commands
    number of vendor commands

n_vendor_events
    number of vendor events

max_ap_assoc_sta
    maximum number of associated stations supported in AP mode (including P2P GO) or 0 to indicate no such limit is advertised. The driver is allowed to advertise a theoretical
    limit that it can reach in some cases, but may not always reach.

max_num_csa_counters
    Number of supported csa_counters in beacons and probe responses. This value should be set if the driver wishes to limit the number of csa counters. Default (0) means infinite.

max_adj_channel_rssi_comp
    max offset of between the channel on which the frame was sent and the channel on which the frame was heard for which the reported rssi is still valid. If a driver is able to
    compensate the low rssi when a frame is heard on different channel, then it should set this variable to the maximal offset for which it can compensate. This value should be set
    in MHz.

priv[0]
    driver private data (sized according to ``wiphy_new`` parameter)
