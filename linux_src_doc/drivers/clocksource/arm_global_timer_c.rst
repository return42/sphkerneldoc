.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clocksource/arm_global_timer.c

.. _`gt_compare_set`:

gt_compare_set
==============

.. c:function:: void gt_compare_set(unsigned long delta, int periodic)

    :param unsigned long delta:
        *undescribed*

    :param int periodic:
        *undescribed*

.. _`gt_compare_set.interrupt-status-register-proceed-as-follows`:

Interrupt Status Register proceed as follows
--------------------------------------------

1. Clear the Comp Enable bit in the Timer Control Register.
2. Write the lower 32-bit Comparator Value Register.
3. Write the upper 32-bit Comparator Value Register.
4. Set the Comp Enable bit and, if necessary, the IRQ enable bit.

.. This file was automatic generated / don't edit.

