.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/dvb/frontend.h

.. _`fe_caps`:

enum fe_caps
============

.. c:type:: enum fe_caps

    Frontend capabilities

.. _`fe_caps.definition`:

Definition
----------

.. code-block:: c

    enum fe_caps {
        FE_IS_STUPID,
        FE_CAN_INVERSION_AUTO,
        FE_CAN_FEC_1_2,
        FE_CAN_FEC_2_3,
        FE_CAN_FEC_3_4,
        FE_CAN_FEC_4_5,
        FE_CAN_FEC_5_6,
        FE_CAN_FEC_6_7,
        FE_CAN_FEC_7_8,
        FE_CAN_FEC_8_9,
        FE_CAN_FEC_AUTO,
        FE_CAN_QPSK,
        FE_CAN_QAM_16,
        FE_CAN_QAM_32,
        FE_CAN_QAM_64,
        FE_CAN_QAM_128,
        FE_CAN_QAM_256,
        FE_CAN_QAM_AUTO,
        FE_CAN_TRANSMISSION_MODE_AUTO,
        FE_CAN_BANDWIDTH_AUTO,
        FE_CAN_GUARD_INTERVAL_AUTO,
        FE_CAN_HIERARCHY_AUTO,
        FE_CAN_8VSB,
        FE_CAN_16VSB,
        FE_HAS_EXTENDED_CAPS,
        FE_CAN_MULTISTREAM,
        FE_CAN_TURBO_FEC,
        FE_CAN_2G_MODULATION,
        FE_NEEDS_BENDING,
        FE_CAN_RECOVER,
        FE_CAN_MUTE_TS
    };

.. _`fe_caps.constants`:

Constants
---------

FE_IS_STUPID
    There's something wrong at the
    frontend, and it can't report its
    capabilities.

FE_CAN_INVERSION_AUTO
    Can auto-detect frequency spectral
    band inversion

FE_CAN_FEC_1_2
    Supports FEC 1/2

FE_CAN_FEC_2_3
    Supports FEC 2/3

FE_CAN_FEC_3_4
    Supports FEC 3/4

FE_CAN_FEC_4_5
    Supports FEC 4/5

FE_CAN_FEC_5_6
    Supports FEC 5/6

FE_CAN_FEC_6_7
    Supports FEC 6/7

FE_CAN_FEC_7_8
    Supports FEC 7/8

FE_CAN_FEC_8_9
    Supports FEC 8/9

FE_CAN_FEC_AUTO
    Can auto-detect FEC

FE_CAN_QPSK
    Supports QPSK modulation

FE_CAN_QAM_16
    Supports 16-QAM modulation

FE_CAN_QAM_32
    Supports 32-QAM modulation

FE_CAN_QAM_64
    Supports 64-QAM modulation

FE_CAN_QAM_128
    Supports 128-QAM modulation

FE_CAN_QAM_256
    Supports 256-QAM modulation

FE_CAN_QAM_AUTO
    Can auto-detect QAM modulation

FE_CAN_TRANSMISSION_MODE_AUTO
    Can auto-detect transmission mode

FE_CAN_BANDWIDTH_AUTO
    Can auto-detect bandwidth

FE_CAN_GUARD_INTERVAL_AUTO
    Can auto-detect guard interval

FE_CAN_HIERARCHY_AUTO
    Can auto-detect hierarchy

FE_CAN_8VSB
    Supports 8-VSB modulation

FE_CAN_16VSB
    Supporta 16-VSB modulation

FE_HAS_EXTENDED_CAPS
    Unused

FE_CAN_MULTISTREAM
    Supports multistream filtering

FE_CAN_TURBO_FEC
    Supports "turbo FEC" modulation

FE_CAN_2G_MODULATION
    Supports "2nd generation" modulation,
    e. g. DVB-S2, DVB-T2, DVB-C2

FE_NEEDS_BENDING
    Unused

FE_CAN_RECOVER
    Can recover from a cable unplug
    automatically

FE_CAN_MUTE_TS
    Can stop spurious TS data output

.. _`dvb_frontend_info`:

struct dvb_frontend_info
========================

.. c:type:: struct dvb_frontend_info

    Frontend properties and capabilities

.. _`dvb_frontend_info.definition`:

Definition
----------

