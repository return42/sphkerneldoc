.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/qcom-spmi-iadc.c

.. _`iadc_chip`:

struct iadc_chip
================

.. c:type:: struct iadc_chip

    IADC Current ADC device structure.

.. _`iadc_chip.definition`:

Definition
----------

.. code-block:: c

    struct iadc_chip {
        struct regmap *regmap;
        struct device *dev;
        u16 base;
        bool poll_eoc;
        u32 rsense;
        u16 offset;
        u16 gain;
        struct mutex lock;
        struct completion complete;
    }

.. _`iadc_chip.members`:

Members
-------

regmap
    regmap for register read/write.

dev
    This device pointer.

base
    base offset for the ADC peripheral.

poll_eoc
    Poll for end of conversion instead of waiting for IRQ.

rsense
    Values of the internal and external sense resister in micro Ohms.

offset
    Raw offset values for the internal and external channels.

gain
    Raw gain of the channels.

lock
    ADC lock for access to the peripheral.

complete
    ADC notification after end of conversion interrupt is received.

.. This file was automatic generated / don't edit.

