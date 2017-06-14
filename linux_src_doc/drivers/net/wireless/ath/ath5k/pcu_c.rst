.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/pcu.c

.. _`protocol-control-unit--pcu--functions`:

Protocol Control Unit (PCU) functions
=====================================

Protocol control unit is responsible to maintain various protocol
properties before a frame is send and after a frame is received to/from
baseband. To be more specific, PCU handles:

- Buffering of RX and TX frames (after QCU/DCUs)

- Encrypting and decrypting (using the built-in engine)

- Generating ACKs, RTS/CTS frames

- Maintaining TSF

- FCS

- Updating beacon data (with TSF etc)

- Generating virtual CCA

- RX/Multicast filtering

- BSSID filtering

- Various statistics

-Different operating modes: AP, STA, IBSS

Note: Most of these functions can be tweaked/bypassed so you can do
them on sw above for debugging or research. For more infos check out PCU
registers on reg.h.

.. _`ack-rates`:

ACK rates
=========

AR5212+ can use higher rates for ack transmission
based on current tx rate instead of the base rate.
It does this to better utilize channel usage.
There is a mapping between G rates (that cover both
CCK and OFDM) and ack rates that we use when setting
rate -> duration table. This mapping is hw-based so
don't change anything.

To enable this functionality we must set
ah->ah_ack_bitrate_high to true else base rate is
used (1Mb for CCK, 6Mb for OFDM).

.. _`ath5k_hw_get_frame_duration`:

ath5k_hw_get_frame_duration
===========================

.. c:function:: int ath5k_hw_get_frame_duration(struct ath5k_hw *ah, enum nl80211_band band, int len, struct ieee80211_rate *rate, bool shortpre)

    Get tx time of a frame

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param enum nl80211_band band:
        *undescribed*

    :param int len:
        Frame's length in bytes

    :param struct ieee80211_rate \*rate:
        The \ ``struct``\  ieee80211_rate

    :param bool shortpre:
        Indicate short preample

.. _`ath5k_hw_get_frame_duration.description`:

Description
-----------

Calculate tx duration of a frame given it's rate and length
It extends ieee80211_generic_frame_duration for non standard
bwmodes.

.. _`ath5k_hw_get_default_slottime`:

ath5k_hw_get_default_slottime
=============================

.. c:function:: unsigned int ath5k_hw_get_default_slottime(struct ath5k_hw *ah)

    Get the default slot time for current mode

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_get_default_sifs`:

ath5k_hw_get_default_sifs
=========================

.. c:function:: unsigned int ath5k_hw_get_default_sifs(struct ath5k_hw *ah)

    Get the default SIFS for current mode

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_update_mib_counters`:

ath5k_hw_update_mib_counters
============================

.. c:function:: void ath5k_hw_update_mib_counters(struct ath5k_hw *ah)

    Update MIB counters (mac layer statistics)

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_update_mib_counters.description`:

Description
-----------

Reads MIB counters from PCU and updates sw statistics. Is called after a
MIB interrupt, because one of these counters might have reached their maximum
and triggered the MIB interrupt, to let us read and clear the counter.

.. _`ath5k_hw_update_mib_counters.note`:

NOTE
----

Is called in interrupt context!

.. _`ath5k_hw_write_rate_duration`:

ath5k_hw_write_rate_duration
============================

.. c:function:: void ath5k_hw_write_rate_duration(struct ath5k_hw *ah)

    Fill rate code to duration table

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_write_rate_duration.description`:

Description
-----------

Write the rate code to duration table upon hw reset. This is a helper for
\ :c:func:`ath5k_hw_pcu_init`\ . It seems all this is doing is setting an ACK timeout on
the hardware, based on current mode, for each rate. The rates which are
capable of short preamble (802.11b rates 2Mbps, 5.5Mbps, and 11Mbps) have
different rate code so we write their value twice (one for long preamble
and one for short).

.. _`ath5k_hw_write_rate_duration.note`:

Note
----

Band doesn't matter here, if we set the values for OFDM it works
on both a and g modes. So all we have to do is set values for all g rates
that include all OFDM and CCK rates.

.. _`ath5k_hw_set_ack_timeout`:

ath5k_hw_set_ack_timeout
========================

.. c:function:: int ath5k_hw_set_ack_timeout(struct ath5k_hw *ah, unsigned int timeout)

    Set ACK timeout on PCU

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param unsigned int timeout:
        Timeout in usec

.. _`ath5k_hw_set_cts_timeout`:

ath5k_hw_set_cts_timeout
========================

.. c:function:: int ath5k_hw_set_cts_timeout(struct ath5k_hw *ah, unsigned int timeout)

    Set CTS timeout on PCU

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param unsigned int timeout:
        Timeout in usec

