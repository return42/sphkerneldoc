.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-omap/include/plat/dmtimer.h

.. _`__omap_dm_timer_override_errata`:

__omap_dm_timer_override_errata
===============================

.. c:function:: void __omap_dm_timer_override_errata(struct omap_dm_timer *timer, u32 errata)

    override errata flags for a timer

    :param struct omap_dm_timer \*timer:
        pointer to timer handle

    :param u32 errata:
        errata flags to be ignored

.. _`__omap_dm_timer_override_errata.description`:

Description
-----------

For a given timer, override a timer errata by clearing the flags
specified by the errata argument. A specific erratum should only be
overridden for a timer if the timer is used in such a way the erratum
has no impact.

.. This file was automatic generated / don't edit.

