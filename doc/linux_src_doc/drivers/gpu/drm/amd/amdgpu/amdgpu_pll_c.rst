.. -*- coding: utf-8; mode: rst -*-

============
amdgpu_pll.c
============


.. _`amdgpu_pll_reduce_ratio`:

amdgpu_pll_reduce_ratio
=======================

.. c:function:: void amdgpu_pll_reduce_ratio (unsigned *nom, unsigned *den, unsigned nom_min, unsigned den_min)

    fractional number reduction

    :param unsigned \*nom:
        nominator

    :param unsigned \*den:
        denominator

    :param unsigned nom_min:
        minimum value for nominator

    :param unsigned den_min:
        minimum value for denominator



.. _`amdgpu_pll_reduce_ratio.description`:

Description
-----------

Find the greatest common divisor and apply it on both nominator and
denominator, but make nominator and denominator are at least as large
as their minimum values.



.. _`amdgpu_pll_get_fb_ref_div`:

amdgpu_pll_get_fb_ref_div
=========================

.. c:function:: void amdgpu_pll_get_fb_ref_div (unsigned nom, unsigned den, unsigned post_div, unsigned fb_div_max, unsigned ref_div_max, unsigned *fb_div, unsigned *ref_div)

    feedback and ref divider calculation

    :param unsigned nom:
        nominator

    :param unsigned den:
        denominator

    :param unsigned post_div:
        post divider

    :param unsigned fb_div_max:
        feedback divider maximum

    :param unsigned ref_div_max:
        reference divider maximum

    :param unsigned \*fb_div:
        resulting feedback divider

    :param unsigned \*ref_div:
        resulting reference divider



.. _`amdgpu_pll_get_fb_ref_div.description`:

Description
-----------

Calculate feedback and reference divider for a given post divider. Makes
sure we stay within the limits.



.. _`amdgpu_pll_compute`:

amdgpu_pll_compute
==================

.. c:function:: void amdgpu_pll_compute (struct amdgpu_pll *pll, u32 freq, u32 *dot_clock_p, u32 *fb_div_p, u32 *frac_fb_div_p, u32 *ref_div_p, u32 *post_div_p)

    compute PLL paramaters

    :param struct amdgpu_pll \*pll:
        information about the PLL

    :param u32 freq:

        *undescribed*

    :param u32 \*dot_clock_p:
        resulting pixel clock

    :param u32 \*fb_div_p:

        *undescribed*

    :param u32 \*frac_fb_div_p:

        *undescribed*

    :param u32 \*ref_div_p:

        *undescribed*

    :param u32 \*post_div_p:

        *undescribed*



.. _`amdgpu_pll_compute.fb_div_p`:

fb_div_p
--------

resulting feedback divider



.. _`amdgpu_pll_compute.frac_fb_div_p`:

frac_fb_div_p
-------------

fractional part of the feedback divider



.. _`amdgpu_pll_compute.ref_div_p`:

ref_div_p
---------

resulting reference divider



.. _`amdgpu_pll_compute.post_div_p`:

post_div_p
----------

resulting reference divider



.. _`amdgpu_pll_compute.try-to-calculate-the-pll-parameters-to-generate-the-given-frequency`:

Try to calculate the PLL parameters to generate the given frequency
-------------------------------------------------------------------

dot_clock = (ref_freq * feedback_div) / (ref_div * post_div)



.. _`amdgpu_pll_get_use_mask`:

amdgpu_pll_get_use_mask
=======================

.. c:function:: u32 amdgpu_pll_get_use_mask (struct drm_crtc *crtc)

    look up a mask of which pplls are in use

    :param struct drm_crtc \*crtc:
        drm crtc



.. _`amdgpu_pll_get_use_mask.description`:

Description
-----------

Returns the mask of which PPLLs (Pixel PLLs) are in use.



.. _`amdgpu_pll_get_shared_dp_ppll`:

amdgpu_pll_get_shared_dp_ppll
=============================

.. c:function:: int amdgpu_pll_get_shared_dp_ppll (struct drm_crtc *crtc)

    return the PPLL used by another crtc for DP

    :param struct drm_crtc \*crtc:
        drm crtc



.. _`amdgpu_pll_get_shared_dp_ppll.description`:

Description
-----------

Returns the PPLL (Pixel PLL) used by another crtc/encoder which is
also in DP mode.  For DP, a single PPLL can be used for all DP
crtcs/encoders.



.. _`amdgpu_pll_get_shared_nondp_ppll`:

amdgpu_pll_get_shared_nondp_ppll
================================

.. c:function:: int amdgpu_pll_get_shared_nondp_ppll (struct drm_crtc *crtc)

    return the PPLL used by another non-DP crtc

    :param struct drm_crtc \*crtc:
        drm crtc



.. _`amdgpu_pll_get_shared_nondp_ppll.description`:

Description
-----------

Returns the PPLL (Pixel PLL) used by another non-DP crtc/encoder which can
be shared (i.e., same clock).

