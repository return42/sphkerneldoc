.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/mdfld_intel_display.c

.. _`psb_intel_panel_fitter_pipe`:

psb_intel_panel_fitter_pipe
===========================

.. c:function:: int psb_intel_panel_fitter_pipe(struct drm_device *dev)

    or -1 if the panel fitter is not present or not in use

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

.. _`mdfld_crtc_dpms`:

mdfld_crtc_dpms
===============

.. c:function:: void mdfld_crtc_dpms(struct drm_crtc *crtc, int mode)

    :param crtc:
        *undescribed*
    :type crtc: struct drm_crtc \*

    :param mode:
        *undescribed*
    :type mode: int

.. _`mdfld_crtc_dpms.description`:

Description
-----------

This code should probably grow support for turning the cursor off and back
on appropriately at the same time as we're turning the pipe off/on.

.. _`mdfldfindbestpll`:

mdfldFindBestPLL
================

.. c:function:: bool mdfldFindBestPLL(struct drm_crtc *crtc, int target, int refclk, struct mrst_clock_t *best_clock)

    or FALSE.  Divisor values are the actual divisors for

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
    :type best_clock: struct mrst_clock_t \*

.. This file was automatic generated / don't edit.

