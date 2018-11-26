.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/dce/dce_clock_source.c

.. _`calculate_fb_and_fractional_fb_divider`:

calculate_fb_and_fractional_fb_divider
======================================

.. c:function:: bool calculate_fb_and_fractional_fb_divider(struct calc_pll_clock_source *calc_pll_cs, uint32_t target_pix_clk_khz, uint32_t ref_divider, uint32_t post_divider, uint32_t *feedback_divider_param, uint32_t *fract_feedback_divider_param)

    calculate_fb_and_fractional_fb_divider

    :param calc_pll_cs:
        *undescribed*
    :type calc_pll_cs: struct calc_pll_clock_source \*

    :param target_pix_clk_khz:
        *undescribed*
    :type target_pix_clk_khz: uint32_t

    :param ref_divider:
        *undescribed*
    :type ref_divider: uint32_t

    :param post_divider:
        *undescribed*
    :type post_divider: uint32_t

    :param feedback_divider_param:
        *undescribed*
    :type feedback_divider_param: uint32_t \*

    :param fract_feedback_divider_param:
        *undescribed*
    :type fract_feedback_divider_param: uint32_t \*

.. _`calculate_fb_and_fractional_fb_divider.description`:

Description
-----------

\* DESCRIPTION: Calculates feedback and fractional feedback dividers values

PARAMETERS:
targetPixelClock             Desired frequency in 10 KHz
ref_divider                  Reference divider (already known)
postDivider                  Post Divider (already known)
feedback_divider_param       Pointer where to store
calculated feedback divider value
fract_feedback_divider_param Pointer where to store
calculated fract feedback divider value

RETURNS:
It fills the locations pointed by feedback_divider_param
and fract_feedback_divider_param
It returns    - true if feedback divider not 0
- false should never happen)

.. _`calc_fb_divider_checking_tolerance`:

calc_fb_divider_checking_tolerance
==================================

.. c:function:: bool calc_fb_divider_checking_tolerance(struct calc_pll_clock_source *calc_pll_cs, struct pll_settings *pll_settings, uint32_t ref_divider, uint32_t post_divider, uint32_t tolerance)

    :param calc_pll_cs:
        *undescribed*
    :type calc_pll_cs: struct calc_pll_clock_source \*

    :param pll_settings:
        *undescribed*
    :type pll_settings: struct pll_settings \*

    :param ref_divider:
        *undescribed*
    :type ref_divider: uint32_t

    :param post_divider:
        *undescribed*
    :type post_divider: uint32_t

    :param tolerance:
        *undescribed*
    :type tolerance: uint32_t

.. _`calc_fb_divider_checking_tolerance.description`:

Description
-----------

DESCRIPTION: Calculates Feedback and Fractional Feedback divider values
for passed Reference and Post divider, checking for tolerance.
PARAMETERS:
pll_settings          Pointer to structure
ref_divider           Reference divider (already known)
postDivider           Post Divider (already known)
tolerance             Tolerance for Calculated Pixel Clock to be within

RETURNS:
It fills the PLLSettings structure with PLL Dividers values
if calculated values are within required tolerance
It returns    - true if eror is within tolerance
- false if eror is not within tolerance

.. _`dce110_get_pix_clk_dividers_helper`:

dce110_get_pix_clk_dividers_helper
==================================

.. c:function:: uint32_t dce110_get_pix_clk_dividers_helper(struct dce110_clk_src *clk_src, struct pll_settings *pll_settings, struct pixel_clk_params *pix_clk_params)

    First will call VBIOS Adjust Exec table to check if requested Pixel clock will be Adjusted based on usage. Then it will calculate PLL Dividers for this Adjusted clock using preferred method (Maximum VCO frequency).

    :param clk_src:
        *undescribed*
    :type clk_src: struct dce110_clk_src \*

    :param pll_settings:
        *undescribed*
    :type pll_settings: struct pll_settings \*

    :param pix_clk_params:
        *undescribed*
    :type pix_clk_params: struct pixel_clk_params \*

.. _`dce110_get_pix_clk_dividers_helper.description`:

Description
-----------

\return
Calculation error in units of 0.01%

.. This file was automatic generated / don't edit.

