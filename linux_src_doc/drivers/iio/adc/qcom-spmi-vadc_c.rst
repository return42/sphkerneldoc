.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/qcom-spmi-vadc.c

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
        enum vadc_scale_fn_type scale_fn_type;
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

scale_fn_type
    Represents the scaling function to convert voltage
    physical units desired by the client for the channel.

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
        struct vadc_linear_graph graph;
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

