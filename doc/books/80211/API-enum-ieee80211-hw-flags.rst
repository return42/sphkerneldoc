
.. _API-enum-ieee80211-hw-flags:

=======================
enum ieee80211_hw_flags
=======================

*man enum ieee80211_hw_flags(9)*

*4.6.0-rc1*

hardware flags


Synopsis
========

.. code-block:: c

    enum ieee80211_hw_flags {
      IEEE80211_HW_HAS_RATE_CONTROL,
      IEEE80211_HW_RX_INCLUDES_FCS,
      IEEE80211_HW_HOST_BROADCAST_PS_BUFFERING,
      IEEE80211_HW_SIGNAL_UNSPEC,
      IEEE80211_HW_SIGNAL_DBM,
      IEEE80211_HW_NEED_DTIM_BEFORE_ASSOC,
      IEEE80211_HW_SPECTRUM_MGMT,
      IEEE80211_HW_AMPDU_AGGREGATION,
      IEEE80211_HW_SUPPORTS_PS,
      IEEE80211_HW_PS_NULLFUNC_STACK,
      IEEE80211_HW_SUPPORTS_DYNAMIC_PS,
      IEEE80211_HW_MFP_CAPABLE,
      IEEE80211_HW_WANT_MONITOR_VIF,
      IEEE80211_HW_NO_AUTO_VIF,
      IEEE80211_HW_SW_CRYPTO_CONTROL,
      IEEE80211_HW_SUPPORT_FAST_XMIT,
      IEEE80211_HW_REPORTS_TX_ACK_STATUS,
      IEEE80211_HW_CONNECTION_MONITOR,
      IEEE80211_HW_QUEUE_CONTROL,
      IEEE80211_HW_SUPPORTS_PER_STA_GTK,
      IEEE80211_HW_AP_LINK_PS,
      IEEE80211_HW_TX_AMPDU_SETUP_IN_HW,
      IEEE80211_HW_SUPPORTS_RC_TABLE,
      IEEE80211_HW_P2P_DEV_ADDR_FOR_INTF,
      IEEE80211_HW_TIMING_BEACON_ONLY,
      IEEE80211_HW_SUPPORTS_HT_CCK_RATES,
      IEEE80211_HW_CHANCTX_STA_CSA,
      IEEE80211_HW_SUPPORTS_CLONED_SKBS,
      IEEE80211_HW_SINGLE_SCAN_ON_ALL_BANDS,
      IEEE80211_HW_TDLS_WIDER_BW,
      IEEE80211_HW_SUPPORTS_AMSDU_IN_AMPDU,
      IEEE80211_HW_BEACON_TX_STATUS,
      IEEE80211_HW_NEEDS_UNIQUE_STA_ADDR,
      IEEE80211_HW_SUPPORTS_REORDERING_BUFFER,
      NUM_IEEE80211_HW_FLAGS
    };


Constants
=========

IEEE80211_HW_HAS_RATE_CONTROL
    The hardware or firmware includes rate control, and cannot be controlled by the stack. As such, no rate control algorithm should be instantiated, and the TX rate reported to
    userspace will be taken from the TX status instead of the rate control algorithm. Note that this requires that the driver implement a number of callbacks so it has the correct
    information, it needs to have the ``set_rts_threshold`` callback and must look at the BSS config ``use_cts_prot`` for G/N protection, ``use_short_slot`` for slot timing in 2.4
    GHz and ``use_short_preamble`` for preambles for CCK frames.

IEEE80211_HW_RX_INCLUDES_FCS
    Indicates that received frames passed to the stack include the FCS at the end.

IEEE80211_HW_HOST_BROADCAST_PS_BUFFERING
    Some wireless LAN chipsets buffer broadcast/multicast frames for power saving stations in the hardware/firmware and others rely on the host system for such buffering. This
    option is used to configure the IEEE 802.11 upper layer to buffer broadcast and multicast frames when there are power saving stations so that the driver can fetch them with
    ``ieee80211_get_buffered_bc``.

IEEE80211_HW_SIGNAL_UNSPEC
    Hardware can provide signal values but we don't know its units. We expect values between 0 and ``max_signal``. If possible please provide dB or dBm instead.

IEEE80211_HW_SIGNAL_DBM
    Hardware gives signal values in dBm, decibel difference from one milliwatt. This is the preferred method since it is standardized between different devices. ``max_signal`` does
    not need to be set.

IEEE80211_HW_NEED_DTIM_BEFORE_ASSOC
    This device needs to get data from beacon before association (i.e. dtim_period).

IEEE80211_HW_SPECTRUM_MGMT
    Hardware supports spectrum management defined in 802.11h Measurement, Channel Switch, Quieting, TPC

IEEE80211_HW_AMPDU_AGGREGATION
    Hardware supports 11n A-MPDU aggregation.

IEEE80211_HW_SUPPORTS_PS
    Hardware has power save support (i.e. can go to sleep).

