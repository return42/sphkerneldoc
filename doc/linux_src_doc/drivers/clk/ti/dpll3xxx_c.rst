.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/dpll3xxx.c

.. _`_lookup_dco`:

_lookup_dco
===========

.. c:function:: void _lookup_dco(struct clk_hw_omap *clk, u8 *dco, u16 m, u8 n)

    Lookup DCO used by j-type DPLL

    :param struct clk_hw_omap \*clk:
        pointer to a DPLL struct clk

    :param u8 \*dco:
        digital control oscillator selector

    :param u16 m:
        DPLL multiplier to set

    :param u8 n:
        DPLL divider to set

.. _`_lookup_dco.description`:

Description
-----------

See 36xx TRM section 3.5.3.3.3.2 "Type B DPLL (Low-Jitter)"

XXX This code is not needed for 3430/AM35xx; can it be optimized
out in non-multi-OMAP builds for those chips?

.. _`_lookup_sddiv`:

_lookup_sddiv
=============

.. c:function:: void _lookup_sddiv(struct clk_hw_omap *clk, u8 *sd_div, u16 m, u8 n)

    Calculate sigma delta divider for j-type DPLL

    :param struct clk_hw_omap \*clk:
        pointer to a DPLL struct clk

    :param u8 \*sd_div:
        target sigma-delta divider

    :param u16 m:
        DPLL multiplier to set

    :param u8 n:
        DPLL divider to set

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

    :param struct clk_hw \*hw:
        *undescribed*

    :param unsigned long parent_rate:
        *undescribed*

.. _`omap3_dpll_recalc.description`:

Description
-----------

Recalculate and propagate the DPLL rate.

.. _`omap3_noncore_dpll_enable`:

omap3_noncore_dpll_enable
=========================

.. c:function:: int omap3_noncore_dpll_enable(struct clk_hw *hw)

    instruct a DPLL to enter bypass or lock mode

    :param struct clk_hw \*hw:
        *undescribed*

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

    :param struct clk_hw \*hw:
        *undescribed*

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

    :param struct clk_hw \*hw:
        pointer to the clock to determine rate for

    :param struct clk_rate_request \*req:
        target rate request

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

    :param struct clk_hw \*hw:
        pointer to the clock to set parent for

    :param u8 index:
        parent index to select

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

    :param struct clk_hw \*hw:
        pointer to the clock to set parent for

    :param unsigned long rate:
        target rate for the clock

    :param unsigned long parent_rate:
        rate of the parent clock

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

    :param struct clk_hw \*hw:
        pointer to the clock to set rate and parent for

    :param unsigned long rate:
        target rate for the DPLL

    :param unsigned long parent_rate:
        clock rate of the DPLL parent

    :param u8 index:
        new parent index for the DPLL, 0 - reference, 1 - bypass

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

    :param struct clk_hw_omap \*clk:
        struct clk \* of the DPLL to read

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

    :param struct clk_hw_omap \*clk:
        struct clk \* of the DPLL to operate on

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

    :param struct clk_hw_omap \*clk:
        struct clk \* of the DPLL to operate on

.. _`omap3_dpll_deny_idle.description`:

Description
-----------

Disable DPLL automatic idle control.  No return value.

.. _`omap3_clkoutx2_recalc`:

omap3_clkoutx2_recalc
=====================

.. c:function:: unsigned long omap3_clkoutx2_recalc(struct clk_hw *hw, unsigned long parent_rate)

    recalculate DPLL X2 output virtual clock rate

    :param struct clk_hw \*hw:
        *undescribed*

    :param unsigned long parent_rate:
        *undescribed*

.. _`omap3_clkoutx2_recalc.description`:

Description
-----------

Using parent clock DPLL data, look up DPLL state.  If locked, set our
rate to the dpll_clk \* 2; otherwise, just use dpll_clk.

.. _`omap3_dpll4_set_rate`:

omap3_dpll4_set_rate
====================

.. c:function:: int omap3_dpll4_set_rate(struct clk_hw *hw, unsigned long rate, unsigned long parent_rate)

    set rate for omap3 per-dpll

    :param struct clk_hw \*hw:
        clock to change

    :param unsigned long rate:
        target rate for clock

    :param unsigned long parent_rate:
        rate of the parent clock

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

    :param struct clk_hw \*hw:
        clock to change

    :param unsigned long rate:
        target rate for clock

    :param unsigned long parent_rate:
        rate of the parent clock

    :param u8 index:
        parent index, 0 - reference clock, 1 - bypass clock

.. _`omap3_dpll4_set_rate_and_parent.description`:

Description
-----------

Check if the current SoC support the per-dpll reprogram operation
or not, and then do the rate + parent change if supported. Returns
-EINVAL if not supported, 0 for success, and potential error codes
from the clock rate change.

.. This file was automatic generated / don't edit.

