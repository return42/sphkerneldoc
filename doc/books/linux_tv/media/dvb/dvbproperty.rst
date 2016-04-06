
.. _frontend-properties:

DVB Frontend properties
=======================

Tuning into a Digital TV physical channel and starting decoding it requires changing a set of parameters, in order to control the tuner, the demodulator, the Linear Low-noise
Amplifier (LNA) and to set the antenna subsystem via Satellite Equipment Control (SEC), on satellite systems. The actual parameters are specific to each particular digital TV
standards, and may change as the digital TV specs evolves.

In the past, the strategy used was to have a union with the parameters needed to tune for DVB-S, DVB-C, DVB-T and ATSC delivery systems grouped there. The problem is that, as the
second generation standards appeared, those structs were not big enough to contain the additional parameters. Also, the union didn't have any space left to be expanded without
breaking userspace. So, the decision was to deprecate the legacy union/struct based approach, in favor of a properties set approach.

NOTE: on Linux DVB API version 3, setting a frontend were done via :ref:`struct dvb_frontend_parameters <dvb-frontend-parameters>`. This got replaced on version 5 (also called
"S2API", as this API were added originally_enabled to provide support for DVB-S2), because the old API has a very limited support to new standards and new hardware. This section
describes the new and recommended way to set the frontend, with suppports all digital TV delivery systems.

Example: with the properties based approach, in order to set the tuner to a DVB-C channel at 651 kHz, modulated with 256-QAM, FEC 3/4 and symbol rate of 5.217 Mbauds, those
properties should be sent to :ref:`FE_SET_PROPERTY <FE_GET_PROPERTY>` ioctl:

-  :ref:`DTV_DELIVERY_SYSTEM <DTV-DELIVERY-SYSTEM>` = SYS_DVBC_ANNEX_A

-  :ref:`DTV_FREQUENCY <DTV-FREQUENCY>` = 651000000

-  :ref:`DTV_MODULATION <DTV-MODULATION>` = QAM_256

-  :ref:`DTV_INVERSION <DTV-INVERSION>` = INVERSION_AUTO

-  :ref:`DTV_SYMBOL_RATE <DTV-SYMBOL-RATE>` = 5217000

-  :ref:`DTV_INNER_FEC <DTV-INNER-FEC>` = FEC_3_4

-  :ref:`DTV_TUNE <DTV-TUNE>`

The code that would do the above is:


.. code-block:: c

    #include <stdio.h>
    #include <fcntl.h>
    #include <sys/ioctl.h>
    #include <linux/dvb/frontend.h>

    static struct dtv_property props[] = {
        { .cmd = DTV_DELIVERY_SYSTEM, .u.data = SYS_DVBC_ANNEX_A },
        { .cmd = DTV_FREQUENCY,       .u.data = 651000000 },
        { .cmd = DTV_MODULATION,      .u.data = QAM_256 },
        { .cmd = DTV_INVERSION,       .u.data = INVERSION_AUTO },
        { .cmd = DTV_SYMBOL_RATE,     .u.data = 5217000 },
        { .cmd = DTV_INNER_FEC,       .u.data = FEC_3_4 },
        { .cmd = DTV_TUNE }
    };

    static struct dtv_properties dtv_prop = {
        .num = 6, .props = props
    };

    int main(void)
    {
        int fd = open("/dev/dvb/adapter0/frontend0", O_RDWR);

        if (!fd) {
            perror ("open");
            return -1;
        }
        if (ioctl(fd, FE_SET_PROPERTY, &dtv_prop) == -1) {
            perror("ioctl");
            return -1;
        }
        printf("Frontend set\\n");
        return 0;
    }

NOTE: While it is possible to directly call the Kernel code like the above example, it is strongly recommended to use `libdvbv5`_, as it provides abstraction to work with the
supported digital TV standards and provides methods for usual operations like program scanning and to read/write channel descriptor files.


.. _dtv-stats:

struct dtv_stats
================


.. code-block:: c

    struct dtv_stats {
        __u8 scale; /* enum fecap_scale_params type */
        union {
            __u64 uvalue;   /* for counters and relative scales */
            __s64 svalue;   /* for 1/1000 dB measures */
        };
    } __packed;


.. _dtv-fe-stats:

struct dtv_fe_stats
===================


.. code-block:: c

    #define MAX_DTV_STATS   4

    struct dtv_fe_stats {
        __u8 len;
        struct dtv_stats stat[MAX_DTV_STATS];
    } __packed;


.. _dtv-property:

struct dtv_property
===================


.. code-block:: c

    /* Reserved fields should be set to 0 */

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
    } __attribute__ ((packed));

    /* num of properties cannot exceed DTV_IOCTL_MAX_MSGS per ioctl */
    #define DTV_IOCTL_MAX_MSGS 64


.. _dtv-properties:

struct dtv_properties
=====================


.. code-block:: c

    struct dtv_properties {
        __u32 num;
        struct dtv_property *props;
    };


Property types
==============

On :ref:`FE_GET_PROPERTY and FE_SET_PROPERTY <FE_GET_PROPERTY>`, the actual action is determined by the dtv_property cmd/data pairs. With one single ioctl, is possible to
get/set up to 64 properties. The actual meaning of each property is described on the next sections.

The available frontend property types are shown on the next section.


.. _fe_property_parameters:

Digital TV property parameters
==============================


.. _DTV-UNDEFINED:

DTV_UNDEFINED
=============

Used internally. A GET/SET operation for it won't change or return anything.


.. _DTV-TUNE:

DTV_TUNE
========

Interpret the cache of data, build either a traditional frontend tunerequest so we can pass validation in the ``FE_SET_FRONTEND`` ioctl.


.. _DTV-CLEAR:

DTV_CLEAR
=========

Reset a cache of data specific to the frontend here. This does not effect hardware.


.. _DTV-FREQUENCY:

DTV_FREQUENCY
=============

Central frequency of the channel.

Notes:

1)For satellite delivery systems, it is measured in kHz. For the other ones, it is measured in Hz.

2)For ISDB-T, the channels are usually transmitted with an offset of 143kHz. E.g. a valid frequency could be 474143 kHz. The stepping is bound to the bandwidth of the channel which
is 6MHz.

3)As in ISDB-Tsb the channel consists of only one or three segments the frequency step is 429kHz, 3⋆429 respectively. As for ISDB-T the central frequency of the channel is
expected.


.. _DTV-MODULATION:

DTV_MODULATION
==============

Specifies the frontend modulation type for delivery systems that supports more than one modulation type. The modulation can be one of the types defined by enum
:ref:`fe_modulation <fe-modulation>`.


.. _fe-modulation-t:

Modulation property
===================

Most of the digital TV standards currently offers more than one possible modulation (sometimes called as "constellation" on some standards). This enum contains the values used by
the Kernel. Please note that not all modulations are supported by a given standard.


.. _fe-modulation:

.. table:: enum fe_modulation

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``QPSK``                                                                                   | QPSK modulation                                                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``QAM_16``                                                                                 | 16-QAM modulation                                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``QAM_32``                                                                                 | 32-QAM modulation                                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``QAM_64``                                                                                 | 64-QAM modulation                                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``QAM_128``                                                                                | 128-QAM modulation                                                                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``QAM_256``                                                                                | 256-QAM modulation                                                                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``QAM_AUTO``                                                                               | Autodetect QAM modulation                                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``VSB_8``                                                                                  | 8-VSB modulation                                                                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``VSB_16``                                                                                 | 16-VSB modulation                                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``PSK_8``                                                                                  | 8-PSK modulation                                                                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``APSK_16``                                                                                | 16-APSK modulation                                                                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``APSK_32``                                                                                | 32-APSK modulation                                                                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``DQPSK``                                                                                  | DQPSK modulation                                                                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``QAM_4_NR``                                                                               | 4-QAM-NR modulation                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DTV-BANDWIDTH-HZ:

