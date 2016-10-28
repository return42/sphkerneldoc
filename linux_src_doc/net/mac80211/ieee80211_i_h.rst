.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/ieee80211_i.h

.. _`ieee80211_bss_corrupt_data_flags`:

enum ieee80211_bss_corrupt_data_flags
=====================================

.. c:type:: enum ieee80211_bss_corrupt_data_flags

    BSS data corruption flags

.. _`ieee80211_bss_corrupt_data_flags.definition`:

Definition
----------

.. code-block:: c

    enum ieee80211_bss_corrupt_data_flags {
        IEEE80211_BSS_CORRUPT_BEACON,
        IEEE80211_BSS_CORRUPT_PROBE_RESP
    };

.. _`ieee80211_bss_corrupt_data_flags.constants`:

Constants
---------

IEEE80211_BSS_CORRUPT_BEACON
    last beacon frame received was corrupted

IEEE80211_BSS_CORRUPT_PROBE_RESP
    last probe response received was corrupted

.. _`ieee80211_bss_corrupt_data_flags.description`:

Description
-----------

These are bss flags that are attached to a bss in the
\ ``corrupt_data``\  field of \ :c:type:`struct ieee80211_bss <ieee80211_bss>`\ .

.. _`ieee80211_bss_valid_data_flags`:

enum ieee80211_bss_valid_data_flags
===================================

.. c:type:: enum ieee80211_bss_valid_data_flags

    BSS valid data flags

.. _`ieee80211_bss_valid_data_flags.definition`:

Definition
----------

.. code-block:: c

    enum ieee80211_bss_valid_data_flags {
        IEEE80211_BSS_VALID_WMM,
        IEEE80211_BSS_VALID_RATES,
        IEEE80211_BSS_VALID_ERP
    };

.. _`ieee80211_bss_valid_data_flags.constants`:

Constants
---------

IEEE80211_BSS_VALID_WMM
    WMM/UAPSD data was gathered from non-corrupt IE

IEEE80211_BSS_VALID_RATES
    Supported rates were gathered from non-corrupt IE

IEEE80211_BSS_VALID_ERP
    ERP flag was gathered from non-corrupt IE

.. _`ieee80211_bss_valid_data_flags.description`:

Description
-----------

These are bss flags that are attached to a bss in the
\ ``valid_data``\  field of \ :c:type:`struct ieee80211_bss <ieee80211_bss>`\ .  They show which parts
of the data structure were received as a result of an un-corrupted
beacon/probe response.

.. _`ieee80211_packet_rx_flags`:

enum ieee80211_packet_rx_flags
==============================

.. c:type:: enum ieee80211_packet_rx_flags

    packet RX flags

.. _`ieee80211_packet_rx_flags.definition`:

Definition
----------

.. code-block:: c

    enum ieee80211_packet_rx_flags {
        IEEE80211_RX_AMSDU,
        IEEE80211_RX_MALFORMED_ACTION_FRM,
        IEEE80211_RX_DEFERRED_RELEASE
    };

.. _`ieee80211_packet_rx_flags.constants`:

Constants
---------

IEEE80211_RX_AMSDU
    a-MSDU packet

IEEE80211_RX_MALFORMED_ACTION_FRM
    action frame is malformed

IEEE80211_RX_DEFERRED_RELEASE
    frame was subjected to receive reordering

.. _`ieee80211_packet_rx_flags.description`:

Description
-----------

These are per-frame flags that are attached to a frame in the
\ ``rx_flags``\  field of \ :c:type:`struct ieee80211_rx_status <ieee80211_rx_status>`\ .

.. _`ieee80211_rx_flags`:

enum ieee80211_rx_flags
=======================

.. c:type:: enum ieee80211_rx_flags

    RX data flags

.. _`ieee80211_rx_flags.definition`:

Definition
----------

.. code-block:: c

    enum ieee80211_rx_flags {
        IEEE80211_RX_CMNTR,
        IEEE80211_RX_BEACON_REPORTED
    };

.. _`ieee80211_rx_flags.constants`:

Constants
---------

IEEE80211_RX_CMNTR
    received on cooked monitor already

