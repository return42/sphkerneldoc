.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/stm32-adc-core.h

.. _`stm32_adc_common`:

struct stm32_adc_common
=======================

.. c:type:: struct stm32_adc_common

    stm32 ADC driver common data (for all instances)

.. _`stm32_adc_common.definition`:

Definition
----------

.. code-block:: c

    struct stm32_adc_common {
        void __iomem *base;
        phys_addr_t phys_base;
        unsigned long rate;
        int vref_mv;
    }

.. _`stm32_adc_common.members`:

Members
-------

base
    control registers base cpu addr

phys_base
    control registers base physical addr

rate
    clock rate used for analog circuitry

vref_mv
    vref voltage (mv)

.. This file was automatic generated / don't edit.