.. _`ath5k_hw_set_lladdr`:

ath5k_hw_set_lladdr
===================

.. c:function:: int ath5k_hw_set_lladdr(struct ath5k_hw *ah, const u8 *mac)

    Set station id

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param const u8 \*mac:
        The card's mac address (array of octets)

.. _`ath5k_hw_set_lladdr.description`:

Description
-----------

Set station id on hw using the provided mac address

.. _`ath5k_hw_set_bssid`:

ath5k_hw_set_bssid
==================

.. c:function:: void ath5k_hw_set_bssid(struct ath5k_hw *ah)

    Set current BSSID on hw

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_set_bssid.description`:

Description
-----------

Sets the current BSSID and BSSID mask we have from the
common struct into the hardware

.. _`ath5k_hw_set_bssid_mask`:

ath5k_hw_set_bssid_mask
=======================

.. c:function:: void ath5k_hw_set_bssid_mask(struct ath5k_hw *ah, const u8 *mask)

    Filter out bssids we listen

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param const u8 \*mask:
        The BSSID mask to set (array of octets)

.. _`ath5k_hw_set_bssid_mask.description`:

Description
-----------

BSSID masking is a method used by AR5212 and newer hardware to inform PCU
which bits of the interface's MAC address should be looked at when trying
to decide which packets to ACK. In station mode and AP mode with a single
BSS every bit matters since we lock to only one BSS. In AP mode with
multiple BSSes (virtual interfaces) not every bit matters because hw must
accept frames for all BSSes and so we tweak some bits of our mac address
in order to have multiple BSSes.

For more information check out ../hw.c of the common ath module.

.. _`ath5k_hw_set_mcast_filter`:

ath5k_hw_set_mcast_filter
=========================

.. c:function:: void ath5k_hw_set_mcast_filter(struct ath5k_hw *ah, u32 filter0, u32 filter1)

    Set multicast filter

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param u32 filter0:
        Lower 32bits of muticast filter

    :param u32 filter1:
        Higher 16bits of multicast filter

.. _`ath5k_hw_get_rx_filter`:

ath5k_hw_get_rx_filter
======================

.. c:function:: u32 ath5k_hw_get_rx_filter(struct ath5k_hw *ah)

    Get current rx filter

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_get_rx_filter.description`:

Description
-----------

Returns the RX filter by reading rx filter and
phy error filter registers. RX filter is used
to set the allowed frame types that PCU will accept
and pass to the driver. For a list of frame types
check out reg.h.

.. _`ath5k_hw_set_rx_filter`:

ath5k_hw_set_rx_filter
======================

.. c:function:: void ath5k_hw_set_rx_filter(struct ath5k_hw *ah, u32 filter)

    Set rx filter

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param u32 filter:
        RX filter mask (see reg.h)

.. _`ath5k_hw_set_rx_filter.description`:

Description
-----------

Sets RX filter register and also handles PHY error filter
register on 5212 and newer chips so that we have proper PHY
error reporting.

.. _`ath5k_hw_get_tsf64`:

ath5k_hw_get_tsf64
==================

.. c:function:: u64 ath5k_hw_get_tsf64(struct ath5k_hw *ah)

    Get the full 64bit TSF

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_get_tsf64.description`:

Description
-----------

Returns the current TSF

.. _`ath5k_hw_set_tsf64`:

ath5k_hw_set_tsf64
==================

.. c:function:: void ath5k_hw_set_tsf64(struct ath5k_hw *ah, u64 tsf64)

    Set a new 64bit TSF

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param u64 tsf64:
        The new 64bit TSF

.. _`ath5k_hw_set_tsf64.description`:

Description
-----------

Sets the new TSF

.. _`ath5k_hw_reset_tsf`:

ath5k_hw_reset_tsf
==================

.. c:function:: void ath5k_hw_reset_tsf(struct ath5k_hw *ah)

    Force a TSF reset

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_reset_tsf.description`:

Description
-----------

Forces a TSF reset on PCU

.. _`ath5k_hw_init_beacon_timers`:

ath5k_hw_init_beacon_timers
===========================

.. c:function:: void ath5k_hw_init_beacon_timers(struct ath5k_hw *ah, u32 next_beacon, u32 interval)

    Initialize beacon timers

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param u32 next_beacon:
        Next TBTT

    :param u32 interval:
        Current beacon interval

.. _`ath5k_hw_init_beacon_timers.description`:

Description
-----------

This function is used to initialize beacon timers based on current
operation mode and settings.

.. _`ath5k_check_timer_win`:

ath5k_check_timer_win
=====================