DTV_BANDWIDTH_HZ
================

Bandwidth for the channel, in HZ.

Possible values: ``1712000``, ``5000000``, ``6000000``, ``7000000``, ``8000000``, ``10000000``.

Notes:

1) For ISDB-T it should be always 6000000Hz (6MHz)

2) For ISDB-Tsb it can vary depending on the number of connected segments

3) Bandwidth doesn't apply for DVB-C transmissions, as the bandwidth for DVB-C depends on the symbol rate

4) Bandwidth in ISDB-T is fixed (6MHz) or can be easily derived from other parameters (DTV_ISDBT_SB_SEGMENT_IDX, DTV_ISDBT_SB_SEGMENT_COUNT).

5) DVB-T supports 6, 7 and 8MHz.

6) In addition, DVB-T2 supports 1.172, 5 and 10MHz.


.. _DTV-INVERSION:

DTV_INVERSION
=============

Specifies if the frontend should do spectral inversion or not.


.. _fe-spectral-inversion-t:

enum fe_modulation: Frontend spectral inversion
===============================================

This parameter indicates if spectral inversion should be presumed or not. In the automatic setting (``INVERSION_AUTO``) the hardware will try to figure out the correct setting by
itself. If the hardware doesn't support, the DVB core will try to lock at the carrier first with inversion off. If it fails, it will try to enable inversion.


.. _fe-spectral-inversion:

.. table:: enum fe_modulation

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``INVERSION_OFF``                                                                          | Don't do spectral band inversion.                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``INVERSION_ON``                                                                           | Do spectral band inversion.                                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``INVERSION_AUTO``                                                                         | Autodetect spectral band inversion.                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DTV-DISEQC-MASTER:

DTV_DISEQC_MASTER
=================

Currently not implemented.


.. _DTV-SYMBOL-RATE:

DTV_SYMBOL_RATE
===============

Digital TV symbol rate, in bauds (symbols/second). Used on cable standards.


.. _DTV-INNER-FEC:

DTV_INNER_FEC
=============

Used cable/satellite transmissions. The acceptable values are:


.. _fe-code-rate-t:

enum fe_code_rate: type of the Forward Error Correction.
========================================================


.. _fe-code-rate:

.. table:: enum fe_code_rate

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``FEC_NONE``                                                                               | No Forward Error Correction Code                                                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``FEC_AUTO``                                                                               | Autodetect Error Correction Code                                                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``FEC_1_2``                                                                                | Forward Error Correction Code 1/2                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``FEC_2_3``                                                                                | Forward Error Correction Code 2/3                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``FEC_3_4``                                                                                | Forward Error Correction Code 3/4                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``FEC_4_5``                                                                                | Forward Error Correction Code 4/5                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``FEC_5_6``                                                                                | Forward Error Correction Code 5/6                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``FEC_6_7``                                                                                | Forward Error Correction Code 6/7                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``FEC_7_8``                                                                                | Forward Error Correction Code 7/8                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``FEC_8_9``                                                                                | Forward Error Correction Code 8/9                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``FEC_9_10``                                                                               | Forward Error Correction Code 9/10                                                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``FEC_2_5``                                                                                | Forward Error Correction Code 2/5                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``FEC_3_5``                                                                                | Forward Error Correction Code 3/5                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DTV-VOLTAGE:

DTV_VOLTAGE
===========

The voltage is usually used with non-DiSEqC capable LNBs to switch the polarzation (horizontal/vertical). When using DiSEqC epuipment this voltage has to be switched consistently
to the DiSEqC commands as described in the DiSEqC spec.


.. _fe-sec-voltage:

.. table:: enum fe_sec_voltage

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``SEC_VOLTAGE_13``                                                                         | Set DC voltage level to 13V                                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SEC_VOLTAGE_18``                                                                         | Set DC voltage level to 18V                                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SEC_VOLTAGE_OFF``                                                                        | Don't send any voltage to the antenna                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DTV-TONE:

DTV_TONE
========

Currently not used.


.. _DTV-PILOT:

DTV_PILOT
=========

Sets DVB-S2 pilot


.. _fe-pilot-t:

fe_pilot type
=============


.. _fe-pilot:

.. table:: enum fe_pilot

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``PILOT_ON``                                                                               | Pilot tones enabled                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``PILOT_OFF``                                                                              | Pilot tones disabled                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``PILOT_AUTO``                                                                             | Autodetect pilot tones                                                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DTV-ROLLOFF:

DTV_ROLLOFF
===========

Sets DVB-S2 rolloff


.. _fe-rolloff-t:

fe_rolloff type
===============


.. _fe-rolloff:

.. table:: enum fe_rolloff

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``ROLLOFF_35``                                                                             | Roloff factor: α=35%                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``ROLLOFF_20``                                                                             | Roloff factor: α=20%                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``ROLLOFF_25``                                                                             | Roloff factor: α=25%                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``ROLLOFF_AUTO``                                                                           | Auto-detect the roloff factor.                                                             |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DTV-DISEQC-SLAVE-REPLY:

DTV_DISEQC_SLAVE_REPLY
======================

Currently not implemented.


.. _DTV-FE-CAPABILITY-COUNT:

DTV_FE_CAPABILITY_COUNT
=======================

Currently not implemented.


.. _DTV-FE-CAPABILITY:

DTV_FE_CAPABILITY
=================

Currently not implemented.


.. _DTV-DELIVERY-SYSTEM:

DTV_DELIVERY_SYSTEM
===================

Specifies the type of Delivery system


.. _fe-delivery-system-t:

fe_delivery_system type
=======================

Possible values:


.. _fe-delivery-system:

.. table:: enum fe_delivery_system

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``SYS_UNDEFINED``                                                                          | Undefined standard. Generally, indicates an error                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_DVBC_ANNEX_A``                                                                       | Cable TV: DVB-C following ITU-T J.83 Annex A spec                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_DVBC_ANNEX_B``                                                                       | Cable TV: DVB-C following ITU-T J.83 Annex B spec (ClearQAM)                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_DVBC_ANNEX_C``                                                                       | Cable TV: DVB-C following ITU-T J.83 Annex C spec                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_ISDBC``                                                                              | Cable TV: ISDB-C (no drivers yet)                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_DVBT``                                                                               | Terrestral TV: DVB-T                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_DVBT2``                                                                              | Terrestral TV: DVB-T2                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_ISDBT``                                                                              | Terrestral TV: ISDB-T                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_ATSC``                                                                               | Terrestral TV: ATSC                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_ATSCMH``                                                                             | Terrestral TV (mobile): ATSC-M/H                                                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_DTMB``                                                                               | Terrestrial TV: DTMB                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_DVBS``                                                                               | Satellite TV: DVB-S                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_DVBS2``                                                                              | Satellite TV: DVB-S2                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_TURBO``                                                                              | Satellite TV: DVB-S Turbo                                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_ISDBS``                                                                              | Satellite TV: ISDB-S                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_DAB``                                                                                | Digital audio: DAB (not fully supported)                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_DSS``                                                                                | Satellite TV:"DSS (not fully supported)                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_CMMB``                                                                               | Terrestral TV (mobile):CMMB (not fully supported)                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``SYS_DVBH``                                                                               | Terrestral TV (mobile): DVB-H (standard deprecated)                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DTV-ISDBT-PARTIAL-RECEPTION:

DTV_ISDBT_PARTIAL_RECEPTION
===========================

If ``DTV_ISDBT_SOUND_BROADCASTING`` is '0' this bit-field represents whether the channel is in partial reception mode or not.

If '1' ``DTV_ISDBT_LAYERA_⋆`` values are assigned to the center segment and ``DTV_ISDBT_LAYERA_SEGMENT_COUNT`` has to be '1'.

