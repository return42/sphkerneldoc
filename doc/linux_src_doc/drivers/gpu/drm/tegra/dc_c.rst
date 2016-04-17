.. -*- coding: utf-8; mode: rst -*-

====
dc.c
====


.. _`tegra_dc_state_setup_clock`:

tegra_dc_state_setup_clock
==========================

.. c:function:: int tegra_dc_state_setup_clock (struct tegra_dc *dc, struct drm_crtc_state *crtc_state, struct clk *clk, unsigned long pclk, unsigned int div)

    check clock settings and store them in atomic state

    :param struct tegra_dc \*dc:
        display controller

    :param struct drm_crtc_state \*crtc_state:
        CRTC atomic state

    :param struct clk \*clk:
        parent clock for display controller

    :param unsigned long pclk:
        pixel clock

    :param unsigned int div:
        shift clock divider



.. _`tegra_dc_state_setup_clock.returns`:

Returns
-------

0 on success or a negative error-code on failure.

