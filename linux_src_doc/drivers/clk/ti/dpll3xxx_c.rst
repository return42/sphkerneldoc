.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/dpll3xxx.c

.. _`_lookup_dco`:

\_lookup_dco
============

.. c:function:: void _lookup_dco(struct clk_hw_omap *clk, u8 *dco, u16 m, u8 n)

    Lookup DCO used by j-type DPLL

    :param clk:
        pointer to a DPLL struct clk
    :type clk: struct clk_hw_omap \*

    :param dco:
        digital control oscillator selector
    :type dco: u8 \*

    :param m:
        DPLL multiplier to set
    :type m: u16

    :param n:
        DPLL divider to set
    :type n: u8

.. _`_lookup_dco.description`:

Description
-----------

See 36xx TRM section 3.5.3.3.3.2 "Type B DPLL (Low-Jitter)"

XXX This code is not needed for 3430/AM35xx; can it be optimized
out in non-multi-OMAP builds for those chips?

.. _`_lookup_sddiv`:

\_lookup_sddiv
==============

.. c:function:: void _lookup_sddiv(struct clk_hw_omap *clk, u8 *sd_div, u16 m, u8 n)

    Calculate sigma delta divider for j-type DPLL

    :param clk:
        pointer to a DPLL struct clk
    :type clk: struct clk_hw_omap \*

    :param sd_div:
        target sigma-delta divider
    :type sd_div: u8 \*

    :param m:
        DPLL multiplier to set
    :type m: u16

    :param n:
        DPLL divider to set
    :type n: u8

.. _`_lookup_sddiv.description`:

Description
-----------

See 36xx TRM section 3.5.3.3.3.2 "Type B DPLL (Low-Jitter)"

XXX This code is not needed for 3430/AM35xx; can it be optimized
out in non-multi-OMAP builds for those chips?

.. _`omap3_dpll_recalc`:

omap3_dpll_recalc
=================

.. c:function:: unsigned long omap3_dpll_recalc(struct clk_hw *hw, unsigned long parent_rate)

    recalculate DPLL rate

    :param hw:
        *undescribed*
    :type hw: struct clk_hw \*

    :param parent_rate:
        *undescribed*
    :type parent_rate: unsigned long

.. _`omap3_dpll_recalc.description`:

Description
-----------

Recalculate and propagate the DPLL rate.

.. _`omap3_noncore_dpll_enable`:

omap3_noncore_dpll_enable
=========================

.. c:function:: int omap3_noncore_dpll_enable(struct clk_hw *hw)

    instruct a DPLL to enter bypass or lock mode

    :param hw:
        *undescribed*
    :type hw: struct clk_hw \*

.. _`omap3_noncore_dpll_enable.description`:

Description
-----------

Instructs a non-CORE DPLL to enable, e.g., to enter bypass or lock.
The choice of modes depends on the DPLL's programmed rate: if it is
the same as the DPLL's parent clock, it will enter bypass;
otherwise, it will enter lock.  This code will wait for the DPLL to
indicate readiness before returning, unless the DPLL takes too long
to enter the target state.  Intended to be used as the struct clk's
enable function.  If DPLL3 was passed in, or the DPLL does not
support low-power stop, or if the DPLL took too long to enter
bypass or lock, return -EINVAL; otherwise, return 0.

.. _`omap3_noncore_dpll_disable`:

omap3_noncore_dpll_disable
==========================

.. c:function:: void omap3_noncore_dpll_disable(struct clk_hw *hw)

    instruct a DPLL to enter low-power stop

    :param hw:
        *undescribed*
    :type hw: struct clk_hw \*

.. _`omap3_noncore_dpll_disable.description`:

Description
-----------

Instructs a non-CORE DPLL to enter low-power stop.  This function is
intended for use in struct clkops.  No return value.

.. _`omap3_noncore_dpll_determine_rate`:

omap3_noncore_dpll_determine_rate
=================================

.. c:function:: int omap3_noncore_dpll_determine_rate(struct clk_hw *hw, struct clk_rate_request *req)

    determine rate for a DPLL

    :param hw:
        pointer to the clock to determine rate for
    :type hw: struct clk_hw \*

    :param req:
        target rate request
    :type req: struct clk_rate_request \*

.. _`omap3_noncore_dpll_determine_rate.description`:

Description
-----------

Determines which DPLL mode to use for reaching a desired target rate.
Checks whether the DPLL shall be in bypass or locked mode, and if
locked, calculates the M,N values for the DPLL via round-rate.
Returns a 0 on success, negative error value in failure.