.. code-block:: c

    struct dvb_frontend_info {
        char name[128];
        enum fe_type type;
        __u32 frequency_min;
        __u32 frequency_max;
        __u32 frequency_stepsize;
        __u32 frequency_tolerance;
        __u32 symbol_rate_min;
        __u32 symbol_rate_max;
        __u32 symbol_rate_tolerance;
        __u32 notifier_delay;
        enum fe_caps caps;
    }

.. _`dvb_frontend_info.members`:

Members
-------

name
    Name of the frontend

type
    **DEPRECATED**.
    Should not be used on modern programs,
    as a frontend may have more than one type.
    In order to get the support types of a given
    frontend, use :c:type:`DTV_ENUM_DELSYS`
    instead.

frequency_min
    Minimal frequency supported by the frontend.

frequency_max
    Minimal frequency supported by the frontend.

frequency_stepsize
    All frequencies are multiple of this value.

frequency_tolerance
    Frequency tolerance.

symbol_rate_min
    Minimal symbol rate, in bauds
    (for Cable/Satellite systems).

symbol_rate_max
    Maximal symbol rate, in bauds
    (for Cable/Satellite systems).

symbol_rate_tolerance
    Maximal symbol rate tolerance, in ppm
    (for Cable/Satellite systems).

notifier_delay
    **DEPRECATED**. Not used by any driver.

caps
    Capabilities supported by the frontend,
    as specified in \ :c:type:`enum fe_caps <fe_caps>`\ .

.. _`dvb_frontend_info.description`:

Description
-----------

.. note:

   #. The frequencies are specified in Hz for Terrestrial and Cable
      systems.
   #. The frequencies are specified in kHz for Satellite systems.

.. _`dvb_diseqc_master_cmd`:

struct dvb_diseqc_master_cmd
============================

.. c:type:: struct dvb_diseqc_master_cmd

    DiSEqC master command

.. _`dvb_diseqc_master_cmd.definition`:

Definition
----------

.. code-block:: c

    struct dvb_diseqc_master_cmd {
        __u8 msg[6];
        __u8 msg_len;
    }

.. _`dvb_diseqc_master_cmd.members`:

Members
-------

msg
    DiSEqC message to be sent. It contains a 3 bytes header with:
    framing + address + command, and an optional argument
    of up to 3 bytes of data.

msg_len
    Length of the DiSEqC message. Valid values are 3 to 6.

.. _`dvb_diseqc_master_cmd.description`:

Description
-----------

Check out the DiSEqC bus spec available on http://www.eutelsat.org/ for
the possible messages that can be used.

.. _`dvb_diseqc_slave_reply`:

struct dvb_diseqc_slave_reply
=============================

.. c:type:: struct dvb_diseqc_slave_reply

    DiSEqC received data

.. _`dvb_diseqc_slave_reply.definition`:

Definition
----------

.. code-block:: c

    struct dvb_diseqc_slave_reply {
        __u8 msg[4];
        __u8 msg_len;
        int timeout;
    }

.. _`dvb_diseqc_slave_reply.members`:

Members
-------

msg
    DiSEqC message buffer to store a message received via DiSEqC.
    It contains one byte header with: framing and
    an optional argument of up to 3 bytes of data.

msg_len
    Length of the DiSEqC message. Valid values are 0 to 4,
    where 0 means no message.

timeout
    Return from ioctl after timeout ms with errorcode when
    no message was received.

.. _`dvb_diseqc_slave_reply.description`:

Description
-----------

Check out the DiSEqC bus spec available on http://www.eutelsat.org/ for
the possible messages that can be used.

.. _`fe_sec_voltage`:

enum fe_sec_voltage
===================

.. c:type:: enum fe_sec_voltage

    DC Voltage used to feed the LNBf

.. _`fe_sec_voltage.definition`:

Definition
----------

.. code-block:: c

    enum fe_sec_voltage {
        SEC_VOLTAGE_13,
        SEC_VOLTAGE_18,
        SEC_VOLTAGE_OFF
    };

.. _`fe_sec_voltage.constants`:

Constants
---------

SEC_VOLTAGE_13
    Output 13V to the LNBf

SEC_VOLTAGE_18
    Output 18V to the LNBf

SEC_VOLTAGE_OFF
    Don't feed the LNBf with a DC voltage

