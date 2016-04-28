.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ieee80211-ops:

====================
struct ieee80211_ops
====================

*man struct ieee80211_ops(9)*

*4.6.0-rc5*

callbacks from mac80211 to the driver


Synopsis
========

.. code-block:: c

    struct ieee80211_ops {
      void (* tx) (struct ieee80211_hw *hw,struct ieee80211_tx_control *control,struct sk_buff *skb);
      int (* start) (struct ieee80211_hw *hw);
      void (* stop) (struct ieee80211_hw *hw);
    #ifdef CONFIG_PM
      int (* suspend) (struct ieee80211_hw *hw, struct cfg80211_wowlan *wowlan);
      int (* resume) (struct ieee80211_hw *hw);
      void (* set_wakeup) (struct ieee80211_hw *hw, bool enabled);
    #endif
      int (* add_interface) (struct ieee80211_hw *hw,struct ieee80211_vif *vif);
      int (* change_interface) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,enum nl80211_iftype new_type, bool p2p);
      void (* remove_interface) (struct ieee80211_hw *hw,struct ieee80211_vif *vif);
      int (* config) (struct ieee80211_hw *hw, u32 changed);
      void (* bss_info_changed) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_bss_conf *info,u32 changed);
      int (* start_ap) (struct ieee80211_hw *hw, struct ieee80211_vif *vif);
      void (* stop_ap) (struct ieee80211_hw *hw, struct ieee80211_vif *vif);
      u64 (* prepare_multicast) (struct ieee80211_hw *hw,struct netdev_hw_addr_list *mc_list);
      void (* configure_filter) (struct ieee80211_hw *hw,unsigned int changed_flags,unsigned int *total_flags,u64 multicast);
      void (* config_iface_filter) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,unsigned int filter_flags,unsigned int changed_flags);
      int (* set_tim) (struct ieee80211_hw *hw, struct ieee80211_sta *sta,bool set);
      int (* set_key) (struct ieee80211_hw *hw, enum set_key_cmd cmd,struct ieee80211_vif *vif, struct ieee80211_sta *sta,struct ieee80211_key_conf *key);
      void (* update_tkip_key) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_key_conf *conf,struct ieee80211_sta *sta,u32 iv32, u16 *phase1key);
      void (* set_rekey_data) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct cfg80211_gtk_rekey_data *data);
      void (* set_default_unicast_key) (struct ieee80211_hw *hw,struct ieee80211_vif *vif, int idx);
      int (* hw_scan) (struct ieee80211_hw *hw, struct ieee80211_vif *vif,struct ieee80211_scan_request *req);
      void (* cancel_hw_scan) (struct ieee80211_hw *hw,struct ieee80211_vif *vif);
      int (* sched_scan_start) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct cfg80211_sched_scan_request *req,struct ieee80211_scan_ies *ies);
      int (* sched_scan_stop) (struct ieee80211_hw *hw,struct ieee80211_vif *vif);
      void (* sw_scan_start) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,const u8 *mac_addr);
      void (* sw_scan_complete) (struct ieee80211_hw *hw,struct ieee80211_vif *vif);
      int (* get_stats) (struct ieee80211_hw *hw,struct ieee80211_low_level_stats *stats);
      void (* get_key_seq) (struct ieee80211_hw *hw,struct ieee80211_key_conf *key,struct ieee80211_key_seq *seq);
      int (* set_frag_threshold) (struct ieee80211_hw *hw, u32 value);
      int (* set_rts_threshold) (struct ieee80211_hw *hw, u32 value);
      int (* sta_add) (struct ieee80211_hw *hw, struct ieee80211_vif *vif,struct ieee80211_sta *sta);
      int (* sta_remove) (struct ieee80211_hw *hw, struct ieee80211_vif *vif,struct ieee80211_sta *sta);
    #ifdef CONFIG_MAC80211_DEBUGFS
      void (* sta_add_debugfs) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_sta *sta,struct dentry *dir);
      void (* sta_remove_debugfs) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_sta *sta,struct dentry *dir);
    #endif
      void (* sta_notify) (struct ieee80211_hw *hw, struct ieee80211_vif *vif,enum sta_notify_cmd, struct ieee80211_sta *sta);
      int (* sta_state) (struct ieee80211_hw *hw, struct ieee80211_vif *vif,struct ieee80211_sta *sta,enum ieee80211_sta_state old_state,enum ieee80211_sta_state new_state);
      void (* sta_pre_rcu_remove) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_sta *sta);
      void (* sta_rc_update) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_sta *sta,u32 changed);
      void (* sta_rate_tbl_update) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_sta *sta);
      void (* sta_statistics) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_sta *sta,struct station_info *sinfo);
      int (* conf_tx) (struct ieee80211_hw *hw,struct ieee80211_vif *vif, u16 ac,const struct ieee80211_tx_queue_params *params);
      u64 (* get_tsf) (struct ieee80211_hw *hw, struct ieee80211_vif *vif);
      void (* set_tsf) (struct ieee80211_hw *hw, struct ieee80211_vif *vif,u64 tsf);
      void (* reset_tsf) (struct ieee80211_hw *hw, struct ieee80211_vif *vif);
      int (* tx_last_beacon) (struct ieee80211_hw *hw);
      int (* ampdu_action) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_ampdu_params *params);
      int (* get_survey) (struct ieee80211_hw *hw, int idx,struct survey_info *survey);
      void (* rfkill_poll) (struct ieee80211_hw *hw);
      void (* set_coverage_class) (struct ieee80211_hw *hw, s16 coverage_class);
    #ifdef CONFIG_NL80211_TESTMODE
      int (* testmode_cmd) (struct ieee80211_hw *hw, struct ieee80211_vif *vif,void *data, int len);
      int (* testmode_dump) (struct ieee80211_hw *hw, struct sk_buff *skb,struct netlink_callback *cb,void *data, int len);
    #endif
      void (* flush) (struct ieee80211_hw *hw, struct ieee80211_vif *vif,u32 queues, bool drop);
      void (* channel_switch) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_channel_switch *ch_switch);
      int (* set_antenna) (struct ieee80211_hw *hw, u32 tx_ant, u32 rx_ant);
      int (* get_antenna) (struct ieee80211_hw *hw, u32 *tx_ant, u32 *rx_ant);
      int (* remain_on_channel) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_channel *chan,int duration,enum ieee80211_roc_type type);
      int (* cancel_remain_on_channel) (struct ieee80211_hw *hw);
      int (* set_ringparam) (struct ieee80211_hw *hw, u32 tx, u32 rx);
      void (* get_ringparam) (struct ieee80211_hw *hw,u32 *tx, u32 *tx_max, u32 *rx, u32 *rx_max);
      bool (* tx_frames_pending) (struct ieee80211_hw *hw);
      int (* set_bitrate_mask) (struct ieee80211_hw *hw, struct ieee80211_vif *vif,const struct cfg80211_bitrate_mask *mask);
      void (* event_callback) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,const struct ieee80211_event *event);
      void (* allow_buffered_frames) (struct ieee80211_hw *hw,struct ieee80211_sta *sta,u16 tids, int num_frames,enum ieee80211_frame_release_type reason,bool more_data);
      void (* release_buffered_frames) (struct ieee80211_hw *hw,struct ieee80211_sta *sta,u16 tids, int num_frames,enum ieee80211_frame_release_type reason,bool more_data);
      int (* get_et_sset_count) (struct ieee80211_hw *hw,struct ieee80211_vif *vif, int sset);
      void (* get_et_stats) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ethtool_stats *stats, u64 *data);
      void (* get_et_strings) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,u32 sset, u8 *data);
      void (* mgd_prepare_tx) (struct ieee80211_hw *hw,struct ieee80211_vif *vif);
      void (* mgd_protect_tdls_discover) (struct ieee80211_hw *hw,struct ieee80211_vif *vif);
      int (* add_chanctx) (struct ieee80211_hw *hw,struct ieee80211_chanctx_conf *ctx);
      void (* remove_chanctx) (struct ieee80211_hw *hw,struct ieee80211_chanctx_conf *ctx);
      void (* change_chanctx) (struct ieee80211_hw *hw,struct ieee80211_chanctx_conf *ctx,u32 changed);
      int (* assign_vif_chanctx) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_chanctx_conf *ctx);
      void (* unassign_vif_chanctx) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_chanctx_conf *ctx);
      int (* switch_vif_chanctx) (struct ieee80211_hw *hw,struct ieee80211_vif_chanctx_switch *vifs,int n_vifs,enum ieee80211_chanctx_switch_mode mode);
      void (* reconfig_complete) (struct ieee80211_hw *hw,enum ieee80211_reconfig_type reconfig_type);
    #if IS_ENABLED(CONFIG_IPV6)
      void (* ipv6_addr_change) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct inet6_dev *idev);
    #endif
      void (* channel_switch_beacon) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct cfg80211_chan_def *chandef);
      int (* pre_channel_switch) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_channel_switch *ch_switch);
      int (* post_channel_switch) (struct ieee80211_hw *hw,struct ieee80211_vif *vif);
      int (* join_ibss) (struct ieee80211_hw *hw, struct ieee80211_vif *vif);
      void (* leave_ibss) (struct ieee80211_hw *hw, struct ieee80211_vif *vif);
      u32 (* get_expected_throughput) (struct ieee80211_sta *sta);
      int (* get_txpower) (struct ieee80211_hw *hw, struct ieee80211_vif *vif,int *dbm);
      int (* tdls_channel_switch) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_sta *sta, u8 oper_class,struct cfg80211_chan_def *chandef,struct sk_buff *tmpl_skb, u32 ch_sw_tm_ie);
      void (* tdls_cancel_channel_switch) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_sta *sta);
      void (* tdls_recv_channel_switch) (struct ieee80211_hw *hw,struct ieee80211_vif *vif,struct ieee80211_tdls_ch_sw_params *params);
      void (* wake_tx_queue) (struct ieee80211_hw *hw,struct ieee80211_txq *txq);
    };


