.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/phy.c

.. _`phy-related-functions`:

PHY related functions
=====================

Here we handle the low-level functions related to baseband
and analog frontend (RF) parts. This is by far the most complex
part of the hw code so make sure you know what you are doing.

Here is a list of what this is all about:

- Channel setting/switching

- Automatic Gain Control (AGC) calibration

- Noise Floor calibration

- I/Q imbalance calibration (QAM correction)

- Calibration due to thermal changes (gain_F)

- Spur noise mitigation

- RF/PHY initialization for the various operating modes and bwmodes

- Antenna control

- TX power control per channel/rate/packet type

Also have in mind we never got documentation for most of these
functions, what we have comes mostly from Atheros's code, reverse
engineering and patent docs/presentations etc.

.. _`ath5k_hw_radio_revision`:

ath5k_hw_radio_revision
=======================

.. c:function:: u16 ath5k_hw_radio_revision(struct ath5k_hw *ah, enum nl80211_band band)

    Get the PHY Chip revision

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param band:
        One of enum nl80211_band
    :type band: enum nl80211_band

.. _`ath5k_hw_radio_revision.description`:

Description
-----------

Returns the revision number of a 2GHz, 5GHz or single chip
radio.

.. _`ath5k_channel_ok`:

ath5k_channel_ok
================