IEEE80211_RX_BEACON_REPORTED
    This frame was already reported
    to \ :c:func:`cfg80211_report_obss_beacon`\ .

.. _`ieee80211_rx_flags.description`:

Description
-----------

These flags are used across handling multiple interfaces
for a single frame.

.. _`ieee80211_if_ocb`:

struct ieee80211_if_ocb
=======================

.. c:type:: struct ieee80211_if_ocb

    OCB mode state

.. _`ieee80211_if_ocb.definition`:

Definition
----------

.. code-block:: c

    struct ieee80211_if_ocb {
        struct timer_list housekeeping_timer;
        unsigned long wrkq_flags;
        spinlock_t incomplete_lock;
        struct list_head incomplete_stations;
        bool joined;
    }

.. _`ieee80211_if_ocb.members`:

Members
-------

housekeeping_timer
    timer for periodic invocation of a housekeeping task

wrkq_flags
    OCB deferred task action

incomplete_lock
    delayed STA insertion lock

incomplete_stations
    list of STAs waiting for delayed insertion

joined
    indication if the interface is connected to an OCB network

.. _`ieee80211_sub_if_data_flags`:

enum ieee80211_sub_if_data_flags
================================

.. c:type:: enum ieee80211_sub_if_data_flags

    virtual interface flags

.. _`ieee80211_sub_if_data_flags.definition`:

Definition
----------

.. code-block:: c

    enum ieee80211_sub_if_data_flags {
        IEEE80211_SDATA_ALLMULTI,
        IEEE80211_SDATA_OPERATING_GMODE,
        IEEE80211_SDATA_DONT_BRIDGE_PACKETS,
        IEEE80211_SDATA_DISCONNECT_RESUME,
        IEEE80211_SDATA_IN_DRIVER
    };

.. _`ieee80211_sub_if_data_flags.constants`:

Constants
---------

IEEE80211_SDATA_ALLMULTI
    interface wants all multicast packets

IEEE80211_SDATA_OPERATING_GMODE
    operating in G-only mode

IEEE80211_SDATA_DONT_BRIDGE_PACKETS
    bridge packets between
    associated stations and deliver multicast frames both
    back to wireless media and to the local net stack.

IEEE80211_SDATA_DISCONNECT_RESUME
    Disconnect after resume.

IEEE80211_SDATA_IN_DRIVER
    indicates interface was added to driver

.. _`ieee80211_sdata_state_bits`:

enum ieee80211_sdata_state_bits
===============================

.. c:type:: enum ieee80211_sdata_state_bits

    virtual interface state bits

.. _`ieee80211_sdata_state_bits.definition`:

Definition
----------

.. code-block:: c

    enum ieee80211_sdata_state_bits {
        SDATA_STATE_RUNNING,
        SDATA_STATE_OFFCHANNEL,
        SDATA_STATE_OFFCHANNEL_BEACON_STOPPED
    };

.. _`ieee80211_sdata_state_bits.constants`:

Constants
---------

SDATA_STATE_RUNNING
    virtual interface is up & running; this
    mirrors \ :c:func:`netif_running`\  but is separate for interface type
    change handling while the interface is up

SDATA_STATE_OFFCHANNEL
    This interface is currently in offchannel
    mode, so queues are stopped

SDATA_STATE_OFFCHANNEL_BEACON_STOPPED
    Beaconing was stopped due
    to offchannel, reset when offchannel returns

.. _`ieee80211_chanctx_mode`:

enum ieee80211_chanctx_mode
===========================

.. c:type:: enum ieee80211_chanctx_mode

    channel context configuration mode

.. _`ieee80211_chanctx_mode.definition`:

Definition
----------

.. code-block:: c

    enum ieee80211_chanctx_mode {
        IEEE80211_CHANCTX_SHARED,
        IEEE80211_CHANCTX_EXCLUSIVE
    };

.. _`ieee80211_chanctx_mode.constants`:

Constants
---------

IEEE80211_CHANCTX_SHARED
    channel context may be used by
    multiple interfaces