If in addition ``DTV_ISDBT_SOUND_BROADCASTING`` is '1' ``DTV_ISDBT_PARTIAL_RECEPTION`` represents whether this ISDB-Tsb channel is consisting of one segment and layer or three
segments and two layers.

Possible values: 0, 1, -1 (AUTO)


.. _DTV-ISDBT-SOUND-BROADCASTING:

DTV_ISDBT_SOUND_BROADCASTING
============================

This field represents whether the other DTV_ISDBT_⋆-parameters are referring to an ISDB-T and an ISDB-Tsb channel. (See also ``DTV_ISDBT_PARTIAL_RECEPTION``).

Possible values: 0, 1, -1 (AUTO)


.. _DTV-ISDBT-SB-SUBCHANNEL-ID:

DTV_ISDBT_SB_SUBCHANNEL_ID
==========================

This field only applies if ``DTV_ISDBT_SOUND_BROADCASTING`` is '1'.

(Note of the author: This might not be the correct description of the ``SUBCHANNEL-ID`` in all details, but it is my understanding of the technical background needed to program a
device)

An ISDB-Tsb channel (1 or 3 segments) can be broadcasted alone or in a set of connected ISDB-Tsb channels. In this set of channels every channel can be received independently. The
number of connected ISDB-Tsb segment can vary, e.g. depending on the frequency spectrum bandwidth available.

Example: Assume 8 ISDB-Tsb connected segments are broadcasted. The broadcaster has several possibilities to put those channels in the air: Assuming a normal 13-segment ISDB-T
spectrum he can align the 8 segments from position 1-8 to 5-13 or anything in between.

The underlying layer of segments are subchannels: each segment is consisting of several subchannels with a predefined IDs. A sub-channel is used to help the demodulator to
synchronize on the channel.

An ISDB-T channel is always centered over all sub-channels. As for the example above, in ISDB-Tsb it is no longer as simple as that.

``The DTV_ISDBT_SB_SUBCHANNEL_ID`` parameter is used to give the sub-channel ID of the segment to be demodulated.

Possible values: 0 .. 41, -1 (AUTO)


.. _DTV-ISDBT-SB-SEGMENT-IDX:

DTV_ISDBT_SB_SEGMENT_IDX
========================

This field only applies if ``DTV_ISDBT_SOUND_BROADCASTING`` is '1'.

``DTV_ISDBT_SB_SEGMENT_IDX`` gives the index of the segment to be demodulated for an ISDB-Tsb channel where several of them are transmitted in the connected manner.

Possible values: 0 .. ``DTV_ISDBT_SB_SEGMENT_COUNT`` - 1

Note: This value cannot be determined by an automatic channel search.


.. _DTV-ISDBT-SB-SEGMENT-COUNT:

DTV_ISDBT_SB_SEGMENT_COUNT
==========================

This field only applies if ``DTV_ISDBT_SOUND_BROADCASTING`` is '1'.

``DTV_ISDBT_SB_SEGMENT_COUNT`` gives the total count of connected ISDB-Tsb channels.

Possible values: 1 .. 13

Note: This value cannot be determined by an automatic channel search.


.. _isdb-hierq-layers:

DTV-ISDBT-LAYER⋆ parameters
===========================

ISDB-T channels can be coded hierarchically. As opposed to DVB-T in ISDB-T hierarchical layers can be decoded simultaneously. For that reason a ISDB-T demodulator has 3 Viterbi and
3 Reed-Solomon decoders.

ISDB-T has 3 hierarchical layers which each can use a part of the available segments. The total number of segments over all layers has to 13 in ISDB-T.

There are 3 parameter sets, for Layers A, B and C.


.. _DTV-ISDBT-LAYER-ENABLED:

DTV_ISDBT_LAYER_ENABLED
=======================

Hierarchical reception in ISDB-T is achieved by enabling or disabling layers in the decoding process. Setting all bits of ``DTV_ISDBT_LAYER_ENABLED`` to '1' forces all layers (if
applicable) to be demodulated. This is the default.

If the channel is in the partial reception mode (``DTV_ISDBT_PARTIAL_RECEPTION`` = 1) the central segment can be decoded independently of the other 12 segments. In that mode layer
A has to have a ``SEGMENT_COUNT`` of 1.

In ISDB-Tsb only layer A is used, it can be 1 or 3 in ISDB-Tsb according to ``DTV_ISDBT_PARTIAL_RECEPTION``. ``SEGMENT_COUNT`` must be filled accordingly.

Possible values: 0x1, 0x2, 0x4 (|-able)

``DTV_ISDBT_LAYER_ENABLED[0:0]`` - layer A

``DTV_ISDBT_LAYER_ENABLED[1:1]`` - layer B

``DTV_ISDBT_LAYER_ENABLED[2:2]`` - layer C

``DTV_ISDBT_LAYER_ENABLED[31:3]`` unused


.. _DTV-ISDBT-LAYER-FEC:

DTV_ISDBT_LAYER⋆_FEC
====================

Possible values: ``FEC_AUTO``, ``FEC_1_2``, ``FEC_2_3``, ``FEC_3_4``, ``FEC_5_6``, ``FEC_7_8``


.. _DTV-ISDBT-LAYER-MODULATION:

DTV_ISDBT_LAYER⋆_MODULATION
===========================

Possible values: ``QAM_AUTO``, QP\ ``SK, QAM_16``, ``QAM_64``, ``DQPSK``

Note: If layer C is ``DQPSK`` layer B has to be ``DQPSK``. If layer B is ``DQPSK`` and ``DTV_ISDBT_PARTIAL_RECEPTION``\ =0 layer has to be ``DQPSK``.


.. _DTV-ISDBT-LAYER-SEGMENT-COUNT:

DTV_ISDBT_LAYER⋆_SEGMENT_COUNT
==============================

Possible values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, -1 (AUTO)

Note: Truth table for ``DTV_ISDBT_SOUND_BROADCASTING`` and ``DTV_ISDBT_PARTIAL_RECEPTION`` and ``LAYER`` ⋆_SEGMENT_COUNT


.. _isdbt-layer_seg-cnt-table:

.. table::

    +--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
    | PR                             | SB                             | Layer A width                  | Layer B width                  | Layer C width                  | total width                    |
    +--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
    | 0                              | 0                              | 1 .. 13                        | 1 .. 13                        | 1 .. 13                        | 13                             |
    +--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
    | 1                              | 0                              | 1                              | 1 .. 13                        | 1 .. 13                        | 13                             |
    +--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
    | 0                              | 1                              | 1                              | 0                              | 0                              | 1                              |
    +--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
    | 1                              | 1                              | 1                              | 2                              | 0                              | 13                             |
    +--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+



.. _DTV-ISDBT-LAYER-TIME-INTERLEAVING:

DTV_ISDBT_LAYER⋆_TIME_INTERLEAVING
==================================

Valid values: 0, 1, 2, 4, -1 (AUTO)

when DTV_ISDBT_SOUND_BROADCASTING is active, value 8 is also valid.

Note: The real time interleaving length depends on the mode (fft-size). The values here are referring to what can be found in the TMCC-structure, as shown in the table below.


.. _isdbt-layer-interleaving-table:

.. table::

    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | DTV_ISDBT_LAYER⋆_TIME_INTERLEAVING            | Mode 1 (2K FFT)                               | Mode 2 (4K FFT)                               | Mode 3 (8K FFT)                               |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | 0                                             | 0                                             | 0                                             | 0                                             |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | 1                                             | 4                                             | 2                                             | 1                                             |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | 2                                             | 8                                             | 4                                             | 2                                             |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+
    | 4                                             | 16                                            | 8                                             | 4                                             |
    +-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+-----------------------------------------------+



.. _DTV-ATSCMH-FIC-VER:

DTV_ATSCMH_FIC_VER
==================

Version number of the FIC (Fast Information Channel) signaling data.