.. _`fe_sec_tone_mode`:

enum fe_sec_tone_mode
=====================

.. c:type:: enum fe_sec_tone_mode

    Type of tone to be send to the LNBf.

.. _`fe_sec_tone_mode.definition`:

Definition
----------

.. code-block:: c

    enum fe_sec_tone_mode {
        SEC_TONE_ON,
        SEC_TONE_OFF
    };

.. _`fe_sec_tone_mode.constants`:

Constants
---------

SEC_TONE_ON
    Sends a 22kHz tone burst to the antenna.

SEC_TONE_OFF
    Don't send a 22kHz tone to the antenna (except
    if the ``FE_DISEQC_*`` ioctls are called).

.. _`fe_sec_mini_cmd`:

enum fe_sec_mini_cmd
====================

.. c:type:: enum fe_sec_mini_cmd

    Type of mini burst to be sent

.. _`fe_sec_mini_cmd.definition`:

Definition
----------

.. code-block:: c

    enum fe_sec_mini_cmd {
        SEC_MINI_A,
        SEC_MINI_B
    };

.. _`fe_sec_mini_cmd.constants`:

Constants
---------

SEC_MINI_A
    Sends a mini-DiSEqC 22kHz '0' Tone Burst to select
    satellite-A

SEC_MINI_B
    Sends a mini-DiSEqC 22kHz '1' Data Burst to select
    satellite-B

.. _`fe_status`:

enum fe_status
==============

.. c:type:: enum fe_status

    Enumerates the possible frontend status.

.. _`fe_status.definition`:

Definition
----------

.. code-block:: c

    enum fe_status {
        FE_NONE,
        FE_HAS_SIGNAL,
        FE_HAS_CARRIER,
        FE_HAS_VITERBI,
        FE_HAS_SYNC,
        FE_HAS_LOCK,
        FE_TIMEDOUT,
        FE_REINIT
    };

.. _`fe_status.constants`:

Constants
---------

FE_NONE
    The frontend doesn't have any kind of lock.
    That's the initial frontend status

FE_HAS_SIGNAL
    Has found something above the noise level.

FE_HAS_CARRIER
    Has found a signal.

FE_HAS_VITERBI
    FEC inner coding (Viterbi, LDPC or other inner code).
    is stable.

FE_HAS_SYNC
    Synchronization bytes was found.

FE_HAS_LOCK
    Digital TV were locked and everything is working.

FE_TIMEDOUT
    Fo lock within the last about 2 seconds.

FE_REINIT
    Frontend was reinitialized, application is recommended
    to reset DiSEqC, tone and parameters.

.. _`fe_spectral_inversion`:

enum fe_spectral_inversion
==========================

.. c:type:: enum fe_spectral_inversion

    Type of inversion band

.. _`fe_spectral_inversion.definition`:

Definition
----------

.. code-block:: c

    enum fe_spectral_inversion {
        INVERSION_OFF,
        INVERSION_ON,
        INVERSION_AUTO
    };

.. _`fe_spectral_inversion.constants`:

Constants
---------

INVERSION_OFF
    Don't do spectral band inversion.

INVERSION_ON
    Do spectral band inversion.

INVERSION_AUTO
    Autodetect spectral band inversion.

.. _`fe_spectral_inversion.description`:

Description
-----------

This parameter indicates if spectral inversion should be presumed or
not. In the automatic setting (``INVERSION_AUTO``) the hardware will try
to figure out the correct setting by itself. If the hardware doesn't
support, the \ ``dvb_frontend``\  will try to lock at the carrier first with
inversion off. If it fails, it will try to enable inversion.

.. _`fe_code_rate`:

enum fe_code_rate
=================

.. c:type:: enum fe_code_rate

    Type of Forward Error Correction (FEC)

.. _`fe_code_rate.definition`:

Definition
----------

.. code-block:: c

    enum fe_code_rate {
        FEC_NONE,
        FEC_1_2,
        FEC_2_3,
        FEC_3_4,
        FEC_4_5,
        FEC_5_6,
        FEC_6_7,
        FEC_7_8,
        FEC_8_9,
        FEC_AUTO,
        FEC_3_5,
        FEC_9_10,
        FEC_2_5
    };

.. _`fe_code_rate.constants`:

Constants
---------

FEC_NONE
    No Forward Error Correction Code

