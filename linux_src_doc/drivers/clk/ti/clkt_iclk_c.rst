.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/clkt_iclk.c

.. _`omap2430_clk_i2chs_find_idlest`:

omap2430_clk_i2chs_find_idlest
==============================

.. c:function:: void omap2430_clk_i2chs_find_idlest(struct clk_hw_omap *clk, void __iomem **idlest_reg, u8 *idlest_bit, u8 *idlest_val)

    return CM_IDLEST info for 2430 I2CHS

    :param struct clk_hw_omap \*clk:
        struct clk \* being enabled

    :param void __iomem \*\*idlest_reg:
        void \__iomem \*\* to store CM_IDLEST reg address into

    :param u8 \*idlest_bit:
        pointer to a u8 to store the CM_IDLEST bit shift into

    :param u8 \*idlest_val:
        pointer to a u8 to store the CM_IDLEST indicator

.. _`omap2430_clk_i2chs_find_idlest.description`:

Description
-----------

OMAP2430 I2CHS CM_IDLEST bits are in CM_IDLEST1_CORE, but the
CM\_\*CLKEN bits are in CM_{I,F}CLKEN2_CORE.  This custom function
passes back the correct CM_IDLEST register address for I2CHS
modules.  No return value.

.. This file was automatic generated / don't edit.

