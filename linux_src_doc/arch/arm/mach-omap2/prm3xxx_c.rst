.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/prm3xxx.c

.. _`omap3xxx_prm_dpll3_reset`:

omap3xxx_prm_dpll3_reset
========================

.. c:function:: void omap3xxx_prm_dpll3_reset( void)

    use DPLL3 reset to reboot the OMAP SoC

    :param void:
        no arguments
    :type void: 

.. _`omap3xxx_prm_dpll3_reset.description`:

Description
-----------

Set the DPLL3 reset bit, which should reboot the SoC.  This is the
recommended way to restart the SoC, considering Errata i520.  No
return value.

.. _`omap3xxx_prm_read_pending_irqs`:

omap3xxx_prm_read_pending_irqs
==============================

.. c:function:: void omap3xxx_prm_read_pending_irqs(unsigned long *events)

    read pending PRM MPU IRQs into \ ``events``\ 

    :param events:
        ptr to a u32, preallocated by caller
    :type events: unsigned long \*

.. _`omap3xxx_prm_read_pending_irqs.description`:

Description
-----------

Read PRM_IRQSTATUS_MPU bits, AND'ed with the currently-enabled PRM
MPU IRQs, and store the result into the u32 pointed to by \ ``events``\ .
No return value.

.. _`omap3xxx_prm_ocp_barrier`:

omap3xxx_prm_ocp_barrier
========================

.. c:function:: void omap3xxx_prm_ocp_barrier( void)

    force buffered MPU writes to the PRM to complete

    :param void:
        no arguments
    :type void: 

.. _`omap3xxx_prm_ocp_barrier.description`:

Description
-----------

Force any buffered writes to the PRM IP block to complete.  Needed
by the PRM IRQ handler, which reads and writes directly to the IP
block, to avoid race conditions after acknowledging or clearing IRQ
bits.  No return value.

.. _`omap3xxx_prm_save_and_clear_irqen`:

omap3xxx_prm_save_and_clear_irqen
=================================

.. c:function:: void omap3xxx_prm_save_and_clear_irqen(u32 *saved_mask)

    save/clear PRM_IRQENABLE_MPU reg

    :param saved_mask:
        ptr to a u32 array to save IRQENABLE bits
    :type saved_mask: u32 \*

.. _`omap3xxx_prm_save_and_clear_irqen.description`:

Description
-----------

Save the PRM_IRQENABLE_MPU register to \ ``saved_mask``\ .  \ ``saved_mask``\ 
must be allocated by the caller.  Intended to be used in the PRM
interrupt handler suspend callback.  The OCP barrier is needed to
ensure the write to disable PRM interrupts reaches the PRM before
returning; otherwise, spurious interrupts might occur.  No return
value.

.. _`omap3xxx_prm_restore_irqen`:

omap3xxx_prm_restore_irqen
==========================

.. c:function:: void omap3xxx_prm_restore_irqen(u32 *saved_mask)

    set PRM_IRQENABLE_MPU register from args

    :param saved_mask:
        ptr to a u32 array of IRQENABLE bits saved previously
    :type saved_mask: u32 \*

.. _`omap3xxx_prm_restore_irqen.description`:

Description
-----------

Restore the PRM_IRQENABLE_MPU register from \ ``saved_mask``\ .  Intended
to be used in the PRM interrupt handler resume callback to restore
values saved by \ :c:func:`omap3xxx_prm_save_and_clear_irqen`\ .  No OCP
barrier should be needed here; any pending PRM interrupts will fire
once the writes reach the PRM.  No return value.

.. _`omap3xxx_prm_clear_mod_irqs`:

omap3xxx_prm_clear_mod_irqs
===========================

.. c:function:: int omap3xxx_prm_clear_mod_irqs(s16 module, u8 regs, u32 wkst_mask)

    clear wake-up events from PRCM interrupt

    :param module:
        PRM module to clear wakeups from
    :type module: s16

    :param regs:
        register set to clear, 1 or 3
    :type regs: u8

    :param wkst_mask:
        wkst bits to clear
    :type wkst_mask: u32

.. _`omap3xxx_prm_clear_mod_irqs.description`:

Description
-----------

The purpose of this function is to clear any wake-up events latched
in the PRCM PM_WKST_x registers. It is possible that a wake-up event
may occur whilst attempting to clear a PM_WKST_x register and thus
set another bit in this register. A while loop is used to ensure
that any peripheral wake-up events occurring while attempting to
clear the PM_WKST_x are detected and cleared.

