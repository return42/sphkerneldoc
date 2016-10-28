.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/pm.c

.. _`omap2_oscillator`:

struct omap2_oscillator
=======================

.. c:type:: struct omap2_oscillator

    Describe the board main oscillator latencies

.. _`omap2_oscillator.definition`:

Definition
----------

.. code-block:: c

    struct omap2_oscillator {
        u32 startup_time;
        u32 shutdown_time;
    }

.. _`omap2_oscillator.members`:

Members
-------

startup_time
    oscillator startup latency

shutdown_time
    oscillator shutdown latency

.. _`omap_common_suspend_init`:

omap_common_suspend_init
========================

.. c:function:: void omap_common_suspend_init(void *pm_suspend)

    Set common suspend routines for OMAP SoCs

    :param void \*pm_suspend:
        function pointer to SoC specific suspend function

.. This file was automatic generated / don't edit.