FIC is used for relaying information to allow rapid service acquisition by the receiver.

Possible values: 0, 1, 2, 3, ..., 30, 31


.. _DTV-ATSCMH-PARADE-ID:

DTV_ATSCMH_PARADE_ID
====================

Parade identification number

A parade is a collection of up to eight MH groups, conveying one or two ensembles.

Possible values: 0, 1, 2, 3, ..., 126, 127


.. _DTV-ATSCMH-NOG:

DTV_ATSCMH_NOG
==============

Number of MH groups per MH subframe for a designated parade.

Possible values: 1, 2, 3, 4, 5, 6, 7, 8


.. _DTV-ATSCMH-TNOG:

DTV_ATSCMH_TNOG
===============

Total number of MH groups including all MH groups belonging to all MH parades in one MH subframe.

Possible values: 0, 1, 2, 3, ..., 30, 31


.. _DTV-ATSCMH-SGN:

DTV_ATSCMH_SGN
==============

Start group number.

Possible values: 0, 1, 2, 3, ..., 14, 15


.. _DTV-ATSCMH-PRC:

DTV_ATSCMH_PRC
==============

Parade repetition cycle.

Possible values: 1, 2, 3, 4, 5, 6, 7, 8


.. _DTV-ATSCMH-RS-FRAME-MODE:

DTV_ATSCMH_RS_FRAME_MODE
========================

Reed Solomon (RS) frame mode.

Possible values are:


.. _atscmh-rs-frame-mode:

.. table:: enum atscmh_rs_frame_mode

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``ATSCMH_RSFRAME_PRI_ONLY``                                                                | Single Frame: There is only a primary RS Frame for all Group Regions.                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``ATSCMH_RSFRAME_PRI_SEC``                                                                 | Dual Frame: There are two separate RS Frames: Primary RS Frame for Group Region A and B    |
    |                                                                                            | and Secondary RS Frame for Group Region C and D.                                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DTV-ATSCMH-RS-FRAME-ENSEMBLE:

DTV_ATSCMH_RS_FRAME_ENSEMBLE
============================

Reed Solomon(RS) frame ensemble.

Possible values are:


.. _atscmh-rs-frame-ensemble:

.. table:: enum atscmh_rs_frame_ensemble

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``ATSCMH_RSFRAME_ENS_PRI``                                                                 | Primary Ensemble.                                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``AATSCMH_RSFRAME_PRI_SEC``                                                                | Secondary Ensemble.                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``AATSCMH_RSFRAME_RES``                                                                    | Reserved. Shouldn't be used.                                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DTV-ATSCMH-RS-CODE-MODE-PRI:

DTV_ATSCMH_RS_CODE_MODE_PRI
===========================

Reed Solomon (RS) code mode (primary).

Possible values are:


.. _atscmh-rs-code-mode:

.. table:: enum atscmh_rs_code_mode

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``ATSCMH_RSCODE_211_187``                                                                  | Reed Solomon code (211,187).                                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``ATSCMH_RSCODE_223_187``                                                                  | Reed Solomon code (223,187).                                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``ATSCMH_RSCODE_235_187``                                                                  | Reed Solomon code (235,187).                                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``ATSCMH_RSCODE_RES``                                                                      | Reserved. Shouldn't be used.                                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DTV-ATSCMH-RS-CODE-MODE-SEC:

DTV_ATSCMH_RS_CODE_MODE_SEC
===========================

Reed Solomon (RS) code mode (secondary).

Possible values are the same as documented on enum :ref:`atscmh_rs_code_mode <atscmh-rs-code-mode>`:


.. _DTV-ATSCMH-SCCC-BLOCK-MODE:

DTV_ATSCMH_SCCC_BLOCK_MODE
==========================

Series Concatenated Convolutional Code Block Mode.

Possible values are:


.. _atscmh-sccc-block-mode:

.. table:: enum atscmh_scc_block_mode

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``ATSCMH_SCCC_BLK_SEP``                                                                    | Separate SCCC: the SCCC outer code mode shall be set independently for each Group Region   |
    |                                                                                            | (A, B, C, D)                                                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``ATSCMH_SCCC_BLK_COMB``                                                                   | Combined SCCC: all four Regions shall have the same SCCC outer code mode.                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``ATSCMH_SCCC_BLK_RES``                                                                    | Reserved. Shouldn't be used.                                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DTV-ATSCMH-SCCC-CODE-MODE-A:

DTV_ATSCMH_SCCC_CODE_MODE_A
===========================

Series Concatenated Convolutional Code Rate.

Possible values are:


.. _atscmh-sccc-code-mode:

.. table:: enum atscmh_sccc_code_mode

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``ATSCMH_SCCC_CODE_HLF``                                                                   | The outer code rate of a SCCC Block is 1/2 rate.                                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``ATSCMH_SCCC_CODE_QTR``                                                                   | The outer code rate of a SCCC Block is 1/4 rate.                                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``ATSCMH_SCCC_CODE_RES``                                                                   | to be documented.                                                                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DTV-ATSCMH-SCCC-CODE-MODE-B:

DTV_ATSCMH_SCCC_CODE_MODE_B
===========================

Series Concatenated Convolutional Code Rate.

Possible values are the same as documented on enum :ref:`atscmh_sccc_code_mode <atscmh-sccc-code-mode>`.


.. _DTV-ATSCMH-SCCC-CODE-MODE-C:

DTV_ATSCMH_SCCC_CODE_MODE_C
===========================

Series Concatenated Convolutional Code Rate.

Possible values are the same as documented on enum :ref:`atscmh_sccc_code_mode <atscmh-sccc-code-mode>`.


.. _DTV-ATSCMH-SCCC-CODE-MODE-D:

DTV_ATSCMH_SCCC_CODE_MODE_D
===========================

Series Concatenated Convolutional Code Rate.

Possible values are the same as documented on enum :ref:`atscmh_sccc_code_mode <atscmh-sccc-code-mode>`.


.. _DTV-API-VERSION:

DTV_API_VERSION
===============

Returns the major/minor version of the DVB API


.. _DTV-CODE-RATE-HP:

DTV_CODE_RATE_HP
================

Used on terrestrial transmissions. The acceptable values are the ones described at :ref:`fe_transmit_mode_t <fe-transmit-mode-t>`.


.. _DTV-CODE-RATE-LP:

DTV_CODE_RATE_LP
================

Used on terrestrial transmissions. The acceptable values are the ones described at :ref:`fe_transmit_mode_t <fe-transmit-mode-t>`.


.. _DTV-GUARD-INTERVAL:

DTV_GUARD_INTERVAL
==================

Possible values are:


.. _fe-guard-interval-t:

Modulation guard interval
=========================


.. _fe-guard-interval:

.. table:: enum fe_guard_interval

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``GUARD_INTERVAL_AUTO``                                                                    | Autodetect the guard interval                                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``GUARD_INTERVAL_1_128``                                                                   | Guard interval 1/128                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``GUARD_INTERVAL_1_32``                                                                    | Guard interval 1/32                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``GUARD_INTERVAL_1_16``                                                                    | Guard interval 1/16                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``GUARD_INTERVAL_1_8``                                                                     | Guard interval 1/8                                                                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``GUARD_INTERVAL_1_4``                                                                     | Guard interval 1/4                                                                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``GUARD_INTERVAL_19_128``                                                                  | Guard interval 19/128                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``GUARD_INTERVAL_19_256``                                                                  | Guard interval 19/256                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``GUARD_INTERVAL_PN420``                                                                   | PN length 420 (1/4)                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``GUARD_INTERVAL_PN595``                                                                   | PN length 595 (1/6)                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``GUARD_INTERVAL_PN945``                                                                   | PN length 945 (1/9)                                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


Notes:

1) If ``DTV_GUARD_INTERVAL`` is set the ``GUARD_INTERVAL_AUTO`` the hardware will try to find the correct guard interval (if capable) and will use TMCC to fill in the missing
parameters.

