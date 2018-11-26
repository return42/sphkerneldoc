.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/wd_timer.c

.. _`omap2_wd_timer_reset`:

omap2_wd_timer_reset
====================

.. c:function:: int omap2_wd_timer_reset(struct omap_hwmod *oh)

    reset and disable the WDTIMER IP block

    :param oh:
        struct omap_hwmod \*
    :type oh: struct omap_hwmod \*

.. _`omap2_wd_timer_reset.description`:

Description
-----------

After the WDTIMER IP blocks are reset on OMAP2/3, we must also take
care to execute the special watchdog disable sequence.  This is
because the watchdog is re-armed upon OCP softreset.  (On OMAP4,
this behavior was apparently changed and the watchdog is no longer
re-armed after an OCP soft-reset.)  Returns -ETIMEDOUT if the reset
did not complete, or 0 upon success.

XXX Most of this code should be moved to the omap_hwmod.c layer
during a normal merge window.  \ :c:func:`omap_hwmod_softreset`\  should be
renamed to \ :c:func:`omap_hwmod_set_ocp_softreset`\ , and \ :c:func:`omap_hwmod_softreset`\ 
should call the hwmod \_ocp_softreset() code.

.. This file was automatic generated / don't edit.

