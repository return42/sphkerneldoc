.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/stm32-adc-core.c

.. _`stm32_adc_priv`:

struct stm32_adc_priv
=====================

.. c:type:: struct stm32_adc_priv

    stm32 ADC core private data

.. _`stm32_adc_priv.definition`:

Definition
----------

.. code-block:: c

    struct stm32_adc_priv {
        int irq[STM32_ADC_MAX_ADCS];
        struct irq_domain *domain;
        struct clk *aclk;
        struct clk *bclk;
        struct regulator *vref;
        const struct stm32_adc_priv_cfg *cfg;
        struct stm32_adc_common common;
    }

.. _`stm32_adc_priv.members`:

Members
-------

irq
    irq(s) for ADC block

domain
    irq domain reference

aclk
    clock reference for the analog circuitry

bclk
    bus clock common for all ADCs, depends on part used

vref
    regulator reference

cfg
    compatible configuration data

common
    common data for all ADC instances

.. _`stm32f4_adc_clk_sel`:

stm32f4_adc_clk_sel
===================

.. c:function:: int stm32f4_adc_clk_sel(struct platform_device *pdev, struct stm32_adc_priv *priv)

    Select stm32f4 ADC common clock prescaler

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

    :param priv:
        stm32 ADC core private data
        Select clock prescaler used for analog conversions, before using ADC.
    :type priv: struct stm32_adc_priv \*

.. _`stm32h7_adc_ck_spec`:

struct stm32h7_adc_ck_spec
==========================

.. c:type:: struct stm32h7_adc_ck_spec

    specification for stm32h7 adc clock

.. _`stm32h7_adc_ck_spec.definition`:

Definition
----------

.. code-block:: c

    struct stm32h7_adc_ck_spec {
        u32 ckmode;
        u32 presc;
        int div;
    }

.. _`stm32h7_adc_ck_spec.members`:

Members
-------

ckmode
    ADC clock mode, Async or sync with prescaler.

presc
    prescaler bitfield for async clock mode

div
    prescaler division ratio

.. This file was automatic generated / don't edit.