2) Intervals 1/128, 19/128 and 19/256 are used only for DVB-T2 at present

3) DTMB specifies PN420, PN595 and PN945.


.. _DTV-TRANSMISSION-MODE:

DTV_TRANSMISSION_MODE
=====================

Specifies the number of carriers used by the standard. This is used only on OFTM-based standards, e. g. DVB-T/T2, ISDB-T, DTMB


.. _fe-transmit-mode-t:

enum fe_transmit_mode: Number of carriers per channel
=====================================================


.. _fe-transmit-mode:

.. table:: enum fe_transmit_mode

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``TRANSMISSION_MODE_AUTO``                                                                 | Autodetect transmission mode. The hardware will try to find the correct FFT-size (if       |
    |                                                                                            | capable) to fill in the missing parameters.                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``TRANSMISSION_MODE_1K``                                                                   | Transmission mode 1K                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``TRANSMISSION_MODE_2K``                                                                   | Transmission mode 2K                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``TRANSMISSION_MODE_8K``                                                                   | Transmission mode 8K                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``TRANSMISSION_MODE_4K``                                                                   | Transmission mode 4K                                                                       |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``TRANSMISSION_MODE_16K``                                                                  | Transmission mode 16K                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``TRANSMISSION_MODE_32K``                                                                  | Transmission mode 32K                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``TRANSMISSION_MODE_C1``                                                                   | Single Carrier (C=1) transmission mode (DTMB)                                              |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``TRANSMISSION_MODE_C3780``                                                                | Multi Carrier (C=3780) transmission mode (DTMB)                                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


Notes:

1) ISDB-T supports three carrier/symbol-size: 8K, 4K, 2K. It is called 'mode' in the standard: Mode 1 is 2K, mode 2 is 4K, mode 3 is 8K

2) If ``DTV_TRANSMISSION_MODE`` is set the ``TRANSMISSION_MODE_AUTO`` the hardware will try to find the correct FFT-size (if capable) and will use TMCC to fill in the missing
parameters.

3) DVB-T specifies 2K and 8K as valid sizes.

4) DVB-T2 specifies 1K, 2K, 4K, 8K, 16K and 32K.

5) DTMB specifies C1 and C3780.


.. _DTV-HIERARCHY:

DTV_HIERARCHY
=============

Frontend hierarchy


.. _fe-hierarchy-t:

Frontend hierarchy
==================


.. _fe-hierarchy:

.. table:: enum fe_hierarchy

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``HIERARCHY_NONE``                                                                         | No hierarchy                                                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``HIERARCHY_AUTO``                                                                         | Autodetect hierarchy (if supported)                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``HIERARCHY_1``                                                                            | Hierarchy 1                                                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``HIERARCHY_2``                                                                            | Hierarchy 2                                                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``HIERARCHY_4``                                                                            | Hierarchy 4                                                                                |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DTV-STREAM-ID:

DTV_STREAM_ID
=============

DVB-S2, DVB-T2 and ISDB-S support the transmission of several streams on a single transport stream. This property enables the DVB driver to handle substream filtering, when
supported by the hardware. By default, substream filtering is disabled.

For DVB-S2 and DVB-T2, the valid substream id range is from 0 to 255.

For ISDB, the valid substream id range is from 1 to 65535.

To disable it, you should use the special macro NO_STREAM_ID_FILTER.

Note: any value outside the id range also disables filtering.


.. _DTV-DVBT2-PLP-ID-LEGACY:

DTV_DVBT2_PLP_ID_LEGACY
=======================

Obsolete, replaced with DTV_STREAM_ID.


.. _DTV-ENUM-DELSYS:

DTV_ENUM_DELSYS
===============

A Multi standard frontend needs to advertise the delivery systems provided. Applications need to enumerate the provided delivery systems, before using any other operation with the
frontend. Prior to it's introduction, FE_GET_INFO was used to determine a frontend type. A frontend which provides more than a single delivery system, FE_GET_INFO doesn't help
much. Applications which intends to use a multistandard frontend must enumerate the delivery systems associated with it, rather than trying to use FE_GET_INFO. In the case of a
legacy frontend, the result is just the same as with FE_GET_INFO, but in a more structured format


.. _DTV-INTERLEAVING:

DTV_INTERLEAVING
================

Time interleaving to be used. Currently, used only on DTMB.


.. _fe-interleaving:

.. table:: enum fe_interleaving

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``INTERLEAVING_NONE``                                                                      | No interleaving.                                                                           |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``INTERLEAVING_AUTO``                                                                      | Auto-detect interleaving.                                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``INTERLEAVING_240``                                                                       | Interleaving of 240 symbols.                                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``INTERLEAVING_720``                                                                       | Interleaving of 720 symbols.                                                               |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _DTV-LNA:

DTV_LNA
=======

Low-noise amplifier.

Hardware might offer controllable LNA which can be set manually using that parameter. Usually LNA could be found only from terrestrial devices if at all.

Possible values: 0, 1, LNA_AUTO

0, LNA off

1, LNA on

use the special macro LNA_AUTO to set LNA auto


.. _frontend-stat-properties:

Frontend statistics indicators
==============================

The values are returned via ``dtv_property.stat``. If the property is supported, ``dtv_property.stat.len`` is bigger than zero.

For most delivery systems, ``dtv_property.stat.len`` will be 1 if the stats is supported, and the properties will return a single value for each parameter.

It should be noted, however, that new OFDM delivery systems like ISDB can use different modulation types for each group of carriers. On such standards, up to 3 groups of statistics
can be provided, and ``dtv_property.stat.len`` is updated to reflect the "global" metrics, plus one metric per each carrier group (called "layer" on ISDB).

So, in order to be consistent with other delivery systems, the first value at :ref:`dtv_property.stat.dtv_stats <dtv-stats>` array refers to the global metric. The other
elements of the array represent each layer, starting from layer A(index 1), layer B (index 2) and so on.

The number of filled elements are stored at ``dtv_property.stat.len``.

Each element of the ``dtv_property.stat.dtv_stats`` array consists on two elements:

-  ``svalue`` or ``uvalue``, where ``svalue`` is for signed values of the measure (dB measures) and ``uvalue`` is for unsigned values (counters, relative scale)

-  ``scale`` - Scale for the value. It can be:

   -  ``FE_SCALE_NOT_AVAILABLE`` - The parameter is supported by the frontend, but it was not possible to collect it (could be a transitory or permanent condition)

   -  ``FE_SCALE_DECIBEL`` - parameter is a signed value, measured in 1/1000 dB

   -  ``FE_SCALE_RELATIVE`` - parameter is a unsigned value, where 0 means 0% and 65535 means 100%.

   -  ``FE_SCALE_COUNTER`` - parameter is a unsigned value that counts the occurrence of an event, like bit error, block error, or lapsed time.


.. _DTV-STAT-SIGNAL-STRENGTH:

DTV_STAT_SIGNAL_STRENGTH
========================

Indicates the signal strength level at the analog part of the tuner or of the demod.

Possible scales for this metric are:

-  ``FE_SCALE_NOT_AVAILABLE`` - it failed to measure it, or the measurement was not complete yet.

-  ``FE_SCALE_DECIBEL`` - signal strength is in 0.001 dBm units, power measured in miliwatts. This value is generally negative.

-  ``FE_SCALE_RELATIVE`` - The frontend provides a 0% to 100% measurement for power (actually, 0 to 65535).


.. _DTV-STAT-CNR:

DTV_STAT_CNR
============

Indicates the Signal to Noise ratio for the main carrier.

Possible scales for this metric are:

-  ``FE_SCALE_NOT_AVAILABLE`` - it failed to measure it, or the measurement was not complete yet.

-  ``FE_SCALE_DECIBEL`` - Signal/Noise ratio is in 0.001 dB units.