FEC_1_2
    Forward Error Correction Code 1/2

FEC_2_3
    Forward Error Correction Code 2/3

FEC_3_4
    Forward Error Correction Code 3/4

FEC_4_5
    Forward Error Correction Code 4/5

FEC_5_6
    Forward Error Correction Code 5/6

FEC_6_7
    Forward Error Correction Code 6/7

FEC_7_8
    Forward Error Correction Code 7/8

FEC_8_9
    Forward Error Correction Code 8/9

FEC_AUTO
    Autodetect Error Correction Code

FEC_3_5
    Forward Error Correction Code 3/5

FEC_9_10
    Forward Error Correction Code 9/10

FEC_2_5
    Forward Error Correction Code 2/5

.. _`fe_code_rate.description`:

Description
-----------

Please note that not all FEC types are supported by a given standard.

.. _`fe_modulation`:

enum fe_modulation
==================

.. c:type:: enum fe_modulation

    Type of modulation/constellation

.. _`fe_modulation.definition`:

Definition
----------

.. code-block:: c

    enum fe_modulation {
        QPSK,
        QAM_16,
        QAM_32,
        QAM_64,
        QAM_128,
        QAM_256,
        QAM_AUTO,
        VSB_8,
        VSB_16,
        PSK_8,
        APSK_16,
        APSK_32,
        DQPSK,
        QAM_4_NR
    };

.. _`fe_modulation.constants`:

Constants
---------

QPSK
    QPSK modulation

QAM_16
    16-QAM modulation

QAM_32
    32-QAM modulation

QAM_64
    64-QAM modulation

QAM_128
    128-QAM modulation

QAM_256
    256-QAM modulation

QAM_AUTO
    Autodetect QAM modulation

VSB_8
    8-VSB modulation

VSB_16
    16-VSB modulation

PSK_8
    8-PSK modulation

APSK_16
    16-APSK modulation

APSK_32
    32-APSK modulation

DQPSK
    DQPSK modulation

QAM_4_NR
    4-QAM-NR modulation

.. _`fe_modulation.description`:

Description
-----------

Please note that not all modulations are supported by a given standard.

.. _`fe_transmit_mode`:

enum fe_transmit_mode
=====================

.. c:type:: enum fe_transmit_mode

    Transmission mode

.. _`fe_transmit_mode.definition`:

Definition
----------

.. code-block:: c

    enum fe_transmit_mode {
        TRANSMISSION_MODE_2K,
        TRANSMISSION_MODE_8K,
        TRANSMISSION_MODE_AUTO,
        TRANSMISSION_MODE_4K,
        TRANSMISSION_MODE_1K,
        TRANSMISSION_MODE_16K,
        TRANSMISSION_MODE_32K,
        TRANSMISSION_MODE_C1,
        TRANSMISSION_MODE_C3780
    };

.. _`fe_transmit_mode.constants`:

Constants
---------

TRANSMISSION_MODE_2K
    Transmission mode 2K

TRANSMISSION_MODE_8K
    Transmission mode 8K

TRANSMISSION_MODE_AUTO
    Autodetect transmission mode. The hardware will try to find the
    correct FFT-size (if capable) to fill in the missing parameters.

TRANSMISSION_MODE_4K
    Transmission mode 4K

TRANSMISSION_MODE_1K
    Transmission mode 1K

TRANSMISSION_MODE_16K
    Transmission mode 16K

TRANSMISSION_MODE_32K
    Transmission mode 32K

TRANSMISSION_MODE_C1
    Single Carrier (C=1) transmission mode (DTMB only)

TRANSMISSION_MODE_C3780
    Multi Carrier (C=3780) transmission mode (DTMB only)

.. _`fe_transmit_mode.description`:

Description
-----------

Please note that not all transmission modes are supported by a given
standard.

.. _`fe_guard_interval`:

enum fe_guard_interval
======================

.. c:type:: enum fe_guard_interval

    Guard interval

.. _`fe_guard_interval.definition`:

Definition
----------

.. code-block:: c

    enum fe_guard_interval {
        GUARD_INTERVAL_1_32,
        GUARD_INTERVAL_1_16,
        GUARD_INTERVAL_1_8,
        GUARD_INTERVAL_1_4,
        GUARD_INTERVAL_AUTO,
        GUARD_INTERVAL_1_128,
        GUARD_INTERVAL_19_128,
        GUARD_INTERVAL_19_256,
        GUARD_INTERVAL_PN420,
        GUARD_INTERVAL_PN595,
        GUARD_INTERVAL_PN945
    };

