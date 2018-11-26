.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/qcom-spmi-adc5.c

.. _`adc5_channel_prop`:

struct adc5_channel_prop
========================

.. c:type:: struct adc5_channel_prop

    ADC channel property.

.. _`adc5_channel_prop.definition`:

Definition
----------

.. code-block:: c

    struct adc5_channel_prop {
        unsigned int channel;
        enum adc5_cal_method cal_method;
        enum adc5_cal_val cal_val;
        unsigned int decimation;
        unsigned int prescale;
        unsigned int hw_settle_time;
        unsigned int avg_samples;
        enum vadc_scale_fn_type scale_fn_type;
        const char *datasheet_name;
    }

.. _`adc5_channel_prop.members`:

Members
-------

channel
    channel number, refer to the channel list.

cal_method
    calibration method.

cal_val
    calibration value

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

datasheet_name
    Channel name used in device tree.

.. _`adc5_chip`:

struct adc5_chip
================

.. c:type:: struct adc5_chip

    ADC private structure.

.. _`adc5_chip.definition`:

Definition
----------

.. code-block:: c

    struct adc5_chip {
        struct regmap *regmap;
        struct device *dev;
        u16 base;
        unsigned int nchannels;
        struct adc5_channel_prop *chan_props;
        struct iio_chan_spec *iio_chans;
        bool poll_eoc;
        struct completion complete;
        struct mutex lock;
        const struct adc5_data *data;
    }

.. _`adc5_chip.members`:

Members
-------

regmap
    SPMI ADC5 peripheral register map field.

dev
    SPMI ADC5 device.

base
    base address for the ADC peripheral.

nchannels
    number of ADC channels.

chan_props
    array of ADC channel properties.

iio_chans
    array of IIO channels specification.

poll_eoc
    use polling instead of interrupt.

complete
    ADC result notification after interrupt is received.

lock
    ADC lock for access to the peripheral.

data
    software configuration data.

.. This file was automatic generated / don't edit.