-  ``FE_SCALE_RELATIVE`` - The frontend provides a 0% to 100% measurement for Signal/Noise (actually, 0 to 65535).


.. _DTV-STAT-PRE-ERROR-BIT-COUNT:

DTV_STAT_PRE_ERROR_BIT_COUNT
============================

Measures the number of bit errors before the forward error correction (FEC) on the inner coding block (before Viterbi, LDPC or other inner code).

This measure is taken during the same interval as ``DTV_STAT_PRE_TOTAL_BIT_COUNT``.

In order to get the BER (Bit Error Rate) measurement, it should be divided by :ref:`DTV_STAT_PRE_TOTAL_BIT_COUNT <DTV-STAT-PRE-TOTAL-BIT-COUNT>`.

This measurement is monotonically increased, as the frontend gets more bit count measurements. The frontend may reset it when a channel/transponder is tuned.

Possible scales for this metric are:

-  ``FE_SCALE_NOT_AVAILABLE`` - it failed to measure it, or the measurement was not complete yet.

-  ``FE_SCALE_COUNTER`` - Number of error bits counted before the inner coding.


.. _DTV-STAT-PRE-TOTAL-BIT-COUNT:

DTV_STAT_PRE_TOTAL_BIT_COUNT
============================

Measures the amount of bits received before the inner code block, during the same period as :ref:`DTV_STAT_PRE_ERROR_BIT_COUNT <DTV-STAT-PRE-ERROR-BIT-COUNT>` measurement
was taken.

It should be noted that this measurement can be smaller than the total amount of bits on the transport stream, as the frontend may need to manually restart the measurement, losing
some data between each measurement interval.

This measurement is monotonically increased, as the frontend gets more bit count measurements. The frontend may reset it when a channel/transponder is tuned.

Possible scales for this metric are:

-  ``FE_SCALE_NOT_AVAILABLE`` - it failed to measure it, or the measurement was not complete yet.

-  ``FE_SCALE_COUNTER`` - Number of bits counted while measuring :ref:`DTV_STAT_PRE_ERROR_BIT_COUNT <DTV-STAT-PRE-ERROR-BIT-COUNT>`.


.. _DTV-STAT-POST-ERROR-BIT-COUNT:

DTV_STAT_POST_ERROR_BIT_COUNT
=============================

Measures the number of bit errors after the forward error correction (FEC) done by inner code block (after Viterbi, LDPC or other inner code).

This measure is taken during the same interval as ``DTV_STAT_POST_TOTAL_BIT_COUNT``.

In order to get the BER (Bit Error Rate) measurement, it should be divided by :ref:`DTV_STAT_POST_TOTAL_BIT_COUNT <DTV-STAT-POST-TOTAL-BIT-COUNT>`.

This measurement is monotonically increased, as the frontend gets more bit count measurements. The frontend may reset it when a channel/transponder is tuned.

Possible scales for this metric are:

-  ``FE_SCALE_NOT_AVAILABLE`` - it failed to measure it, or the measurement was not complete yet.

-  ``FE_SCALE_COUNTER`` - Number of error bits counted after the inner coding.


.. _DTV-STAT-POST-TOTAL-BIT-COUNT:

DTV_STAT_POST_TOTAL_BIT_COUNT
=============================

Measures the amount of bits received after the inner coding, during the same period as :ref:`DTV_STAT_POST_ERROR_BIT_COUNT <DTV-STAT-POST-ERROR-BIT-COUNT>` measurement was
taken.

It should be noted that this measurement can be smaller than the total amount of bits on the transport stream, as the frontend may need to manually restart the measurement, losing
some data between each measurement interval.

This measurement is monotonically increased, as the frontend gets more bit count measurements. The frontend may reset it when a channel/transponder is tuned.

Possible scales for this metric are:

-  ``FE_SCALE_NOT_AVAILABLE`` - it failed to measure it, or the measurement was not complete yet.

-  ``FE_SCALE_COUNTER`` - Number of bits counted while measuring :ref:`DTV_STAT_POST_ERROR_BIT_COUNT <DTV-STAT-POST-ERROR-BIT-COUNT>`.


.. _DTV-STAT-ERROR-BLOCK-COUNT:

DTV_STAT_ERROR_BLOCK_COUNT
==========================

Measures the number of block errors after the outer forward error correction coding (after Reed-Solomon or other outer code).

This measurement is monotonically increased, as the frontend gets more bit count measurements. The frontend may reset it when a channel/transponder is tuned.

Possible scales for this metric are:

-  ``FE_SCALE_NOT_AVAILABLE`` - it failed to measure it, or the measurement was not complete yet.

-  ``FE_SCALE_COUNTER`` - Number of error blocks counted after the outer coding.


.. _DTV-STAT-TOTAL-BLOCK-COUNT:

DTV-STAT_TOTAL_BLOCK_COUNT
==========================

Measures the total number of blocks received during the same period as :ref:`DTV_STAT_ERROR_BLOCK_COUNT <DTV-STAT-ERROR-BLOCK-COUNT>` measurement was taken.

It can be used to calculate the PER indicator, by dividing :ref:`DTV_STAT_ERROR_BLOCK_COUNT <DTV-STAT-ERROR-BLOCK-COUNT>` by
:ref:`DTV-STAT-TOTAL-BLOCK-COUNT <DTV-STAT-TOTAL-BLOCK-COUNT>`.

Possible scales for this metric are:

-  ``FE_SCALE_NOT_AVAILABLE`` - it failed to measure it, or the measurement was not complete yet.

-  ``FE_SCALE_COUNTER`` - Number of blocks counted while measuring :ref:`DTV_STAT_ERROR_BLOCK_COUNT <DTV-STAT-ERROR-BLOCK-COUNT>`.


.. _frontend-property-terrestrial-systems:

Properties used on terrestrial delivery systems
===============================================


.. _dvbt-params:

DVB-T delivery system
=====================

The following parameters are valid for DVB-T:

-  :ref:`DTV_API_VERSION <DTV-API-VERSION>`

-  :ref:`DTV_DELIVERY_SYSTEM <DTV-DELIVERY-SYSTEM>`

-  :ref:`DTV_TUNE <DTV-TUNE>`

-  :ref:`DTV_CLEAR <DTV-CLEAR>`

-  :ref:`DTV_FREQUENCY <DTV-FREQUENCY>`

-  :ref:`DTV_MODULATION <DTV-MODULATION>`

-  :ref:`DTV_BANDWIDTH_HZ <DTV-BANDWIDTH-HZ>`

-  :ref:`DTV_INVERSION <DTV-INVERSION>`

-  :ref:`DTV_CODE_RATE_HP <DTV-CODE-RATE-HP>`

-  :ref:`DTV_CODE_RATE_LP <DTV-CODE-RATE-LP>`

-  :ref:`DTV_GUARD_INTERVAL <DTV-GUARD-INTERVAL>`

-  :ref:`DTV_TRANSMISSION_MODE <DTV-TRANSMISSION-MODE>`

-  :ref:`DTV_HIERARCHY <DTV-HIERARCHY>`

-  :ref:`DTV_LNA <DTV-LNA>`

In addition, the :ref:`DTV QoS statistics <frontend-stat-properties>` are also valid.


.. _dvbt2-params:

DVB-T2 delivery system
======================

DVB-T2 support is currently in the early stages of development, so expect that this section maygrow and become more detailed with time.

The following parameters are valid for DVB-T2:

-  :ref:`DTV_API_VERSION <DTV-API-VERSION>`

-  :ref:`DTV_DELIVERY_SYSTEM <DTV-DELIVERY-SYSTEM>`

-  :ref:`DTV_TUNE <DTV-TUNE>`

-  :ref:`DTV_CLEAR <DTV-CLEAR>`

-  :ref:`DTV_FREQUENCY <DTV-FREQUENCY>`