Members
=======

tx
    Handler that 802.11 module calls for each transmitted frame. skb
    contains the buffer starting from the IEEE 802.11 header. The
    low-level driver should send the frame out based on configuration in
    the TX control data. This handler should, preferably, never fail and
    stop queues appropriately. Must be atomic.

start
    Called before the first netdevice attached to the hardware is
    enabled. This should turn on the hardware and must turn on frame
    reception (for possibly enabled monitor interfaces.) Returns
    negative error codes, these may be seen in userspace, or zero. When
    the device is started it should not have a MAC address to avoid
    acknowledging frames before a non-monitor device is added. Must be
    implemented and can sleep.

stop
    Called after last netdevice attached to the hardware is disabled.
    This should turn off the hardware (at least it must turn off frame
    reception.) May be called right after add_interface if that rejects
    an interface. If you added any work onto the mac80211 workqueue you
    should ensure to cancel it on this callback. Must be implemented and
    can sleep.

suspend
    Suspend the device; mac80211 itself will quiesce before and stop
    transmitting and doing any other configuration, and then ask the
    device to suspend. This is only invoked when WoWLAN is configured,
    otherwise the device is deconfigured completely and reconfigured at
    resume time. The driver may also impose special conditions under
    which it wants to use the “normal” suspend (deconfigure), say if it
    only supports WoWLAN when the device is associated. In this case, it
    must return 1 from this function.

