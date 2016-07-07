.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pwm/pwm-spear.c

.. _`spear_pwm_chip`:

struct spear_pwm_chip
=====================

.. c:type:: struct spear_pwm_chip

    struct representing pwm chip

.. _`spear_pwm_chip.definition`:

Definition
----------

.. code-block:: c

    struct spear_pwm_chip {
        void __iomem *mmio_base;
        struct clk *clk;
        struct pwm_chip chip;
    }

.. _`spear_pwm_chip.members`:

Members
-------

mmio_base
    base address of pwm chip

clk
    pointer to clk structure of pwm chip

chip
    linux pwm chip representation

.. This file was automatic generated / don't edit.

