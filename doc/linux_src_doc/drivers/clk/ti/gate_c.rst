.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/gate.c

.. _`omap36xx_gate_clk_enable_with_hsdiv_restore`:

omap36xx_gate_clk_enable_with_hsdiv_restore
===========================================

.. c:function:: int omap36xx_gate_clk_enable_with_hsdiv_restore(struct clk_hw *hw)

    enable clocks suffering from HSDivider PWRDN problem Implements Errata ID: i556.

    :param struct clk_hw \*hw:
        *undescribed*

.. _`omap36xx_gate_clk_enable_with_hsdiv_restore.3630-only`:

3630 only
---------

dpll3_m3_ck, dpll4_m2_ck, dpll4_m3_ck, dpll4_m4_ck,
dpll4_m5_ck & dpll4_m6_ck dividers gets loaded with reset
valueafter their respective PWRDN bits are set.  Any dummy write
(Any other value different from the Read value) to the
corresponding CM_CLKSEL register will refresh the dividers.

.. This file was automatic generated / don't edit.