-  :ref:`DTV_MODULATION <DTV-MODULATION>`

-  :ref:`DTV_BANDWIDTH_HZ <DTV-BANDWIDTH-HZ>`

-  :ref:`DTV_INVERSION <DTV-INVERSION>`

-  :ref:`DTV_CODE_RATE_HP <DTV-CODE-RATE-HP>`

-  :ref:`DTV_CODE_RATE_LP <DTV-CODE-RATE-LP>`

-  :ref:`DTV_GUARD_INTERVAL <DTV-GUARD-INTERVAL>`

-  :ref:`DTV_TRANSMISSION_MODE <DTV-TRANSMISSION-MODE>`

-  :ref:`DTV_HIERARCHY <DTV-HIERARCHY>`

-  :ref:`DTV_STREAM_ID <DTV-STREAM-ID>`

-  :ref:`DTV_LNA <DTV-LNA>`

In addition, the :ref:`DTV QoS statistics <frontend-stat-properties>` are also valid.


.. _isdbt:

ISDB-T delivery system
======================

This ISDB-T/ISDB-Tsb API extension should reflect all information needed to tune any ISDB-T/ISDB-Tsb hardware. Of course it is possible that some very sophisticated devices won't
need certain parameters to tune.

The information given here should help application writers to know how to handle ISDB-T and ISDB-Tsb hardware using the Linux DVB-API.

The details given here about ISDB-T and ISDB-Tsb are just enough to basically show the dependencies between the needed parameter values, but surely some information is left out.
For more detailed information see the following documents:

ARIB STD-B31 - "Transmission System for Digital Terrestrial Television Broadcasting" and

ARIB TR-B14 - "Operational Guidelines for Digital Terrestrial Television Broadcasting".

In order to understand the ISDB specific parameters, one has to have some knowledge the channel structure in ISDB-T and ISDB-Tsb. I.e. it has to be known to the reader that an
ISDB-T channel consists of 13 segments, that it can have up to 3 layer sharing those segments, and things like that.

The following parameters are valid for ISDB-T:

-  :ref:`DTV_API_VERSION <DTV-API-VERSION>`

-  :ref:`DTV_DELIVERY_SYSTEM <DTV-DELIVERY-SYSTEM>`

-  :ref:`DTV_TUNE <DTV-TUNE>`

-  :ref:`DTV_CLEAR <DTV-CLEAR>`

-  :ref:`DTV_FREQUENCY <DTV-FREQUENCY>`

-  :ref:`DTV_BANDWIDTH_HZ <DTV-BANDWIDTH-HZ>`

-  :ref:`DTV_INVERSION <DTV-INVERSION>`

-  :ref:`DTV_GUARD_INTERVAL <DTV-GUARD-INTERVAL>`

-  :ref:`DTV_TRANSMISSION_MODE <DTV-TRANSMISSION-MODE>`

-  :ref:`DTV_ISDBT_LAYER_ENABLED <DTV-ISDBT-LAYER-ENABLED>`

-  :ref:`DTV_ISDBT_PARTIAL_RECEPTION <DTV-ISDBT-PARTIAL-RECEPTION>`

-  :ref:`DTV_ISDBT_SOUND_BROADCASTING <DTV-ISDBT-SOUND-BROADCASTING>`

-  :ref:`DTV_ISDBT_SB_SUBCHANNEL_ID <DTV-ISDBT-SB-SUBCHANNEL-ID>`

-  :ref:`DTV_ISDBT_SB_SEGMENT_IDX <DTV-ISDBT-SB-SEGMENT-IDX>`

-  :ref:`DTV_ISDBT_SB_SEGMENT_COUNT <DTV-ISDBT-SB-SEGMENT-COUNT>`

-  :ref:`DTV_ISDBT_LAYERA_FEC <DTV-ISDBT-LAYER-FEC>`

-  :ref:`DTV_ISDBT_LAYERA_MODULATION <DTV-ISDBT-LAYER-MODULATION>`

-  :ref:`DTV_ISDBT_LAYERA_SEGMENT_COUNT <DTV-ISDBT-LAYER-SEGMENT-COUNT>`

-  :ref:`DTV_ISDBT_LAYERA_TIME_INTERLEAVING <DTV-ISDBT-LAYER-TIME-INTERLEAVING>`

-  :ref:`DTV_ISDBT_LAYERB_FEC <DTV-ISDBT-LAYER-FEC>`

-  :ref:`DTV_ISDBT_LAYERB_MODULATION <DTV-ISDBT-LAYER-MODULATION>`

-  :ref:`DTV_ISDBT_LAYERB_SEGMENT_COUNT <DTV-ISDBT-LAYER-SEGMENT-COUNT>`

-  :ref:`DTV_ISDBT_LAYERB_TIME_INTERLEAVING <DTV-ISDBT-LAYER-TIME-INTERLEAVING>`

-  :ref:`DTV_ISDBT_LAYERC_FEC <DTV-ISDBT-LAYER-FEC>`

-  :ref:`DTV_ISDBT_LAYERC_MODULATION <DTV-ISDBT-LAYER-MODULATION>`

-  :ref:`DTV_ISDBT_LAYERC_SEGMENT_COUNT <DTV-ISDBT-LAYER-SEGMENT-COUNT>`

-  :ref:`DTV_ISDBT_LAYERC_TIME_INTERLEAVING <DTV-ISDBT-LAYER-TIME-INTERLEAVING>`

In addition, the :ref:`DTV QoS statistics <frontend-stat-properties>` are also valid.


.. _atsc-params:

ATSC delivery system
====================

The following parameters are valid for ATSC:

-  :ref:`DTV_API_VERSION <DTV-API-VERSION>`

-  :ref:`DTV_DELIVERY_SYSTEM <DTV-DELIVERY-SYSTEM>`

-  :ref:`DTV_TUNE <DTV-TUNE>`

-  :ref:`DTV_CLEAR <DTV-CLEAR>`

-  :ref:`DTV_FREQUENCY <DTV-FREQUENCY>`

-  :ref:`DTV_MODULATION <DTV-MODULATION>`

-  :ref:`DTV_BANDWIDTH_HZ <DTV-BANDWIDTH-HZ>`

In addition, the :ref:`DTV QoS statistics <frontend-stat-properties>` are also valid.


.. _atscmh-params:

ATSC-MH delivery system
=======================

The following parameters are valid for ATSC-MH:

-  :ref:`DTV_API_VERSION <DTV-API-VERSION>`

-  :ref:`DTV_DELIVERY_SYSTEM <DTV-DELIVERY-SYSTEM>`

-  :ref:`DTV_TUNE <DTV-TUNE>`

-  :ref:`DTV_CLEAR <DTV-CLEAR>`

-  :ref:`DTV_FREQUENCY <DTV-FREQUENCY>`

-  :ref:`DTV_BANDWIDTH_HZ <DTV-BANDWIDTH-HZ>`

-  :ref:`DTV_ATSCMH_FIC_VER <DTV-ATSCMH-FIC-VER>`

-  :ref:`DTV_ATSCMH_PARADE_ID <DTV-ATSCMH-PARADE-ID>`

-  :ref:`DTV_ATSCMH_NOG <DTV-ATSCMH-NOG>`

-  :ref:`DTV_ATSCMH_TNOG <DTV-ATSCMH-TNOG>`

-  :ref:`DTV_ATSCMH_SGN <DTV-ATSCMH-SGN>`

-  :ref:`DTV_ATSCMH_PRC <DTV-ATSCMH-PRC>`

-  :ref:`DTV_ATSCMH_RS_FRAME_MODE <DTV-ATSCMH-RS-FRAME-MODE>`

-  :ref:`DTV_ATSCMH_RS_FRAME_ENSEMBLE <DTV-ATSCMH-RS-FRAME-ENSEMBLE>`

