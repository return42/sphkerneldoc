.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/dac/stm32-dac-core.c

.. _`stm32_dac_priv`:

struct stm32_dac_priv
=====================

.. c:type:: struct stm32_dac_priv

    stm32 DAC core private data

.. _`stm32_dac_priv.definition`:

Definition
----------

.. code-block:: c

    struct stm32_dac_priv {
        struct clk *pclk;
        struct reset_control *rst;
        struct regulator *vref;
        struct stm32_dac_common common;
    }

.. _`stm32_dac_priv.members`:

Members
-------

pclk
    peripheral clock common for all DACs

rst
    peripheral reset control

vref
    regulator reference

common
    Common data for all DAC instances

.. This file was automatic generated / don't edit.