resume
    If WoWLAN was configured, this indicates that mac80211 is now
    resuming its operation, after this the device must be fully
    functional again. If this returns an error, the only way out is to
    also unregister the device. If it returns 1, then mac80211 will also
    go through the regular complete restart on resume.

set_wakeup
    Enable or disable wakeup when WoWLAN configuration is modified. The
    reason is that ``device_set_wakeup_enable`` is supposed to be called
    when the configuration changes, not only in ``suspend``.

add_interface
    Called when a netdevice attached to the hardware is enabled. Because
    it is not called for monitor mode devices, ``start`` and ``stop``
    must be implemented. The driver should perform any initialization it
    needs before the device can be enabled. The initial configuration
    for the interface is given in the conf parameter. The callback may
    refuse to add an interface by returning a negative error code (which
    will be seen in userspace.) Must be implemented and can sleep.

change_interface
    Called when a netdevice changes type. This callback is optional, but
    only if it is supported can interface types be switched while the
    interface is UP. The callback may sleep. Note that while an
    interface is being switched, it will not be found by the interface
    iteration callbacks.

remove_interface
    Notifies a driver that an interface is going down. The ``stop``
    callback is called after this if it is the last interface and no
    monitor interfaces are present. When all interfaces are removed, the
    MAC address in the hardware must be cleared so the device no longer
    acknowledges packets, the mac_addr member of the conf structure is,
    however, set to the MAC address of the device going away. Hence,
    this callback must be implemented. It can sleep.

