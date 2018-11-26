.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/tegra/dc.c

.. _`tegra_dc_state_setup_clock`:

tegra_dc_state_setup_clock
==========================

.. c:function:: int tegra_dc_state_setup_clock(struct tegra_dc *dc, struct drm_crtc_state *crtc_state, struct clk *clk, unsigned long pclk, unsigned int div)

    check clock settings and store them in atomic state

    :param dc:
        display controller
    :type dc: struct tegra_dc \*

    :param crtc_state:
        CRTC atomic state
    :type crtc_state: struct drm_crtc_state \*

    :param clk:
        parent clock for display controller
    :type clk: struct clk \*

    :param pclk:
        pixel clock
    :type pclk: unsigned long

    :param div:
        shift clock divider
    :type div: unsigned int

.. _`tegra_dc_state_setup_clock.return`:

Return
------

0 on success or a negative error-code on failure.

.. This file was automatic generated / don't edit.