.. _`omap3_noncore_dpll_set_parent`:

omap3_noncore_dpll_set_parent
=============================

.. c:function:: int omap3_noncore_dpll_set_parent(struct clk_hw *hw, u8 index)

    set parent for a DPLL clock

    :param hw:
        pointer to the clock to set parent for
    :type hw: struct clk_hw \*

    :param index:
        parent index to select
    :type index: u8

.. _`omap3_noncore_dpll_set_parent.description`:

Description
-----------

Sets parent for a DPLL clock. This sets the DPLL into bypass or
locked mode. Returns 0 with success, negative error value otherwise.

.. _`omap3_noncore_dpll_set_rate`:

omap3_noncore_dpll_set_rate
===========================

.. c:function:: int omap3_noncore_dpll_set_rate(struct clk_hw *hw, unsigned long rate, unsigned long parent_rate)

    set rate for a DPLL clock

    :param hw:
        pointer to the clock to set parent for
    :type hw: struct clk_hw \*

    :param rate:
        target rate for the clock
    :type rate: unsigned long

    :param parent_rate:
        rate of the parent clock
    :type parent_rate: unsigned long

.. _`omap3_noncore_dpll_set_rate.description`:

Description
-----------

Sets rate for a DPLL clock. First checks if the clock parent is
reference clock (in bypass mode, the rate of the clock can't be
changed) and proceeds with the rate change operation. Returns 0
with success, negative error value otherwise.

.. _`omap3_noncore_dpll_set_rate_and_parent`:

omap3_noncore_dpll_set_rate_and_parent
======================================

.. c:function:: int omap3_noncore_dpll_set_rate_and_parent(struct clk_hw *hw, unsigned long rate, unsigned long parent_rate, u8 index)

    set rate and parent for a DPLL clock

    :param hw:
        pointer to the clock to set rate and parent for
    :type hw: struct clk_hw \*

    :param rate:
        target rate for the DPLL
    :type rate: unsigned long

    :param parent_rate:
        clock rate of the DPLL parent
    :type parent_rate: unsigned long

    :param index:
        new parent index for the DPLL, 0 - reference, 1 - bypass
    :type index: u8

.. _`omap3_noncore_dpll_set_rate_and_parent.description`:

Description
-----------

Sets rate and parent for a DPLL clock. If new parent is the bypass
clock, only selects the parent. Otherwise proceeds with a rate
change, as this will effectively also change the parent as the
DPLL is put into locked mode. Returns 0 with success, negative error
value otherwise.

.. _`omap3_dpll_autoidle_read`:

omap3_dpll_autoidle_read
========================

.. c:function:: u32 omap3_dpll_autoidle_read(struct clk_hw_omap *clk)

    read a DPLL's autoidle bits

    :param clk:
        struct clk \* of the DPLL to read
    :type clk: struct clk_hw_omap \*

.. _`omap3_dpll_autoidle_read.description`:

Description
-----------

Return the DPLL's autoidle bits, shifted down to bit 0.  Returns
-EINVAL if passed a null pointer or if the struct clk does not
appear to refer to a DPLL.

.. _`omap3_dpll_allow_idle`:

omap3_dpll_allow_idle
=====================

.. c:function:: void omap3_dpll_allow_idle(struct clk_hw_omap *clk)

    enable DPLL autoidle bits

    :param clk:
        struct clk \* of the DPLL to operate on
    :type clk: struct clk_hw_omap \*

.. _`omap3_dpll_allow_idle.description`:

Description
-----------

Enable DPLL automatic idle control.  This automatic idle mode
switching takes effect only when the DPLL is locked, at least on
OMAP3430.  The DPLL will enter low-power stop when its downstream
clocks are gated.  No return value.

.. _`omap3_dpll_deny_idle`:

omap3_dpll_deny_idle
====================

.. c:function:: void omap3_dpll_deny_idle(struct clk_hw_omap *clk)

    prevent DPLL from automatically idling

    :param clk:
        struct clk \* of the DPLL to operate on
    :type clk: struct clk_hw_omap \*

.. _`omap3_dpll_deny_idle.description`:

Description
-----------

Disable DPLL automatic idle control.  No return value.

.. _`omap3_clkoutx2_recalc`:

omap3_clkoutx2_recalc
=====================

.. c:function:: unsigned long omap3_clkoutx2_recalc(struct clk_hw *hw, unsigned long parent_rate)

    recalculate DPLL X2 output virtual clock rate

    :param hw:
        *undescribed*
    :type hw: struct clk_hw \*

    :param parent_rate:
        *undescribed*
    :type parent_rate: unsigned long