config
    Handler for configuration requests. IEEE 802.11 code calls this
    function to change hardware configuration, e.g., channel. This
    function should never fail but returns a negative error code if it
    does. The callback can sleep.

bss_info_changed
    Handler for configuration requests related to BSS parameters that
    may vary during BSS's lifespan, and may affect low level driver
    (e.g. assoc/disassoc status, erp parameters). This function should
    not be used if no BSS has been set, unless for association
    indication. The ``changed`` parameter indicates which of the bss
    parameters has changed when a call is made. The callback can sleep.

start_ap
    Start operation on the AP interface, this is called after all the
    information in bss_conf is set and beacon can be retrieved. A
    channel context is bound before this is called. Note that if the
    driver uses software scan or ROC, this (and ``stop_ap``) isn't
    called when the AP is just “paused” for scanning/ROC, which is
    indicated by the beacon being disabled/enabled via
    ``bss_info_changed``.

stop_ap
    Stop operation on the AP interface.

prepare_multicast
    Prepare for multicast filter configuration. This callback is
    optional, and its return value is passed to ``configure_filter``.
    This callback must be atomic.

configure_filter
    Configure the device's RX filter. See the section “Frame filtering”
    for more information. This callback must be implemented and can
    sleep.

config_iface_filter
    Configure the interface's RX filter. This callback is optional and
    is used to configure which frames should be passed to mac80211. The
    filter_flags is the combination of FIF_* flags. The changed_flags
    is a bit mask that indicates which flags are changed. This callback
    can sleep.

set_tim
    Set TIM bit. mac80211 calls this function when a TIM bit must be set
    or cleared for a given STA. Must be atomic.

set_key
    See the section “Hardware crypto acceleration” This callback is only
    called between add_interface and remove_interface calls, i.e.
    while the given virtual interface is enabled. Returns a negative
    error code if the key can't be added. The callback can sleep.

update_tkip_key
    See the section “Hardware crypto acceleration” This callback will be
    called in the context of Rx. Called for drivers which set
    IEEE80211_KEY_FLAG_TKIP_REQ_RX_P1_KEY. The callback must be
    atomic.

set_rekey_data
    If the device supports GTK rekeying, for example while the host is
    suspended, it can assign this callback to retrieve the data
    necessary to do GTK rekeying, this is the KEK, KCK and replay
    counter. After rekeying was done it should (for example during
    resume) notify userspace of the new replay counter using
    ``ieee80211_gtk_rekey_notify``.

set_default_unicast_key
    Set the default (unicast) key index, useful for WEP when the device
    sends data packets autonomously, e.g. for ARP offloading. The index
    can be 0-3, or -1 for unsetting it.

hw_scan
    Ask the hardware to service the scan request, no need to start the
    scan state machine in stack. The scan must honour the channel
    configuration done by the regulatory agent in the wiphy's registered
    bands. The hardware (or the driver) needs to make sure that power
    save is disabled. The ``req`` ie/ie_len members are rewritten by
    mac80211 to contain the entire IEs after the SSID, so that drivers
    need not look at these at all but just send them after the SSID --
    mac80211 includes the (extended) supported rates and HT information
    (where applicable). When the scan finishes,
    ``ieee80211_scan_completed`` must be called; note that it also must
    be called when the scan cannot finish due to any error unless this
    callback returned a negative error code. The callback can sleep.

cancel_hw_scan
    Ask the low-level tp cancel the active hw scan. The driver should
    ask the hardware to cancel the scan (if possible), but the scan will
    be completed only after the driver will call
    ``ieee80211_scan_completed``. This callback is needed for wowlan, to
    prevent enqueueing a new scan_work after the low-level driver was
    already suspended. The callback can sleep.

