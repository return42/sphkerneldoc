.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/dac/stm32-dac-core.h

.. _`stm32_dac_common`:

struct stm32_dac_common
=======================

.. c:type:: struct stm32_dac_common

    stm32 DAC driver common data (for all instances)

.. _`stm32_dac_common.definition`:

Definition
----------

.. code-block:: c

    struct stm32_dac_common {
        struct regmap *regmap;
        int vref_mv;
        bool hfsel;
    }

.. _`stm32_dac_common.members`:

Members
-------

regmap
    DAC registers shared via regmap

vref_mv
    reference voltage (mv)

hfsel
    high speed bus clock selected

.. This file was automatic generated / don't edit.