.. _`fe_guard_interval.constants`:

Constants
---------

GUARD_INTERVAL_1_32
    Guard interval 1/32

GUARD_INTERVAL_1_16
    Guard interval 1/16

GUARD_INTERVAL_1_8
    Guard interval 1/8

GUARD_INTERVAL_1_4
    Guard interval 1/4

GUARD_INTERVAL_AUTO
    Autodetect the guard interval

GUARD_INTERVAL_1_128
    Guard interval 1/128

GUARD_INTERVAL_19_128
    Guard interval 19/128

GUARD_INTERVAL_19_256
    Guard interval 19/256

GUARD_INTERVAL_PN420
    PN length 420 (1/4)

GUARD_INTERVAL_PN595
    PN length 595 (1/6)

GUARD_INTERVAL_PN945
    PN length 945 (1/9)

.. _`fe_guard_interval.description`:

Description
-----------

Please note that not all guard intervals are supported by a given standard.

.. _`fe_hierarchy`:

enum fe_hierarchy
=================

.. c:type:: enum fe_hierarchy

    Hierarchy

.. _`fe_hierarchy.definition`:

Definition
----------

.. code-block:: c

    enum fe_hierarchy {
        HIERARCHY_NONE,
        HIERARCHY_1,
        HIERARCHY_2,
        HIERARCHY_4,
        HIERARCHY_AUTO
    };

.. _`fe_hierarchy.constants`:

Constants
---------

HIERARCHY_NONE
    No hierarchy

HIERARCHY_1
    Hierarchy 1

HIERARCHY_2
    Hierarchy 2

HIERARCHY_4
    Hierarchy 4

HIERARCHY_AUTO
    Autodetect hierarchy (if supported)

.. _`fe_hierarchy.description`:

Description
-----------

Please note that not all hierarchy types are supported by a given standard.

.. _`fe_interleaving`:

enum fe_interleaving
====================

.. c:type:: enum fe_interleaving

    Interleaving

.. _`fe_interleaving.definition`:

Definition
----------

.. code-block:: c

    enum fe_interleaving {
        INTERLEAVING_NONE,
        INTERLEAVING_AUTO,
        INTERLEAVING_240,
        INTERLEAVING_720
    };

.. _`fe_interleaving.constants`:

Constants
---------

INTERLEAVING_NONE
    No interleaving.

INTERLEAVING_AUTO
    Auto-detect interleaving.

INTERLEAVING_240
    Interleaving of 240 symbols.

INTERLEAVING_720
    Interleaving of 720 symbols.

.. _`fe_interleaving.description`:

Description
-----------

Please note that, currently, only DTMB uses it.

.. _`fe_pilot`:

enum fe_pilot
=============

.. c:type:: enum fe_pilot

    Type of pilot tone

.. _`fe_pilot.definition`:

Definition
----------

.. code-block:: c

    enum fe_pilot {
        PILOT_ON,
        PILOT_OFF,
        PILOT_AUTO
    };

.. _`fe_pilot.constants`:

Constants
---------

PILOT_ON
    Pilot tones enabled

PILOT_OFF
    Pilot tones disabled

PILOT_AUTO
    Autodetect pilot tones

.. _`fe_rolloff`:

enum fe_rolloff
===============

.. c:type:: enum fe_rolloff

    Rolloff factor

.. _`fe_rolloff.definition`:

Definition
----------

.. code-block:: c

    enum fe_rolloff {
        ROLLOFF_35,
        ROLLOFF_20,
        ROLLOFF_25,
        ROLLOFF_AUTO
    };

.. _`fe_rolloff.constants`:

Constants
---------

ROLLOFF_35
    Roloff factor: α=35%

ROLLOFF_20
    Roloff factor: α=20%

ROLLOFF_25
    Roloff factor: α=25%

ROLLOFF_AUTO
    Auto-detect the roloff factor.

.. _`fe_rolloff.description`:

Description
-----------

.. note:

   Roloff factor of 35% is implied on DVB-S. On DVB-S2, it is default.