sched_scan_start
    Ask the hardware to start scanning repeatedly at specific intervals.
    The driver must call the ``ieee80211_sched_scan_results`` function
    whenever it finds results. This process will continue until
    sched_scan_stop is called.

sched_scan_stop
    Tell the hardware to stop an ongoing scheduled scan. In this case,
    ``ieee80211_sched_scan_stopped`` must not be called.

sw_scan_start
    Notifier function that is called just before a software scan is
    started. Can be NULL, if the driver doesn't need this notification.
    The mac_addr parameter allows supporting
    NL80211_SCAN_FLAG_RANDOM_ADDR, the driver may set the
    NL80211_FEATURE_SCAN_RANDOM_MAC_ADDR flag if it can use this
    parameter. The callback can sleep.

sw_scan_complete
    Notifier function that is called just after a software scan
    finished. Can be NULL, if the driver doesn't need this notification.
    The callback can sleep.

get_stats
    Return low-level statistics. Returns zero if statistics are
    available. The callback can sleep.

get_key_seq
    If your device implements encryption in hardware and does IV/PN
    assignment then this callback should be provided to read the IV/PN
    for the given key from hardware. The callback must be atomic.

set_frag_threshold
    Configuration of fragmentation threshold. Assign this if the device
    does fragmentation by itself; if this callback is implemented then
    the stack will not do fragmentation. The callback can sleep.

set_rts_threshold
    Configuration of RTS threshold (if device needs it) The callback can
    sleep.

sta_add
    Notifies low level driver about addition of an associated station,
    AP, IBSS/WDS/mesh peer etc. This callback can sleep.

sta_remove
    Notifies low level driver about removal of an associated station,
    AP, IBSS/WDS/mesh peer etc. Note that after the callback returns it
    isn't safe to use the pointer, not even RCU protected; no RCU grace
    period is guaranteed between returning here and freeing the station.
    See ``sta_pre_rcu_remove`` if needed. This callback can sleep.

sta_add_debugfs
    Drivers can use this callback to add debugfs files when a station is
    added to mac80211's station list. This callback and
    ``sta_remove_debugfs`` should be within a CONFIG_MAC80211_DEBUGFS
    conditional. This callback can sleep.

sta_remove_debugfs
    Remove the debugfs files which were added using ``sta_add_debugfs``.
    This callback can sleep.

sta_notify
    Notifies low level driver about power state transition of an
    associated station, AP, IBSS/WDS/mesh peer etc. For a VIF operating
    in AP mode, this callback will not be called when the flag
    ``IEEE80211_HW_AP_LINK_PS`` is set. Must be atomic.

sta_state
    Notifies low level driver about state transition of a station (which
    can be the AP, a client, IBSS/WDS/mesh peer etc.) This callback is
    mutually exclusive with ``sta_add``/``sta_remove``. It must not fail
    for down transitions but may fail for transitions up the list of
    states. Also note that after the callback returns it isn't safe to
    use the pointer, not even RCU protected - no RCU grace period is
    guaranteed between returning here and freeing the station. See
    ``sta_pre_rcu_remove`` if needed. The callback can sleep.

sta_pre_rcu_remove
    Notify driver about station removal before RCU synchronisation. This
    is useful if a driver needs to have station pointers protected using
    RCU, it can then use this call to clear the pointers instead of
    waiting for an RCU grace period to elapse in ``sta_state``. The
    callback can sleep.

sta_rc_update
    Notifies the driver of changes to the bitrates that can be used to
    transmit to the station. The changes are advertised with bits from
    ``enum`` ieee80211_rate_control_changed and the values are
    reflected in the station data. This callback should only be used
    when the driver uses hardware rate control
    (``IEEE80211_HW_HAS_RATE_CONTROL``) since otherwise the rate control
    algorithm is notified directly. Must be atomic.

sta_rate_tbl_update
    Notifies the driver that the rate table changed. This is only used
    if the configured rate control algorithm actually uses the new rate
    table API, and is therefore optional. Must be atomic.

