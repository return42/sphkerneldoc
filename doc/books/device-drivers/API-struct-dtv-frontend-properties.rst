
.. _API-struct-dtv-frontend-properties:

==============================
struct dtv_frontend_properties
==============================

*man struct dtv_frontend_properties(9)*

*4.6.0-rc1*

contains a list of properties that are specific to a digital TV standard.


Synopsis
========

.. code-block:: c

    struct dtv_frontend_properties {
      u32 frequency;
      enum fe_modulation modulation;
      enum fe_sec_voltage voltage;
      enum fe_sec_tone_mode sectone;
      enum fe_spectral_inversion inversion;
      enum fe_code_rate fec_inner;
      enum fe_transmit_mode transmission_mode;
      u32 bandwidth_hz;
      enum fe_guard_interval guard_interval;
      enum fe_hierarchy hierarchy;
      u32 symbol_rate;
      enum fe_code_rate code_rate_HP;
      enum fe_code_rate code_rate_LP;
      enum fe_pilot pilot;
      enum fe_rolloff rolloff;
      enum fe_delivery_system delivery_system;
      enum fe_interleaving interleaving;
      u8 isdbt_partial_reception;
      u8 isdbt_sb_mode;
      u8 isdbt_sb_subchannel;
      u32 isdbt_sb_segment_idx;
      u32 isdbt_sb_segment_count;
      u8 isdbt_layer_enabled;
      struct layer[3];
      u32 stream_id;
      u8 atscmh_fic_ver;
      u8 atscmh_parade_id;
      u8 atscmh_nog;
      u8 atscmh_tnog;
      u8 atscmh_sgn;
      u8 atscmh_prc;
      u8 atscmh_rs_frame_mode;
      u8 atscmh_rs_frame_ensemble;
      u8 atscmh_rs_code_mode_pri;
      u8 atscmh_rs_code_mode_sec;
      u8 atscmh_sccc_block_mode;
      u8 atscmh_sccc_code_mode_a;
      u8 atscmh_sccc_code_mode_b;
      u8 atscmh_sccc_code_mode_c;
      u8 atscmh_sccc_code_mode_d;
      u32 lna;
      struct dtv_fe_stats strength;
      struct dtv_fe_stats cnr;
      struct dtv_fe_stats pre_bit_error;
      struct dtv_fe_stats pre_bit_count;
      struct dtv_fe_stats post_bit_error;
      struct dtv_fe_stats post_bit_count;
      struct dtv_fe_stats block_error;
      struct dtv_fe_stats block_count;
    };


Members
=======

frequency
    frequency in Hz for terrestrial/cable or in kHz for Satellite

modulation
    Frontend modulation type

voltage
    SEC voltage (only Satellite)

sectone
    SEC tone mode (only Satellite)

inversion
    Spectral inversion

fec_inner
    Forward error correction inner Code Rate

transmission_mode
    Transmission Mode

bandwidth_hz
    Bandwidth, in Hz. A zero value means that userspace wants to autodetect.

guard_interval
    Guard Interval

hierarchy
    Hierarchy

symbol_rate
    Symbol Rate

code_rate_HP
    high priority stream code rate

code_rate_LP
    low priority stream code rate

pilot
    Enable/disable/autodetect pilot tones

rolloff
    Rolloff factor (alpha)

delivery_system
    FE delivery system (e. g. digital TV standard)

interleaving
    interleaving

isdbt_partial_reception
    ISDB-T partial reception (only ISDB standard)

isdbt_sb_mode
    ISDB-T Sound Broadcast (SB) mode (only ISDB standard)

isdbt_sb_subchannel
    ISDB-T SB subchannel (only ISDB standard)

isdbt_sb_segment_idx
    ISDB-T SB segment index (only ISDB standard)

isdbt_sb_segment_count
    ISDB-T SB segment count (only ISDB standard)

isdbt_layer_enabled
    ISDB Layer enabled (only ISDB standard)

layer[3]
    ISDB per-layer data (only ISDB standard) ``layer``.segment_count: Segment Count; ``layer``.fec: per layer code rate; ``layer``.modulation: per layer modulation;
    ``layer``.interleaving: per layer interleaving.

stream_id
    If different than zero, enable substream filtering, if hardware supports (DVB-S2 and DVB-T2).

atscmh_fic_ver
    Version number of the FIC (Fast Information Channel) signaling data (only ATSC-M/H)

atscmh_parade_id
    Parade identification number (only ATSC-M/H)

atscmh_nog
    Number of MH groups per MH subframe for a designated parade (only ATSC-M/H)

atscmh_tnog
    Total number of MH groups including all MH groups belonging to all MH parades in one MH subframe (only ATSC-M/H)

atscmh_sgn
    Start group number (only ATSC-M/H)

atscmh_prc
    Parade repetition cycle (only ATSC-M/H)

atscmh_rs_frame_mode
    Reed Solomon (RS) frame mode (only ATSC-M/H)

atscmh_rs_frame_ensemble
    RS frame ensemble (only ATSC-M/H)

atscmh_rs_code_mode_pri
    RS code mode pri (only ATSC-M/H)

atscmh_rs_code_mode_sec
    RS code mode sec (only ATSC-M/H)

atscmh_sccc_block_mode
    Series Concatenated Convolutional Code (SCCC) Block Mode (only ATSC-M/H)

atscmh_sccc_code_mode_a
    SCCC code mode A (only ATSC-M/H)

atscmh_sccc_code_mode_b
    SCCC code mode B (only ATSC-M/H)

atscmh_sccc_code_mode_c
    SCCC code mode C (only ATSC-M/H)

atscmh_sccc_code_mode_d
    SCCC code mode D (only ATSC-M/H)

lna
    Power ON/OFF/AUTO the Linear Now-noise Amplifier (LNA)

strength
    DVBv5 API statistics: Signal Strength

cnr
    DVBv5 API statistics: Signal to Noise ratio of the (main) carrier

pre_bit_error
    DVBv5 API statistics: pre-Viterbi bit error count

pre_bit_count
    DVBv5 API statistics: pre-Viterbi bit count

post_bit_error
    DVBv5 API statistics: post-Viterbi bit error count

post_bit_count
    DVBv5 API statistics: post-Viterbi bit count

block_error
    DVBv5 API statistics: block error count

block_count
    DVBv5 API statistics: block count


NOTE
====

derivated statistics like Uncorrected Error blocks (UCE) are calculated on userspace.

Only a subset of the properties are needed for a given delivery system. For more info, consult the media_api.html with the documentation of the Userspace API.
