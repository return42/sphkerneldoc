.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/palmas_gpadc.c

.. _`palmas_gpadc`:

struct palmas_gpadc
===================

.. c:type:: struct palmas_gpadc

    the palmas_gpadc structure

.. _`palmas_gpadc.definition`:

Definition
----------

.. code-block:: c

    struct palmas_gpadc {
        struct device *dev;
        struct palmas *palmas;
        u8 ch0_current;
        u8 ch3_current;
        bool extended_delay;
        int irq;
        int irq_auto_0;
        int irq_auto_1;
        struct palmas_gpadc_info *adc_info;
        struct completion conv_completion;
        struct palmas_adc_wakeup_property wakeup1_data;
        struct palmas_adc_wakeup_property wakeup2_data;
        bool wakeup1_enable;
        bool wakeup2_enable;
        int auto_conversion_period;
    }

.. _`palmas_gpadc.members`:

Members
-------

dev
    *undescribed*

palmas
    *undescribed*

ch0_current
    channel 0 current source setting
    0: 0 uA
    1: 5 uA
    2: 15 uA
    3: 20 uA

ch3_current
    channel 0 current source setting
    0: 0 uA
    1: 10 uA
    2: 400 uA
    3: 800 uA

extended_delay
    enable the gpadc extended delay mode

irq
    *undescribed*

irq_auto_0
    *undescribed*

irq_auto_1
    *undescribed*

adc_info
    *undescribed*

conv_completion
    *undescribed*

wakeup1_data
    *undescribed*

wakeup2_data
    *undescribed*

wakeup1_enable
    *undescribed*

wakeup2_enable
    *undescribed*

auto_conversion_period
    define the auto_conversion_period

.. _`palmas_gpadc.description`:

Description
-----------

This is the palmas_gpadc structure to store run-time information
and pointers for this driver instance.

.. This file was automatic generated / don't edit.