sta_statistics
    Get statistics for this station. For example with beacon filtering,
    the statistics kept by mac80211 might not be accurate, so let the
    driver pre-fill the statistics. The driver can fill most of the
    values (indicating which by setting the filled bitmap), but not all
    of them make sense - see the source for which ones are possible.
    Statistics that the driver doesn't fill will be filled by mac80211.
    The callback can sleep.

conf_tx
    Configure TX queue parameters (EDCF (aifs, cw_min, cw_max),
    bursting) for a hardware TX queue. Returns a negative error code on
    failure. The callback can sleep.

get_tsf
    Get the current TSF timer value from firmware/hardware. Currently,
    this is only used for IBSS mode BSSID merging and debugging. Is not
    a required function. The callback can sleep.

set_tsf
    Set the TSF timer to the specified value in the firmware/hardware.
    Currently, this is only used for IBSS mode debugging. Is not a
    required function. The callback can sleep.

reset_tsf
    Reset the TSF timer and allow firmware/hardware to synchronize with
    other STAs in the IBSS. This is only used in IBSS mode. This
    function is optional if the firmware/hardware takes full care of TSF
    synchronization. The callback can sleep.

tx_last_beacon
    Determine whether the last IBSS beacon was sent by us. This is
    needed only for IBSS mode and the result of this function is used to
    determine whether to reply to Probe Requests. Returns non-zero if
    this device sent the last beacon. The callback can sleep.

ampdu_action
    Perform a certain A-MPDU action The RA/TID combination determines
    the destination and TID we want the ampdu action to be performed
    for. The action is defined through ieee80211_ampdu_mlme_action.
    When the action is set to ``IEEE80211_AMPDU_TX_OPERATIONAL`` the
    driver may neither send aggregates containing more subframes than
    ``buf_size`` nor send aggregates in a way that lost frames would
    exceed the buffer size. If just limiting the aggregate size, this
    would be

get_survey
    Return per-channel survey information

rfkill_poll
    Poll rfkill hardware state. If you need this, you also need to set
    wiphy->rfkill_poll to ``true`` before registration, and need to
    call ``wiphy_rfkill_set_hw_state`` in the callback. The callback can
    sleep.

set_coverage_class
    Set slot time for given coverage class as specified in IEEE
    802.11-2007 section 17.3.8.6 and modify ACK timeout accordingly;
    coverage class equals to -1 to enable ACK timeout estimation
    algorithm (dynack). To disable dynack set valid value for coverage
    class. This callback is not required and may sleep.

testmode_cmd
    Implement a cfg80211 test mode command. The passed ``vif`` may be
    ``NULL``. The callback can sleep.

testmode_dump
    Implement a cfg80211 test mode dump. The callback can sleep.

flush
    Flush all pending frames from the hardware queue, making sure that
    the hardware queues are empty. The ``queues`` parameter is a bitmap
    of queues to flush, which is useful if different virtual interfaces
    use different hardware queues; it may also indicate all queues. If
    the parameter ``drop`` is set to ``true``, pending frames may be
    dropped. Note that vif can be NULL. The callback can sleep.

channel_switch
    Drivers that need (or want) to offload the channel switch operation
    for CSAs received from the AP may implement this callback. They must
    then call ``ieee80211_chswitch_done`` to indicate completion of the
    channel switch.

set_antenna
    Set antenna configuration (tx_ant, rx_ant) on the device.
    Parameters are bitmaps of allowed antennas to use for TX/RX. Drivers
    may reject TX/RX mask combinations they cannot support by returning
    -EINVAL (also see nl80211.h ``NL80211_ATTR_WIPHY_ANTENNA_TX``).

get_antenna
    Get current antenna configuration from device (tx_ant, rx_ant).

remain_on_channel
    Starts an off-channel period on the given channel, must call back to
    ``ieee80211_ready_on_channel`` when on that channel. Note that
    normal channel traffic is not stopped as this is intended for hw
    offload. Frames to transmit on the off-channel channel are
    transmitted normally except for the ``IEEE80211_TX_CTL_TX_OFFCHAN``
    flag. When the duration (which will always be non-zero) expires, the
    driver must call ``ieee80211_remain_on_channel_expired``. Note that
    this callback may be called while the device is in IDLE and must be
    accepted in this case. This callback may sleep.

