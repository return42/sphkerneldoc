.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/clocksource/timer-ti-dm.h

.. _`__omap_dm_timer_override_errata`:

\__omap_dm_timer_override_errata
================================

.. c:function:: void __omap_dm_timer_override_errata(struct omap_dm_timer *timer, u32 errata)

    override errata flags for a timer

    :param timer:
        pointer to timer handle
    :type timer: struct omap_dm_timer \*

    :param errata:
        errata flags to be ignored
    :type errata: u32

.. _`__omap_dm_timer_override_errata.description`:

Description
-----------

For a given timer, override a timer errata by clearing the flags
specified by the errata argument. A specific erratum should only be
overridden for a timer if the timer is used in such a way the erratum
has no impact.

.. This file was automatic generated / don't edit.

