.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/oaktrail_crtc.c

.. _`mrst_lvds_find_best_pll`:

mrst_lvds_find_best_pll
=======================

.. c:function:: bool mrst_lvds_find_best_pll(const struct gma_limit_t *limit, struct drm_crtc *crtc, int target, int refclk, struct gma_clock_t *best_clock)

    or FALSE.  Divisor values are the actual divisors for

    :param limit:
        *undescribed*
    :type limit: const struct gma_limit_t \*

    :param crtc:
        *undescribed*
    :type crtc: struct drm_crtc \*

    :param target:
        *undescribed*
    :type target: int

    :param refclk:
        *undescribed*
    :type refclk: int

    :param best_clock:
        *undescribed*
    :type best_clock: struct gma_clock_t \*

.. _`oaktrail_crtc_dpms`:

oaktrail_crtc_dpms
==================

.. c:function:: void oaktrail_crtc_dpms(struct drm_crtc *crtc, int mode)

    :param crtc:
        *undescribed*
    :type crtc: struct drm_crtc \*

    :param mode:
        *undescribed*
    :type mode: int

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

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

.. This file was automatic generated / don't edit.

