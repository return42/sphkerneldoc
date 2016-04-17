.. -*- coding: utf-8; mode: rst -*-

============
radeon_uvd.c
============


.. _`radeon_uvd_count_handles`:

radeon_uvd_count_handles
========================

.. c:function:: void radeon_uvd_count_handles (struct radeon_device *rdev, unsigned *sd, unsigned *hd)

    count number of open streams

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param unsigned \*sd:
        number of SD streams

    :param unsigned \*hd:
        number of HD streams



.. _`radeon_uvd_count_handles.description`:

Description
-----------

Count the number of open SD/HD streams as a hint for power mangement



.. _`radeon_uvd_calc_upll_dividers`:

radeon_uvd_calc_upll_dividers
=============================

.. c:function:: int radeon_uvd_calc_upll_dividers (struct radeon_device *rdev, unsigned vclk, unsigned dclk, unsigned vco_min, unsigned vco_max, unsigned fb_factor, unsigned fb_mask, unsigned pd_min, unsigned pd_max, unsigned pd_even, unsigned *optimal_fb_div, unsigned *optimal_vclk_div, unsigned *optimal_dclk_div)

    calc UPLL clock dividers

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param unsigned vclk:
        wanted VCLK

    :param unsigned dclk:
        wanted DCLK

    :param unsigned vco_min:
        minimum VCO frequency

    :param unsigned vco_max:
        maximum VCO frequency

    :param unsigned fb_factor:
        factor to multiply vco freq with

    :param unsigned fb_mask:
        limit and bitmask for feedback divider

    :param unsigned pd_min:
        post divider minimum

    :param unsigned pd_max:
        post divider maximum

    :param unsigned pd_even:
        post divider must be even above this value

    :param unsigned \*optimal_fb_div:
        resulting feedback divider

    :param unsigned \*optimal_vclk_div:
        resulting vclk post divider

    :param unsigned \*optimal_dclk_div:
        resulting dclk post divider



.. _`radeon_uvd_calc_upll_dividers.description`:

Description
-----------

Calculate dividers for UVDs UPLL (R6xx-SI, except APUs).
Returns zero on success -EINVAL on error.

