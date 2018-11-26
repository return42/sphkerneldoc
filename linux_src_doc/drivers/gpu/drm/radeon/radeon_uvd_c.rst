.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_uvd.c

.. _`radeon_uvd_count_handles`:

radeon_uvd_count_handles
========================

.. c:function:: void radeon_uvd_count_handles(struct radeon_device *rdev, unsigned *sd, unsigned *hd)

    count number of open streams

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param sd:
        number of SD streams
    :type sd: unsigned \*

    :param hd:
        number of HD streams
    :type hd: unsigned \*

.. _`radeon_uvd_count_handles.description`:

Description
-----------

Count the number of open SD/HD streams as a hint for power mangement

.. _`radeon_uvd_calc_upll_dividers`:

radeon_uvd_calc_upll_dividers
=============================

.. c:function:: int radeon_uvd_calc_upll_dividers(struct radeon_device *rdev, unsigned vclk, unsigned dclk, unsigned vco_min, unsigned vco_max, unsigned fb_factor, unsigned fb_mask, unsigned pd_min, unsigned pd_max, unsigned pd_even, unsigned *optimal_fb_div, unsigned *optimal_vclk_div, unsigned *optimal_dclk_div)

    calc UPLL clock dividers

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param vclk:
        wanted VCLK
    :type vclk: unsigned

    :param dclk:
        wanted DCLK
    :type dclk: unsigned

    :param vco_min:
        minimum VCO frequency
    :type vco_min: unsigned

    :param vco_max:
        maximum VCO frequency
    :type vco_max: unsigned

    :param fb_factor:
        factor to multiply vco freq with
    :type fb_factor: unsigned

    :param fb_mask:
        limit and bitmask for feedback divider
    :type fb_mask: unsigned

    :param pd_min:
        post divider minimum
    :type pd_min: unsigned

    :param pd_max:
        post divider maximum
    :type pd_max: unsigned

    :param pd_even:
        post divider must be even above this value
    :type pd_even: unsigned

    :param optimal_fb_div:
        resulting feedback divider
    :type optimal_fb_div: unsigned \*

    :param optimal_vclk_div:
        resulting vclk post divider
    :type optimal_vclk_div: unsigned \*

    :param optimal_dclk_div:
        resulting dclk post divider
    :type optimal_dclk_div: unsigned \*

.. _`radeon_uvd_calc_upll_dividers.description`:

Description
-----------

Calculate dividers for UVDs UPLL (R6xx-SI, except APUs).
Returns zero on success -EINVAL on error.

.. This file was automatic generated / don't edit.

