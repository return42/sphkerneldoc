
.. _API-struct-ieee80211-hw:

===================
struct ieee80211_hw
===================

*man struct ieee80211_hw(9)*

*4.6.0-rc1*

hardware information and state


Synopsis
========

.. code-block:: c

    struct ieee80211_hw {
      struct ieee80211_conf conf;
      struct wiphy * wiphy;
      const char * rate_control_algorithm;
      void * priv;
      unsigned long flags[BITS_TO_LONGS(NUM_IEEE80211_HW_FLAGS)];
      unsigned int extra_tx_headroom;
      unsigned int extra_beacon_tailroom;
      int vif_data_size;
      int sta_data_size;
      int chanctx_data_size;
      int txq_data_size;
      u16 queues;
      u16 max_listen_interval;
      s8 max_signal;
      u8 max_rates;
      u8 max_report_rates;
      u8 max_rate_tries;
      u8 max_rx_aggregation_subframes;
      u8 max_tx_aggregation_subframes;
      u8 offchannel_tx_hw_queue;
      u8 radiotap_mcs_details;
      u16 radiotap_vht_details;
      netdev_features_t netdev_features;
      u8 uapsd_queues;
      u8 uapsd_max_sp_len;
      u8 n_cipher_schemes;
      const struct ieee80211_cipher_scheme * cipher_schemes;
      int txq_ac_max_pending;
    };


Members
=======

conf
    ``struct ieee80211_conf``, device configuration, don't use.

wiphy
    This points to the ``struct wiphy`` allocated for this 802.11 PHY. You must fill in the ``perm_addr`` and ``dev`` members of this structure using ``SET_IEEE80211_DEV`` and
    ``SET_IEEE80211_PERM_ADDR``. Additionally, all supported bands (with channels, bitrates) are registered here.

rate_control_algorithm
    rate control algorithm for this hardware. If unset (NULL), the default algorithm will be used. Must be set before calling ``ieee80211_register_hw``.

priv
    pointer to private area that was allocated for driver use along with this structure.

flags[BITS_TO_LONGS(NUM_IEEE80211_HW_FLAGS)]
    hardware flags, see ``enum`` ieee80211_hw_flags.

extra_tx_headroom
    headroom to reserve in each transmit skb for use by the driver (e.g. for transmit headers.)

extra_beacon_tailroom
    tailroom to reserve in each beacon tx skb. Can be used by drivers to add extra IEs.

vif_data_size
    size (in bytes) of the drv_priv data area within ``struct ieee80211_vif``.

sta_data_size
    size (in bytes) of the drv_priv data area within ``struct ieee80211_sta``.

chanctx_data_size
    size (in bytes) of the drv_priv data area within ``struct ieee80211_chanctx_conf``.

txq_data_size
    size (in bytes) of the drv_priv data area within ``struct`` ieee80211_txq.

queues
    number of available hardware transmit queues for data packets. WMM/QoS requires at least four, these queues need to have configurable access parameters.

max_listen_interval
    max listen interval in units of beacon interval that HW supports

max_signal
    Maximum value for signal (rssi) in RX information, used only when ``IEEE80211_HW_SIGNAL_UNSPEC`` or ``IEEE80211_HW_SIGNAL_DB``

max_rates
    maximum number of alternate rate retry stages the hw can handle.

max_report_rates
    maximum number of alternate rate retry stages the hw can report back.

max_rate_tries
    maximum number of tries for each stage

max_rx_aggregation_subframes
    maximum buffer size (number of sub-frames) to be used for A-MPDU block ack receiver aggregation. This is only relevant if the device has restrictions on the number of
    subframes, if it relies on mac80211 to do reordering it shouldn't be set.

max_tx_aggregation_subframes
    maximum number of subframes in an aggregate an HT driver will transmit. Though ADDBA will advertise a constant value of 64 as some older APs can crash if the window size is
    smaller (an example is LinkSys WRT120N with FW v1.0.07 build 002 Jun 18 2012).

offchannel_tx_hw_queue
    HW queue ID to use for offchannel TX (if ``IEEE80211_HW_QUEUE_CONTROL`` is set)

radiotap_mcs_details
    lists which MCS information can the HW reports, by default it is set to _MCS, _GI and _BW but doesn't include _FMT. Use ``IEEE80211_RADIOTAP_MCS_HAVE_`` ⋆ values, only
    adding _BW is supported today.

radiotap_vht_details
    lists which VHT MCS information the HW reports, the default is _GI | _BANDWIDTH. Use the ``IEEE80211_RADIOTAP_VHT_KNOWN_`` ⋆ values.

netdev_features
    netdev features to be set in each netdev created from this HW. Note that not all features are usable with mac80211, other features will be rejected during HW registration.

uapsd_queues
    This bitmap is included in (re)association frame to indicate for each access category if it is uAPSD trigger-enabled and delivery- enabled. Use
    IEEE80211_WMM_IE_STA_QOSINFO_AC_⋆ to set this bitmap. Each bit corresponds to different AC. Value '1' in specific bit means that corresponding AC is both trigger- and
    delivery-enabled. '0' means neither enabled.

uapsd_max_sp_len
    maximum number of total buffered frames the WMM AP may deliver to a WMM STA during any Service Period triggered by the WMM STA. Use IEEE80211_WMM_IE_STA_QOSINFO_SP_⋆ for
    correct values.

n_cipher_schemes
    a size of an array of cipher schemes definitions.

cipher_schemes
    a pointer to an array of cipher scheme definitions supported by HW.

txq_ac_max_pending
    maximum number of frames per AC pending in all txq entries for a vif.


Description
===========

This structure contains the configuration and hardware information for an 802.11 PHY.
