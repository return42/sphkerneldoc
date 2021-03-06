.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/cminst44xx.c

.. _`omap_cm_base_init`:

omap_cm_base_init
=================

.. c:function:: void omap_cm_base_init( void)

    Populates the cm partitions

    :param void:
        no arguments
    :type void: 

.. _`omap_cm_base_init.description`:

Description
-----------

Populates the base addresses of the \_cm_bases
array used for read/write of cm module registers.

.. _`_clkctrl_idlest`:

\_clkctrl_idlest
================

.. c:function:: u32 _clkctrl_idlest(u8 part, u16 inst, u16 clkctrl_offs)

    read a CM\_\*\_CLKCTRL register; mask & shift IDLEST bitfield

    :param part:
        PRCM partition ID that the CM_CLKCTRL register exists in
    :type part: u8

    :param inst:
        CM instance register offset (\*\_INST macro)
    :type inst: u16

    :param clkctrl_offs:
        Module clock control register offset (\*\_CLKCTRL macro)
    :type clkctrl_offs: u16

.. _`_clkctrl_idlest.description`:

Description
-----------

Return the IDLEST bitfield of a CM\_\*\_CLKCTRL register, shifted down to
bit 0.

.. _`_is_module_ready`:

\_is_module_ready
=================

.. c:function:: bool _is_module_ready(u8 part, u16 inst, u16 clkctrl_offs)

    can module registers be accessed without causing an abort?

    :param part:
        PRCM partition ID that the CM_CLKCTRL register exists in
    :type part: u8

    :param inst:
        CM instance register offset (\*\_INST macro)
    :type inst: u16

    :param clkctrl_offs:
        Module clock control register offset (\*\_CLKCTRL macro)
    :type clkctrl_offs: u16

.. _`_is_module_ready.description`:

Description
-----------

Returns true if the module's CM\_\*\_CLKCTRL.IDLEST bitfield is either
\*FUNCTIONAL or \*INTERFACE_IDLE; false otherwise.

.. _`_clktrctrl_write`:

\_clktrctrl_write
=================

.. c:function:: void _clktrctrl_write(u8 c, u8 part, u16 inst, u16 cdoffs)

    write \ ``c``\  to a CM_CLKSTCTRL.CLKTRCTRL register bitfield

    :param c:
        CLKTRCTRL register bitfield (LSB = bit 0, i.e., unshifted)
    :type c: u8

    :param part:
        PRCM partition ID that the CM_CLKSTCTRL register exists in
    :type part: u8

    :param inst:
        CM instance register offset (\*\_INST macro)
    :type inst: u16

    :param cdoffs:
        Clockdomain register offset (\*\_CDOFFS macro)
    :type cdoffs: u16

.. _`_clktrctrl_write.description`:

Description
-----------

\ ``c``\  must be the unshifted value for CLKTRCTRL - i.e., this function
will handle the shift itself.

.. _`omap4_cminst_is_clkdm_in_hwsup`:

omap4_cminst_is_clkdm_in_hwsup
==============================

.. c:function:: bool omap4_cminst_is_clkdm_in_hwsup(u8 part, u16 inst, u16 cdoffs)

    is a clockdomain in hwsup idle mode?

    :param part:
        PRCM partition ID that the CM_CLKSTCTRL register exists in
    :type part: u8

    :param inst:
        CM instance register offset (\*\_INST macro)
    :type inst: u16

    :param cdoffs:
        Clockdomain register offset (\*\_CDOFFS macro)
    :type cdoffs: u16

.. _`omap4_cminst_is_clkdm_in_hwsup.description`:

Description
-----------

Returns true if the clockdomain referred to by (@part, \ ``inst``\ , \ ``cdoffs``\ )
is in hardware-supervised idle mode, or 0 otherwise.

.. _`omap4_cminst_clkdm_enable_hwsup`:

omap4_cminst_clkdm_enable_hwsup
===============================

.. c:function:: void omap4_cminst_clkdm_enable_hwsup(u8 part, u16 inst, u16 cdoffs)

    put a clockdomain in hwsup-idle mode

    :param part:
        PRCM partition ID that the clockdomain registers exist in
    :type part: u8

    :param inst:
        CM instance register offset (\*\_INST macro)
    :type inst: u16

    :param cdoffs:
        Clockdomain register offset (\*\_CDOFFS macro)
    :type cdoffs: u16

.. _`omap4_cminst_clkdm_enable_hwsup.description`:

Description
-----------

Put a clockdomain referred to by (@part, \ ``inst``\ , \ ``cdoffs``\ ) into
hardware-supervised idle mode.  No return value.

.. _`omap4_cminst_clkdm_disable_hwsup`:

omap4_cminst_clkdm_disable_hwsup
================================

.. c:function:: void omap4_cminst_clkdm_disable_hwsup(u8 part, u16 inst, u16 cdoffs)

    put a clockdomain in swsup-idle mode

    :param part:
        PRCM partition ID that the clockdomain registers exist in
    :type part: u8

    :param inst:
        CM instance register offset (\*\_INST macro)
    :type inst: u16

    :param cdoffs:
        Clockdomain register offset (\*\_CDOFFS macro)
    :type cdoffs: u16

.. _`omap4_cminst_clkdm_disable_hwsup.description`:

Description
-----------

