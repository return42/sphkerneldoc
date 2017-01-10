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
        int irq;
        struct irq_domain *domain;
        struct clk *aclk;
        struct regulator *vref;
        struct stm32_adc_common common;
    }

.. _`stm32_adc_priv.members`:

Members
-------

irq
    irq for ADC block

domain
    irq domain reference

aclk
    clock reference for the analog circuitry

vref
    regulator reference

common
    common data for all ADC instances

.. _`stm32f4_adc_clk_sel`:

stm32f4_adc_clk_sel
===================

.. c:function:: int stm32f4_adc_clk_sel(struct platform_device *pdev, struct stm32_adc_priv *priv)

    Select stm32f4 ADC common clock prescaler

    :param struct platform_device \*pdev:
        *undescribed*

    :param struct stm32_adc_priv \*priv:
        stm32 ADC core private data
        Select clock prescaler used for analog conversions, before using ADC.

.. This file was automatic generated / don't edit.