IEEE80211_HW_PS_NULLFUNC_STACK
    Hardware requires nullfunc frame handling in stack, implies stack support for dynamic PS.

IEEE80211_HW_SUPPORTS_DYNAMIC_PS
    Hardware has support for dynamic PS.

IEEE80211_HW_MFP_CAPABLE
    Hardware supports management frame protection (MFP, IEEE 802.11w).

IEEE80211_HW_WANT_MONITOR_VIF
    The driver would like to be informed of a virtual monitor interface when monitor interfaces are the only active interfaces.

IEEE80211_HW_NO_AUTO_VIF
    The driver would like for no wlanX to be created. It is expected user-space will create vifs as desired (and thus have them named as desired).

IEEE80211_HW_SW_CRYPTO_CONTROL
    The driver wants to control which of the crypto algorithms can be done in software - so don't automatically try to fall back to it if hardware crypto fails, but do so only if
    the driver returns 1. This also forces the driver to advertise its supported cipher suites.

IEEE80211_HW_SUPPORT_FAST_XMIT
    The driver/hardware supports fast-xmit, this currently requires only the ability to calculate the duration for frames.

IEEE80211_HW_REPORTS_TX_ACK_STATUS
    Hardware can provide ack status reports of Tx frames to the stack.

IEEE80211_HW_CONNECTION_MONITOR
    The hardware performs its own connection monitoring, including periodic keep-alives to the AP and probing the AP on beacon loss.

IEEE80211_HW_QUEUE_CONTROL
    The driver wants to control per-interface queue mapping in order to use different queues (not just one per AC) for different virtual interfaces. See the doc section on HW queue
    control for more details.

IEEE80211_HW_SUPPORTS_PER_STA_GTK
    The device's crypto engine supports per-station GTKs as used by IBSS RSN or during fast transition. If the device doesn't support per-station GTKs, but can be asked not to
    decrypt group addressed frames, then IBSS RSN support is still possible but software crypto will be used. Advertise the wiphy flag only in that case.

IEEE80211_HW_AP_LINK_PS
    When operating in AP mode the device autonomously manages the PS status of connected stations. When this flag is set mac80211 will not trigger PS mode for connected stations
    based on the PM bit of incoming frames. Use ``ieee80211_start_ps``/``ieee8021_end_ps`` to manually configure the PS mode of connected stations.

IEEE80211_HW_TX_AMPDU_SETUP_IN_HW
    The device handles TX A-MPDU session setup strictly in HW. mac80211 should not attempt to do this in software.

IEEE80211_HW_SUPPORTS_RC_TABLE
    The driver supports using a rate selection table provided by the rate control algorithm.

IEEE80211_HW_P2P_DEV_ADDR_FOR_INTF
    Use the P2P Device address for any P2P Interface. This will be honoured even if more than one interface is supported.

IEEE80211_HW_TIMING_BEACON_ONLY
    Use sync timing from beacon frames only, to allow getting TBTT of a DTIM beacon.

IEEE80211_HW_SUPPORTS_HT_CCK_RATES
    Hardware supports mixing HT/CCK rates and can cope with CCK rates in an aggregation session (e.g. by not using aggregation for such frames.)

IEEE80211_HW_CHANCTX_STA_CSA
    Support 802.11h based channel-switch (CSA) for a single active channel while using channel contexts. When support is not enabled the default action is to disconnect when
    getting the CSA frame.

IEEE80211_HW_SUPPORTS_CLONED_SKBS
    The driver will never modify the payload or tailroom of TX skbs without copying them first.

IEEE80211_HW_SINGLE_SCAN_ON_ALL_BANDS
    The HW supports scanning on all bands in one command, mac80211 doesn't have to run separate scans per band.

IEEE80211_HW_TDLS_WIDER_BW
    The device/driver supports wider bandwidth than then BSS bandwidth for a TDLS link on the base channel.

IEEE80211_HW_SUPPORTS_AMSDU_IN_AMPDU
    The driver supports receiving A-MSDUs within A-MPDU.

IEEE80211_HW_BEACON_TX_STATUS
    The device/driver provides TX status for sent beacons.

IEEE80211_HW_NEEDS_UNIQUE_STA_ADDR
    Hardware (or driver) requires that each station has a unique address, i.e. each station entry can be identified by just its MAC address; this prevents, for example, the same
    station from connecting to two virtual AP interfaces at the same time.

IEEE80211_HW_SUPPORTS_REORDERING_BUFFER
    Hardware (or driver) manages the reordering buffer internally, guaranteeing mac80211 receives frames in order and does not need to manage its own reorder buffer or BA session
    timeout.

NUM_IEEE80211_HW_FLAGS
    number of hardware flags, used for sizing arrays


Description
===========

These flags are used to indicate hardware capabilities to the stack. Generally, flags here should have their meaning done in a way that the simplest hardware doesn't need setting
any particular flags. There are some exceptions to this rule, however, so you are advised to review these flags carefully.
