.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/twl6030-gpadc.c

.. _`twl6030_chnl_calib`:

struct twl6030_chnl_calib
=========================

.. c:type:: struct twl6030_chnl_calib

    channel calibration

.. _`twl6030_chnl_calib.definition`:

Definition
----------

.. code-block:: c

    struct twl6030_chnl_calib {
        s32 gain;
        s32 gain_error;
        s32 offset_error;
    }

.. _`twl6030_chnl_calib.members`:

Members
-------

gain
    slope coefficient for ideal curve

gain_error
    gain error

offset_error
    offset of the real curve

.. _`twl6030_ideal_code`:

struct twl6030_ideal_code
=========================

.. c:type:: struct twl6030_ideal_code

    GPADC calibration parameters

.. _`twl6030_ideal_code.definition`:

Definition
----------

.. code-block:: c

    struct twl6030_ideal_code {
        int channel;
        u16 code1;
        u16 code2;
        u16 volt1;
        u16 volt2;
    }

.. _`twl6030_ideal_code.members`:

Members
-------

channel
    channel number

code1
    ideal code for the input at the beginning

code2
    ideal code for at the end of the range

volt1
    voltage input at the beginning(low voltage)

volt2
    voltage input at the end(high voltage)

.. _`twl6030_ideal_code.gpadc-is-calibrated-in-two-points`:

GPADC is calibrated in two points
---------------------------------

close to the beginning and
to the and of the measurable input range

.. _`twl6030_gpadc_platform_data`:

struct twl6030_gpadc_platform_data
==================================

.. c:type:: struct twl6030_gpadc_platform_data

    platform specific data

.. _`twl6030_gpadc_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct twl6030_gpadc_platform_data {
        const int nchannels;
        const struct iio_chan_spec *iio_channels;
        const struct twl6030_ideal_code *ideal;
        int (*start_conversion)(int channel);
        u8 (*channel_to_reg)(int channel);
        int (*calibrate)(struct twl6030_gpadc_data *gpadc);
    }

.. _`twl6030_gpadc_platform_data.members`:

Members
-------

nchannels
    number of GPADC channels

iio_channels
    iio channels

ideal
    *undescribed*

start_conversion
    pointer to ADC start conversion function
    \ ``channel_to_reg``\       pointer to ADC function to convert channel to
    register address for reading conversion result

channel_to_reg
    *undescribed*

calibrate
    pointer to calibration function

.. _`twl6030_gpadc_data`:

struct twl6030_gpadc_data
=========================

.. c:type:: struct twl6030_gpadc_data

    GPADC data

.. _`twl6030_gpadc_data.definition`:

Definition
----------

.. code-block:: c

    struct twl6030_gpadc_data {
        struct device *dev;
        struct mutex lock;
        struct completion irq_complete;
        struct twl6030_chnl_calib *twl6030_cal_tbl;
        const struct twl6030_gpadc_platform_data *pdata;
    }

.. _`twl6030_gpadc_data.members`:

Members
-------

dev
    device pointer

lock
    mutual exclusion lock for the structure

irq_complete
    completion to signal end of conversion

twl6030_cal_tbl
    pointer to calibration data for each
    channel with gain error and offset

pdata
    pointer to device specific data

.. This file was automatic generated / don't edit.

