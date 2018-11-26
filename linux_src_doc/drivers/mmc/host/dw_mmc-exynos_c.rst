.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/dw_mmc-exynos.c

.. _`dw_mci_exynos_suspend_noirq`:

dw_mci_exynos_suspend_noirq
===========================

.. c:function:: int dw_mci_exynos_suspend_noirq(struct device *dev)

    Exynos-specific suspend code

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`dw_mci_exynos_suspend_noirq.description`:

Description
-----------

This ensures that device will be in runtime active state in
dw_mci_exynos_resume_noirq after calling \ :c:func:`pm_runtime_force_resume`\ 

.. _`dw_mci_exynos_resume_noirq`:

dw_mci_exynos_resume_noirq
==========================

.. c:function:: int dw_mci_exynos_resume_noirq(struct device *dev)

    Exynos-specific resume code

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`dw_mci_exynos_resume_noirq.description`:

Description
-----------

On exynos5420 there is a silicon errata that will sometimes leave the
WAKEUP_INT bit in the CLKSEL register asserted.  This bit is 1 to indicate
that it fired and we can clear it by writing a 1 back.  Clear it to prevent
interrupts from going off constantly.

We run this code on all exynos variants because it doesn't hurt.

.. This file was automatic generated / don't edit.