.. _`fe_delivery_system`:

enum fe_delivery_system
=======================

.. c:type:: enum fe_delivery_system

    Type of the delivery system

.. _`fe_delivery_system.definition`:

Definition
----------

.. code-block:: c

    enum fe_delivery_system {
        SYS_UNDEFINED,
        SYS_DVBC_ANNEX_A,
        SYS_DVBC_ANNEX_B,
        SYS_DVBT,
        SYS_DSS,
        SYS_DVBS,
        SYS_DVBS2,
        SYS_DVBH,
        SYS_ISDBT,
        SYS_ISDBS,
        SYS_ISDBC,
        SYS_ATSC,
        SYS_ATSCMH,
        SYS_DTMB,
        SYS_CMMB,
        SYS_DAB,
        SYS_DVBT2,
        SYS_TURBO,
        SYS_DVBC_ANNEX_C
    };

.. _`fe_delivery_system.constants`:

Constants
---------

SYS_UNDEFINED
    Undefined standard. Generally, indicates an error

SYS_DVBC_ANNEX_A
    Cable TV: DVB-C following ITU-T J.83 Annex A spec

SYS_DVBC_ANNEX_B
    Cable TV: DVB-C following ITU-T J.83 Annex B spec (ClearQAM)

SYS_DVBT
    Terrestrial TV: DVB-T

SYS_DSS
    Satellite TV: DSS (not fully supported)

SYS_DVBS
    Satellite TV: DVB-S

SYS_DVBS2
    Satellite TV: DVB-S2

SYS_DVBH
    Terrestrial TV (mobile): DVB-H (standard deprecated)

SYS_ISDBT
    Terrestrial TV: ISDB-T

SYS_ISDBS
    Satellite TV: ISDB-S

SYS_ISDBC
    Cable TV: ISDB-C (no drivers yet)

SYS_ATSC
    Terrestrial TV: ATSC

SYS_ATSCMH
    Terrestrial TV (mobile): ATSC-M/H

SYS_DTMB
    Terrestrial TV: DTMB

SYS_CMMB
    Terrestrial TV (mobile): CMMB (not fully supported)

SYS_DAB
    Digital audio: DAB (not fully supported)

SYS_DVBT2
    Terrestrial TV: DVB-T2

SYS_TURBO
    Satellite TV: DVB-S Turbo

SYS_DVBC_ANNEX_C
    Cable TV: DVB-C following ITU-T J.83 Annex C spec

.. _`atscmh_sccc_block_mode`:

enum atscmh_sccc_block_mode
===========================

.. c:type:: enum atscmh_sccc_block_mode

    Type of Series Concatenated Convolutional Code Block Mode.

.. _`atscmh_sccc_block_mode.definition`:

Definition
----------

.. code-block:: c

    enum atscmh_sccc_block_mode {
        ATSCMH_SCCC_BLK_SEP,
        ATSCMH_SCCC_BLK_COMB,
        ATSCMH_SCCC_BLK_RES
    };

.. _`atscmh_sccc_block_mode.constants`:

Constants
---------

ATSCMH_SCCC_BLK_SEP
    Separate SCCC: the SCCC outer code mode shall be set independently
    for each Group Region (A, B, C, D)

ATSCMH_SCCC_BLK_COMB
    Combined SCCC: all four Regions shall have the same SCCC outer
    code mode.

ATSCMH_SCCC_BLK_RES
    Reserved. Shouldn't be used.

.. _`atscmh_sccc_code_mode`:

enum atscmh_sccc_code_mode
==========================

.. c:type:: enum atscmh_sccc_code_mode

    Type of Series Concatenated Convolutional Code Rate.

.. _`atscmh_sccc_code_mode.definition`:

Definition
----------

.. code-block:: c

    enum atscmh_sccc_code_mode {
        ATSCMH_SCCC_CODE_HLF,
        ATSCMH_SCCC_CODE_QTR,
        ATSCMH_SCCC_CODE_RES
    };

.. _`atscmh_sccc_code_mode.constants`:

Constants
---------

ATSCMH_SCCC_CODE_HLF
    The outer code rate of a SCCC Block is 1/2 rate.

ATSCMH_SCCC_CODE_QTR
    The outer code rate of a SCCC Block is 1/4 rate.