IEEE80211_CHANCTX_EXCLUSIVE
    channel context can be used
    only by a single interface. This can be used for example for
    non-fixed channel IBSS.

.. _`ieee80211_chanctx_replace_state`:

enum ieee80211_chanctx_replace_state
====================================

.. c:type:: enum ieee80211_chanctx_replace_state

    channel context replacement state

.. _`ieee80211_chanctx_replace_state.definition`:

Definition
----------

.. code-block:: c

    enum ieee80211_chanctx_replace_state {
        IEEE80211_CHANCTX_REPLACE_NONE,
        IEEE80211_CHANCTX_WILL_BE_REPLACED,
        IEEE80211_CHANCTX_REPLACES_OTHER
    };

.. _`ieee80211_chanctx_replace_state.constants`:

Constants
---------

IEEE80211_CHANCTX_REPLACE_NONE
    no replacement is taking place

IEEE80211_CHANCTX_WILL_BE_REPLACED
    this channel context will be replaced
    by a (not yet registered) channel context pointed by \ ``replace_ctx``\ .

IEEE80211_CHANCTX_REPLACES_OTHER
    this (not yet registered) channel context
    replaces an existing channel context pointed to by \ ``replace_ctx``\ .

.. _`ieee80211_chanctx_replace_state.description`:

Description
-----------

This is used for channel context in-place reservations that require channel
context switch/swap.

.. _`mac80211_scan_state`:

enum mac80211_scan_state
========================

.. c:type:: enum mac80211_scan_state

    scan state machine states

.. _`mac80211_scan_state.definition`:

Definition
----------

.. code-block:: c

    enum mac80211_scan_state {
        SCAN_DECISION,
        SCAN_SET_CHANNEL,
        SCAN_SEND_PROBE,
        SCAN_SUSPEND,
        SCAN_RESUME,
        SCAN_ABORT
    };

.. _`mac80211_scan_state.constants`:

Constants
---------

SCAN_DECISION
    Main entry point to the scan state machine, this state
    determines if we should keep on scanning or switch back to the
    operating channel

SCAN_SET_CHANNEL
    Set the next channel to be scanned

SCAN_SEND_PROBE
    Send probe requests and wait for probe responses

SCAN_SUSPEND
    Suspend the scan and go back to operating channel to
    send out data

SCAN_RESUME
    Resume the scan and scan the next channel

SCAN_ABORT
    Abort the scan and go back to operating channel

.. _`ieee80211_parse_ch_switch_ie`:

ieee80211_parse_ch_switch_ie
============================

.. c:function:: int ieee80211_parse_ch_switch_ie(struct ieee80211_sub_if_data *sdata, struct ieee802_11_elems *elems, enum nl80211_band current_band, u32 sta_flags, u8 *bssid, struct ieee80211_csa_ie *csa_ie)

    parses channel switch IEs

    :param struct ieee80211_sub_if_data \*sdata:
        the sdata of the interface which has received the frame

    :param struct ieee802_11_elems \*elems:
        parsed 802.11 elements received with the frame

    :param enum nl80211_band current_band:
        indicates the current band

    :param u32 sta_flags:
        contains information about own capabilities and restrictions
        to decide which channel switch announcements can be accepted. Only the
        following subset of \ :c:type:`enum ieee80211_sta_flags <ieee80211_sta_flags>`\  are evaluated:
        \ ``IEEE80211_STA_DISABLE_HT``\ , \ ``IEEE80211_STA_DISABLE_VHT``\ ,
        \ ``IEEE80211_STA_DISABLE_40MHZ``\ , \ ``IEEE80211_STA_DISABLE_80P80MHZ``\ ,
        \ ``IEEE80211_STA_DISABLE_160MHZ``\ .

    :param u8 \*bssid:
        the currently connected bssid (for reporting)

    :param struct ieee80211_csa_ie \*csa_ie:
        parsed 802.11 csa elements on count, mode, chandef and mesh ttl.

.. _`ieee80211_parse_ch_switch_ie.return`:

Return
------

0 on success, <0 on error and >0 if there is nothing to parse.

.. This file was automatic generated / don't edit.

