.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/oaktrail_crtc.c

.. _`mrst_lvds_find_best_pll`:

mrst_lvds_find_best_pll
=======================

.. c:function:: bool mrst_lvds_find_best_pll(const struct gma_limit_t *limit, struct drm_crtc *crtc, int target, int refclk, struct gma_clock_t *best_clock)

    or FALSE.  Divisor values are the actual divisors for

    :param const struct gma_limit_t \*limit:
        *undescribed*

    :param struct drm_crtc \*crtc:
        *undescribed*

    :param int target:
        *undescribed*

    :param int refclk:
        *undescribed*

    :param struct gma_clock_t \*best_clock:
        *undescribed*

.. _`oaktrail_crtc_dpms`:

oaktrail_crtc_dpms
==================

.. c:function:: void oaktrail_crtc_dpms(struct drm_crtc *crtc, int mode)

    :param struct drm_crtc \*crtc:
        *undescribed*

    :param int mode:
        *undescribed*

.. _`oaktrail_crtc_dpms.description`:

Description
-----------

This code should probably grow support for turning the cursor off and back
on appropriately at the same time as we're turning the pipe off/on.

.. _`oaktrail_panel_fitter_pipe`:

oaktrail_panel_fitter_pipe
==========================

.. c:function:: int oaktrail_panel_fitter_pipe(struct drm_device *dev)

    or -1 if the panel fitter is not present or not in use

    :param struct drm_device \*dev:
        *undescribed*

.. This file was automatic generated / don't edit.

