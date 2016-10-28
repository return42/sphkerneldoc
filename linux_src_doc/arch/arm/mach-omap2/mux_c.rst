.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/mux.c

.. _`omap_hwmod_mux_scan_wakeups`:

omap_hwmod_mux_scan_wakeups
===========================

.. c:function:: bool omap_hwmod_mux_scan_wakeups(struct omap_hwmod_mux_info *hmux, struct omap_hwmod_irq_info *mpu_irqs)

    omap hwmod scan wakeup pads

    :param struct omap_hwmod_mux_info \*hmux:
        Pads for a hwmod

    :param struct omap_hwmod_irq_info \*mpu_irqs:
        MPU irq array for a hwmod

.. _`omap_hwmod_mux_scan_wakeups.description`:

Description
-----------

Scans the wakeup status of pads for a single hwmod.  If an irq
array is defined for this mux, the parser will call the registered
ISRs for corresponding pads, otherwise the parser will stop at the
first wakeup active pad and return.  Returns true if there is a
pending and non-served wakeup event for the mux, otherwise false.

.. _`_omap_hwmod_mux_handle_irq`:

_omap_hwmod_mux_handle_irq
==========================

.. c:function:: int _omap_hwmod_mux_handle_irq(struct omap_hwmod *oh, void *data)

    Process wakeup events for a single hwmod

    :param struct omap_hwmod \*oh:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`_omap_hwmod_mux_handle_irq.description`:

Description
-----------

Checks a single hwmod for every wakeup capable pad to see if there is an
active wakeup event. If this is the case, call the corresponding ISR.

.. _`omap_hwmod_mux_handle_irq`:

omap_hwmod_mux_handle_irq
=========================

.. c:function:: irqreturn_t omap_hwmod_mux_handle_irq(int irq, void *unused)

    Process pad wakeup irqs.

    :param int irq:
        *undescribed*

    :param void \*unused:
        *undescribed*

.. _`omap_hwmod_mux_handle_irq.description`:

Description
-----------

Calls a function for each registered omap_hwmod to check
pad wakeup statuses.

.. This file was automatic generated / don't edit.