ATSCMH_SCCC_CODE_RES
    Reserved. Should not be used.

.. _`atscmh_rs_frame_ensemble`:

enum atscmh_rs_frame_ensemble
=============================

.. c:type:: enum atscmh_rs_frame_ensemble

    Reed Solomon(RS) frame ensemble.

.. _`atscmh_rs_frame_ensemble.definition`:

Definition
----------

.. code-block:: c

    enum atscmh_rs_frame_ensemble {
        ATSCMH_RSFRAME_ENS_PRI,
        ATSCMH_RSFRAME_ENS_SEC
    };

.. _`atscmh_rs_frame_ensemble.constants`:

Constants
---------

ATSCMH_RSFRAME_ENS_PRI
    Primary Ensemble.

ATSCMH_RSFRAME_ENS_SEC
    Secondary Ensemble.

.. _`atscmh_rs_frame_mode`:

enum atscmh_rs_frame_mode
=========================

.. c:type:: enum atscmh_rs_frame_mode

    Reed Solomon (RS) frame mode.

.. _`atscmh_rs_frame_mode.definition`:

Definition
----------

.. code-block:: c

    enum atscmh_rs_frame_mode {
        ATSCMH_RSFRAME_PRI_ONLY,
        ATSCMH_RSFRAME_PRI_SEC,
        ATSCMH_RSFRAME_RES
    };

.. _`atscmh_rs_frame_mode.constants`:

Constants
---------

ATSCMH_RSFRAME_PRI_ONLY
    Single Frame: There is only a primary RS Frame for all Group
    Regions.

ATSCMH_RSFRAME_PRI_SEC
    Dual Frame: There are two separate RS Frames: Primary RS Frame for
    Group Region A and B and Secondary RS Frame for Group Region C and
    D.

ATSCMH_RSFRAME_RES
    Reserved. Shouldn't be used.

.. _`atscmh_rs_code_mode`:

enum atscmh_rs_code_mode
========================

.. c:type:: enum atscmh_rs_code_mode


.. _`atscmh_rs_code_mode.definition`:

Definition
----------

.. code-block:: c

    enum atscmh_rs_code_mode {
        ATSCMH_RSCODE_211_187,
        ATSCMH_RSCODE_223_187,
        ATSCMH_RSCODE_235_187,
        ATSCMH_RSCODE_RES
    };

.. _`atscmh_rs_code_mode.constants`:

Constants
---------

ATSCMH_RSCODE_211_187
    Reed Solomon code (211,187).

ATSCMH_RSCODE_223_187
    Reed Solomon code (223,187).

ATSCMH_RSCODE_235_187
    Reed Solomon code (235,187).

ATSCMH_RSCODE_RES
    Reserved. Shouldn't be used.

.. _`fecap_scale_params`:

enum fecap_scale_params
=======================

.. c:type:: enum fecap_scale_params

    scale types for the quality parameters.

.. _`fecap_scale_params.definition`:

Definition
----------

.. code-block:: c

    enum fecap_scale_params {
        FE_SCALE_NOT_AVAILABLE,
        FE_SCALE_DECIBEL,
        FE_SCALE_RELATIVE,
        FE_SCALE_COUNTER
    };

.. _`fecap_scale_params.constants`:

Constants
---------

FE_SCALE_NOT_AVAILABLE
    That QoS measure is not available. That
    could indicate a temporary or a permanent
    condition.

FE_SCALE_DECIBEL
    The scale is measured in 0.001 dB steps, typically
    used on signal measures.

FE_SCALE_RELATIVE
    The scale is a relative percentual measure,
    ranging from 0 (0%) to 0xffff (100%).

FE_SCALE_COUNTER
    The scale counts the occurrence of an event, like
    bit error, block error, lapsed time.

.. _`dtv_stats`:

struct dtv_stats
================

.. c:type:: struct dtv_stats

    Used for reading a DTV status property

.. _`dtv_stats.definition`:

Definition
----------

.. code-block:: c

    struct dtv_stats {
        __u8 scale;
        union {
            __u64 uvalue;
            __s64 svalue;
        } ;
    }

.. _`dtv_stats.members`:

Members
-------

scale
    Filled with enum fecap_scale_params - the scale
    in usage for that parameter

{unnamed_union}
    anonymous

.. _`dtv_stats.description`:

Description
-----------

