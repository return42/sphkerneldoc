.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/phy.c

.. _`ath5k_hw_radio_revision`:

ath5k_hw_radio_revision
=======================

.. c:function:: u16 ath5k_hw_radio_revision(struct ath5k_hw *ah, enum nl80211_band band)

    Get the PHY Chip revision

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param enum nl80211_band band:
        One of enum nl80211_band

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

.. _`ath5k_hw_rfb_op`:

ath5k_hw_rfb_op
===============

.. c:function:: unsigned int ath5k_hw_rfb_op(struct ath5k_hw *ah, const struct ath5k_rf_reg *rf_regs, u32 val, u8 reg_id, bool set)

    Perform an operation on the given RF Buffer

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param const struct ath5k_rf_reg \*rf_regs:
        The struct ath5k_rf_reg

    :param u32 val:
        New value

    :param u8 reg_id:
        RF register ID

    :param bool set:
        Indicate we need to swap data

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

    :param struct ath5k_hw \*ah:
        the \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        the currently set channel upon reset

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_wait_for_synth`:

ath5k_hw_wait_for_synth
=======================

.. c:function:: void ath5k_hw_wait_for_synth(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Wait for synth to settle

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

.. _`ath5k_hw_rfgain_opt_init`:

ath5k_hw_rfgain_opt_init
========================

.. c:function:: int ath5k_hw_rfgain_opt_init(struct ath5k_hw *ah)

    Initialize ah_gain during attach

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_request_rfgain_probe`:

ath5k_hw_request_rfgain_probe
=============================

.. c:function:: void ath5k_hw_request_rfgain_probe(struct ath5k_hw *ah)

    Request a PAPD probe packet

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param enum nl80211_band band:
        One of enum nl80211_band

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

    :param unsigned int mode:
        One of enum ath5k_driver_mode

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

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

.. _`ath5k_hw_rf5111_chan2athchan`:

ath5k_hw_rf5111_chan2athchan
============================

.. c:function:: int ath5k_hw_rf5111_chan2athchan(unsigned int ieee, struct ath5k_athchan_2ghz *athchan)

    Handle 2GHz channels on RF5111/2111

    :param unsigned int ieee:
        IEEE channel number

    :param struct ath5k_athchan_2ghz \*athchan:
        The \ :c:type:`struct ath5k_athchan_2ghz <ath5k_athchan_2ghz>`\ 

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

.. _`ath5k_hw_rf5112_channel`:

ath5k_hw_rf5112_channel
=======================

