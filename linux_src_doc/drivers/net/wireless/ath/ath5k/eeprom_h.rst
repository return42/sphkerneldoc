.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/eeprom.h

.. _`ath5k_eeprom_info`:

struct ath5k_eeprom_info
========================

.. c:type:: struct ath5k_eeprom_info

    EEPROM calibration data

.. _`ath5k_eeprom_info.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_eeprom_info {
        u16 ee_magic;
        u16 ee_protect;
        u16 ee_regdomain;
        u16 ee_version;
        u16 ee_header;
        u16 ee_ant_gain;
        u8 ee_rfkill_pin;
        bool ee_rfkill_pol;
        bool ee_is_hb63;
        bool ee_serdes;
        u16 ee_misc0;
        u16 ee_misc1;
        u16 ee_misc2;
        u16 ee_misc3;
        u16 ee_misc4;
        u16 ee_misc5;
        u16 ee_misc6;
        u16 ee_cck_ofdm_gain_delta;
        u16 ee_cck_ofdm_power_delta;
        u16 ee_scaled_cck_delta;
        u16 ee_i_cal;
        u16 ee_q_cal;
        u16 ee_fixed_bias;
        u16 ee_turbo_max_power;
        u16 ee_xr_power;
        u16 ee_switch_settling;
        u16 ee_atn_tx_rx;
        u16 ee_ant_control;
        u16 ee_ob;
        u16 ee_db;
        u16 ee_tx_end2xlna_enable;
        u16 ee_tx_end2xpa_disable;
        u16 ee_tx_frm2xpa_enable;
        u16 ee_thr_62;
        u16 ee_xlna_gain;
        u16 ee_xpd;
        u16 ee_x_gain;
        u16 ee_i_gain;
        u16 ee_margin_tx_rx;
        u16 ee_switch_settling_turbo;
        u16 ee_margin_tx_rx_turbo;
        u16 ee_atn_tx_rx_turbo;
        u16 ee_false_detect;
        u8 ee_pd_gains;
        u8 ee_pdc_to_idx;
        u8 ee_n_piers;
        struct ath5k_chan_pcal_info ee_pwr_cal_a;
        struct ath5k_chan_pcal_info ee_pwr_cal_b;
        struct ath5k_chan_pcal_info ee_pwr_cal_g;
        u8 ee_rate_target_pwr_num;
        struct ath5k_rate_pcal_info ee_rate_tpwr_a;
        struct ath5k_rate_pcal_info ee_rate_tpwr_b;
        struct ath5k_rate_pcal_info ee_rate_tpwr_g;
        u8 ee_ctls;
        u8 ee_ctl;
        struct ath5k_edge_power ee_ctl_pwr;
        s16 ee_noise_floor_thr;
        s8 ee_adc_desired_size;
        s8 ee_pga_desired_size;
        s8 ee_adc_desired_size_turbo;
        s8 ee_pga_desired_size_turbo;
        s8 ee_pd_gain_overlap;
        u16 ee_spur_chans;
        u32 ee_antenna;
    }

.. _`ath5k_eeprom_info.members`:

Members
-------

ee_magic
    *undescribed*

ee_protect
    *undescribed*

ee_regdomain
    ath/regd.c takes care of COUNTRY_ERD and WORLDWIDE_ROAMING
    flags

ee_version
    *undescribed*

ee_header
    *undescribed*

ee_ant_gain
    Antenna gain in 0.5dB steps signed [5211 only?]

ee_rfkill_pin
    *undescribed*

ee_rfkill_pol
    *undescribed*

ee_is_hb63
    *undescribed*

ee_serdes
    *undescribed*

ee_misc0
    *undescribed*

ee_misc1
    *undescribed*

ee_misc2
    *undescribed*

ee_misc3
    *undescribed*

ee_misc4
    *undescribed*

ee_misc5
    *undescribed*

ee_misc6
    *undescribed*

ee_cck_ofdm_gain_delta
    difference in gainF to output the same power for
    OFDM and CCK packets

ee_cck_ofdm_power_delta
    power difference between OFDM (6Mbps) and CCK
    (11Mbps) rate in G mode. 0.1dB steps

ee_scaled_cck_delta
    for Japan Channel 14: 0.1dB resolution

ee_i_cal
    Initial I coefficient to correct I/Q mismatch in the receive path

ee_q_cal
    Initial Q coefficient to correct I/Q mismatch in the receive path

ee_fixed_bias
    use ee_ob and ee_db settings or use automatic control

ee_turbo_max_power
    *undescribed*

ee_xr_power
    *undescribed*

ee_switch_settling
    RX/TX Switch settling time

ee_atn_tx_rx
    Difference in attenuation between TX and RX in 1dB steps

ee_ant_control
    Antenna Control Settings

ee_ob
    Bias current for Output stage of PA
    B/G mode: Index [0] is used for AR2112/5112, otherwise [1]

ee_db
    Bias current for Output stage of PA. see \ ``ee_ob``\ 

ee_tx_end2xlna_enable
    Time difference from when BB finishes sending a frame
    to when the external LNA is activated

ee_tx_end2xpa_disable
    Time difference from when BB finishes sending a frame
    to when the external PA switch is deactivated

ee_tx_frm2xpa_enable
    Time difference from when MAC sends frame to when
    external PA switch is activated

ee_thr_62
    Clear Channel Assessment (CCA) sensitivity
    (IEEE802.11a section 17.3.10.5 )

ee_xlna_gain
    Total gain of the LNA (information only)

ee_xpd
    Use external (1) or internal power detector

ee_x_gain
    Gain for external power detector output (differences in EEMAP
    versions!)

ee_i_gain
    Initial gain value after reset

ee_margin_tx_rx
    Margin in dB when final attenuation stage should be used

ee_switch_settling_turbo
    *undescribed*

ee_margin_tx_rx_turbo
    *undescribed*

ee_atn_tx_rx_turbo
    *undescribed*

ee_false_detect
    Backoff in Sensitivity (dB) on channels with spur signals

ee_pd_gains
    *undescribed*

ee_pdc_to_idx
    *undescribed*

ee_n_piers
    *undescribed*

ee_pwr_cal_a
    *undescribed*

ee_pwr_cal_b
    *undescribed*

ee_pwr_cal_g
    *undescribed*

ee_rate_target_pwr_num
    *undescribed*

ee_rate_tpwr_a
    *undescribed*

ee_rate_tpwr_b
    *undescribed*

ee_rate_tpwr_g
    *undescribed*

ee_ctls
    *undescribed*

ee_ctl
    *undescribed*

ee_ctl_pwr
    *undescribed*

ee_noise_floor_thr
    Noise floor threshold in 1dB steps

ee_adc_desired_size
    Desired amplitude for ADC, used by AGC; in 0.5 dB steps

ee_pga_desired_size
    Desired output of PGA (for BB gain) in 0.5 dB steps

ee_adc_desired_size_turbo
    *undescribed*

ee_pga_desired_size_turbo
    *undescribed*

ee_pd_gain_overlap
    PD ADC curves need to overlap in 0.5dB steps (ee_map>=2)

ee_spur_chans
    *undescribed*

ee_antenna
    *undescribed*

.. _`ath5k_eeprom_info.a-mode`:

A mode
------

[0] 5.15-5.25 [1] 5.25-5.50 [2] 5.50-5.70 [3] 5.70-5.85 GHz

.. This file was automatic generated / don't edit.