-  :ref:`DTV_ATSCMH_RS_CODE_MODE_PRI <DTV-ATSCMH-RS-CODE-MODE-PRI>`

-  :ref:`DTV_ATSCMH_RS_CODE_MODE_SEC <DTV-ATSCMH-RS-CODE-MODE-SEC>`

-  :ref:`DTV_ATSCMH_SCCC_BLOCK_MODE <DTV-ATSCMH-SCCC-BLOCK-MODE>`

-  :ref:`DTV_ATSCMH_SCCC_CODE_MODE_A <DTV-ATSCMH-SCCC-CODE-MODE-A>`

-  :ref:`DTV_ATSCMH_SCCC_CODE_MODE_B <DTV-ATSCMH-SCCC-CODE-MODE-B>`

-  :ref:`DTV_ATSCMH_SCCC_CODE_MODE_C <DTV-ATSCMH-SCCC-CODE-MODE-C>`

-  :ref:`DTV_ATSCMH_SCCC_CODE_MODE_D <DTV-ATSCMH-SCCC-CODE-MODE-D>`

In addition, the :ref:`DTV QoS statistics <frontend-stat-properties>` are also valid.


.. _dtmb-params:

DTMB delivery system
====================

The following parameters are valid for DTMB:

-  :ref:`DTV_API_VERSION <DTV-API-VERSION>`

-  :ref:`DTV_DELIVERY_SYSTEM <DTV-DELIVERY-SYSTEM>`

-  :ref:`DTV_TUNE <DTV-TUNE>`

-  :ref:`DTV_CLEAR <DTV-CLEAR>`

-  :ref:`DTV_FREQUENCY <DTV-FREQUENCY>`

-  :ref:`DTV_MODULATION <DTV-MODULATION>`

-  :ref:`DTV_BANDWIDTH_HZ <DTV-BANDWIDTH-HZ>`

-  :ref:`DTV_INVERSION <DTV-INVERSION>`

-  :ref:`DTV_INNER_FEC <DTV-INNER-FEC>`

-  :ref:`DTV_GUARD_INTERVAL <DTV-GUARD-INTERVAL>`

-  :ref:`DTV_TRANSMISSION_MODE <DTV-TRANSMISSION-MODE>`

-  :ref:`DTV_INTERLEAVING <DTV-INTERLEAVING>`

-  :ref:`DTV_LNA <DTV-LNA>`

In addition, the :ref:`DTV QoS statistics <frontend-stat-properties>` are also valid.


.. _frontend-property-cable-systems:

Properties used on cable delivery systems
=========================================


.. _dvbc-params:

DVB-C delivery system
=====================

The DVB-C Annex-A is the widely used cable standard. Transmission uses QAM modulation.

The DVB-C Annex-C is optimized for 6MHz, and is used in Japan. It supports a subset of the Annex A modulation types, and a roll-off of 0.13, instead of 0.15

The following parameters are valid for DVB-C Annex A/C:

-  :ref:`DTV_API_VERSION <DTV-API-VERSION>`

-  :ref:`DTV_DELIVERY_SYSTEM <DTV-DELIVERY-SYSTEM>`

-  :ref:`DTV_TUNE <DTV-TUNE>`

-  :ref:`DTV_CLEAR <DTV-CLEAR>`

-  :ref:`DTV_FREQUENCY <DTV-FREQUENCY>`

-  :ref:`DTV_MODULATION <DTV-MODULATION>`

-  :ref:`DTV_INVERSION <DTV-INVERSION>`

-  :ref:`DTV_SYMBOL_RATE <DTV-SYMBOL-RATE>`

-  :ref:`DTV_INNER_FEC <DTV-INNER-FEC>`

-  :ref:`DTV_LNA <DTV-LNA>`

In addition, the :ref:`DTV QoS statistics <frontend-stat-properties>` are also valid.


.. _dvbc-annex-b-params:

DVB-C Annex B delivery system
=============================

The DVB-C Annex-B is only used on a few Countries like the United States.

The following parameters are valid for DVB-C Annex B:

-  :ref:`DTV_API_VERSION <DTV-API-VERSION>`

-  :ref:`DTV_DELIVERY_SYSTEM <DTV-DELIVERY-SYSTEM>`

-  :ref:`DTV_TUNE <DTV-TUNE>`

-  :ref:`DTV_CLEAR <DTV-CLEAR>`

-  :ref:`DTV_FREQUENCY <DTV-FREQUENCY>`

-  :ref:`DTV_MODULATION <DTV-MODULATION>`

-  :ref:`DTV_INVERSION <DTV-INVERSION>`

-  :ref:`DTV_LNA <DTV-LNA>`

In addition, the :ref:`DTV QoS statistics <frontend-stat-properties>` are also valid.


.. _frontend-property-satellite-systems:

Properties used on satellite delivery systems
=============================================


.. _dvbs-params:

DVB-S delivery system
=====================

The following parameters are valid for DVB-S:

-  :ref:`DTV_API_VERSION <DTV-API-VERSION>`

-  :ref:`DTV_DELIVERY_SYSTEM <DTV-DELIVERY-SYSTEM>`

-  :ref:`DTV_TUNE <DTV-TUNE>`

-  :ref:`DTV_CLEAR <DTV-CLEAR>`

-  :ref:`DTV_FREQUENCY <DTV-FREQUENCY>`

-  :ref:`DTV_INVERSION <DTV-INVERSION>`

-  :ref:`DTV_SYMBOL_RATE <DTV-SYMBOL-RATE>`

-  :ref:`DTV_INNER_FEC <DTV-INNER-FEC>`

-  :ref:`DTV_VOLTAGE <DTV-VOLTAGE>`

-  :ref:`DTV_TONE <DTV-TONE>`

In addition, the :ref:`DTV QoS statistics <frontend-stat-properties>` are also valid.

Future implementations might add those two missing parameters:

-  :ref:`DTV_DISEQC_MASTER <DTV-DISEQC-MASTER>`

-  :ref:`DTV_DISEQC_SLAVE_REPLY <DTV-DISEQC-SLAVE-REPLY>`


.. _dvbs2-params:

DVB-S2 delivery system
======================

In addition to all parameters valid for DVB-S, DVB-S2 supports the following parameters:

-  :ref:`DTV_MODULATION <DTV-MODULATION>`

-  :ref:`DTV_PILOT <DTV-PILOT>`

-  :ref:`DTV_ROLLOFF <DTV-ROLLOFF>`

-  :ref:`DTV_STREAM_ID <DTV-STREAM-ID>`

In addition, the :ref:`DTV QoS statistics <frontend-stat-properties>` are also valid.


.. _turbo-params:

Turbo code delivery system
==========================

In addition to all parameters valid for DVB-S, turbo code supports the following parameters:

-  :ref:`DTV_MODULATION <DTV-MODULATION>`


.. _isdbs-params:

ISDB-S delivery system
======================

The following parameters are valid for ISDB-S:

-  :ref:`DTV_API_VERSION <DTV-API-VERSION>`

-  :ref:`DTV_DELIVERY_SYSTEM <DTV-DELIVERY-SYSTEM>`

-  :ref:`DTV_TUNE <DTV-TUNE>`

-  :ref:`DTV_CLEAR <DTV-CLEAR>`

-  :ref:`DTV_FREQUENCY <DTV-FREQUENCY>`

-  :ref:`DTV_INVERSION <DTV-INVERSION>`

-  :ref:`DTV_SYMBOL_RATE <DTV-SYMBOL-RATE>`

-  :ref:`DTV_INNER_FEC <DTV-INNER-FEC>`

-  :ref:`DTV_VOLTAGE <DTV-VOLTAGE>`

-  :ref:`DTV_STREAM_ID <DTV-STREAM-ID>`

.. _libdvbv5: https://linuxtv.org/docs/libdvbv5/index.html