The ``{unnamed_union}`` may have either one of the values below:

\ ``svalue``\ 
     integer value of the measure, for \ ``FE_SCALE_DECIBEL``\ ,
     used for dB measures. The unit is 0.001 dB.

\ ``uvalue``\ 
     unsigned integer value of the measure, used when \ ``scale``\  is
     either \ ``FE_SCALE_RELATIVE``\  or \ ``FE_SCALE_COUNTER``\ .

For most delivery systems, this will return a single value for each
parameter.

It should be noticed, however, that new OFDM delivery systems like
ISDB can use different modulation types for each group of carriers.
On such standards, up to 8 groups of statistics can be provided, one
for each carrier group (called "layer" on ISDB).

In order to be consistent with other delivery systems, the first
value refers to the entire set of carriers ("global").

\ ``scale``\  should use the value \ ``FE_SCALE_NOT_AVAILABLE``\  when
the value for the entire group of carriers or from one specific layer
is not provided by the hardware.

\ ``len``\  should be filled with the latest filled status + 1.

In other words, for ISDB, those values should be filled like::

     u.st.stat.svalue[0] = global statistics;
     u.st.stat.scale[0] = FE_SCALE_DECIBEL;
     u.st.stat.value[1] = layer A statistics;
     u.st.stat.scale[1] = FE_SCALE_NOT_AVAILABLE (if not available);
     u.st.stat.svalue[2] = layer B statistics;
     u.st.stat.scale[2] = FE_SCALE_DECIBEL;
     u.st.stat.svalue[3] = layer C statistics;
     u.st.stat.scale[3] = FE_SCALE_DECIBEL;
     u.st.len = 4;

.. _`dtv_fe_stats`:

struct dtv_fe_stats
===================

.. c:type:: struct dtv_fe_stats

    store Digital TV frontend statistics

.. _`dtv_fe_stats.definition`:

Definition
----------

.. code-block:: c

    struct dtv_fe_stats {
        __u8 len;
        struct dtv_stats stat[MAX_DTV_STATS];
    }

.. _`dtv_fe_stats.members`:

Members
-------

len
    length of the statistics - if zero, stats is disabled.

stat
    array with digital TV statistics.

.. _`dtv_fe_stats.description`:

Description
-----------

On most standards, \ ``len``\  can either be 0 or 1. However, for ISDB, each
layer is modulated in separate. So, each layer may have its own set
of statistics. If so, stat[0] carries on a global value for the property.
Indexes 1 to 3 means layer A to B.

.. _`dtv_property`:

struct dtv_property
===================

.. c:type:: struct dtv_property

    store one of frontend command and its value

.. _`dtv_property.definition`:

Definition
----------

.. code-block:: c

    struct dtv_property {
        __u32 cmd;
        __u32 reserved[3];
        union {
            __u32 data;
            struct dtv_fe_stats st;
            struct {
                __u8 data[32];
                __u32 len;
                __u32 reserved1[3];
                void *reserved2;
            } buffer;
        } u;
        int result;
    }

.. _`dtv_property.members`:

Members
-------

cmd
    Digital TV command.

reserved
    Not used.

data
    *undescribed*

st
    *undescribed*

data
    *undescribed*

len
    *undescribed*

reserved1
    *undescribed*

reserved2
    *undescribed*

uffer
    *undescribed*

void
    no arguments

result
    Result of the command set (currently unused).

.. _`dtv_property.description`:

Description
-----------

The \ ``u``\  union may have either one of the values below:

\ ``data``\ 
     an unsigned 32-bits number.
\ ``st``\ 
     a \ :c:type:`struct dtv_fe_stats <dtv_fe_stats>`\  array of statistics.
\ ``buffer``\ 
     a buffer of up to 32 characters (currently unused).

.. _`dtv_properties`:

struct dtv_properties
=====================

.. c:type:: struct dtv_properties

    a set of command/value pairs.

.. _`dtv_properties.definition`:

Definition
----------

.. code-block:: c

    struct dtv_properties {
        __u32 num;
        struct dtv_property *props;
    }

.. _`dtv_properties.members`:

Members
-------

num
    amount of commands stored at the struct.

props
    a pointer to \ :c:type:`struct dtv_property <dtv_property>`\ .

.. This file was automatic generated / don't edit.

