.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath9k/hw.h

.. _`ath_hw_radar_conf`:

struct ath_hw_radar_conf
========================

.. c:type:: struct ath_hw_radar_conf

    radar detection initialization parameters

.. _`ath_hw_radar_conf.definition`:

Definition
----------

.. code-block:: c

    struct ath_hw_radar_conf {
        unsigned int pulse_inband;
        unsigned int pulse_inband_step;
        unsigned int pulse_height;
        unsigned int pulse_rssi;
        unsigned int pulse_maxlen;
        unsigned int radar_rssi;
        unsigned int radar_inband;
        int fir_power;
        bool ext_channel;
    }

.. _`ath_hw_radar_conf.members`:

Members
-------

pulse_inband
    threshold for checking the ratio of in-band power
    to total power for short radar pulses (half dB steps)

pulse_inband_step
    threshold for checking an in-band power to total
    power ratio increase for short radar pulses (half dB steps)

pulse_height
    threshold for detecting the beginning of a short
    radar pulse (dB step)

pulse_rssi
    threshold for detecting if a short radar pulse is
    gone (dB step)

pulse_maxlen
    maximum pulse length (0.8 us steps)

radar_rssi
    RSSI threshold for starting long radar detection (dB steps)

radar_inband
    threshold for checking the ratio of in-band power
    to total power for long radar pulses (half dB steps)

fir_power
    threshold for detecting the end of a long radar pulse (dB)

ext_channel
    enable extension channel radar detection

.. _`ath_hw_private_ops`:

struct ath_hw_private_ops
=========================

.. c:type:: struct ath_hw_private_ops

    callbacks used internally by hardware code

.. _`ath_hw_private_ops.definition`:

Definition
----------

.. code-block:: c

    struct ath_hw_private_ops {
        void (*init_hang_checks)(struct ath_hw *ah);
        bool (*detect_mac_hang)(struct ath_hw *ah);
        bool (*detect_bb_hang)(struct ath_hw *ah);
        void (*init_cal_settings)(struct ath_hw *ah);
        bool (*init_cal)(struct ath_hw *ah, struct ath9k_channel *chan);
        void (*init_mode_gain_regs)(struct ath_hw *ah);
        void (*setup_calibration)(struct ath_hw *ah, struct ath9k_cal_list *currCal);
        int (*rf_set_freq)(struct ath_hw *ah, struct ath9k_channel *chan);
        void (*spur_mitigate_freq)(struct ath_hw *ah, struct ath9k_channel *chan);
        bool (*set_rf_regs)(struct ath_hw *ah,struct ath9k_channel *chan, u16 modesIndex);
        void (*set_channel_regs)(struct ath_hw *ah, struct ath9k_channel *chan);
        void (*init_bb)(struct ath_hw *ah, struct ath9k_channel *chan);
        int (*process_ini)(struct ath_hw *ah, struct ath9k_channel *chan);
        void (*olc_init)(struct ath_hw *ah);
        void (*set_rfmode)(struct ath_hw *ah, struct ath9k_channel *chan);
        void (*mark_phy_inactive)(struct ath_hw *ah);
        void (*set_delta_slope)(struct ath_hw *ah, struct ath9k_channel *chan);
        bool (*rfbus_req)(struct ath_hw *ah);
        void (*rfbus_done)(struct ath_hw *ah);
        void (*restore_chainmask)(struct ath_hw *ah);
        u32 (*compute_pll_control)(struct ath_hw *ah, struct ath9k_channel *chan);
        bool (*ani_control)(struct ath_hw *ah, enum ath9k_ani_cmd cmd, int param);
        void (*do_getnf)(struct ath_hw *ah, int16_t nfarray[NUM_NF_READINGS]);
        void (*set_radar_params)(struct ath_hw *ah, struct ath_hw_radar_conf *conf);
        int (*fast_chan_change)(struct ath_hw *ah, struct ath9k_channel *chan, u8 *ini_reloaded);
        void (*ani_cache_ini_regs)(struct ath_hw *ah);
    #ifdef CONFIG_ATH9K_BTCOEX_SUPPORT
        bool (*is_aic_enabled)(struct ath_hw *ah);
    #endif 
    }

.. _`ath_hw_private_ops.members`:

Members
-------

init_hang_checks
    *undescribed*

detect_mac_hang
    *undescribed*

detect_bb_hang
    *undescribed*

init_cal_settings
    setup types of calibrations supported

init_cal
    starts actual calibration

init_mode_gain_regs
    Initialize TX/RX gain registers

setup_calibration
    set up calibration

rf_set_freq
    change frequency

spur_mitigate_freq
    spur mitigation

set_rf_regs
    *undescribed*

set_channel_regs
    *undescribed*

init_bb
    *undescribed*

process_ini
    *undescribed*

olc_init
    *undescribed*

set_rfmode
    *undescribed*

mark_phy_inactive
    *undescribed*

set_delta_slope
    *undescribed*

rfbus_req
    *undescribed*

