.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/exynos/exynos_drm_gsc.c

.. _`gsc_driverdata`:

struct gsc_driverdata
=====================

.. c:type:: struct gsc_driverdata

    per device type driver data for init time.

.. _`gsc_driverdata.definition`:

Definition
----------

.. code-block:: c

    struct gsc_driverdata {
        const struct drm_exynos_ipp_limit *limits;
        int num_limits;
        const char *clk_names[GSC_MAX_CLOCKS];
        int num_clocks;
    }

.. _`gsc_driverdata.members`:

Members
-------

limits
    picture size limits array

num_limits
    *undescribed*

clk_names
    names of clocks needed by this variant

num_clocks
    the number of clocks needed by this variant

.. This file was automatic generated / don't edit.

