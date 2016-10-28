.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap1/reset.c

.. _`omap1_get_reset_sources`:

omap1_get_reset_sources
=======================

.. c:function:: u32 omap1_get_reset_sources( void)

    return the source of the SoC's last reset

    :param  void:
        no arguments

.. _`omap1_get_reset_sources.description`:

Description
-----------

Returns bits that represent the last reset source for the SoC.  The
format is standardized across OMAPs for use by the OMAP watchdog.

.. This file was automatic generated / don't edit.