.. c:function:: bool ath5k_check_timer_win(int a, int b, int window, int intval)

    Check if timer B is timer A + window

    :param int a:
        timer a (before b)

    :param int b:
        timer b (after a)

    :param int window:
        difference between a and b

    :param int intval:
        timers are increased by this interval

.. _`ath5k_check_timer_win.description`:

Description
-----------

This helper function checks if timer B is timer A + window and covers
cases where timer A or B might have already been updated or wrapped
around (Timers are 16 bit).

Returns true if O.K.

.. _`ath5k_hw_check_beacon_timers`:

ath5k_hw_check_beacon_timers
============================

.. c:function:: bool ath5k_hw_check_beacon_timers(struct ath5k_hw *ah, int intval)

    Check if the beacon timers are correct

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param int intval:
        beacon interval

.. _`ath5k_hw_check_beacon_timers.description`:

Description
-----------

This is a workaround for IBSS mode

The need for this function arises from the fact that we have 4 separate
HW timer registers (TIMER0 - TIMER3), which are closely related to the
next beacon target time (NBTT), and that the HW updates these timers
separately based on the current TSF value. The hardware increments each
timer by the beacon interval, when the local TSF converted to TU is equal
to the value stored in the timer.

The reception of a beacon with the same BSSID can update the local HW TSF
at any time - this is something we can't avoid. If the TSF jumps to a
time which is later than the time stored in a timer, this timer will not
be updated until the TSF in TU wraps around at 16 bit (the size of the
timers) and reaches the time which is stored in the timer.

The problem is that these timers are closely related to TIMER0 (NBTT) and
that they define a time "window". When the TSF jumps between two timers
(e.g. ATIM and NBTT), the one in the past will be left behind (not
updated), while the one in the future will be updated every beacon
interval. This causes the window to get larger, until the TSF wraps
around as described above and the timer which was left behind gets
updated again. But - because the beacon interval is usually not an exact
divisor of the size of the timers (16 bit), an unwanted "window" between
these timers has developed!

This is especially important with the ATIM window, because during
the ATIM window only ATIM frames and no data frames are allowed to be
sent, which creates transmission pauses after each beacon. This symptom
has been described as "ramping ping" because ping times increase linearly
for some time and then drop down again. A wrong window on the DMA beacon
timer has the same effect, so we check for these two conditions.

Returns true if O.K.

.. _`ath5k_hw_set_coverage_class`:

ath5k_hw_set_coverage_class
===========================

.. c:function:: void ath5k_hw_set_coverage_class(struct ath5k_hw *ah, u8 coverage_class)

    Set IEEE 802.11 coverage class

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param u8 coverage_class:
        IEEE 802.11 coverage class number

.. _`ath5k_hw_set_coverage_class.description`:

Description
-----------

Sets IFS intervals and ACK/CTS timeouts for given coverage class.

.. _`ath5k_hw_start_rx_pcu`:

ath5k_hw_start_rx_pcu
=====================

.. c:function:: void ath5k_hw_start_rx_pcu(struct ath5k_hw *ah)

    Start RX engine

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_start_rx_pcu.description`:

Description
-----------

Starts RX engine on PCU so that hw can process RXed frames
(ACK etc).

.. _`ath5k_hw_start_rx_pcu.note`:

NOTE
----

RX DMA should be already enabled using ath5k_hw_start_rx_dma

.. _`ath5k_hw_stop_rx_pcu`:

ath5k_hw_stop_rx_pcu
====================

.. c:function:: void ath5k_hw_stop_rx_pcu(struct ath5k_hw *ah)

    Stop RX engine

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_stop_rx_pcu.description`:

Description
-----------

Stops RX engine on PCU

.. _`ath5k_hw_set_opmode`:

ath5k_hw_set_opmode
===================

.. c:function:: int ath5k_hw_set_opmode(struct ath5k_hw *ah, enum nl80211_iftype op_mode)

    Set PCU operating mode

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param enum nl80211_iftype op_mode:
        One of enum nl80211_iftype

.. _`ath5k_hw_set_opmode.description`:

Description
-----------

Configure PCU for the various operating modes (AP/STA etc)

.. _`ath5k_hw_pcu_init`:

ath5k_hw_pcu_init
=================

.. c:function:: void ath5k_hw_pcu_init(struct ath5k_hw *ah, enum nl80211_iftype op_mode)

    Initialize PCU

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param enum nl80211_iftype op_mode:
        One of enum nl80211_iftype

.. _`ath5k_hw_pcu_init.description`:

Description
-----------

This function is used to initialize PCU by setting current
operation mode and various other settings.

.. This file was automatic generated / don't edit.

