.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pwm/pwm-mediatek.c

.. _`mtk_pwm_chip`:

struct mtk_pwm_chip
===================

.. c:type:: struct mtk_pwm_chip

    struct representing PWM chip

.. _`mtk_pwm_chip.definition`:

Definition
----------

.. code-block:: c

    struct mtk_pwm_chip {
        struct pwm_chip chip;
        void __iomem *regs;
        struct clk  *clks;
    }

.. _`mtk_pwm_chip.members`:

Members
-------

chip
    linux PWM chip representation

regs
    base address of PWM chip

clks
    list of clocks

.. This file was automatic generated / don't edit.

