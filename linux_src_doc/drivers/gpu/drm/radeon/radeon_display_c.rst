.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_display.c

.. _`radeon_unpin_work_func`:

radeon_unpin_work_func
======================

.. c:function:: void radeon_unpin_work_func(struct work_struct *__work)

    unpin old buffer object

    :param __work:
        *undescribed*
    :type __work: struct work_struct \*

.. _`radeon_unpin_work_func.description`:

Description
-----------

\ ``__work``\  - kernel work item

Unpin the old frame buffer object outside of the interrupt handler

.. _`radeon_crtc_handle_flip`:

radeon_crtc_handle_flip
=======================

.. c:function:: void radeon_crtc_handle_flip(struct radeon_device *rdev, int crtc_id)

    page flip completed

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

    :param crtc_id:
        crtc number this event is for
    :type crtc_id: int

.. _`radeon_crtc_handle_flip.description`:

Description
-----------

Called when we are sure that a page flip for this crtc is completed.

.. _`radeon_flip_work_func`:

radeon_flip_work_func
=====================

.. c:function:: void radeon_flip_work_func(struct work_struct *__work)

    page flip framebuffer

    :param __work:
        *undescribed*
    :type __work: struct work_struct \*

.. _`radeon_flip_work_func.description`:

Description
-----------

\ ``work``\  - kernel work item

Wait for the buffer object to become idle and do the actual page flip

.. _`avivo_reduce_ratio`:

avivo_reduce_ratio
==================

.. c:function:: void avivo_reduce_ratio(unsigned *nom, unsigned *den, unsigned nom_min, unsigned den_min)

    fractional number reduction

    :param nom:
        nominator
    :type nom: unsigned \*

    :param den:
        denominator
    :type den: unsigned \*

    :param nom_min:
        minimum value for nominator
    :type nom_min: unsigned

    :param den_min:
        minimum value for denominator
    :type den_min: unsigned

.. _`avivo_reduce_ratio.description`:

Description
-----------

Find the greatest common divisor and apply it on both nominator and
denominator, but make nominator and denominator are at least as large
as their minimum values.

.. _`avivo_get_fb_ref_div`:

avivo_get_fb_ref_div
====================

.. c:function:: void avivo_get_fb_ref_div(unsigned nom, unsigned den, unsigned post_div, unsigned fb_div_max, unsigned ref_div_max, unsigned *fb_div, unsigned *ref_div)

    feedback and ref divider calculation

    :param nom:
        nominator
    :type nom: unsigned

    :param den:
        denominator
    :type den: unsigned

    :param post_div:
        post divider
    :type post_div: unsigned

    :param fb_div_max:
        feedback divider maximum
    :type fb_div_max: unsigned

    :param ref_div_max:
        reference divider maximum
    :type ref_div_max: unsigned

    :param fb_div:
        resulting feedback divider
    :type fb_div: unsigned \*

    :param ref_div:
        resulting reference divider
    :type ref_div: unsigned \*

.. _`avivo_get_fb_ref_div.description`:

Description
-----------

Calculate feedback and reference divider for a given post divider. Makes
sure we stay within the limits.

.. _`radeon_compute_pll_avivo`:

radeon_compute_pll_avivo
========================

.. c:function:: void radeon_compute_pll_avivo(struct radeon_pll *pll, u32 freq, u32 *dot_clock_p, u32 *fb_div_p, u32 *frac_fb_div_p, u32 *ref_div_p, u32 *post_div_p)

    compute PLL paramaters

    :param pll:
        information about the PLL
    :type pll: struct radeon_pll \*

    :param freq:
        *undescribed*
    :type freq: u32

    :param dot_clock_p:
        resulting pixel clock
    :type dot_clock_p: u32 \*

    :param fb_div_p:
        *undescribed*
    :type fb_div_p: u32 \*

    :param frac_fb_div_p:
        *undescribed*
    :type frac_fb_div_p: u32 \*

    :param ref_div_p:
        *undescribed*
    :type ref_div_p: u32 \*

    :param post_div_p:
        *undescribed*
    :type post_div_p: u32 \*

.. _`radeon_compute_pll_avivo.fb_div_p`:

fb_div_p
--------

resulting feedback divider

.. _`radeon_compute_pll_avivo.frac_fb_div_p`:

frac_fb_div_p
-------------

fractional part of the feedback divider

.. _`radeon_compute_pll_avivo.ref_div_p`:

ref_div_p
---------

resulting reference divider

.. _`radeon_compute_pll_avivo.post_div_p`:

post_div_p
----------

resulting reference divider

.. _`radeon_compute_pll_avivo.try-to-calculate-the-pll-parameters-to-generate-the-given-frequency`:

Try to calculate the PLL parameters to generate the given frequency
-------------------------------------------------------------------

dot_clock = (ref_freq \* feedback_div) / (ref_div \* post_div)

.. This file was automatic generated / don't edit.

