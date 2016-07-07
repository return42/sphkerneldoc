.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-exynos/suspend.c

.. _`exynos_wkup_irq`:

struct exynos_wkup_irq
======================

.. c:type:: struct exynos_wkup_irq

    PMU IRQ to mask mapping

.. _`exynos_wkup_irq.definition`:

Definition
----------

.. code-block:: c

    struct exynos_wkup_irq {
        unsigned int hwirq;
        u32 mask;
    }

.. _`exynos_wkup_irq.members`:

Members
-------

hwirq
    Hardware IRQ signal of the PMU

mask
    Mask in PMU wake-up mask register

.. This file was automatic generated / don't edit.

