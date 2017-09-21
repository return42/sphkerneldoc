.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/rockchip/dw_hdmi-rockchip.c

.. _`rockchip_hdmi_chip_data`:

struct rockchip_hdmi_chip_data
==============================

.. c:type:: struct rockchip_hdmi_chip_data

    splite the grf setting of kind of chips

.. _`rockchip_hdmi_chip_data.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_hdmi_chip_data {
        u32 lcdsel_grf_reg;
        u32 lcdsel_big;
        u32 lcdsel_lit;
    }

.. _`rockchip_hdmi_chip_data.members`:

Members
-------

lcdsel_grf_reg
    grf register offset of lcdc select

lcdsel_big
    reg value of selecting vop big for HDMI

lcdsel_lit
    reg value of selecting vop little for HDMI

.. This file was automatic generated / don't edit.

