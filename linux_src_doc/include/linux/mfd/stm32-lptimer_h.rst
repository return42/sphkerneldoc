.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/stm32-lptimer.h

.. _`stm32_lptimer`:

struct stm32_lptimer
====================

.. c:type:: struct stm32_lptimer

    STM32 Low-Power Timer data assigned by parent device

.. _`stm32_lptimer.definition`:

Definition
----------

.. code-block:: c

    struct stm32_lptimer {
        struct clk *clk;
        struct regmap *regmap;
        bool has_encoder;
    }

.. _`stm32_lptimer.members`:

Members
-------

clk
    clock reference for this instance

regmap
    register map reference for this instance

has_encoder
    indicates this Low-Power Timer supports encoder mode

.. This file was automatic generated / don't edit.