.. c:function:: bool ath5k_channel_ok(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Check if a channel is supported by the hw

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_channel_ok.note`:

Note
----

We don't do any regulatory domain checks here, it's just
a sanity check.

.. _`ath5k_hw_chan_has_spur_noise`:

ath5k_hw_chan_has_spur_noise
============================

.. c:function:: bool ath5k_hw_chan_has_spur_noise(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Check if channel is sensitive to spur noise

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_hw_rfb_op`:

ath5k_hw_rfb_op
===============

.. c:function:: unsigned int ath5k_hw_rfb_op(struct ath5k_hw *ah, const struct ath5k_rf_reg *rf_regs, u32 val, u8 reg_id, bool set)

    Perform an operation on the given RF Buffer

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param rf_regs:
        The struct ath5k_rf_reg
    :type rf_regs: const struct ath5k_rf_reg \*

    :param val:
        New value
    :type val: u32

    :param reg_id:
        RF register ID
    :type reg_id: u8

    :param set:
        Indicate we need to swap data
    :type set: bool

.. _`ath5k_hw_rfb_op.description`:

Description
-----------

This is an internal function used to modify RF Banks before
writing them to AR5K_RF_BUFFER. Check out rfbuffer.h for more
infos.

.. _`ath5k_hw_write_ofdm_timings`:

ath5k_hw_write_ofdm_timings
===========================

.. c:function:: int ath5k_hw_write_ofdm_timings(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    set OFDM timings on AR5212

    :param ah:
        the \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        the currently set channel upon reset
    :type channel: struct ieee80211_channel \*

.. _`ath5k_hw_write_ofdm_timings.description`:

Description
-----------

Write the delta slope coefficient (used on pilot tracking ?) for OFDM
operation on the AR5212 upon reset. This is a helper for ath5k_hw_phy_init.

Since delta slope is floating point we split it on its exponent and
mantissa and provide these values on hw.

For more infos i think this patent is related
"http://www.freepatentsonline.com/7184495.html"

.. _`ath5k_hw_phy_disable`:

ath5k_hw_phy_disable
====================

.. c:function:: int ath5k_hw_phy_disable(struct ath5k_hw *ah)

    Disable PHY

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_wait_for_synth`:

ath5k_hw_wait_for_synth
=======================

.. c:function:: void ath5k_hw_wait_for_synth(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Wait for synth to settle

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`rf-gain-optimization`:

RF Gain optimization
====================

This code is used to optimize RF gain on different environments
(temperature mostly) based on feedback from a power detector.

It's only used on RF5111 and RF5112, later RF chips seem to have
auto adjustment on hw -notice they have a much smaller BANK 7 and
no gain optimization ladder-.

For more infos check out this patent doc
"http://www.freepatentsonline.com/7400691.html"

This paper describes power drops as seen on the receiver due to
probe packets
"http://www.cnri.dit.ie/publications/ICT08%20-%20Practical%20Issues
\ ``20of``\ %20Power%20Control.pdf"

And this is the MadWiFi bug entry related to the above
"http://madwifi-project.org/ticket/1659"
with various measurements and diagrams

.. _`ath5k_hw_rfgain_opt_init`:

ath5k_hw_rfgain_opt_init
========================

.. c:function:: int ath5k_hw_rfgain_opt_init(struct ath5k_hw *ah)

    Initialize ah_gain during attach

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_request_rfgain_probe`:

ath5k_hw_request_rfgain_probe
=============================

.. c:function:: void ath5k_hw_request_rfgain_probe(struct ath5k_hw *ah)

    Request a PAPD probe packet

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_request_rfgain_probe.description`:

Description
-----------

Schedules a gain probe check on the next transmitted packet.
That means our next packet is going to be sent with lower
tx power and a Peak to Average Power Detector (PAPD) will try
to measure the gain.

.. _`ath5k_hw_request_rfgain_probe.todo`:

TODO
----

Force a tx packet (bypassing PCU arbitrator etc)
just after we enable the probe so that we don't mess with
standard traffic.

.. _`ath5k_hw_rf_gainf_corr`:

ath5k_hw_rf_gainf_corr
======================

.. c:function:: u32 ath5k_hw_rf_gainf_corr(struct ath5k_hw *ah)

    Calculate Gain_F measurement correction

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_rf_gainf_corr.description`:

Description
-----------

Calculate Gain_F measurement correction
based on the current step for RF5112 rev. 2

.. _`ath5k_hw_rf_check_gainf_readback`:

ath5k_hw_rf_check_gainf_readback
================================

.. c:function:: bool ath5k_hw_rf_check_gainf_readback(struct ath5k_hw *ah)

    Validate Gain_F feedback from detector

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_rf_check_gainf_readback.description`:

Description
-----------

Check if current gain_F measurement is in the range of our
power detector windows. If we get a measurement outside range
we know it's not accurate (detectors can't measure anything outside
their detection window) so we must ignore it.

Returns true if readback was O.K. or false on failure

.. _`ath5k_hw_rf_gainf_adjust`:

ath5k_hw_rf_gainf_adjust
========================

.. c:function:: s8 ath5k_hw_rf_gainf_adjust(struct ath5k_hw *ah)

    Perform Gain_F adjustment

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_rf_gainf_adjust.description`:

Description
-----------

Choose the right target gain based on current gain
and RF gain optimization ladder

.. _`ath5k_hw_gainf_calibrate`:

ath5k_hw_gainf_calibrate
========================

.. c:function:: enum ath5k_rfgain ath5k_hw_gainf_calibrate(struct ath5k_hw *ah)

    Do a gain_F calibration

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_gainf_calibrate.description`:

Description
-----------

Main callback for thermal RF gain calibration engine
Check for a new gain reading and schedule an adjustment
if needed.

Returns one of enum ath5k_rfgain codes

.. _`ath5k_hw_rfgain_init`:

ath5k_hw_rfgain_init
====================

.. c:function:: int ath5k_hw_rfgain_init(struct ath5k_hw *ah, enum nl80211_band band)

    Write initial RF gain settings to hw

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param band:
        One of enum nl80211_band
    :type band: enum nl80211_band

.. _`ath5k_hw_rfgain_init.description`:

Description
-----------

Write initial RF gain table to set the RF sensitivity.

.. _`ath5k_hw_rfgain_init.note`:

NOTE
----

This one works on all RF chips and has nothing to do
with Gain_F calibration

.. _`ath5k_hw_rfregs_init`:

ath5k_hw_rfregs_init
====================

.. c:function:: int ath5k_hw_rfregs_init(struct ath5k_hw *ah, struct ieee80211_channel *channel, unsigned int mode)

    Initialize RF register settings

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

    :param mode:
        One of enum ath5k_driver_mode
    :type mode: unsigned int

.. _`ath5k_hw_rfregs_init.description`:

Description
-----------

Setup RF registers by writing RF buffer on hw. For
more infos on this, check out rfbuffer.h

.. _`ath5k_hw_rf5110_chan2athchan`:

ath5k_hw_rf5110_chan2athchan
============================

.. c:function:: u32 ath5k_hw_rf5110_chan2athchan(struct ieee80211_channel *channel)

    Convert channel freq on RF5110

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_hw_rf5110_chan2athchan.description`:

Description
-----------

Map channel frequency to IEEE channel number and convert it
to an internal channel value used by the RF5110 chipset.

.. _`ath5k_hw_rf5110_channel`:

ath5k_hw_rf5110_channel
=======================

.. c:function:: int ath5k_hw_rf5110_channel(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Set channel frequency on RF5110

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_hw_rf5111_chan2athchan`:

ath5k_hw_rf5111_chan2athchan
============================

.. c:function:: int ath5k_hw_rf5111_chan2athchan(unsigned int ieee, struct ath5k_athchan_2ghz *athchan)

    Handle 2GHz channels on RF5111/2111

    :param ieee:
        IEEE channel number
    :type ieee: unsigned int

    :param athchan:
        The \ :c:type:`struct ath5k_athchan_2ghz <ath5k_athchan_2ghz>`\ 
    :type athchan: struct ath5k_athchan_2ghz \*

.. _`ath5k_hw_rf5111_chan2athchan.description`:

Description
-----------

In order to enable the RF2111 frequency converter on RF5111/2111 setups
we need to add some offsets and extra flags to the data values we pass
on to the PHY. So for every 2GHz channel this function gets called
to do the conversion.

.. _`ath5k_hw_rf5111_channel`:

ath5k_hw_rf5111_channel
=======================

.. c:function:: int ath5k_hw_rf5111_channel(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Set channel frequency on RF5111/2111

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_hw_rf5112_channel`:

ath5k_hw_rf5112_channel
=======================

.. c:function:: int ath5k_hw_rf5112_channel(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Set channel frequency on 5112 and newer

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_hw_rf5112_channel.description`:

Description
-----------

On RF5112/2112 and newer we don't need to do any conversion.
We pass the frequency value after a few modifications to the
chip directly.

.. _`ath5k_hw_rf5112_channel.note`:

NOTE
----

Make sure channel frequency given is within our range or else
we might damage the chip ! Use ath5k_channel_ok before calling this one.

.. _`ath5k_hw_rf2425_channel`:

ath5k_hw_rf2425_channel
=======================

.. c:function:: int ath5k_hw_rf2425_channel(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Set channel frequency on RF2425

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_hw_rf2425_channel.description`:

Description
-----------

AR2425/2417 have a different 2GHz RF so code changes
a little bit from RF5112.

.. _`ath5k_hw_channel`:

ath5k_hw_channel
================

.. c:function:: int ath5k_hw_channel(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Set a channel on the radio chip

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_hw_channel.description`:

Description
-----------

This is the main function called to set a channel on the
radio chip based on the radio chip version.

.. _`phy-calibration-routines`:

PHY Calibration routines
========================

Noise floor calibration: When we tell the hardware to
perform a noise floor calibration by setting the
AR5K_PHY_AGCCTL_NF bit on AR5K_PHY_AGCCTL, it will periodically
sample-and-hold the minimum noise level seen at the antennas.
This value is then stored in a ring buffer of recently measured
noise floor values so we have a moving window of the last few
samples. The median of the values in the history is then loaded
into the hardware for its own use for RSSI and CCA measurements.
This type of calibration doesn't interfere with traffic.

AGC calibration: When we tell the hardware to perform
an AGC (Automatic Gain Control) calibration by setting the
AR5K_PHY_AGCCTL_CAL, hw disconnects the antennas and does
a calibration on the DC offsets of ADCs. During this period
rx/tx gets disabled so we have to deal with it on the driver
part.

I/Q calibration: When we tell the hardware to perform
an I/Q calibration, it tries to correct I/Q imbalance and
fix QAM constellation by sampling data from rxed frames.
It doesn't interfere with traffic.

For more infos on AGC and I/Q calibration check out patent doc
#03/094463.

.. _`ath5k_hw_read_measured_noise_floor`:

ath5k_hw_read_measured_noise_floor
==================================

.. c:function:: s32 ath5k_hw_read_measured_noise_floor(struct ath5k_hw *ah)

    Read measured NF from hw

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_init_nfcal_hist`:

ath5k_hw_init_nfcal_hist
========================

.. c:function:: void ath5k_hw_init_nfcal_hist(struct ath5k_hw *ah)

    Initialize NF calibration history buffer

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_update_nfcal_hist`:

ath5k_hw_update_nfcal_hist
==========================

.. c:function:: void ath5k_hw_update_nfcal_hist(struct ath5k_hw *ah, s16 noise_floor)

    Update NF calibration history buffer

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param noise_floor:
        The NF we got from hw
    :type noise_floor: s16

.. _`ath5k_hw_get_median_noise_floor`:

ath5k_hw_get_median_noise_floor
===============================

.. c:function:: s16 ath5k_hw_get_median_noise_floor(struct ath5k_hw *ah)

    Get median NF from history buffer

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_update_noise_floor`:

ath5k_hw_update_noise_floor
===========================

.. c:function:: void ath5k_hw_update_noise_floor(struct ath5k_hw *ah)

    Update NF on hardware

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_update_noise_floor.description`:

Description
-----------

This is the main function we call to perform a NF calibration,
it reads NF from hardware, calculates the median and updates
NF on hw.

.. _`ath5k_hw_rf5110_calibrate`:

ath5k_hw_rf5110_calibrate
=========================

.. c:function:: int ath5k_hw_rf5110_calibrate(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Perform a PHY calibration on RF5110

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_hw_rf5110_calibrate.description`:

Description
-----------

Do a complete PHY calibration (AGC + NF + I/Q) on RF5110

.. _`ath5k_hw_rf511x_iq_calibrate`:

ath5k_hw_rf511x_iq_calibrate
============================

.. c:function:: int ath5k_hw_rf511x_iq_calibrate(struct ath5k_hw *ah)

    Perform I/Q calibration on RF5111 and newer

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`ath5k_hw_phy_calibrate`:

ath5k_hw_phy_calibrate
======================

.. c:function:: int ath5k_hw_phy_calibrate(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Perform a PHY calibration

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_hw_phy_calibrate.description`:

Description
-----------

The main function we call from above to perform
a short or full PHY calibration based on RF chip
and current channel

.. _`ath5k_hw_set_spur_mitigation_filter`:

ath5k_hw_set_spur_mitigation_filter
===================================

.. c:function:: void ath5k_hw_set_spur_mitigation_filter(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Configure SPUR filter

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_hw_set_spur_mitigation_filter.description`:

Description
-----------

This function gets called during PHY initialization to
configure the spur filter for the given channel. Spur is noise
generated due to "reflection" effects, for more information on this
method check out patent US7643810

.. _`antenna-control`:

Antenna control
===============

Hw supports up to 14 antennas ! I haven't found any card that implements
that. The maximum number of antennas I've seen is up to 4 (2 for 2GHz and 2
for 5GHz). Antenna 1 (MAIN) should be omnidirectional, 2 (AUX)
omnidirectional or sectorial and antennas 3-14 sectorial (or directional).

We can have a single antenna for RX and multiple antennas for TX.
RX antenna is our "default" antenna (usually antenna 1) set on
DEFAULT_ANTENNA register and TX antenna is set on each TX control descriptor
(0 for automatic selection, 1 - 14 antenna number).

We can let hw do all the work doing fast antenna diversity for both
tx and rx or we can do things manually. Here are the options we have
(all are bits of STA_ID1 register):

AR5K_STA_ID1_DEFAULT_ANTENNA -> When 0 is set as the TX antenna on TX
control descriptor, use the default antenna to transmit or else use the last
antenna on which we received an ACK.

AR5K_STA_ID1_DESC_ANTENNA -> Update default antenna after each TX frame to
the antenna on which we got the ACK for that frame.

AR5K_STA_ID1_RTS_DEF_ANTENNA -> Use default antenna for RTS or else use the
one on the TX descriptor.

AR5K_STA_ID1_SELFGEN_DEF_ANT -> Use default antenna for self generated frames
(ACKs etc), or else use current antenna (the one we just used for TX).

Using the above we support the following scenarios:

AR5K_ANTMODE_DEFAULT -> Hw handles antenna diversity etc automatically

AR5K_ANTMODE_FIXED_A -> Only antenna A (MAIN) is present

AR5K_ANTMODE_FIXED_B -> Only antenna B (AUX) is present

AR5K_ANTMODE_SINGLE_AP -> Sta locked on a single ap

AR5K_ANTMODE_SECTOR_AP -> AP with tx antenna set on tx desc

AR5K_ANTMODE_SECTOR_STA -> STA with tx antenna set on tx desc

AR5K_ANTMODE_DEBUG Debug mode -A -> Rx, B-> Tx-

Also note that when setting antenna to F on tx descriptor card inverts
current tx antenna.

.. _`ath5k_hw_set_def_antenna`:

ath5k_hw_set_def_antenna
========================

.. c:function:: void ath5k_hw_set_def_antenna(struct ath5k_hw *ah, u8 ant)

    Set default rx antenna on AR5211/5212 and newer

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param ant:
        Antenna number
    :type ant: u8

.. _`ath5k_hw_set_fast_div`:

ath5k_hw_set_fast_div
=====================

.. c:function:: void ath5k_hw_set_fast_div(struct ath5k_hw *ah, u8 ee_mode, bool enable)

    Enable/disable fast rx antenna diversity

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param ee_mode:
        One of enum ath5k_driver_mode
    :type ee_mode: u8

    :param enable:
        True to enable, false to disable
    :type enable: bool

.. _`ath5k_hw_set_antenna_switch`:

ath5k_hw_set_antenna_switch
===========================

.. c:function:: void ath5k_hw_set_antenna_switch(struct ath5k_hw *ah, u8 ee_mode)

    Set up antenna switch table

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param ee_mode:
        One of enum ath5k_driver_mode
    :type ee_mode: u8

.. _`ath5k_hw_set_antenna_switch.description`:

Description
-----------

Switch table comes from EEPROM and includes information on controlling
the 2 antenna RX attenuators

.. _`ath5k_hw_set_antenna_mode`:

ath5k_hw_set_antenna_mode
=========================

.. c:function:: void ath5k_hw_set_antenna_mode(struct ath5k_hw *ah, u8 ant_mode)

    Set antenna operating mode

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param ant_mode:
        One of enum ath5k_ant_mode
    :type ant_mode: u8

.. _`ath5k_get_interpolated_value`:

ath5k_get_interpolated_value
============================

.. c:function:: s16 ath5k_get_interpolated_value(s16 target, s16 x_left, s16 x_right, s16 y_left, s16 y_right)

    Get interpolated Y val between two points

    :param target:
        X value of the middle point
    :type target: s16

    :param x_left:
        X value of the left point
    :type x_left: s16

    :param x_right:
        X value of the right point
    :type x_right: s16

    :param y_left:
        Y value of the left point
    :type y_left: s16

    :param y_right:
        Y value of the right point
    :type y_right: s16

.. _`ath5k_get_linear_pcdac_min`:

ath5k_get_linear_pcdac_min
==========================

.. c:function:: s16 ath5k_get_linear_pcdac_min(const u8 *stepL, const u8 *stepR, const s16 *pwrL, const s16 *pwrR)

    Find vertical boundary (min pwr) for the linear PCDAC curve

    :param stepL:
        Left array with y values (pcdac steps)
    :type stepL: const u8 \*

    :param stepR:
        Right array with y values (pcdac steps)
    :type stepR: const u8 \*

    :param pwrL:
        Left array with x values (power steps)
    :type pwrL: const s16 \*

    :param pwrR:
        Right array with x values (power steps)
    :type pwrR: const s16 \*

.. _`ath5k_get_linear_pcdac_min.description`:

Description
-----------

Since we have the top of the curve and we draw the line below
until we reach 1 (1 pcdac step) we need to know which point
(x value) that is so that we don't go below x axis and have negative
pcdac values when creating the curve, or fill the table with zeros.

.. _`ath5k_create_power_curve`:

ath5k_create_power_curve
========================

.. c:function:: void ath5k_create_power_curve(s16 pmin, s16 pmax, const s16 *pwr, const u8 *vpd, u8 num_points, u8 *vpd_table, u8 type)

    Create a Power to PDADC or PCDAC curve

    :param pmin:
        Minimum power value (xmin)
    :type pmin: s16

    :param pmax:
        Maximum power value (xmax)
    :type pmax: s16

    :param pwr:
        Array of power steps (x values)
    :type pwr: const s16 \*

    :param vpd:
        Array of matching PCDAC/PDADC steps (y values)
    :type vpd: const u8 \*

    :param num_points:
        Number of provided points
    :type num_points: u8

    :param vpd_table:
        Array to fill with the full PCDAC/PDADC values (y values)
    :type vpd_table: u8 \*

    :param type:
        One of enum ath5k_powertable_type (eeprom.h)
    :type type: u8

.. _`ath5k_create_power_curve.description`:

Description
-----------

Interpolate (pwr,vpd) points to create a Power to PDADC or a
Power to PCDAC curve.

Each curve has power on x axis (in 0.5dB units) and PCDAC/PDADC
steps (offsets) on y axis. Power can go up to 31.5dB and max
PCDAC/PDADC step for each curve is 64 but we can write more than
one curves on hw so we can go up to 128 (which is the max step we
can write on the final table).

We write y values (PCDAC/PDADC steps) on hw.

.. _`ath5k_get_chan_pcal_surrounding_piers`:

ath5k_get_chan_pcal_surrounding_piers
=====================================

.. c:function:: void ath5k_get_chan_pcal_surrounding_piers(struct ath5k_hw *ah, struct ieee80211_channel *channel, struct ath5k_chan_pcal_info **pcinfo_l, struct ath5k_chan_pcal_info **pcinfo_r)

    Get surrounding calibration piers for a given channel.

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

    :param pcinfo_l:
        The \ :c:type:`struct ath5k_chan_pcal_info <ath5k_chan_pcal_info>`\  to put the left cal. pier
    :type pcinfo_l: struct ath5k_chan_pcal_info \*\*

    :param pcinfo_r:
        The \ :c:type:`struct ath5k_chan_pcal_info <ath5k_chan_pcal_info>`\  to put the right cal. pier
    :type pcinfo_r: struct ath5k_chan_pcal_info \*\*

.. _`ath5k_get_chan_pcal_surrounding_piers.description`:

Description
-----------

Get the surrounding per-channel power calibration piers
for a given frequency so that we can interpolate between
them and come up with an appropriate dataset for our current
channel.

.. _`ath5k_get_rate_pcal_data`:

ath5k_get_rate_pcal_data
========================

.. c:function:: void ath5k_get_rate_pcal_data(struct ath5k_hw *ah, struct ieee80211_channel *channel, struct ath5k_rate_pcal_info *rates)

    Get the interpolated per-rate power calibration data

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\  \*ah,
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

    :param rates:
        The \ :c:type:`struct ath5k_rate_pcal_info <ath5k_rate_pcal_info>`\  to fill
    :type rates: struct ath5k_rate_pcal_info \*

.. _`ath5k_get_rate_pcal_data.description`:

Description
-----------

Get the surrounding per-rate power calibration data
for a given frequency and interpolate between power
values to set max target power supported by hw for
each rate on this frequency.

.. _`ath5k_get_max_ctl_power`:

ath5k_get_max_ctl_power
=======================

.. c:function:: void ath5k_get_max_ctl_power(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Get max edge power for a given frequency

    :param ah:
        the \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

.. _`ath5k_get_max_ctl_power.description`:

Description
-----------

Get the max edge power for this channel if
we have such data from EEPROM's Conformance Test
Limits (CTL), and limit max power if needed.

.. _`power-to-pcdac-table-functions`:

Power to PCDAC table functions
==============================

For RF5111 we have an XPD -eXternal Power Detector- curve
for each calibrated channel. Each curve has 0,5dB Power steps
on x axis and PCDAC steps (offsets) on y axis and looks like an
exponential function. To recreate the curve we read 11 points
from eeprom (eeprom.c) and interpolate here.

For RF5112 we have 4 XPD -eXternal Power Detector- curves
for each calibrated channel on 0, -6, -12 and -18dBm but we only
use the higher (3) and the lower (0) curves. Each curve again has 0.5dB
power steps on x axis and PCDAC steps on y axis and looks like a
linear function. To recreate the curve and pass the power values
on hw, we get 4 points for xpd 0 (lower gain -> max power)
and 3 points for xpd 3 (higher gain -> lower power) from eeprom (eeprom.c)
and interpolate here.

For a given channel we get the calibrated points (piers) for it or
-if we don't have calibration data for this specific channel- from the
available surrounding channels we have calibration data for, after we do a
linear interpolation between them. Then since we have our calibrated points
for this channel, we do again a linear interpolation between them to get the
whole curve.

We finally write the Y values of the curve(s) (the PCDAC values) on hw

.. _`ath5k_fill_pwr_to_pcdac_table`:

ath5k_fill_pwr_to_pcdac_table
=============================

.. c:function:: void ath5k_fill_pwr_to_pcdac_table(struct ath5k_hw *ah, s16* table_min, s16 *table_max)

    Fill Power to PCDAC table on RF5111

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param table_min:
        Minimum power (x min)
    :type table_min: s16\*

    :param table_max:
        Maximum power (x max)
    :type table_max: s16 \*

.. _`ath5k_fill_pwr_to_pcdac_table.description`:

Description
-----------

No further processing is needed for RF5111, the only thing we have to
do is fill the values below and above calibration range since eeprom data
may not cover the entire PCDAC table.

.. _`ath5k_combine_linear_pcdac_curves`:

ath5k_combine_linear_pcdac_curves
=================================

.. c:function:: void ath5k_combine_linear_pcdac_curves(struct ath5k_hw *ah, s16* table_min, s16 *table_max, u8 pdcurves)

    Combine available PCDAC Curves

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param table_min:
        Minimum power (x min)
    :type table_min: s16\*

    :param table_max:
        Maximum power (x max)
    :type table_max: s16 \*

    :param pdcurves:
        Number of pd curves
    :type pdcurves: u8

.. _`ath5k_combine_linear_pcdac_curves.description`:

Description
-----------

Combine available XPD Curves and fill Linear Power to PCDAC table on RF5112
RFX112 can have up to 2 curves (one for low txpower range and one for
higher txpower range). We need to put them both on pcdac_out and place
them in the correct location. In case we only have one curve available
just fit it on pcdac_out (it's supposed to cover the entire range of
available pwr levels since it's always the higher power curve). Extrapolate
below and above final table if needed.

.. _`ath5k_write_pcdac_table`:

ath5k_write_pcdac_table
=======================

.. c:function:: void ath5k_write_pcdac_table(struct ath5k_hw *ah)

    Write the PCDAC values on hw

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

.. _`power-to-pdadc-table-functions`:

Power to PDADC table functions
==============================

For RF2413 and later we have a Power to PDADC table (Power Detector)
instead of a PCDAC (Power Control) and 4 pd gain curves for each
calibrated channel. Each curve has power on x axis in 0.5 db steps and
PDADC steps on y axis and looks like an exponential function like the
RF5111 curve.

To recreate the curves we read the points from eeprom (eeprom.c)
and interpolate here. Note that in most cases only 2 (higher and lower)
curves are used (like RF5112) but vendors have the opportunity to include
all 4 curves on eeprom. The final curve (higher power) has an extra
point for better accuracy like RF5112.

The process is similar to what we do above for RF5111/5112

.. _`ath5k_combine_pwr_to_pdadc_curves`:

ath5k_combine_pwr_to_pdadc_curves
=================================

.. c:function:: void ath5k_combine_pwr_to_pdadc_curves(struct ath5k_hw *ah, s16 *pwr_min, s16 *pwr_max, u8 pdcurves)

    Combine the various PDADC curves

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param pwr_min:
        Minimum power (x min)
    :type pwr_min: s16 \*

    :param pwr_max:
        Maximum power (x max)
    :type pwr_max: s16 \*

    :param pdcurves:
        Number of available curves
    :type pdcurves: u8

.. _`ath5k_combine_pwr_to_pdadc_curves.description`:

Description
-----------

Combine the various pd curves and create the final Power to PDADC table
We can have up to 4 pd curves, we need to do a similar process
as we do for RF5112. This time we don't have an edge_flag but we
set the gain boundaries on a separate register.

.. _`ath5k_write_pwr_to_pdadc_table`:

ath5k_write_pwr_to_pdadc_table
==============================

.. c:function:: void ath5k_write_pwr_to_pdadc_table(struct ath5k_hw *ah, u8 ee_mode)

    Write the PDADC values on hw

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param ee_mode:
        One of enum ath5k_driver_mode
    :type ee_mode: u8

.. _`ath5k_setup_channel_powertable`:

ath5k_setup_channel_powertable
==============================

.. c:function:: int ath5k_setup_channel_powertable(struct ath5k_hw *ah, struct ieee80211_channel *channel, u8 ee_mode, u8 type)

    Set up power table for this channel

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

    :param ee_mode:
        One of enum ath5k_driver_mode
    :type ee_mode: u8

    :param type:
        One of enum ath5k_powertable_type (eeprom.h)
    :type type: u8

.. _`ath5k_setup_channel_powertable.description`:

Description
-----------

This is the main function that uses all of the above
to set PCDAC/PDADC table on hw for the current channel.
This table is used for tx power calibration on the baseband,
without it we get weird tx power levels and in some cases
distorted spectral mask

.. _`ath5k_write_channel_powertable`:

ath5k_write_channel_powertable
==============================

.. c:function:: void ath5k_write_channel_powertable(struct ath5k_hw *ah, u8 ee_mode, u8 type)

    Set power table for current channel on hw

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param ee_mode:
        One of enum ath5k_driver_mode
    :type ee_mode: u8

    :param type:
        One of enum ath5k_powertable_type (eeprom.h)
    :type type: u8

.. _`per-rate-tx-power-setting`:

Per-rate tx power setting
=========================

This is the code that sets the desired tx power limit (below
maximum) on hw for each rate (we also have TPC that sets
power per packet type). We do that by providing an index on the
PCDAC/PDADC table we set up above, for each rate.

For now we only limit txpower based on maximum tx power
supported by hw (what's inside rate_info) + conformance test
limits. We need to limit this even more, based on regulatory domain
etc to be safe. Normally this is done from above so we don't care
here, all we care is that the tx power we set will be O.K.
for the hw (e.g. won't create noise on PA etc).

Rate power table contains indices to PCDAC/PDADC table (0.5dB steps -
x values) and is indexed as follows:
rates[0] - rates[7] -> OFDM rates
rates[8] - rates[14] -> CCK rates
rates[15] -> XR rates (they all have the same power)

.. _`ath5k_setup_rate_powertable`:

ath5k_setup_rate_powertable
===========================

.. c:function:: void ath5k_setup_rate_powertable(struct ath5k_hw *ah, u16 max_pwr, struct ath5k_rate_pcal_info *rate_info, u8 ee_mode)

    Set up rate power table for a given tx power

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param max_pwr:
        The maximum tx power requested in 0.5dB steps
    :type max_pwr: u16

    :param rate_info:
        The \ :c:type:`struct ath5k_rate_pcal_info <ath5k_rate_pcal_info>`\  to fill
    :type rate_info: struct ath5k_rate_pcal_info \*

    :param ee_mode:
        One of enum ath5k_driver_mode
    :type ee_mode: u8

.. _`ath5k_hw_txpower`:

ath5k_hw_txpower
================

.. c:function:: int ath5k_hw_txpower(struct ath5k_hw *ah, struct ieee80211_channel *channel, u8 txpower)

    Set transmission power limit for a given channel

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 
    :type channel: struct ieee80211_channel \*

    :param txpower:
        Requested tx power in 0.5dB steps
    :type txpower: u8

.. _`ath5k_hw_txpower.description`:

Description
-----------

Combines all of the above to set the requested tx power limit
on hw.

.. _`ath5k_hw_set_txpower_limit`:

ath5k_hw_set_txpower_limit
==========================

.. c:function:: int ath5k_hw_set_txpower_limit(struct ath5k_hw *ah, u8 txpower)

    Set txpower limit for the current channel

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param txpower:
        The requested tx power limit in 0.5dB steps
    :type txpower: u8

.. _`ath5k_hw_set_txpower_limit.description`:

Description
-----------

This function provides access to ath5k_hw_txpower to the driver in
case user or an application changes it while PHY is running.

.. _`ath5k_hw_phy_init`:

ath5k_hw_phy_init
=================

.. c:function:: int ath5k_hw_phy_init(struct ath5k_hw *ah, struct ieee80211_channel *channel, u8 mode, bool fast)

    Initialize PHY

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param channel:
        The \ ``struct``\  ieee80211_channel
    :type channel: struct ieee80211_channel \*

    :param mode:
        One of enum ath5k_driver_mode
    :type mode: u8

    :param fast:
        Try a fast channel switch instead
    :type fast: bool

.. _`ath5k_hw_phy_init.description`:

Description
-----------

This is the main function used during reset to initialize PHY
or do a fast channel change if possible.

.. _`ath5k_hw_phy_init.note`:

NOTE
----

Do not call this one from the driver, it assumes PHY is in a
warm reset state !

.. This file was automatic generated / don't edit.

