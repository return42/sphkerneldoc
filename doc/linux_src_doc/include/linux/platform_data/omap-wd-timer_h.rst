.. -*- coding: utf-8; mode: rst -*-

===============
omap-wd-timer.h
===============


.. _`omap_wd_timer_platform_data`:

struct omap_wd_timer_platform_data
==================================

.. c:type:: omap_wd_timer_platform_data

    WDTIMER integration to the host SoC @read_reset_sources - fn ptr for the SoC to indicate the last reset cause


.. _`omap_wd_timer_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct omap_wd_timer_platform_data {
  };


.. _`omap_wd_timer_platform_data.members`:

Members
-------




.. _`omap_wd_timer_platform_data.description`:

Description
-----------


The function pointed to by ``read_reset_sources`` must return its data
in a standard format - search for RST_SRC_ID_SHIFT in
arch/arm/mach-omap2

