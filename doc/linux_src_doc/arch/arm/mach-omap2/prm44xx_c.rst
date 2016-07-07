.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/prm44xx.c

.. _`omap44xx_prm_read_pending_irqs`:

omap44xx_prm_read_pending_irqs
==============================

.. c:function:: void omap44xx_prm_read_pending_irqs(unsigned long *events)

    read pending PRM MPU IRQs into \ ``events``\ 

    :param unsigned long \*events:
        ptr to two consecutive u32s, preallocated by caller

.. _`omap44xx_prm_read_pending_irqs.description`:

Description
-----------

Read PRM_IRQSTATUS_MPU\* bits, AND'ed with the currently-enabled PRM
MPU IRQs, and store the result into the two u32s pointed to by \ ``events``\ .
No return value.

.. _`omap44xx_prm_ocp_barrier`:

omap44xx_prm_ocp_barrier
========================

.. c:function:: void omap44xx_prm_ocp_barrier( void)

    force buffered MPU writes to the PRM to complete

    :param  void:
        no arguments

.. _`omap44xx_prm_ocp_barrier.description`:

Description
-----------

Force any buffered writes to the PRM IP block to complete.  Needed
by the PRM IRQ handler, which reads and writes directly to the IP
block, to avoid race conditions after acknowledging or clearing IRQ
bits.  No return value.

.. _`omap44xx_prm_save_and_clear_irqen`:

omap44xx_prm_save_and_clear_irqen
=================================

.. c:function:: void omap44xx_prm_save_and_clear_irqen(u32 *saved_mask)

    save/clear PRM_IRQENABLE_MPU\* regs

    :param u32 \*saved_mask:
        ptr to a u32 array to save IRQENABLE bits

.. _`omap44xx_prm_save_and_clear_irqen.description`:

Description
-----------

Save the PRM_IRQENABLE_MPU and PRM_IRQENABLE_MPU_2 registers to
\ ``saved_mask``\ .  \ ``saved_mask``\  must be allocated by the caller.
Intended to be used in the PRM interrupt handler suspend callback.
The OCP barrier is needed to ensure the write to disable PRM
interrupts reaches the PRM before returning; otherwise, spurious
interrupts might occur.  No return value.

.. _`omap44xx_prm_restore_irqen`:

omap44xx_prm_restore_irqen
==========================

.. c:function:: void omap44xx_prm_restore_irqen(u32 *saved_mask)

    set PRM_IRQENABLE_MPU\* registers from args

    :param u32 \*saved_mask:
        ptr to a u32 array of IRQENABLE bits saved previously

.. _`omap44xx_prm_restore_irqen.description`:

Description
-----------

Restore the PRM_IRQENABLE_MPU and PRM_IRQENABLE_MPU_2 registers from
\ ``saved_mask``\ .  Intended to be used in the PRM interrupt handler resume
callback to restore values saved by \ :c:func:`omap44xx_prm_save_and_clear_irqen`\ .
No OCP barrier should be needed here; any pending PRM interrupts will fire
once the writes reach the PRM.  No return value.

.. _`omap44xx_prm_reconfigure_io_chain`:

omap44xx_prm_reconfigure_io_chain
=================================

.. c:function:: void omap44xx_prm_reconfigure_io_chain( void)

    clear latches and reconfigure I/O chain

    :param  void:
        no arguments

.. _`omap44xx_prm_reconfigure_io_chain.description`:

Description
-----------

Clear any previously-latched I/O wakeup events and ensure that the
I/O wakeup gates are aligned with the current mux settings.  Works
by asserting WUCLKIN, waiting for WUCLKOUT to be asserted, and then
deasserting WUCLKIN and waiting for WUCLKOUT to be deasserted.
No return value. XXX Are the final two steps necessary?

.. _`omap44xx_prm_enable_io_wakeup`:

omap44xx_prm_enable_io_wakeup
=============================

.. c:function:: void omap44xx_prm_enable_io_wakeup( void)

    enable wakeup events from I/O wakeup latches

    :param  void:
        no arguments

.. _`omap44xx_prm_enable_io_wakeup.description`:

Description
-----------

