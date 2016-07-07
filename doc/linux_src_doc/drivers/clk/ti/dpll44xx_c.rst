.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/dpll44xx.c

.. _`omap4_dpll_lpmode_recalc`:

omap4_dpll_lpmode_recalc
========================

.. c:function:: void omap4_dpll_lpmode_recalc(struct dpll_data *dd)

    compute DPLL low-power setting

    :param struct dpll_data \*dd:
        pointer to the dpll data structure

.. _`omap4_dpll_lpmode_recalc.description`:

Description
-----------

Calculates if low-power mode can be enabled based upon the last
multiplier and divider values calculated. If low-power mode can be
enabled, then the bit to enable low-power mode is stored in the
last_rounded_lpmode variable. This implementation is based upon the
criteria for enabling low-power mode as described in the OMAP4430/60
Public TRM section 3.6.3.3.2 "Enable Control, Status, and Low-Power
Operation Mode".

.. _`omap4_dpll_regm4xen_recalc`:

omap4_dpll_regm4xen_recalc
==========================

.. c:function:: unsigned long omap4_dpll_regm4xen_recalc(struct clk_hw *hw, unsigned long parent_rate)

    compute DPLL rate, considering REGM4XEN bit

    :param struct clk_hw \*hw:
        *undescribed*

    :param unsigned long parent_rate:
        *undescribed*

.. _`omap4_dpll_regm4xen_recalc.description`:

Description
-----------

Compute the output rate for the OMAP4 DPLL represented by \ ``clk``\ .
Takes the REGM4XEN bit into consideration, which is needed for the
OMAP4 ABE DPLL.  Returns the DPLL's output rate (before M-dividers)
upon success, or 0 upon error.

.. _`omap4_dpll_regm4xen_round_rate`:

omap4_dpll_regm4xen_round_rate
==============================

.. c:function:: long omap4_dpll_regm4xen_round_rate(struct clk_hw *hw, unsigned long target_rate, unsigned long *parent_rate)

    round DPLL rate, considering REGM4XEN bit

    :param struct clk_hw \*hw:
        *undescribed*

    :param unsigned long target_rate:
        the desired rate of the DPLL

    :param unsigned long \*parent_rate:
        *undescribed*

.. _`omap4_dpll_regm4xen_round_rate.description`:

Description
-----------

Compute the rate that would be programmed into the DPLL hardware
for \ ``clk``\  if \ :c:func:`set_rate`\  were to be provided with the rate
\ ``target_rate``\ .  Takes the REGM4XEN bit into consideration, which is
needed for the OMAP4 ABE DPLL.  Returns the rounded rate (before
M-dividers) upon success, -EINVAL if \ ``clk``\  is null or not a DPLL, or
~0 if an error occurred in \ :c:func:`omap2_dpll_round_rate`\ .

.. _`omap4_dpll_regm4xen_determine_rate`:

omap4_dpll_regm4xen_determine_rate
==================================

.. c:function:: int omap4_dpll_regm4xen_determine_rate(struct clk_hw *hw, struct clk_rate_request *req)

    determine rate for a DPLL

    :param struct clk_hw \*hw:
        pointer to the clock to determine rate for

    :param struct clk_rate_request \*req:
        target rate request

.. _`omap4_dpll_regm4xen_determine_rate.description`:

Description
-----------

Determines which DPLL mode to use for reaching a desired rate.
Checks whether the DPLL shall be in bypass or locked mode, and if
locked, calculates the M,N values for the DPLL via round-rate.
Returns 0 on success and a negative error value otherwise.

.. This file was automatic generated / don't edit.