Put a clockdomain referred to by (@part, \ ``inst``\ , \ ``cdoffs``\ ) into
software-supervised idle mode, i.e., controlled manually by the
Linux OMAP clockdomain code.  No return value.

.. _`omap4_cminst_clkdm_force_wakeup`:

omap4_cminst_clkdm_force_wakeup
===============================

.. c:function:: void omap4_cminst_clkdm_force_wakeup(u8 part, u16 inst, u16 cdoffs)

    try to take a clockdomain out of idle

    :param part:
        PRCM partition ID that the clockdomain registers exist in
    :type part: u8

    :param inst:
        CM instance register offset (\*\_INST macro)
    :type inst: u16

    :param cdoffs:
        Clockdomain register offset (\*\_CDOFFS macro)
    :type cdoffs: u16

.. _`omap4_cminst_clkdm_force_wakeup.description`:

Description
-----------

Take a clockdomain referred to by (@part, \ ``inst``\ , \ ``cdoffs``\ ) out of idle,
waking it up.  No return value.

.. _`omap4_cminst_wait_module_ready`:

omap4_cminst_wait_module_ready
==============================

.. c:function:: int omap4_cminst_wait_module_ready(u8 part, s16 inst, u16 clkctrl_offs, u8 bit_shift)

    wait for a module to be in 'func' state

    :param part:
        PRCM partition ID that the CM_CLKCTRL register exists in
    :type part: u8

    :param inst:
        CM instance register offset (\*\_INST macro)
    :type inst: s16

    :param clkctrl_offs:
        Module clock control register offset (\*\_CLKCTRL macro)
    :type clkctrl_offs: u16

    :param bit_shift:
        bit shift for the register, ignored for OMAP4+
    :type bit_shift: u8

.. _`omap4_cminst_wait_module_ready.description`:

Description
-----------

Wait for the module IDLEST to be functional. If the idle state is in any
the non functional state (trans, idle or disabled), module and thus the
sysconfig cannot be accessed and will probably lead to an "imprecise
external abort"

.. _`omap4_cminst_wait_module_idle`:

omap4_cminst_wait_module_idle
=============================

.. c:function:: int omap4_cminst_wait_module_idle(u8 part, s16 inst, u16 clkctrl_offs, u8 bit_shift)

    wait for a module to be in 'disabled' state

    :param part:
        PRCM partition ID that the CM_CLKCTRL register exists in
    :type part: u8

    :param inst:
        CM instance register offset (\*\_INST macro)
    :type inst: s16

    :param clkctrl_offs:
        Module clock control register offset (\*\_CLKCTRL macro)
    :type clkctrl_offs: u16

    :param bit_shift:
        Bit shift for the register, ignored for OMAP4+
    :type bit_shift: u8

.. _`omap4_cminst_wait_module_idle.description`:

Description
-----------

Wait for the module IDLEST to be disabled. Some PRCM transition,
like reset assertion or parent clock de-activation must wait the
module to be fully disabled.

.. _`omap4_cminst_module_enable`:

omap4_cminst_module_enable
==========================

.. c:function:: void omap4_cminst_module_enable(u8 mode, u8 part, u16 inst, u16 clkctrl_offs)

    Enable the modulemode inside CLKCTRL

    :param mode:
        Module mode (SW or HW)
    :type mode: u8

    :param part:
        PRCM partition ID that the CM_CLKCTRL register exists in
    :type part: u8

    :param inst:
        CM instance register offset (\*\_INST macro)
    :type inst: u16

    :param clkctrl_offs:
        Module clock control register offset (\*\_CLKCTRL macro)
    :type clkctrl_offs: u16

.. _`omap4_cminst_module_enable.description`:

Description
-----------

No return value.

.. _`omap4_cminst_module_disable`:

omap4_cminst_module_disable
===========================

.. c:function:: void omap4_cminst_module_disable(u8 part, u16 inst, u16 clkctrl_offs)

    Disable the module inside CLKCTRL

    :param part:
        PRCM partition ID that the CM_CLKCTRL register exists in
    :type part: u8

    :param inst:
        CM instance register offset (\*\_INST macro)
    :type inst: u16

    :param clkctrl_offs:
        Module clock control register offset (\*\_CLKCTRL macro)
    :type clkctrl_offs: u16

.. _`omap4_cminst_module_disable.description`:

Description
-----------

No return value.

.. _`omap4_clkdm_save_context`:

omap4_clkdm_save_context
========================

.. c:function:: int omap4_clkdm_save_context(struct clockdomain *clkdm)

    Save the clockdomain modulemode context

    :param clkdm:
        The clockdomain pointer whose context needs to be saved
    :type clkdm: struct clockdomain \*

.. _`omap4_clkdm_save_context.description`:

Description
-----------

Save the clockdomain modulemode context.

.. _`omap4_clkdm_restore_context`:

omap4_clkdm_restore_context
===========================

.. c:function:: int omap4_clkdm_restore_context(struct clockdomain *clkdm)

    Restore the clockdomain modulemode context

    :param clkdm:
        The clockdomain pointer whose context needs to be restored
    :type clkdm: struct clockdomain \*

.. _`omap4_clkdm_restore_context.description`:

Description
-----------

Restore the clockdomain modulemode context.

.. This file was automatic generated / don't edit.

