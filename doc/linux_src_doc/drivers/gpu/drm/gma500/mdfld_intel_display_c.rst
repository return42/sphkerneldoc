.. -*- coding: utf-8; mode: rst -*-

=====================
mdfld_intel_display.c
=====================


.. _`psb_intel_panel_fitter_pipe`:

psb_intel_panel_fitter_pipe
===========================

.. c:function:: int psb_intel_panel_fitter_pipe (struct drm_device *dev)

    :param struct drm_device \*dev:

        *undescribed*



.. _`psb_intel_panel_fitter_pipe.description`:

Description
-----------

or -1 if the panel fitter is not present or not in use



.. _`mdfld_crtc_dpms`:

mdfld_crtc_dpms
===============

.. c:function:: void mdfld_crtc_dpms (struct drm_crtc *crtc, int mode)

    :param struct drm_crtc \*crtc:

        *undescribed*

    :param int mode:

        *undescribed*



.. _`mdfld_crtc_dpms.description`:

Description
-----------


This code should probably grow support for turning the cursor off and back
on appropriately at the same time as we're turning the pipe off/on.



.. _`mdfldfindbestpll`:

mdfldFindBestPLL
================

.. c:function:: bool mdfldFindBestPLL (struct drm_crtc *crtc, int target, int refclk, struct mrst_clock_t *best_clock)

    :param struct drm_crtc \*crtc:

        *undescribed*

    :param int target:

        *undescribed*

    :param int refclk:

        *undescribed*

    :param struct mrst_clock_t \*best_clock:

        *undescribed*



.. _`mdfldfindbestpll.description`:

Description
-----------

or FALSE.  Divisor values are the actual divisors for