cancel_remain_on_channel
    Requests that an ongoing off-channel period is aborted before it
    expires. This callback may sleep.

set_ringparam
    Set tx and rx ring sizes.

get_ringparam
    Get tx and rx ring current and maximum sizes.

tx_frames_pending
    Check if there is any pending frame in the hardware queues before
    entering power save.

set_bitrate_mask
    Set a mask of rates to be used for rate control selection when
    transmitting a frame. Currently only legacy rates are handled. The
    callback can sleep.

event_callback
    Notify driver about any event in mac80211. See ``enum``
    ieee80211_event_type for the different types. The callback must be
    atomic.

allow_buffered_frames
    Prepare device to allow the given number of frames to go out to the
    given station. The frames will be sent by mac80211 via the usual TX
    path after this call. The TX information for frames released will
    also have the ``IEEE80211_TX_CTL_NO_PS_BUFFER`` flag set and the
    last one will also have ``IEEE80211_TX_STATUS_EOSP`` set. In case
    frames from multiple TIDs are released and the driver might reorder
    them between the TIDs, it must set the ``IEEE80211_TX_STATUS_EOSP``
    flag on the last frame and clear it on all others and also handle
    the EOSP bit in the QoS header correctly. Alternatively, it can also
    call the ``ieee80211_sta_eosp`` function. The ``tids`` parameter is
    a bitmap and tells the driver which TIDs the frames will be on; it
    will at most have two bits set. This callback must be atomic.

release_buffered_frames
    Release buffered frames according to the given parameters. In the
    case where the driver buffers some frames for sleeping stations
    mac80211 will use this callback to tell the driver to release some
    frames, either for PS-poll or uAPSD. Note that if the ``more_data``
    parameter is ``false`` the driver must check if there are more
    frames on the given TIDs, and if there are more than the frames
    being released then it must still set the more-data bit in the
    frame. If the ``more_data`` parameter is ``true``, then of course
    the more-data bit must always be set. The ``tids`` parameter tells
    the driver which TIDs to release frames from, for PS-poll it will
    always have only a single bit set. In the case this is used for a
    PS-poll initiated release, the ``num_frames`` parameter will always
    be 1 so code can be shared. In this case the driver must also set
    ``IEEE80211_TX_STATUS_EOSP`` flag on the TX status (and must report
    TX status) so that the PS-poll period is properly ended. This is
    used to avoid sending multiple responses for a retried PS-poll
    frame. In the case this is used for uAPSD, the ``num_frames``
    parameter may be bigger than one, but the driver may send fewer
    frames (it must send at least one, however). In this case it is also
    responsible for setting the EOSP flag in the QoS header of the
    frames. Also, when the service period ends, the driver must set
    ``IEEE80211_TX_STATUS_EOSP`` on the last frame in the SP.
    Alternatively, it may call the function ``ieee80211_sta_eosp`` to
    inform mac80211 of the end of the SP. This callback must be atomic.

get_et_sset_count
    Ethtool API to get string-set count.

get_et_stats
    Ethtool API to get a set of u64 stats.

get_et_strings
    Ethtool API to get a set of strings to describe stats and perhaps
    other supported types of ethtool data-sets.

mgd_prepare_tx
    Prepare for transmitting a management frame for association before
    associated. In multi-channel scenarios, a virtual interface is bound
    to a channel before it is associated, but as it isn't associated yet
    it need not necessarily be given airtime, in particular since any
    transmission to a P2P GO needs to be synchronized against the GO's
    powersave state. mac80211 will call this function before
    transmitting a management frame prior to having successfully
    associated to allow the driver to give it channel time for the
    transmission, to get a response and to be able to synchronize with
    the GO. The callback will be called before each transmission and
    upon return mac80211 will transmit the frame right away. The
    callback is optional and can (should!) sleep.

mgd_protect_tdls_discover
    Protect a TDLS discovery session. After sending a TDLS
    discovery-request, we expect a reply to arrive on the AP's channel.
    We must stay on the channel (no PSM, scan, etc.), since a TDLS
    setup-response is a direct packet not buffered by the AP. mac80211
    will call this function just before the transmission of a TDLS
    discovery-request. The recommended period of protection is at least
    2 * (DTIM period). The callback is optional and can sleep.

