.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-cfg80211-ops:

===================
struct cfg80211_ops
===================

*man struct cfg80211_ops(9)*

*4.6.0-rc5*

backend description for wireless configuration


Synopsis
========

.. code-block:: c

    struct cfg80211_ops {
      int (* suspend) (struct wiphy *wiphy, struct cfg80211_wowlan *wow);
      int (* resume) (struct wiphy *wiphy);
      void (* set_wakeup) (struct wiphy *wiphy, bool enabled);
      struct wireless_dev * (* add_virtual_intf) (struct wiphy *wiphy,const char *name,unsigned char name_assign_type,enum nl80211_iftype type,u32 *flags,struct vif_params *params);
      int (* del_virtual_intf) (struct wiphy *wiphy,struct wireless_dev *wdev);
      int (* change_virtual_intf) (struct wiphy *wiphy,struct net_device *dev,enum nl80211_iftype type, u32 *flags,struct vif_params *params);
      int (* add_key) (struct wiphy *wiphy, struct net_device *netdev,u8 key_index, bool pairwise, const u8 *mac_addr,struct key_params *params);
      int (* get_key) (struct wiphy *wiphy, struct net_device *netdev,u8 key_index, bool pairwise, const u8 *mac_addr,void *cookie,void (*callback);
      int (* del_key) (struct wiphy *wiphy, struct net_device *netdev,u8 key_index, bool pairwise, const u8 *mac_addr);
      int (* set_default_key) (struct wiphy *wiphy,struct net_device *netdev,u8 key_index, bool unicast, bool multicast);
      int (* set_default_mgmt_key) (struct wiphy *wiphy,struct net_device *netdev,u8 key_index);
      int (* start_ap) (struct wiphy *wiphy, struct net_device *dev,struct cfg80211_ap_settings *settings);
      int (* change_beacon) (struct wiphy *wiphy, struct net_device *dev,struct cfg80211_beacon_data *info);
      int (* stop_ap) (struct wiphy *wiphy, struct net_device *dev);
      int (* add_station) (struct wiphy *wiphy, struct net_device *dev,const u8 *mac,struct station_parameters *params);
      int (* del_station) (struct wiphy *wiphy, struct net_device *dev,struct station_del_parameters *params);
      int (* change_station) (struct wiphy *wiphy, struct net_device *dev,const u8 *mac,struct station_parameters *params);
      int (* get_station) (struct wiphy *wiphy, struct net_device *dev,const u8 *mac, struct station_info *sinfo);
      int (* dump_station) (struct wiphy *wiphy, struct net_device *dev,int idx, u8 *mac, struct station_info *sinfo);
      int (* add_mpath) (struct wiphy *wiphy, struct net_device *dev,const u8 *dst, const u8 *next_hop);
      int (* del_mpath) (struct wiphy *wiphy, struct net_device *dev,const u8 *dst);
      int (* change_mpath) (struct wiphy *wiphy, struct net_device *dev,const u8 *dst, const u8 *next_hop);
      int (* get_mpath) (struct wiphy *wiphy, struct net_device *dev,u8 *dst, u8 *next_hop, struct mpath_info *pinfo);
      int (* dump_mpath) (struct wiphy *wiphy, struct net_device *dev,int idx, u8 *dst, u8 *next_hop,struct mpath_info *pinfo);
      int (* get_mpp) (struct wiphy *wiphy, struct net_device *dev,u8 *dst, u8 *mpp, struct mpath_info *pinfo);
      int (* dump_mpp) (struct wiphy *wiphy, struct net_device *dev,int idx, u8 *dst, u8 *mpp,struct mpath_info *pinfo);
      int (* get_mesh_config) (struct wiphy *wiphy,struct net_device *dev,struct mesh_config *conf);
      int (* update_mesh_config) (struct wiphy *wiphy,struct net_device *dev, u32 mask,const struct mesh_config *nconf);
      int (* join_mesh) (struct wiphy *wiphy, struct net_device *dev,const struct mesh_config *conf,const struct mesh_setup *setup);
      int (* leave_mesh) (struct wiphy *wiphy, struct net_device *dev);
      int (* join_ocb) (struct wiphy *wiphy, struct net_device *dev,struct ocb_setup *setup);
      int (* leave_ocb) (struct wiphy *wiphy, struct net_device *dev);
      int (* change_bss) (struct wiphy *wiphy, struct net_device *dev,struct bss_parameters *params);
      int (* set_txq_params) (struct wiphy *wiphy, struct net_device *dev,struct ieee80211_txq_params *params);
      int (* libertas_set_mesh_channel) (struct wiphy *wiphy,struct net_device *dev,struct ieee80211_channel *chan);
      int (* set_monitor_channel) (struct wiphy *wiphy,struct cfg80211_chan_def *chandef);
      int (* scan) (struct wiphy *wiphy,struct cfg80211_scan_request *request);
      void (* abort_scan) (struct wiphy *wiphy, struct wireless_dev *wdev);
      int (* auth) (struct wiphy *wiphy, struct net_device *dev,struct cfg80211_auth_request *req);
      int (* assoc) (struct wiphy *wiphy, struct net_device *dev,struct cfg80211_assoc_request *req);
      int (* deauth) (struct wiphy *wiphy, struct net_device *dev,struct cfg80211_deauth_request *req);
      int (* disassoc) (struct wiphy *wiphy, struct net_device *dev,struct cfg80211_disassoc_request *req);
      int (* connect) (struct wiphy *wiphy, struct net_device *dev,struct cfg80211_connect_params *sme);
      int (* disconnect) (struct wiphy *wiphy, struct net_device *dev,u16 reason_code);
      int (* join_ibss) (struct wiphy *wiphy, struct net_device *dev,struct cfg80211_ibss_params *params);
      int (* leave_ibss) (struct wiphy *wiphy, struct net_device *dev);
      int (* set_mcast_rate) (struct wiphy *wiphy, struct net_device *dev,int rate[IEEE80211_NUM_BANDS]);
      int (* set_wiphy_params) (struct wiphy *wiphy, u32 changed);
      int (* set_tx_power) (struct wiphy *wiphy, struct wireless_dev *wdev,enum nl80211_tx_power_setting type, int mbm);
      int (* get_tx_power) (struct wiphy *wiphy, struct wireless_dev *wdev,int *dbm);
      int (* set_wds_peer) (struct wiphy *wiphy, struct net_device *dev,const u8 *addr);
      void (* rfkill_poll) (struct wiphy *wiphy);
    #ifdef CONFIG_NL80211_TESTMODE
      int (* testmode_cmd) (struct wiphy *wiphy, struct wireless_dev *wdev,void *data, int len);
      int (* testmode_dump) (struct wiphy *wiphy, struct sk_buff *skb,struct netlink_callback *cb,void *data, int len);
    #endif
      int (* set_bitrate_mask) (struct wiphy *wiphy,struct net_device *dev,const u8 *peer,const struct cfg80211_bitrate_mask *mask);
      int (* dump_survey) (struct wiphy *wiphy, struct net_device *netdev,int idx, struct survey_info *info);
      int (* set_pmksa) (struct wiphy *wiphy, struct net_device *netdev,struct cfg80211_pmksa *pmksa);
      int (* del_pmksa) (struct wiphy *wiphy, struct net_device *netdev,struct cfg80211_pmksa *pmksa);
      int (* flush_pmksa) (struct wiphy *wiphy, struct net_device *netdev);
      int (* remain_on_channel) (struct wiphy *wiphy,struct wireless_dev *wdev,struct ieee80211_channel *chan,unsigned int duration,u64 *cookie);
      int (* cancel_remain_on_channel) (struct wiphy *wiphy,struct wireless_dev *wdev,u64 cookie);
      int (* mgmt_tx) (struct wiphy *wiphy, struct wireless_dev *wdev,struct cfg80211_mgmt_tx_params *params,u64 *cookie);
      int (* mgmt_tx_cancel_wait) (struct wiphy *wiphy,struct wireless_dev *wdev,u64 cookie);
      int (* set_power_mgmt) (struct wiphy *wiphy, struct net_device *dev,bool enabled, int timeout);
      int (* set_cqm_rssi_config) (struct wiphy *wiphy,struct net_device *dev,s32 rssi_thold, u32 rssi_hyst);
      int (* set_cqm_txe_config) (struct wiphy *wiphy,struct net_device *dev,u32 rate, u32 pkts, u32 intvl);
      void (* mgmt_frame_register) (struct wiphy *wiphy,struct wireless_dev *wdev,u16 frame_type, bool reg);
      int (* set_antenna) (struct wiphy *wiphy, u32 tx_ant, u32 rx_ant);
      int (* get_antenna) (struct wiphy *wiphy, u32 *tx_ant, u32 *rx_ant);
      int (* sched_scan_start) (struct wiphy *wiphy,struct net_device *dev,struct cfg80211_sched_scan_request *request);
      int (* sched_scan_stop) (struct wiphy *wiphy, struct net_device *dev);
      int (* set_rekey_data) (struct wiphy *wiphy, struct net_device *dev,struct cfg80211_gtk_rekey_data *data);
      int (* tdls_mgmt) (struct wiphy *wiphy, struct net_device *dev,const u8 *peer, u8 action_code,  u8 dialog_token,u16 status_code, u32 peer_capability,bool initiator, const u8 *buf, size_t len);
      int (* tdls_oper) (struct wiphy *wiphy, struct net_device *dev,const u8 *peer, enum nl80211_tdls_operation oper);
      int (* probe_client) (struct wiphy *wiphy, struct net_device *dev,const u8 *peer, u64 *cookie);
      int (* set_noack_map) (struct wiphy *wiphy,struct net_device *dev,u16 noack_map);
      int (* get_channel) (struct wiphy *wiphy,struct wireless_dev *wdev,struct cfg80211_chan_def *chandef);
      int (* start_p2p_device) (struct wiphy *wiphy,struct wireless_dev *wdev);
      void (* stop_p2p_device) (struct wiphy *wiphy,struct wireless_dev *wdev);
      int (* set_mac_acl) (struct wiphy *wiphy, struct net_device *dev,const struct cfg80211_acl_data *params);
      int (* start_radar_detection) (struct wiphy *wiphy,struct net_device *dev,struct cfg80211_chan_def *chandef,u32 cac_time_ms);
      int (* update_ft_ies) (struct wiphy *wiphy, struct net_device *dev,struct cfg80211_update_ft_ies_params *ftie);
      int (* crit_proto_start) (struct wiphy *wiphy,struct wireless_dev *wdev,enum nl80211_crit_proto_id protocol,u16 duration);
      void (* crit_proto_stop) (struct wiphy *wiphy,struct wireless_dev *wdev);
      int (* set_coalesce) (struct wiphy *wiphy,struct cfg80211_coalesce *coalesce);
      int (* channel_switch) (struct wiphy *wiphy,struct net_device *dev,struct cfg80211_csa_settings *params);
      int (* set_qos_map) (struct wiphy *wiphy,struct net_device *dev,struct cfg80211_qos_map *qos_map);
      int (* set_ap_chanwidth) (struct wiphy *wiphy, struct net_device *dev,struct cfg80211_chan_def *chandef);
      int (* add_tx_ts) (struct wiphy *wiphy, struct net_device *dev,u8 tsid, const u8 *peer, u8 user_prio,u16 admitted_time);
      int (* del_tx_ts) (struct wiphy *wiphy, struct net_device *dev,u8 tsid, const u8 *peer);
      int (* tdls_channel_switch) (struct wiphy *wiphy,struct net_device *dev,const u8 *addr, u8 oper_class,struct cfg80211_chan_def *chandef);
      void (* tdls_cancel_channel_switch) (struct wiphy *wiphy,struct net_device *dev,const u8 *addr);
    };


Members
=======

suspend
    wiphy device needs to be suspended. The variable ``wow`` will be
    ``NULL`` or contain the enabled Wake-on-Wireless triggers that are
    configured for the device.

resume
    wiphy device needs to be resumed

set_wakeup
    Called when WoWLAN is enabled/disabled, use this callback to call
    ``device_set_wakeup_enable`` to enable/disable wakeup from the
    device.

add_virtual_intf
    create a new virtual interface with the given name, must set the
    struct wireless_dev's iftype. Beware: You must create the new
    netdev in the wiphy's network namespace! Returns the struct
    wireless_dev, or an ERR_PTR. For P2P device wdevs, the driver must
    also set the address member in the wdev.

del_virtual_intf
    remove the virtual interface

change_virtual_intf
    change type/configuration of virtual interface, keep the struct
    wireless_dev's iftype updated.

add_key
    add a key with the given parameters. ``mac_addr`` will be ``NULL``
    when adding a group key.

get_key
    get information about the key with the given parameters.
    ``mac_addr`` will be ``NULL`` when requesting information for a
    group key. All pointers given to the ``callback`` function need not
    be valid after it returns. This function should return an error if
    it is not possible to retrieve the key, -ENOENT if it doesn't exist.

del_key
    remove a key given the ``mac_addr`` (``NULL`` for a group key) and
    ``key_index``, return -ENOENT if the key doesn't exist.

set_default_key
    set the default key on an interface

set_default_mgmt_key
    set the default management frame key on an interface

start_ap
    Start acting in AP mode defined by the parameters.

change_beacon
    Change the beacon parameters for an access point mode interface.
    This should reject the call when AP mode wasn't started.

stop_ap
    Stop being an AP, including stopping beaconing.

add_station
    Add a new station.

del_station
    Remove a station

change_station
    Modify a given station. Note that flags changes are not much
    validated in cfg80211, in particular the auth/assoc/authorized flags
    might come to the driver in invalid combinations -- make sure to
    check them, also against the existing state! Drivers must call
    ``cfg80211_check_station_change`` to validate the information.

get_station
    get station information for the station identified by ``mac``

dump_station
    dump station callback -- resume dump at index ``idx``

add_mpath
    add a fixed mesh path

del_mpath
    delete a given mesh path

change_mpath
    change a given mesh path

get_mpath
    get a mesh path for the given parameters

dump_mpath
    dump mesh path callback -- resume dump at index ``idx``

get_mpp
    get a mesh proxy path for the given parameters

dump_mpp
    dump mesh proxy path callback -- resume dump at index ``idx``

get_mesh_config
    Get the current mesh configuration

update_mesh_config
    Update mesh parameters on a running mesh. The mask is a bitfield
    which tells us which parameters to set, and which to leave alone.

join_mesh
    join the mesh network with the specified parameters (invoked with
    the wireless_dev mutex held)

leave_mesh
    leave the current mesh network (invoked with the wireless_dev mutex
    held)

join_ocb
    join the OCB network with the specified parameters (invoked with the
    wireless_dev mutex held)

leave_ocb
    leave the current OCB network (invoked with the wireless_dev mutex
    held)

change_bss
    Modify parameters for a given BSS.

set_txq_params
    Set TX queue parameters

libertas_set_mesh_channel
    Only for backward compatibility for libertas, as it doesn't
    implement join_mesh and needs to set the channel to join the mesh
    instead.

set_monitor_channel
    Set the monitor mode channel for the device. If other interfaces are
    active this callback should reject the configuration. If no
    interfaces are active or the device is down, the channel should be
    stored for when a monitor interface becomes active.

scan
    Request to do a scan. If returning zero, the scan request is given
    the driver, and will be valid until passed to
    ``cfg80211_scan_done``. For scan results, call
    ``cfg80211_inform_bss``; you can call this outside the
    scan/scan_done bracket too.

abort_scan
    Tell the driver to abort an ongoing scan. The driver shall indicate
    the status of the scan through ``cfg80211_scan_done``.

auth
    Request to authenticate with the specified peer (invoked with the
    wireless_dev mutex held)

assoc
    Request to (re)associate with the specified peer (invoked with the
    wireless_dev mutex held)

deauth
    Request to deauthenticate from the specified peer (invoked with the
    wireless_dev mutex held)

disassoc
    Request to disassociate from the specified peer (invoked with the
    wireless_dev mutex held)

connect
    Connect to the ESS with the specified parameters. When connected,
    call ``cfg80211_connect_result`` with status code
    ``WLAN_STATUS_SUCCESS``. If the connection fails for some reason,
    call ``cfg80211_connect_result`` with the status from the AP.
    (invoked with the wireless_dev mutex held)

disconnect
    Disconnect from the BSS/ESS. (invoked with the wireless_dev mutex
    held)

join_ibss
    Join the specified IBSS (or create if necessary). Once done, call
    ``cfg80211_ibss_joined``, also call that function when changing
    BSSID due to a merge. (invoked with the wireless_dev mutex held)

leave_ibss
    Leave the IBSS. (invoked with the wireless_dev mutex held)

set_mcast_rate
    Set the specified multicast rate (only if vif is in ADHOC or MESH
    mode)

set_wiphy_params
    Notify that wiphy parameters have changed; ``changed`` bitfield (see
    ``enum`` wiphy_params_flags) describes which values have changed.
    The actual parameter values are available in struct wiphy. If
    returning an error, no value should be changed.

set_tx_power
    set the transmit power according to the parameters, the power passed
    is in mBm, to get dBm use ``MBM_TO_DBM``. The wdev may be ``NULL``
    if power was set for the wiphy, and will always be ``NULL`` unless
    the driver supports per-vif TX power (as advertised by the nl80211
    feature flag.)

get_tx_power
    store the current TX power into the dbm variable; return 0 if
    successful

set_wds_peer
    set the WDS peer for a WDS interface

rfkill_poll
    polls the hw rfkill line, use cfg80211 reporting functions to adjust
    rfkill hw state

testmode_cmd
    run a test mode command; ``wdev`` may be ``NULL``

testmode_dump
    Implement a test mode dump. The cb->args[2] and up may be used by
    the function, but 0 and 1 must not be touched. Additionally, return
    error codes other than -ENOBUFS and -ENOENT will terminate the dump
    and return to userspace with an error, so be careful. If any data
    was passed in from userspace then the data/len arguments will be
    present and point to the data contained in
    ``NL80211_ATTR_TESTDATA``.

set_bitrate_mask
    set the bitrate mask configuration

dump_survey
    get site survey information.

set_pmksa
    Cache a PMKID for a BSSID. This is mostly useful for fullmac devices
    running firmwares capable of generating the (re) association RSN IE.
    It allows for faster roaming between WPA2 BSSIDs.

del_pmksa
    Delete a cached PMKID.

flush_pmksa
    Flush all cached PMKIDs.

remain_on_channel
    Request the driver to remain awake on the specified channel for the
    specified duration to complete an off-channel operation (e.g.,
    public action frame exchange). When the driver is ready on the
    requested channel, it must indicate this with an event notification
    by calling ``cfg80211_ready_on_channel``.

cancel_remain_on_channel
    Cancel an on-going remain-on-channel operation. This allows the
    operation to be terminated prior to timeout based on the duration
    value.

mgmt_tx
    Transmit a management frame.

mgmt_tx_cancel_wait
    Cancel the wait time from transmitting a management frame on another
    channel

set_power_mgmt
    Configure WLAN power management. A timeout value of -1 allows the
    driver to adjust the dynamic ps timeout value.

set_cqm_rssi_config
    Configure connection quality monitor RSSI threshold. After
    configuration, the driver should (soon) send an event indicating the
    current level is above/below the configured threshold; this may need
    some care when the configuration is changed (without first being
    disabled.)

set_cqm_txe_config
    Configure connection quality monitor TX error thresholds.

mgmt_frame_register
    Notify driver that a management frame type was registered. The
    callback is allowed to sleep.

set_antenna
    Set antenna configuration (tx_ant, rx_ant) on the device.
    Parameters are bitmaps of allowed antennas to use for TX/RX. Drivers
    may reject TX/RX mask combinations they cannot support by returning
    -EINVAL (also see nl80211.h ``NL80211_ATTR_WIPHY_ANTENNA_TX``).

get_antenna
    Get current antenna configuration from device (tx_ant, rx_ant).

sched_scan_start
    Tell the driver to start a scheduled scan.

sched_scan_stop
    Tell the driver to stop an ongoing scheduled scan. This call must
    stop the scheduled scan and be ready for starting a new one before
    it returns, i.e. ``sched_scan_start`` may be called immediately
    after that again and should not fail in that case. The driver should
    not call ``cfg80211_sched_scan_stopped`` for a requested stop (when
    this method returns 0.)

set_rekey_data
    give the data necessary for GTK rekeying to the driver

tdls_mgmt
    Transmit a TDLS management frame.

tdls_oper
    Perform a high-level TDLS operation (e.g. TDLS link setup).

probe_client
    probe an associated client, must return a cookie that it later
    passes to ``cfg80211_probe_status``.

set_noack_map
    Set the NoAck Map for the TIDs.

get_channel
    Get the current operating channel for the virtual interface. For
    monitor interfaces, it should return ``NULL`` unless there's a
    single current monitoring channel.

start_p2p_device
    Start the given P2P device.

stop_p2p_device
    Stop the given P2P device.

set_mac_acl
    Sets MAC address control list in AP and P2P GO mode. Parameters
    include ACL policy, an array of MAC address of stations and the
    number of MAC addresses. If there is already a list in driver this
    new list replaces the existing one. Driver has to clear its ACL when
    number of MAC addresses entries is passed as 0. Drivers which
    advertise the support for MAC based ACL have to implement this
    callback.

start_radar_detection
    Start radar detection in the driver.

update_ft_ies
    Provide updated Fast BSS Transition information to the driver. If
    the SME is in the driver/firmware, this information can be used in
    building Authentication and Reassociation Request frames.

crit_proto_start
    Indicates a critical protocol needs more link reliability for a
    given duration (milliseconds). The protocol is provided so the
    driver can take the most appropriate actions.

crit_proto_stop
    Indicates critical protocol no longer needs increased link
    reliability. This operation can not fail.

set_coalesce
    Set coalesce parameters.

channel_switch
    initiate channel-switch procedure (with CSA). Driver is responsible
    for veryfing if the switch is possible. Since this is inherently
    tricky driver may decide to disconnect an interface later with
    ``cfg80211_stop_iface``. This doesn't mean driver can accept
    everything. It should do it's best to verify requests and reject
    them as soon as possible.

set_qos_map
    Set QoS mapping information to the driver

set_ap_chanwidth
    Set the AP (including P2P GO) mode channel width for the given
    interface This is used e.g. for dynamic HT 20/40 MHz channel width
    changes during the lifetime of the BSS.

add_tx_ts
    validate (if admitted_time is 0) or add a TX TS to the device with
    the given parameters; action frame exchange has been handled by
    userspace so this just has to modify the TX path to take the TS into
    account. If the admitted time is 0 just validate the parameters to
    make sure the session can be created at all; it is valid to just
    always return success for that but that may result in inefficient
    behaviour (handshake with the peer followed by immediate teardown
    when the addition is later rejected)

del_tx_ts
    remove an existing TX TS

tdls_channel_switch
    Start channel-switching with a TDLS peer. The driver is responsible
    for continually initiating channel-switching operations and
    returning to the base channel for communication with the AP.

tdls_cancel_channel_switch
    Stop channel-switching with a TDLS peer. Both peers must be on the
    base channel when the call completes.


Description
===========

This struct is registered by fullmac card drivers and/or wireless stacks
in order to handle configuration requests on their interfaces.

All callbacks except where otherwise noted should return 0 on success or
a negative error code.

All operations are currently invoked under rtnl for consistency with the
wireless extensions but this is subject to reevaluation as soon as this
code is used more widely and we have a first user without wext.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
