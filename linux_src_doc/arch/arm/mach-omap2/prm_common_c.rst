.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/prm_common.c

.. _`omap_prcm_event_to_irq`:

omap_prcm_event_to_irq
======================

.. c:function:: int omap_prcm_event_to_irq(const char *name)

    given a PRCM event name, returns the corresponding IRQ on which the handler should be registered

    :param const char \*name:
        name of the PRCM interrupt bit to look up - see struct omap_prcm_irq

.. _`omap_prcm_event_to_irq.description`:

Description
-----------

Returns the Linux internal IRQ ID corresponding to \ ``name``\  upon success,
or -ENOENT upon failure.

.. _`omap_prcm_irq_cleanup`:

omap_prcm_irq_cleanup
=====================

.. c:function:: void omap_prcm_irq_cleanup( void)

    reverses memory allocated and other steps done by \ :c:func:`omap_prcm_register_chain_handler`\ 

    :param  void:
        no arguments

.. _`omap_prcm_irq_cleanup.description`:

Description
-----------

No return value.

.. _`omap_prcm_register_chain_handler`:

omap_prcm_register_chain_handler
================================

.. c:function:: int omap_prcm_register_chain_handler(struct omap_prcm_irq_setup *irq_setup)

    initializes the prcm chained interrupt handler based on provided parameters

    :param struct omap_prcm_irq_setup \*irq_setup:
        hardware data about the underlying PRM/PRCM

.. _`omap_prcm_register_chain_handler.description`:

Description
-----------

Set up the PRCM chained interrupt handler on the PRCM IRQ.  Sets up
one generic IRQ chip per PRM interrupt status/enable register pair.
Returns 0 upon success, -EINVAL if called twice or if invalid
arguments are passed, or -ENOMEM on any other error.

.. _`omap2_set_globals_prm`:

omap2_set_globals_prm
=====================

.. c:function:: void omap2_set_globals_prm(void __iomem *prm)

    set the PRM base address (for early use)

    :param void __iomem \*prm:
        PRM base virtual address

.. _`omap2_set_globals_prm.description`:

Description
-----------

XXX Will be replaced when the PRM/CM drivers are completed.

.. _`prm_read_reset_sources`:

prm_read_reset_sources
======================

.. c:function:: u32 prm_read_reset_sources( void)

    return the sources of the SoC's last reset

    :param  void:
        no arguments

.. _`prm_read_reset_sources.description`:

Description
-----------

Return a u32 bitmask representing the reset sources that caused the
SoC to reset.  The low-level per-SoC functions called by this
function remap the SoC-specific reset source bits into an
OMAP-common set of reset source bits, defined in
arch/arm/mach-omap2/prm.h.  Returns the standardized reset source
u32 bitmask from the hardware upon success, or returns (1 <<
OMAP_UNKNOWN_RST_SRC_ID_SHIFT) if no low-level \ :c:func:`read_reset_sources`\ 
function was registered.

.. _`prm_was_any_context_lost_old`:

prm_was_any_context_lost_old
============================

.. c:function:: bool prm_was_any_context_lost_old(u8 part, s16 inst, u16 idx)

    was device context lost? (old API)

    :param u8 part:
        PRM partition ID (e.g., OMAP4430_PRM_PARTITION)

    :param s16 inst:
        PRM instance offset (e.g., OMAP4430_PRM_MPU_INST)

    :param u16 idx:
        CONTEXT register offset

.. _`prm_was_any_context_lost_old.description`:

Description
-----------

Return 1 if any bits were set in the \*\_CONTEXT\_\* register
identified by (@part, \ ``inst``\ , \ ``idx``\ ), which means that some context
was lost for that module; otherwise, return 0.  XXX Deprecated;
callers need to use a less-SoC-dependent way to identify hardware
IP blocks.

.. _`prm_clear_context_loss_flags_old`:

prm_clear_context_loss_flags_old
================================

.. c:function:: void prm_clear_context_loss_flags_old(u8 part, s16 inst, u16 idx)

    clear context loss flags (old API)

    :param u8 part:
        PRM partition ID (e.g., OMAP4430_PRM_PARTITION)

    :param s16 inst:
        PRM instance offset (e.g., OMAP4430_PRM_MPU_INST)

    :param u16 idx:
        CONTEXT register offset

.. _`prm_clear_context_loss_flags_old.description`:

Description
-----------

Clear hardware context loss bits for the module identified by
(@part, \ ``inst``\ , \ ``idx``\ ).  No return value.  XXX Deprecated; callers
need to use a less-SoC-dependent way to identify hardware IP
blocks.

.. _`omap_prm_assert_hardreset`:

omap_prm_assert_hardreset
=========================

.. c:function:: int omap_prm_assert_hardreset(u8 shift, u8 part, s16 prm_mod, u16 offset)

    assert hardreset for an IP block

    :param u8 shift:
        register bit shift corresponding to the reset line

    :param u8 part:
        PRM partition

    :param s16 prm_mod:
        PRM submodule base or instance offset

    :param u16 offset:
        register offset

.. _`omap_prm_assert_hardreset.description`:

Description
-----------

Asserts a hardware reset line for an IP block.

.. _`omap_prm_deassert_hardreset`:

omap_prm_deassert_hardreset
===========================

.. c:function:: int omap_prm_deassert_hardreset(u8 shift, u8 st_shift, u8 part, s16 prm_mod, u16 offset, u16 st_offset)

    deassert hardreset for an IP block

    :param u8 shift:
        register bit shift corresponding to the reset line

    :param u8 st_shift:
        reset status bit shift corresponding to the reset line

    :param u8 part:
        PRM partition

    :param s16 prm_mod:
        PRM submodule base or instance offset

    :param u16 offset:
        register offset

    :param u16 st_offset:
        status register offset