.. _`omap3_prm_reset_modem`:

omap3_prm_reset_modem
=====================

.. c:function:: void omap3_prm_reset_modem( void)

    toggle reset signal for modem

    :param void:
        no arguments
    :type void: 

.. _`omap3_prm_reset_modem.description`:

Description
-----------

Toggles the reset signal to modem IP block. Required to allow
OMAP3430 without stacked modem to idle properly.

.. _`omap3_prm_init_pm`:

omap3_prm_init_pm
=================

.. c:function:: void omap3_prm_init_pm(bool has_uart4, bool has_iva)

    initialize PM related registers for PRM

    :param has_uart4:
        SoC has UART4
    :type has_uart4: bool

    :param has_iva:
        SoC has IVA
    :type has_iva: bool

.. _`omap3_prm_init_pm.description`:

Description
-----------

Initializes PRM registers for PM use. Called from PM init.

.. _`omap3430_pre_es3_1_reconfigure_io_chain`:

omap3430_pre_es3_1_reconfigure_io_chain
=======================================

.. c:function:: void omap3430_pre_es3_1_reconfigure_io_chain( void)

    restart wake-up daisy chain

    :param void:
        no arguments
    :type void: 

.. _`omap3430_pre_es3_1_reconfigure_io_chain.description`:

Description
-----------

The ST_IO_CHAIN bit does not exist in 3430 before es3.1. The only
thing we can do is toggle EN_IO bit for earlier omaps.

.. _`omap3_prm_reconfigure_io_chain`:

omap3_prm_reconfigure_io_chain
==============================

.. c:function:: void omap3_prm_reconfigure_io_chain( void)

    clear latches and reconfigure I/O chain

    :param void:
        no arguments
    :type void: 

.. _`omap3_prm_reconfigure_io_chain.description`:

Description
-----------

Clear any previously-latched I/O wakeup events and ensure that the
I/O wakeup gates are aligned with the current mux settings.  Works
by asserting WUCLKIN, waiting for WUCLKOUT to be asserted, and then
deasserting WUCLKIN and clearing the ST_IO_CHAIN WKST bit.  No
return value. These registers are only available in 3430 es3.1 and later.

.. _`omap3xxx_prm_enable_io_wakeup`:

omap3xxx_prm_enable_io_wakeup
=============================

.. c:function:: void omap3xxx_prm_enable_io_wakeup( void)

    enable wakeup events from I/O wakeup latches

    :param void:
        no arguments
    :type void: 

.. _`omap3xxx_prm_enable_io_wakeup.description`:

Description
-----------

Activates the I/O wakeup event latches and allows events logged by
those latches to signal a wakeup event to the PRCM.  For I/O
wakeups to occur, WAKEUPENABLE bits must be set in the pad mux
registers, and \ :c:func:`omap3xxx_prm_reconfigure_io_chain`\  must be called.
No return value.

.. _`omap3xxx_prm_read_reset_sources`:

omap3xxx_prm_read_reset_sources
===============================

.. c:function:: u32 omap3xxx_prm_read_reset_sources( void)

    return the last SoC reset source

    :param void:
        no arguments
    :type void: 

.. _`omap3xxx_prm_read_reset_sources.description`:

Description
-----------

Return a u32 representing the last reset sources of the SoC.  The
returned reset source bits are standardized across OMAP SoCs.

.. _`omap3xxx_prm_iva_idle`:

omap3xxx_prm_iva_idle
=====================

.. c:function:: void omap3xxx_prm_iva_idle( void)

    ensure IVA is in idle so it can be put into retention

    :param void:
        no arguments
    :type void: 

.. _`omap3xxx_prm_iva_idle.description`:

Description
-----------

In cases where IVA2 is activated by bootcode, it may prevent
full-chip retention or off-mode because it is not idle.  This
function forces the IVA2 into idle state so it can go
into retention/off and thus allow full-chip retention/off.

.. _`omap3xxx_prm_clear_global_cold_reset`:

omap3xxx_prm_clear_global_cold_reset
====================================

.. c:function:: int omap3xxx_prm_clear_global_cold_reset( void)

    checks the global cold reset status and clears it if asserted

    :param void:
        no arguments
    :type void: 

.. _`omap3xxx_prm_clear_global_cold_reset.description`:

Description
-----------

Checks if cold-reset has occurred and clears the status bit if yes. Returns
1 if cold-reset has occurred, 0 otherwise.

.. This file was automatic generated / don't edit.

