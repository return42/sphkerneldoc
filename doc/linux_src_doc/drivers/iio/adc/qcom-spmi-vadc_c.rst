.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/qcom-spmi-vadc.c

.. _`vadc_linear_graph`:

struct vadc_linear_graph
========================

.. c:type:: struct vadc_linear_graph

    Represent ADC characteristics.

.. _`vadc_linear_graph.definition`:

Definition
----------

.. code-block:: c

    struct vadc_linear_graph {
        s32 dy;
        s32 dx;
        s32 gnd;
    }

.. _`vadc_linear_graph.members`:

Members
-------

dy
    numerator slope to calculate the gain.

dx
    denominator slope to calculate the gain.

gnd
    A/D word of the ground reference used for the channel.

.. _`vadc_linear_graph.description`:

Description
-----------

Each ADC device has different offset and gain parameters which are
computed to calibrate the device.

.. _`vadc_prescale_ratio`:

struct vadc_prescale_ratio
==========================

.. c:type:: struct vadc_prescale_ratio

    Represent scaling ratio for ADC input.

.. _`vadc_prescale_ratio.definition`:

Definition
----------

.. code-block:: c

    struct vadc_prescale_ratio {
        u32 num;
        u32 den;
    }

.. _`vadc_prescale_ratio.members`:

Members
-------

num
    the inverse numerator of the gain applied to the input channel.

den
    the inverse denominator of the gain applied to the input channel.

.. _`vadc_channel_prop`:

struct vadc_channel_prop
========================

.. c:type:: struct vadc_channel_prop

    VADC channel property.

.. _`vadc_channel_prop.definition`:

Definition
----------

.. code-block:: c

    struct vadc_channel_prop {
        unsigned int channel;
        enum vadc_calibration calibration;
        unsigned int decimation;
        unsigned int prescale;
        unsigned int hw_settle_time;
        unsigned int avg_samples;
    }

.. _`vadc_channel_prop.members`:

Members
-------

channel
    channel number, refer to the channel list.

calibration
    calibration type.

decimation
    sampling rate supported for the channel.

prescale
    channel scaling performed on the input signal.

hw_settle_time
    the time between AMUX being configured and the
    start of conversion.

avg_samples
    ability to provide single result from the ADC
    that is an average of multiple measurements.

.. _`vadc_priv`:

struct vadc_priv
================

.. c:type:: struct vadc_priv

    VADC private structure.

.. _`vadc_priv.definition`:

Definition
----------

.. code-block:: c

    struct vadc_priv {
        struct regmap *regmap;
        struct device *dev;
        u16 base;
        unsigned int nchannels;
        struct vadc_channel_prop *chan_props;
        struct iio_chan_spec *iio_chans;
        bool are_ref_measured;
        bool poll_eoc;
        struct completion complete;
        struct vadc_linear_graph graph[2];
        struct mutex lock;
    }

.. _`vadc_priv.members`:

Members
-------

regmap
    pointer to struct regmap.

dev
    pointer to struct device.

base
    base address for the ADC peripheral.

nchannels
    number of VADC channels.

chan_props
    array of VADC channel properties.

iio_chans
    array of IIO channels specification.

are_ref_measured
    are reference points measured.

poll_eoc
    use polling instead of interrupt.

complete
    VADC result notification after interrupt is received.

graph
    store parameters for calibration.

lock
    ADC lock for access to the peripheral.

.. This file was automatic generated / don't edit.

