.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/qcom-pm8xxx-xoadc.c

.. _`pm8xxx_channel_internal`:

PM8XXX_CHANNEL_INTERNAL
=======================

.. c:function::  PM8XXX_CHANNEL_INTERNAL()

    proper reference points for calibration.

.. _`xoadc_channel`:

struct xoadc_channel
====================

.. c:type:: struct xoadc_channel

    encodes channel properties and defaults

.. _`xoadc_channel.definition`:

Definition
----------

.. code-block:: c

    struct xoadc_channel {
        const char *datasheet_name;
        u8 pre_scale_mux:2;
        u8 amux_channel:4;
        const struct vadc_prescale_ratio prescale;
        enum iio_chan_type type;
        enum vadc_scale_fn_type scale_fn_type;
        u8 amux_ip_rsv:3;
    }

.. _`xoadc_channel.members`:

Members
-------

datasheet_name
    the hardwarename of this channel

pre_scale_mux
    prescale (PM8058) or premux (PM8921) for selecting
    this channel. Both this and the amux channel is needed to uniquely
    identify a channel. Values 0..3.

amux_channel
    value of the ADC_ARB_USRP_AMUX_CNTRL register for this
    channel, bits 4..7, selects the amux, values 0..f

prescale
    the channels have hard-coded prescale ratios defined
    by the hardware, this tells us what it is

type
    corresponding IIO channel type, usually IIO_VOLTAGE or
    IIO_TEMP

scale_fn_type
    the liner interpolation etc to convert the
    ADC code to the value that IIO expects, in uV or millicelsius
    etc. This scale function can be pretty elaborate if different
    thermistors are connected or other hardware characteristics are
    deployed.

amux_ip_rsv
    ratiometric scale value used by the analog muxer: this
    selects the reference voltage for ratiometric scaling

.. _`xoadc_variant`:

struct xoadc_variant
====================

.. c:type:: struct xoadc_variant

    encodes the XOADC variant characteristics

.. _`xoadc_variant.definition`:

Definition
----------

.. code-block:: c

    struct xoadc_variant {
        const char name;
        const struct xoadc_channel *channels;
        bool broken_ratiometric;
        bool prescaling;
        bool second_level_mux;
    }

.. _`xoadc_variant.members`:

Members
-------

name
    name of this PMIC variant

channels
    the hardware channels and respective settings and defaults

broken_ratiometric
    if the PMIC has broken ratiometric scaling (this
    is a known problem on PM8058)

prescaling
    this variant uses AMUX bits 2 & 3 for prescaling (PM8058)

second_level_mux
    this variant uses AMUX bits 2 & 3 for a second level
    mux

.. _`pm8xxx_chan_info`:

struct pm8xxx_chan_info
=======================

.. c:type:: struct pm8xxx_chan_info

    ADC channel information

.. _`pm8xxx_chan_info.definition`:

Definition
----------

.. code-block:: c

    struct pm8xxx_chan_info {
        const char *name;
        const struct xoadc_channel *hwchan;
        enum vadc_calibration calibration;
        u8 decimation:2;
        u8 amux_ip_rsv:3;
    }

.. _`pm8xxx_chan_info.members`:

Members
-------

name
    name of this channel

hwchan
    pointer to hardware channel information (muxing & scaling settings)

calibration
    whether to use absolute or ratiometric calibration

decimation
    0,1,2,3

amux_ip_rsv
    ratiometric scale value if using ratiometric

.. _`pm8xxx_chan_info.calibration`:

calibration
-----------

0, 1, 2, 4, 5.

.. _`pm8xxx_xoadc`:

struct pm8xxx_xoadc
===================

.. c:type:: struct pm8xxx_xoadc

    state container for the XOADC

.. _`pm8xxx_xoadc.definition`:

Definition
----------

.. code-block:: c

    struct pm8xxx_xoadc {
        struct device *dev;
        struct regmap *map;
        const struct xoadc_variant *variant;
        struct regulator *vref;
        unsigned int nchans;
        struct pm8xxx_chan_info *chans;
        struct iio_chan_spec *iio_chans;
        struct vadc_linear_graph graph;
        struct completion complete;
        struct mutex lock;
    }

.. _`pm8xxx_xoadc.members`:

Members
-------

dev
    pointer to device

map
    regmap to access registers

variant
    *undescribed*

vref
    reference voltage regulator
    characteristics of the channels, and sensible default settings

nchans
    number of channels, configured by the device tree

chans
    the channel information per-channel, configured by the device tree

iio_chans
    IIO channel specifiers

graph
    linear calibration parameters for absolute and
    ratiometric measurements

complete
    completion to indicate end of conversion

lock
    lock to restrict access to the hardware to one client at the time

.. This file was automatic generated / don't edit.

