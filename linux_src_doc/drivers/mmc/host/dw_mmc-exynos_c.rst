.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/dw_mmc-exynos.c

.. _`dw_mci_exynos_resume_noirq`:

dw_mci_exynos_resume_noirq
==========================

.. c:function:: int dw_mci_exynos_resume_noirq(struct device *dev)

    Exynos-specific resume code

    :param struct device \*dev:
        *undescribed*

.. _`dw_mci_exynos_resume_noirq.description`:

Description
-----------

On exynos5420 there is a silicon errata that will sometimes leave the
WAKEUP_INT bit in the CLKSEL register asserted.  This bit is 1 to indicate
that it fired and we can clear it by writing a 1 back.  Clear it to prevent
interrupts from going off constantly.

We run this code on all exynos variants because it doesn't hurt.

.. This file was automatic generated / don't edit.