Activates the I/O wakeup event latches and allows events logged by
those latches to signal a wakeup event to the PRCM.  For I/O wakeups
to occur, WAKEUPENABLE bits must be set in the pad mux registers, and
\ :c:func:`omap44xx_prm_reconfigure_io_chain`\  must be called.  No return value.

.. _`omap44xx_prm_read_reset_sources`:

omap44xx_prm_read_reset_sources
===============================

.. c:function:: u32 omap44xx_prm_read_reset_sources( void)

    return the last SoC reset source

    :param  void:
        no arguments

.. _`omap44xx_prm_read_reset_sources.description`:

Description
-----------

Return a u32 representing the last reset sources of the SoC.  The
returned reset source bits are standardized across OMAP SoCs.

.. _`omap44xx_prm_was_any_context_lost_old`:

omap44xx_prm_was_any_context_lost_old
=====================================

.. c:function:: bool omap44xx_prm_was_any_context_lost_old(u8 part, s16 inst, u16 idx)

    was module hardware context lost?

    :param u8 part:
        PRM partition ID (e.g., OMAP4430_PRM_PARTITION)

    :param s16 inst:
        PRM instance offset (e.g., OMAP4430_PRM_MPU_INST)

    :param u16 idx:
        CONTEXT register offset

.. _`omap44xx_prm_was_any_context_lost_old.description`:

Description
-----------

Return 1 if any bits were set in the \*\_CONTEXT\_\* register
identified by (\ ``part``\ , \ ``inst``\ , \ ``idx``\ ), which means that some context
was lost for that module; otherwise, return 0.

.. _`omap44xx_prm_clear_context_loss_flags_old`:

omap44xx_prm_clear_context_loss_flags_old
=========================================

.. c:function:: void omap44xx_prm_clear_context_loss_flags_old(u8 part, s16 inst, u16 idx)

    clear context loss flags

    :param u8 part:
        PRM partition ID (e.g., OMAP4430_PRM_PARTITION)

    :param s16 inst:
        PRM instance offset (e.g., OMAP4430_PRM_MPU_INST)

    :param u16 idx:
        CONTEXT register offset

.. _`omap44xx_prm_clear_context_loss_flags_old.description`:

Description
-----------

Clear hardware context loss bits for the module identified by
(\ ``part``\ , \ ``inst``\ , \ ``idx``\ ).  No return value.  XXX Writes to reserved bits;
is there a way to avoid this?

.. _`omap4_pwrdm_read_prev_logic_pwrst`:

omap4_pwrdm_read_prev_logic_pwrst
=================================

.. c:function:: int omap4_pwrdm_read_prev_logic_pwrst(struct powerdomain *pwrdm)

    read the previous logic powerstate

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to read the state for

.. _`omap4_pwrdm_read_prev_logic_pwrst.description`:

Description
-----------

Reads the previous logic powerstate for a powerdomain. This
function must determine the previous logic powerstate by first
checking the previous powerstate for the domain. If that was OFF,
then logic has been lost. If previous state was RETENTION, the
function reads the setting for the next retention logic state to
see the actual value.  In every other case, the logic is
retained. Returns either PWRDM_POWER_OFF or PWRDM_POWER_RET
depending whether the logic was retained or not.

.. _`omap4_pwrdm_read_prev_mem_pwrst`:

omap4_pwrdm_read_prev_mem_pwrst
===============================

.. c:function:: int omap4_pwrdm_read_prev_mem_pwrst(struct powerdomain *pwrdm, u8 bank)

    reads the previous memory powerstate

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to read mem powerstate for

    :param u8 bank:
        memory bank index

.. _`omap4_pwrdm_read_prev_mem_pwrst.description`:

Description
-----------

Reads the previous memory powerstate for a powerdomain. This
function must determine the previous memory powerstate by first
checking the previous powerstate for the domain. If that was OFF,
then logic has been lost. If previous state was RETENTION, the
function reads the setting for the next memory retention state to
see the actual value.  In every other case, the logic is
retained. Returns either PWRDM_POWER_OFF or PWRDM_POWER_RET
depending whether logic was retained or not.

.. This file was automatic generated / don't edit.