rfbus_done
    *undescribed*

restore_chainmask
    *undescribed*

compute_pll_control
    compute the PLL control value to use for
    AR_RTC_PLL_CONTROL for a given channel

ani_control
    *undescribed*

do_getnf
    *undescribed*

set_radar_params
    *undescribed*

fast_chan_change
    *undescribed*

ani_cache_ini_regs
    cache the values for ANI from the initial
    register settings through the register initialization.

is_aic_enabled
    *undescribed*

.. _`ath_hw_private_ops.description`:

Description
-----------

This structure contains private callbacks designed to only be used internally
by the hardware core.

.. _`ath_spec_scan`:

struct ath_spec_scan
====================

.. c:type:: struct ath_spec_scan

    parameters for Atheros spectral scan

.. _`ath_spec_scan.definition`:

Definition
----------

.. code-block:: c

    struct ath_spec_scan {
        bool enabled;
        bool short_repeat;
        bool endless;
        u8 count;
        u8 period;
        u8 fft_period;
    }

.. _`ath_spec_scan.members`:

Members
-------

enabled
    enable/disable spectral scan

short_repeat
    controls whether the chip is in spectral scan mode
    for 4 usec (enabled) or 204 usec (disabled)

endless
    true if endless mode is intended. Otherwise, count value is
    corrected to the next possible value.

count
    number of scan results requested. There are special meanings
    in some chip revisions:
    AR92xx: highest bit set (>=128) for endless mode
    (spectral scan won't stopped until explicitly disabled)
    AR9300 and newer: 0 for endless mode

period
    time duration between successive spectral scan entry points
    (period\*256\*Tclk). Tclk = ath_common->clockrate

fft_period
    PHY passes FFT frames to MAC every (fft_period+1)\*4uS

.. _`ath_spec_scan.note`:

Note
----

Tclk = 40MHz or 44MHz depending upon operating mode.
Typically it's 44MHz in 2/5GHz on later chips, but there's
a "fast clock" check for this in 5GHz.

.. _`ath_hw_ops`:

struct ath_hw_ops
=================

.. c:type:: struct ath_hw_ops

    callbacks used by hardware code and driver code

.. _`ath_hw_ops.definition`:

Definition
----------

.. code-block:: c

    struct ath_hw_ops {
        void (*config_pci_powersave)(struct ath_hw *ah, bool power_off);
        void (*rx_enable)(struct ath_hw *ah);
        void (*set_desc_link)(void *ds, u32 link);
        int (*calibrate)(struct ath_hw *ah, struct ath9k_channel *chan, u8 rxchainmask, bool longcal);
        bool (*get_isr)(struct ath_hw *ah, enum ath9k_int *masked, u32 *sync_cause_p);
        void (*set_txdesc)(struct ath_hw *ah, void *ds, struct ath_tx_info *i);
        int (*proc_txdesc)(struct ath_hw *ah, void *ds, struct ath_tx_status *ts);
        int (*get_duration)(struct ath_hw *ah, const void *ds, int index);
        void (*antdiv_comb_conf_get)(struct ath_hw *ah, struct ath_hw_antcomb_conf *antconf);
        void (*antdiv_comb_conf_set)(struct ath_hw *ah, struct ath_hw_antcomb_conf *antconf);
        void (*spectral_scan_config)(struct ath_hw *ah, struct ath_spec_scan *param);
        void (*spectral_scan_trigger)(struct ath_hw *ah);
        void (*spectral_scan_wait)(struct ath_hw *ah);
        void (*tx99_start)(struct ath_hw *ah, u32 qnum);
        void (*tx99_stop)(struct ath_hw *ah);
        void (*tx99_set_txpower)(struct ath_hw *ah, u8 power);
    #ifdef CONFIG_ATH9K_BTCOEX_SUPPORT
        void (*set_bt_ant_diversity)(struct ath_hw *hw, bool enable);
    #endif
    }

.. _`ath_hw_ops.members`:

Members
-------

config_pci_powersave
    *undescribed*

rx_enable
    *undescribed*

set_desc_link
    *undescribed*

calibrate
    periodic calibration for NF, ANI, IQ, ADC gain, ADC-DC

get_isr
    *undescribed*

set_txdesc
    *undescribed*

proc_txdesc
    *undescribed*

get_duration
    *undescribed*

antdiv_comb_conf_get
    *undescribed*

antdiv_comb_conf_set
    *undescribed*

spectral_scan_config
    set parameters for spectral scan and enable/disable it

spectral_scan_trigger
    trigger a spectral scan run

spectral_scan_wait
    wait for a spectral scan run to finish

tx99_start
    *undescribed*

tx99_stop
    *undescribed*

tx99_set_txpower
    *undescribed*

set_bt_ant_diversity
    *undescribed*

.. _`ath_hw_ops.description`:

Description
-----------

This structure contains callbacks designed to to be used internally by
hardware code and also by the lower level driver.

.. This file was automatic generated / don't edit.