add_chanctx
    Notifies device driver about new channel context creation. This
    callback may sleep.

remove_chanctx
    Notifies device driver about channel context destruction. This
    callback may sleep.

change_chanctx
    Notifies device driver about channel context changes that may happen
    when combining different virtual interfaces on the same channel
    context with different settings This callback may sleep.

assign_vif_chanctx
    Notifies device driver about channel context being bound to vif.
    Possible use is for hw queue remapping. This callback may sleep.

unassign_vif_chanctx
    Notifies device driver about channel context being unbound from vif.
    This callback may sleep.

switch_vif_chanctx
    switch a number of vifs from one chanctx to another, as specified in
    the list of ``ieee80211_vif_chanctx_switch`` passed to the driver,
    according to the mode defined in ``ieee80211_chanctx_switch_mode``.
    This callback may sleep.

reconfig_complete
    Called after a call to ``ieee80211_restart_hw`` and during resume,
    when the reconfiguration has completed. This can help the driver
    implement the reconfiguration step (and indicate mac80211 is ready
    to receive frames). This callback may sleep.

ipv6_addr_change
    IPv6 address assignment on the given interface changed. Currently,
    this is only called for managed or P2P client interfaces. This
    callback is optional; it must not sleep.

channel_switch_beacon
    Starts a channel switch to a new channel. Beacons are modified to
    include CSA or ECSA IEs before calling this function. The
    corresponding count fields in these IEs must be decremented, and
    when they reach 1 the driver must call ``ieee80211_csa_finish``.
    Drivers which use ``ieee80211_beacon_get`` get the csa counter
    decremented by mac80211, but must check if it is 1 using
    ``ieee80211_csa_is_complete`` after the beacon has been transmitted
    and then call ``ieee80211_csa_finish``. If the CSA count starts as
    zero or 1, this function will not be called, since there won't be
    any time to beacon before the switch anyway.

pre_channel_switch
    This is an optional callback that is called before a channel switch
    procedure is started (ie. when a STA gets a CSA or an userspace
    initiated channel-switch), allowing the driver to prepare for the
    channel switch.

post_channel_switch
    This is an optional callback that is called after a channel switch
    procedure is completed, allowing the driver to go back to a normal
    configuration.

join_ibss
    Join an IBSS (on an IBSS interface); this is called after all
    information in bss_conf is set up and the beacon can be retrieved.
    A channel context is bound before this is called.

leave_ibss
    Leave the IBSS again.

get_expected_throughput
    extract the expected throughput towards the specified station. The
    returned value is expressed in Kbps. It returns 0 if the RC
    algorithm does not have proper data to provide.

get_txpower
    get current maximum tx power (in dBm) based on configuration and
    hardware limits.

tdls_channel_switch
    Start channel-switching with a TDLS peer. The driver is responsible
    for continually initiating channel-switching operations and
    returning to the base channel for communication with the AP. The
    driver receives a channel-switch request template and the location
    of the switch-timing IE within the template as part of the
    invocation. The template is valid only within the call, and the
    driver can optionally copy the skb for further re-use.

tdls_cancel_channel_switch
    Stop channel-switching with a TDLS peer. Both peers must be on the
    base channel when the call completes.

tdls_recv_channel_switch
    a TDLS channel-switch related frame (request or response) has been
    received from a remote peer. The driver gets parameters parsed from
    the incoming frame and may use them to continue an ongoing
    channel-switch operation. In addition, a channel-switch response
    template is provided, together with the location of the
    switch-timing IE within the template. The skb can only be used
    within the function call.

wake_tx_queue
    Called when new packets have been added to the queue.


Description
===========

This structure contains various callbacks that the driver may handle or,
in some cases, must handle, for example to configure the hardware to a
new channel or to transmit a frame.


possible with a buf_size of 8
=============================

- TX: 1.....7 - RX: 2....7 (lost frame #1) - TX: 8..1... which is
invalid since #1 was now re-transmitted well past the buffer size of 8.
Correct ways to retransmit #1 would be: - TX: 1 or 18 or 81 Even “189”
would be wrong since 1 could be lost again.

Returns a negative error code on failure. The callback can sleep.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