.. _`omap3_clkoutx2_recalc.description`:

Description
-----------

Using parent clock DPLL data, look up DPLL state.  If locked, set our
rate to the dpll_clk \* 2; otherwise, just use dpll_clk.

.. _`omap3_core_dpll_save_context`:

omap3_core_dpll_save_context
============================

.. c:function:: int omap3_core_dpll_save_context(struct clk_hw *hw)

    Save the m and n values of the divider

    :param hw:
        pointer  struct clk_hw
    :type hw: struct clk_hw \*

.. _`omap3_core_dpll_save_context.description`:

Description
-----------

Before the dpll registers are lost save the last rounded rate m and n
and the enable mask.

.. _`omap3_core_dpll_restore_context`:

omap3_core_dpll_restore_context
===============================

.. c:function:: void omap3_core_dpll_restore_context(struct clk_hw *hw)

    restore the m and n values of the divider

    :param hw:
        pointer  struct clk_hw
    :type hw: struct clk_hw \*

.. _`omap3_core_dpll_restore_context.description`:

Description
-----------

Restore the last rounded rate m and n
and the enable mask.

.. _`omap3_noncore_dpll_save_context`:

omap3_noncore_dpll_save_context
===============================

.. c:function:: int omap3_noncore_dpll_save_context(struct clk_hw *hw)

    Save the m and n values of the divider

    :param hw:
        pointer  struct clk_hw
    :type hw: struct clk_hw \*

.. _`omap3_noncore_dpll_save_context.description`:

Description
-----------

Before the dpll registers are lost save the last rounded rate m and n
and the enable mask.

.. _`omap3_noncore_dpll_restore_context`:

omap3_noncore_dpll_restore_context
==================================

.. c:function:: void omap3_noncore_dpll_restore_context(struct clk_hw *hw)

    restore the m and n values of the divider

    :param hw:
        pointer  struct clk_hw
    :type hw: struct clk_hw \*

.. _`omap3_noncore_dpll_restore_context.description`:

Description
-----------

Restore the last rounded rate m and n
and the enable mask.

.. _`omap3_dpll4_set_rate`:

omap3_dpll4_set_rate
====================

.. c:function:: int omap3_dpll4_set_rate(struct clk_hw *hw, unsigned long rate, unsigned long parent_rate)

    set rate for omap3 per-dpll

    :param hw:
        clock to change
    :type hw: struct clk_hw \*

    :param rate:
        target rate for clock
    :type rate: unsigned long

    :param parent_rate:
        rate of the parent clock
    :type parent_rate: unsigned long

.. _`omap3_dpll4_set_rate.description`:

Description
-----------

Check if the current SoC supports the per-dpll reprogram operation
or not, and then do the rate change if supported. Returns -EINVAL
if not supported, 0 for success, and potential error codes from the
clock rate change.

.. _`omap3_dpll4_set_rate_and_parent`:

omap3_dpll4_set_rate_and_parent
===============================

.. c:function:: int omap3_dpll4_set_rate_and_parent(struct clk_hw *hw, unsigned long rate, unsigned long parent_rate, u8 index)

    set rate and parent for omap3 per-dpll

    :param hw:
        clock to change
    :type hw: struct clk_hw \*

    :param rate:
        target rate for clock
    :type rate: unsigned long

    :param parent_rate:
        rate of the parent clock
    :type parent_rate: unsigned long

    :param index:
        parent index, 0 - reference clock, 1 - bypass clock
    :type index: u8

.. _`omap3_dpll4_set_rate_and_parent.description`:

Description
-----------

Check if the current SoC support the per-dpll reprogram operation
or not, and then do the rate + parent change if supported. Returns
-EINVAL if not supported, 0 for success, and potential error codes
from the clock rate change.

.. _`omap3_dpll5_set_rate`:

omap3_dpll5_set_rate
====================

.. c:function:: int omap3_dpll5_set_rate(struct clk_hw *hw, unsigned long rate, unsigned long parent_rate)

    set rate for omap3 dpll5

    :param hw:
        clock to change
    :type hw: struct clk_hw \*

    :param rate:
        target rate for clock
    :type rate: unsigned long

    :param parent_rate:
        rate of the parent clock
    :type parent_rate: unsigned long

.. _`omap3_dpll5_set_rate.description`:

Description
-----------

Set rate for the DPLL5 clock. Apply the sprz319 advisory 2.1 on OMAP36xx if
the DPLL is used for USB host (detected through the requested rate).

.. This file was automatic generated / don't edit.

