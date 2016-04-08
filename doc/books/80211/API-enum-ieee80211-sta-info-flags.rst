
.. _API-enum-ieee80211-sta-info-flags:

=============================
enum ieee80211_sta_info_flags
=============================

*man enum ieee80211_sta_info_flags(9)*

*4.6.0-rc1*

Stations flags


Synopsis
========

.. code-block:: c

    enum ieee80211_sta_info_flags {
      WLAN_STA_AUTH,
      WLAN_STA_ASSOC,
      WLAN_STA_PS_STA,
      WLAN_STA_AUTHORIZED,
      WLAN_STA_SHORT_PREAMBLE,
      WLAN_STA_WDS,
      WLAN_STA_CLEAR_PS_FILT,
      WLAN_STA_MFP,
      WLAN_STA_BLOCK_BA,
      WLAN_STA_PS_DRIVER,
      WLAN_STA_PSPOLL,
      WLAN_STA_TDLS_PEER,
      WLAN_STA_TDLS_PEER_AUTH,
      WLAN_STA_TDLS_INITIATOR,
      WLAN_STA_TDLS_CHAN_SWITCH,
      WLAN_STA_TDLS_OFF_CHANNEL,
      WLAN_STA_TDLS_WIDER_BW,
      WLAN_STA_UAPSD,
      WLAN_STA_SP,
      WLAN_STA_4ADDR_EVENT,
      WLAN_STA_INSERTED,
      WLAN_STA_RATE_CONTROL,
      WLAN_STA_TOFFSET_KNOWN,
      WLAN_STA_MPSP_OWNER,
      WLAN_STA_MPSP_RECIPIENT,
      WLAN_STA_PS_DELIVER
    };


Constants
=========

WLAN_STA_AUTH
    Station is authenticated.

WLAN_STA_ASSOC
    Station is associated.

WLAN_STA_PS_STA
    Station is in power-save mode

WLAN_STA_AUTHORIZED
    Station is authorized to send/receive traffic. This bit is always checked so needs to be enabled for all stations when virtual port control is not in use.

WLAN_STA_SHORT_PREAMBLE
    Station is capable of receiving short-preamble frames.

WLAN_STA_WDS
    Station is one of our WDS peers.

WLAN_STA_CLEAR_PS_FILT
    Clear PS filter in hardware (using the IEEE80211_TX_CTL_CLEAR_PS_FILT control flag) when the next frame to this station is transmitted.

WLAN_STA_MFP
    Management frame protection is used with this STA.

WLAN_STA_BLOCK_BA
    Used to deny ADDBA requests (both TX and RX) during suspend/resume and station removal.

WLAN_STA_PS_DRIVER
    driver requires keeping this station in power-save mode logically to flush frames that might still be in the queues

WLAN_STA_PSPOLL
    Station sent PS-poll while driver was keeping station in power-save mode, reply when the driver unblocks.

WLAN_STA_TDLS_PEER
    Station is a TDLS peer.

WLAN_STA_TDLS_PEER_AUTH
    This TDLS peer is authorized to send direct packets. This means the link is enabled.

WLAN_STA_TDLS_INITIATOR
    We are the initiator of the TDLS link with this station.

WLAN_STA_TDLS_CHAN_SWITCH
    This TDLS peer supports TDLS channel-switching

WLAN_STA_TDLS_OFF_CHANNEL
    The local STA is currently off-channel with this TDLS peer

WLAN_STA_TDLS_WIDER_BW
    This TDLS peer supports working on a wider bw on the BSS base channel.

WLAN_STA_UAPSD
    Station requested unscheduled SP while driver was keeping station in power-save mode, reply when the driver unblocks the station.

WLAN_STA_SP
    Station is in a service period, so don't try to reply to other uAPSD trigger frames or PS-Poll.

WLAN_STA_4ADDR_EVENT
    4-addr event was already sent for this frame.

WLAN_STA_INSERTED
    This station is inserted into the hash table.

WLAN_STA_RATE_CONTROL
    rate control was initialized for this station.

WLAN_STA_TOFFSET_KNOWN
    toffset calculated for this station is valid.

WLAN_STA_MPSP_OWNER
    local STA is owner of a mesh Peer Service Period.

WLAN_STA_MPSP_RECIPIENT
    local STA is recipient of a MPSP.

WLAN_STA_PS_DELIVER
    station woke up, but we're still blocking TX until pending frames are delivered


Description
===========

These flags are used with ``struct sta_info``'s ``flags`` member, but only indirectly with ``set_sta_flag`` and friends.