.. _`omap_prm_deassert_hardreset.description`:

Description
-----------

Deasserts a hardware reset line for an IP block.

.. _`omap_prm_is_hardreset_asserted`:

omap_prm_is_hardreset_asserted
==============================

.. c:function:: int omap_prm_is_hardreset_asserted(u8 shift, u8 part, s16 prm_mod, u16 offset)

    check the hardreset status for an IP block

    :param u8 shift:
        register bit shift corresponding to the reset line

    :param u8 part:
        PRM partition

    :param s16 prm_mod:
        PRM submodule base or instance offset

    :param u16 offset:
        register offset

.. _`omap_prm_is_hardreset_asserted.description`:

Description
-----------

Checks if a hardware reset line for an IP block is enabled or not.

.. _`omap_prm_reconfigure_io_chain`:

omap_prm_reconfigure_io_chain
=============================

.. c:function:: void omap_prm_reconfigure_io_chain( void)

    clear latches and reconfigure I/O chain

    :param  void:
        no arguments

.. _`omap_prm_reconfigure_io_chain.description`:

Description
-----------

Clear any previously-latched I/O wakeup events and ensure that the
I/O wakeup gates are aligned with the current mux settings.
Calls SoC specific I/O chain reconfigure function if available,
otherwise does nothing.

.. _`omap_prm_reset_system`:

omap_prm_reset_system
=====================

.. c:function:: void omap_prm_reset_system( void)

    trigger global SW reset

    :param  void:
        no arguments

.. _`omap_prm_reset_system.description`:

Description
-----------

Triggers SoC specific global warm reset to reboot the device.

.. _`omap_prm_clear_mod_irqs`:

omap_prm_clear_mod_irqs
=======================

.. c:function:: int omap_prm_clear_mod_irqs(s16 module, u8 regs, u32 wkst_mask)

    clear wake-up events from PRCM interrupt

    :param s16 module:
        PRM module to clear wakeups from

    :param u8 regs:
        register to clear

    :param u32 wkst_mask:
        wkst bits to clear

.. _`omap_prm_clear_mod_irqs.description`:

Description
-----------

Clears any wakeup events for the module and register set defined.
Uses SoC specific implementation to do the actual wakeup status
clearing.

.. _`omap_prm_vp_check_txdone`:

omap_prm_vp_check_txdone
========================

.. c:function:: u32 omap_prm_vp_check_txdone(u8 vp_id)

    check voltage processor TX done status

    :param u8 vp_id:
        *undescribed*

.. _`omap_prm_vp_check_txdone.description`:

Description
-----------

Checks if voltage processor transmission has been completed.
Returns non-zero if a transmission has completed, 0 otherwise.

.. _`omap_prm_vp_clear_txdone`:

omap_prm_vp_clear_txdone
========================

.. c:function:: void omap_prm_vp_clear_txdone(u8 vp_id)

    clears voltage processor TX done status

    :param u8 vp_id:
        *undescribed*

.. _`omap_prm_vp_clear_txdone.description`:

Description
-----------

Clears the status bit for completed voltage processor transmission
returned by prm_vp_check_txdone.

.. _`prm_register`:

prm_register
============

.. c:function:: int prm_register(struct prm_ll_data *pld)

    register per-SoC low-level data with the PRM

    :param struct prm_ll_data \*pld:
        low-level per-SoC OMAP PRM data & function pointers to register

.. _`prm_register.description`:

Description
-----------

Register per-SoC low-level OMAP PRM data and function pointers with
the OMAP PRM common interface.  The caller must keep the data
pointed to by \ ``pld``\  valid until it calls \ :c:func:`prm_unregister`\  and
it returns successfully.  Returns 0 upon success, -EINVAL if \ ``pld``\ 
is NULL, or -EEXIST if \ :c:func:`prm_register`\  has already been called
without an intervening \ :c:func:`prm_unregister`\ .

.. _`prm_unregister`:

prm_unregister
==============

.. c:function:: int prm_unregister(struct prm_ll_data *pld)

    unregister per-SoC low-level data & function pointers

    :param struct prm_ll_data \*pld:
        low-level per-SoC OMAP PRM data & function pointers to unregister

.. _`prm_unregister.description`:

Description
-----------

Unregister per-SoC low-level OMAP PRM data and function pointers
that were previously registered with \ :c:func:`prm_register`\ .  The
caller may not destroy any of the data pointed to by \ ``pld``\  until
this function returns successfully.  Returns 0 upon success, or
-EINVAL if \ ``pld``\  is NULL or if \ ``pld``\  does not match the struct
prm_ll_data \* previously registered by \ :c:func:`prm_register`\ .

.. _`omap2_prm_base_init`:

omap2_prm_base_init
===================

.. c:function:: int omap2_prm_base_init( void)

    initialize iomappings for the PRM driver

    :param  void:
        no arguments

.. _`omap2_prm_base_init.description`:

Description
-----------

Detects and initializes the iomappings for the PRM driver, based
on the DT data. Returns 0 in success, negative error value
otherwise.

.. _`omap_prcm_init`:

omap_prcm_init
==============

.. c:function:: int omap_prcm_init( void)

    low level init for the PRCM drivers

    :param  void:
        no arguments

.. _`omap_prcm_init.description`:

Description
-----------

Initializes the low level clock infrastructure for PRCM drivers.
Returns 0 in success, negative error value in failure.

.. This file was automatic generated / don't edit.