.. c:function:: int ath5k_hw_rf5112_channel(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Set channel frequency on 5112 and newer

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

.. _`ath5k_hw_channel.description`:

Description
-----------

This is the main function called to set a channel on the
radio chip based on the radio chip version.

.. _`ath5k_hw_read_measured_noise_floor`:

ath5k_hw_read_measured_noise_floor
==================================

.. c:function:: s32 ath5k_hw_read_measured_noise_floor(struct ath5k_hw *ah)

    Read measured NF from hw

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_init_nfcal_hist`:

ath5k_hw_init_nfcal_hist
========================

.. c:function:: void ath5k_hw_init_nfcal_hist(struct ath5k_hw *ah)

    Initialize NF calibration history buffer

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_update_nfcal_hist`:

ath5k_hw_update_nfcal_hist
==========================

.. c:function:: void ath5k_hw_update_nfcal_hist(struct ath5k_hw *ah, s16 noise_floor)

    Update NF calibration history buffer

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param s16 noise_floor:
        The NF we got from hw

.. _`ath5k_hw_get_median_noise_floor`:

ath5k_hw_get_median_noise_floor
===============================

.. c:function:: s16 ath5k_hw_get_median_noise_floor(struct ath5k_hw *ah)

    Get median NF from history buffer

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_update_noise_floor`:

ath5k_hw_update_noise_floor
===========================

.. c:function:: void ath5k_hw_update_noise_floor(struct ath5k_hw *ah)

    Update NF on hardware

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

.. _`ath5k_hw_rf5110_calibrate.description`:

Description
-----------

Do a complete PHY calibration (AGC + NF + I/Q) on RF5110

.. _`ath5k_hw_rf511x_iq_calibrate`:

ath5k_hw_rf511x_iq_calibrate
============================

.. c:function:: int ath5k_hw_rf511x_iq_calibrate(struct ath5k_hw *ah)

    Perform I/Q calibration on RF5111 and newer

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_phy_calibrate`:

ath5k_hw_phy_calibrate
======================

.. c:function:: int ath5k_hw_phy_calibrate(struct ath5k_hw *ah, struct ieee80211_channel *channel)

    Perform a PHY calibration

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

.. _`ath5k_hw_set_spur_mitigation_filter.description`:

Description
-----------

This function gets called during PHY initialization to
configure the spur filter for the given channel. Spur is noise
generated due to "reflection" effects, for more information on this
method check out patent US7643810

.. _`ath5k_hw_set_def_antenna`:

ath5k_hw_set_def_antenna
========================

.. c:function:: void ath5k_hw_set_def_antenna(struct ath5k_hw *ah, u8 ant)

    Set default rx antenna on AR5211/5212 and newer

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param u8 ant:
        Antenna number

.. _`ath5k_hw_set_fast_div`:

ath5k_hw_set_fast_div
=====================

.. c:function:: void ath5k_hw_set_fast_div(struct ath5k_hw *ah, u8 ee_mode, bool enable)

    Enable/disable fast rx antenna diversity

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param u8 ee_mode:
        One of enum ath5k_driver_mode

    :param bool enable:
        True to enable, false to disable

.. _`ath5k_hw_set_antenna_switch`:

ath5k_hw_set_antenna_switch
===========================

.. c:function:: void ath5k_hw_set_antenna_switch(struct ath5k_hw *ah, u8 ee_mode)

    Set up antenna switch table

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param u8 ee_mode:
        One of enum ath5k_driver_mode

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param u8 ant_mode:
        One of enum ath5k_ant_mode

.. _`ath5k_get_interpolated_value`:

ath5k_get_interpolated_value
============================

.. c:function:: s16 ath5k_get_interpolated_value(s16 target, s16 x_left, s16 x_right, s16 y_left, s16 y_right)

    Get interpolated Y val between two points

    :param s16 target:
        X value of the middle point

    :param s16 x_left:
        X value of the left point

    :param s16 x_right:
        X value of the right point

    :param s16 y_left:
        Y value of the left point

    :param s16 y_right:
        Y value of the right point

.. _`ath5k_get_linear_pcdac_min`:

ath5k_get_linear_pcdac_min
==========================

.. c:function:: s16 ath5k_get_linear_pcdac_min(const u8 *stepL, const u8 *stepR, const s16 *pwrL, const s16 *pwrR)

    Find vertical boundary (min pwr) for the linear PCDAC curve

    :param const u8 \*stepL:
        Left array with y values (pcdac steps)

    :param const u8 \*stepR:
        Right array with y values (pcdac steps)

    :param const s16 \*pwrL:
        Left array with x values (power steps)

    :param const s16 \*pwrR:
        Right array with x values (power steps)

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

    :param s16 pmin:
        Minimum power value (xmin)

    :param s16 pmax:
        Maximum power value (xmax)

    :param const s16 \*pwr:
        Array of power steps (x values)

    :param const u8 \*vpd:
        Array of matching PCDAC/PDADC steps (y values)

    :param u8 num_points:
        Number of provided points

    :param u8 \*vpd_table:
        Array to fill with the full PCDAC/PDADC values (y values)

    :param u8 type:
        One of enum ath5k_powertable_type (eeprom.h)

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

    :param struct ath5k_chan_pcal_info \*\*pcinfo_l:
        The \ :c:type:`struct ath5k_chan_pcal_info <ath5k_chan_pcal_info>`\  to put the left cal. pier

    :param struct ath5k_chan_pcal_info \*\*pcinfo_r:
        The \ :c:type:`struct ath5k_chan_pcal_info <ath5k_chan_pcal_info>`\  to put the right cal. pier

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\  \*ah,

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

    :param struct ath5k_rate_pcal_info \*rates:
        The \ :c:type:`struct ath5k_rate_pcal_info <ath5k_rate_pcal_info>`\  to fill

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

    :param struct ath5k_hw \*ah:
        the \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

.. _`ath5k_get_max_ctl_power.description`:

Description
-----------

Get the max edge power for this channel if
we have such data from EEPROM's Conformance Test
Limits (CTL), and limit max power if needed.

.. _`ath5k_fill_pwr_to_pcdac_table`:

ath5k_fill_pwr_to_pcdac_table
=============================

.. c:function:: void ath5k_fill_pwr_to_pcdac_table(struct ath5k_hw *ah, s16*table_min, s16 *table_max)

    Fill Power to PCDAC table on RF5111

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param s16\*table_min:
        Minimum power (x min)

    :param s16 \*table_max:
        Maximum power (x max)

.. _`ath5k_fill_pwr_to_pcdac_table.description`:

Description
-----------

No further processing is needed for RF5111, the only thing we have to
do is fill the values below and above calibration range since eeprom data
may not cover the entire PCDAC table.

.. _`ath5k_combine_linear_pcdac_curves`:

ath5k_combine_linear_pcdac_curves
=================================

.. c:function:: void ath5k_combine_linear_pcdac_curves(struct ath5k_hw *ah, s16*table_min, s16 *table_max, u8 pdcurves)

    Combine available PCDAC Curves

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param s16\*table_min:
        Minimum power (x min)

    :param s16 \*table_max:
        Maximum power (x max)

    :param u8 pdcurves:
        Number of pd curves

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_combine_pwr_to_pdadc_curves`:

ath5k_combine_pwr_to_pdadc_curves
=================================

.. c:function:: void ath5k_combine_pwr_to_pdadc_curves(struct ath5k_hw *ah, s16 *pwr_min, s16 *pwr_max, u8 pdcurves)

    Combine the various PDADC curves

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param s16 \*pwr_min:
        Minimum power (x min)

    :param s16 \*pwr_max:
        Maximum power (x max)

    :param u8 pdcurves:
        Number of available curves

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param u8 ee_mode:
        One of enum ath5k_driver_mode

.. _`ath5k_setup_channel_powertable`:

ath5k_setup_channel_powertable
==============================

.. c:function:: int ath5k_setup_channel_powertable(struct ath5k_hw *ah, struct ieee80211_channel *channel, u8 ee_mode, u8 type)

    Set up power table for this channel

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

    :param u8 ee_mode:
        One of enum ath5k_driver_mode

    :param u8 type:
        One of enum ath5k_powertable_type (eeprom.h)

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param u8 ee_mode:
        One of enum ath5k_driver_mode

    :param u8 type:
        One of enum ath5k_powertable_type (eeprom.h)

.. _`ath5k_setup_rate_powertable`:

ath5k_setup_rate_powertable
===========================

.. c:function:: void ath5k_setup_rate_powertable(struct ath5k_hw *ah, u16 max_pwr, struct ath5k_rate_pcal_info *rate_info, u8 ee_mode)

    Set up rate power table for a given tx power

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param u16 max_pwr:
        The maximum tx power requested in 0.5dB steps

    :param struct ath5k_rate_pcal_info \*rate_info:
        The \ :c:type:`struct ath5k_rate_pcal_info <ath5k_rate_pcal_info>`\  to fill

    :param u8 ee_mode:
        One of enum ath5k_driver_mode

.. _`ath5k_hw_txpower`:

ath5k_hw_txpower
================

.. c:function:: int ath5k_hw_txpower(struct ath5k_hw *ah, struct ieee80211_channel *channel, u8 txpower)

    Set transmission power limit for a given channel

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ :c:type:`struct ieee80211_channel <ieee80211_channel>`\ 

    :param u8 txpower:
        Requested tx power in 0.5dB steps

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param u8 txpower:
        The requested tx power limit in 0.5dB steps

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

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ieee80211_channel \*channel:
        The \ ``struct``\  ieee80211_channel

    :param u8 mode:
        One of enum ath5k_driver_mode

    :param bool fast:
        Try a fast channel switch instead

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

