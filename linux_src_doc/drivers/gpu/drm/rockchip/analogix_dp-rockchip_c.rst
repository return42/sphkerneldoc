.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/rockchip/analogix_dp-rockchip.c

.. _`rockchip_dp_chip_data`:

struct rockchip_dp_chip_data
============================

.. c:type:: struct rockchip_dp_chip_data

    splite the grf setting of kind of chips

.. _`rockchip_dp_chip_data.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_dp_chip_data {
        u32 lcdsel_grf_reg;
        u32 lcdsel_big;
        u32 lcdsel_lit;
        u32 chip_type;
    }

.. _`rockchip_dp_chip_data.members`:

Members
-------

lcdsel_grf_reg
    grf register offset of lcdc select

lcdsel_big
    reg value of selecting vop big for eDP

lcdsel_lit
    reg value of selecting vop little for eDP

chip_type
    specific chip type

.. This file was automatic generated / don't edit.

