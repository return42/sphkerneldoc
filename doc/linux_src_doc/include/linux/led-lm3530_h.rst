.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/led-lm3530.h

.. _`lm3530_platform_data`:

struct lm3530_platform_data
===========================

.. c:type:: struct lm3530_platform_data


.. _`lm3530_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct lm3530_platform_data {
        enum lm3530_mode mode;
        enum lm3530_als_mode als_input_mode;
        u8 max_current;
        bool pwm_pol_hi;
        u8 als_avrg_time;
        bool brt_ramp_law;
        u8 brt_ramp_fall;
        u8 brt_ramp_rise;
        u8 als1_resistor_sel;
        u8 als2_resistor_sel;
        u32 als_vmin;
        u32 als_vmax;
        u8 brt_val;
        struct lm3530_pwm_data pwm_data;
    }

.. _`lm3530_platform_data.members`:

Members
-------

mode
    mode of operation i.e. Manual, ALS or PWM

als_input_mode
    select source of ALS input - ALS1/2 or average

max_current
    full scale LED current

pwm_pol_hi
    PWM input polarity - active high/active low

als_avrg_time
    ALS input averaging time

brt_ramp_law
    brightness mapping mode - exponential/linear

brt_ramp_fall
    rate of fall of led current

brt_ramp_rise
    rate of rise of led current

als1_resistor_sel
    internal resistance from ALS1 input to ground

als2_resistor_sel
    internal resistance from ALS2 input to ground

als_vmin
    als input voltage calibrated for max brightness in mV

als_vmax
    als input voltage calibrated for min brightness in mV

brt_val
    brightness value (0-127)

pwm_data
    PWM control functions (only valid when the mode is PWM)

.. This file was automatic generated / don't edit.

