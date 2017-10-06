.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pwm/pwm-samsung.c

.. _`samsung_pwm_channel`:

struct samsung_pwm_channel
==========================

.. c:type:: struct samsung_pwm_channel

    private data of PWM channel

.. _`samsung_pwm_channel.definition`:

Definition
----------

.. code-block:: c

    struct samsung_pwm_channel {
        u32 period_ns;
        u32 duty_ns;
        u32 tin_ns;
    }

.. _`samsung_pwm_channel.members`:

Members
-------

period_ns
    current period in nanoseconds programmed to the hardware

duty_ns
    current duty time in nanoseconds programmed to the hardware

tin_ns
    time of one timer tick in nanoseconds with current timer rate

.. _`samsung_pwm_chip`:

struct samsung_pwm_chip
=======================

.. c:type:: struct samsung_pwm_chip

    private data of PWM chip

.. _`samsung_pwm_chip.definition`:

Definition
----------

.. code-block:: c

    struct samsung_pwm_chip {
        struct pwm_chip chip;
        struct samsung_pwm_variant variant;
        u8 inverter_mask;
        u8 disabled_mask;
        void __iomem *base;
        struct clk *base_clk;
        struct clk *tclk0;
        struct clk *tclk1;
    }

.. _`samsung_pwm_chip.members`:

Members
-------

chip
    generic PWM chip

variant
    local copy of hardware variant data

inverter_mask
    inverter status for all channels - one bit per channel

disabled_mask
    disabled status for all channels - one bit per channel

base
    base address of mapped PWM registers

base_clk
    base clock used to drive the timers

tclk0
    external clock 0 (can be ERR_PTR if not present)

tclk1
    external clock 1 (can be ERR_PTR if not present)

.. This file was automatic generated / don't edit.

