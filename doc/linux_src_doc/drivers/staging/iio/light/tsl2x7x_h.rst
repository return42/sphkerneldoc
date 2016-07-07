.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/iio/light/tsl2x7x.h

.. _`tsl2x7x_settings`:

struct tsl2x7x_settings
=======================

.. c:type:: struct tsl2x7x_settings

    power on defaults unless overridden by platform data.

.. _`tsl2x7x_settings.definition`:

Definition
----------

.. code-block:: c

    struct tsl2x7x_settings {
        int als_time;
        int als_gain;
        int als_gain_trim;
        int wait_time;
        int prx_time;
        int prox_gain;
        int prox_config;
        int als_cal_target;
        u8 interrupts_en;
        u8 persistence;
        int als_thresh_low;
        int als_thresh_high;
        int prox_thres_low;
        int prox_thres_high;
        int prox_pulse_count;
        int prox_max_samples_cal;
    }

.. _`tsl2x7x_settings.members`:

Members
-------

als_time
    ALS Integration time - multiple of 50mS

als_gain
    Index into the ALS gain table.

als_gain_trim
    default gain trim to account for
    aperture effects.

wait_time
    Time between PRX and ALS cycles
    in 2.7 periods

prx_time
    5.2ms prox integration time -
    decrease in 2.7ms periods

prox_gain
    *undescribed*

prox_config
    Prox configuration filters.

als_cal_target
    Known external ALS reading for
    calibration.

interrupts_en
    Enable/Disable - 0x00 = none, 0x10 = als,
    0x20 = prx,  0x30 = bth

persistence
    H/W Filters, Number of 'out of limits'
    ADC readings PRX/ALS.

als_thresh_low
    CH0 'low' count to trigger interrupt.

als_thresh_high
    CH0 'high' count to trigger interrupt.

prox_thres_low
    Low threshold proximity detection.

prox_thres_high
    High threshold proximity detection

prox_pulse_count
    Number if proximity emitter pulses

prox_max_samples_cal
    Used for prox cal.

.. _`tsl2x7x_platform_data`:

struct tsl2X7X_platform_data
============================

.. c:type:: struct tsl2X7X_platform_data

    Platform callback, glass and defaults

.. _`tsl2x7x_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct tsl2X7X_platform_data {
        int (* platform_power) (struct device *dev, pm_message_t);
        int (* power_on) (struct iio_dev *indio_dev);
        int (* power_off) (struct i2c_client *dev);
        struct tsl2x7x_lux platform_lux_table[TSL2X7X_MAX_LUX_TABLE_SIZE];
        struct tsl2x7x_settings *platform_default_settings;
    }

.. _`tsl2x7x_platform_data.members`:

Members
-------

platform_power
    Suspend/resume platform callback

power_on
    Power on callback

power_off
    Power off callback

platform_lux_table
    Device specific glass coefficents

platform_default_settings
    Device specific power on defaults

.. This file was automatic generated / don't edit.

