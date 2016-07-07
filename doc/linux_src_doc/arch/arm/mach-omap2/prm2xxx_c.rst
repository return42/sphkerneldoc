.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/prm2xxx.c

.. _`omap2xxx_prm_read_reset_sources`:

omap2xxx_prm_read_reset_sources
===============================

.. c:function:: u32 omap2xxx_prm_read_reset_sources( void)

    return the last SoC reset source

    :param  void:
        no arguments

.. _`omap2xxx_prm_read_reset_sources.description`:

Description
-----------

Return a u32 representing the last reset sources of the SoC.  The
returned reset source bits are standardized across OMAP SoCs.

.. _`omap2xxx_pwrst_to_common_pwrst`:

omap2xxx_pwrst_to_common_pwrst
==============================

.. c:function:: int omap2xxx_pwrst_to_common_pwrst(u8 omap2xxx_pwrst)

    convert OMAP2xxx pwrst to common pwrst

    :param u8 omap2xxx_pwrst:
        OMAP2xxx hardware power state to convert

.. _`omap2xxx_pwrst_to_common_pwrst.description`:

Description
-----------

Return the common power state bits corresponding to the OMAP2xxx
hardware power state bits \ ``omap2xxx_pwrst``\ , or -EINVAL upon error.

.. _`omap2xxx_prm_dpll_reset`:

omap2xxx_prm_dpll_reset
=======================

.. c:function:: void omap2xxx_prm_dpll_reset( void)

    use DPLL reset to reboot the OMAP SoC

    :param  void:
        no arguments

.. _`omap2xxx_prm_dpll_reset.description`:

Description
-----------

Set the DPLL reset bit, which should reboot the SoC.  This is the
recommended way to restart the SoC.  No return value.

.. _`omap2xxx_prm_clear_mod_irqs`:

omap2xxx_prm_clear_mod_irqs
===========================

.. c:function:: int omap2xxx_prm_clear_mod_irqs(s16 module, u8 regs, u32 wkst_mask)

    clear wakeup status bits for a module

    :param s16 module:
        PRM module to clear wakeups from

    :param u8 regs:
        register offset to clear

    :param u32 wkst_mask:
        wakeup status mask to clear

.. _`omap2xxx_prm_clear_mod_irqs.description`:

Description
-----------

Clears wakeup status bits for a given module, so that the device can
re-enter idle.

.. This file was automatic generated / don't edit.

