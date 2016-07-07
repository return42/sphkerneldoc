.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/touchscreen/stmpe-ts.c

.. _`stmpe_touch`:

struct stmpe_touch
==================

.. c:type:: struct stmpe_touch

    stmpe811 touch screen controller state

.. _`stmpe_touch.definition`:

Definition
----------

.. code-block:: c

    struct stmpe_touch {
        struct stmpe *stmpe;
        struct input_dev *idev;
        struct delayed_work work;
        struct device *dev;
        u8 sample_time;
        u8 mod_12b;
        u8 ref_sel;
        u8 adc_freq;
        u8 ave_ctrl;
        u8 touch_det_delay;
        u8 settling;
        u8 fraction_z;
        u8 i_drive;
    }

.. _`stmpe_touch.members`:

Members
-------

stmpe
    pointer back to STMPE MFD container

idev
    registered input device

work
    a work item used to scan the device

dev
    a pointer back to the MFD cell struct device\*

sample_time
    ADC converstion time in number of clock.
    (0 -> 36 clocks, 1 -> 44 clocks, 2 -> 56 clocks, 3 -> 64 clocks,
    4 -> 80 clocks, 5 -> 96 clocks, 6 -> 144 clocks),
    recommended is 4.

mod_12b
    ADC Bit mode (0 -> 10bit ADC, 1 -> 12bit ADC)

ref_sel
    ADC reference source
    (0 -> internal reference, 1 -> external reference)

adc_freq
    ADC Clock speed
    (0 -> 1.625 MHz, 1 -> 3.25 MHz, 2 \|\| 3 -> 6.5 MHz)

ave_ctrl
    Sample average control
    (0 -> 1 sample, 1 -> 2 samples, 2 -> 4 samples, 3 -> 8 samples)

touch_det_delay
    Touch detect interrupt delay
    (0 -> 10 us, 1 -> 50 us, 2 -> 100 us, 3 -> 500 us,
    4-> 1 ms, 5 -> 5 ms, 6 -> 10 ms, 7 -> 50 ms)
    recommended is 3

settling
    Panel driver settling time
    (0 -> 10 us, 1 -> 100 us, 2 -> 500 us, 3 -> 1 ms,
    4 -> 5 ms, 5 -> 10 ms, 6 for 50 ms, 7 -> 100 ms)
    recommended is 2

fraction_z
    Length of the fractional part in z
    (fraction_z ([0..7]) = Count of the fractional part)
    recommended is 7

i_drive
    current limit value of the touchscreen drivers
    (0 -> 20 mA typical 35 mA max, 1 -> 50 mA typical 80 mA max)

.. This file was automatic generated / don't edit.

