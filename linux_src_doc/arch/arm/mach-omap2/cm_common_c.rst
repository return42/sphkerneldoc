.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/cm_common.c

.. _`omap2_set_globals_cm`:

omap2_set_globals_cm
====================

.. c:function:: void omap2_set_globals_cm(void __iomem *cm, void __iomem *cm2)

    set the CM/CM2 base addresses (for early use)

    :param void __iomem \*cm:
        CM base virtual address

    :param void __iomem \*cm2:
        CM2 base virtual address (if present on the booted SoC)

.. _`omap2_set_globals_cm.description`:

Description
-----------

XXX Will be replaced when the PRM/CM drivers are completed.

.. _`cm_split_idlest_reg`:

cm_split_idlest_reg
===================

.. c:function:: int cm_split_idlest_reg(void __iomem *idlest_reg, s16 *prcm_inst, u8 *idlest_reg_id)

    split CM_IDLEST reg addr into its components

    :param void __iomem \*idlest_reg:
        CM_IDLEST\* virtual address

    :param s16 \*prcm_inst:
        pointer to an s16 to return the PRCM instance offset

    :param u8 \*idlest_reg_id:
        pointer to a u8 to return the CM_IDLESTx register ID

.. _`cm_split_idlest_reg.description`:

Description
-----------

Given an absolute CM_IDLEST register address \ ``idlest_reg``\ , passes
the PRCM instance offset and IDLEST register ID back to the caller
via the \ ``prcm_inst``\  and \ ``idlest_reg_id``\ .  Returns -EINVAL upon error,
or 0 upon success.  XXX This function is only needed until absolute
register addresses are removed from the OMAP struct clk records.

.. _`omap_cm_wait_module_ready`:

omap_cm_wait_module_ready
=========================

.. c:function:: int omap_cm_wait_module_ready(u8 part, s16 prcm_mod, u16 idlest_reg, u8 idlest_shift)

    wait for a module to leave idle or standby

    :param u8 part:
        PRCM partition

    :param s16 prcm_mod:
        PRCM module offset

    :param u16 idlest_reg:
        CM_IDLESTx register

    :param u8 idlest_shift:
        shift of the bit in the CM_IDLEST\* register to check

.. _`omap_cm_wait_module_ready.description`:

Description
-----------

Wait for the PRCM to indicate that the module identified by
(@prcm_mod, \ ``idlest_id``\ , \ ``idlest_shift``\ ) is clocked.  Return 0 upon
success, -EBUSY if the module doesn't enable in time, or -EINVAL if
no per-SoC \ :c:func:`wait_module_ready`\  function pointer has been registered
or if the idlest register is unknown on the SoC.

.. _`omap_cm_wait_module_idle`:

omap_cm_wait_module_idle
========================

.. c:function:: int omap_cm_wait_module_idle(u8 part, s16 prcm_mod, u16 idlest_reg, u8 idlest_shift)

    wait for a module to enter idle or standby

    :param u8 part:
        PRCM partition

    :param s16 prcm_mod:
        PRCM module offset

    :param u16 idlest_reg:
        CM_IDLESTx register

    :param u8 idlest_shift:
        shift of the bit in the CM_IDLEST\* register to check

.. _`omap_cm_wait_module_idle.description`:

Description
-----------

Wait for the PRCM to indicate that the module identified by
(@prcm_mod, \ ``idlest_id``\ , \ ``idlest_shift``\ ) is no longer clocked.  Return
0 upon success, -EBUSY if the module doesn't enable in time, or
-EINVAL if no per-SoC \ :c:func:`wait_module_idle`\  function pointer has been
registered or if the idlest register is unknown on the SoC.

.. _`omap_cm_module_enable`:

omap_cm_module_enable
=====================

.. c:function:: int omap_cm_module_enable(u8 mode, u8 part, u16 inst, u16 clkctrl_offs)

    enable a module

    :param u8 mode:
        target mode for the module

    :param u8 part:
        PRCM partition

    :param u16 inst:
        PRCM instance

    :param u16 clkctrl_offs:
        CM_CLKCTRL register offset for the module

.. _`omap_cm_module_enable.description`:

Description
-----------

Enables clocks for a module identified by (@part, \ ``inst``\ , \ ``clkctrl_offs``\ )
making its IO space accessible. Return 0 upon success, -EINVAL if no
per-SoC \ :c:func:`module_enable`\  function pointer has been registered.

.. _`omap_cm_module_disable`:

omap_cm_module_disable
======================

.. c:function:: int omap_cm_module_disable(u8 part, u16 inst, u16 clkctrl_offs)

    disable a module

    :param u8 part:
        PRCM partition

    :param u16 inst:
        PRCM instance

    :param u16 clkctrl_offs:
        CM_CLKCTRL register offset for the module

.. _`omap_cm_module_disable.description`:

Description
-----------

Disables clocks for a module identified by (@part, \ ``inst``\ , \ ``clkctrl_offs``\ )
makings its IO space inaccessible. Return 0 upon success, -EINVAL if
no per-SoC \ :c:func:`module_disable`\  function pointer has been registered.

.. _`cm_register`:

cm_register
===========

.. c:function:: int cm_register(struct cm_ll_data *cld)

    register per-SoC low-level data with the CM

    :param struct cm_ll_data \*cld:
        low-level per-SoC OMAP CM data & function pointers to register

.. _`cm_register.description`:

Description
-----------

Register per-SoC low-level OMAP CM data and function pointers with
the OMAP CM common interface.  The caller must keep the data
pointed to by \ ``cld``\  valid until it calls \ :c:func:`cm_unregister`\  and
it returns successfully.  Returns 0 upon success, -EINVAL if \ ``cld``\ 
is NULL, or -EEXIST if \ :c:func:`cm_register`\  has already been called
without an intervening \ :c:func:`cm_unregister`\ .

.. _`cm_unregister`:

cm_unregister
=============

.. c:function:: int cm_unregister(struct cm_ll_data *cld)

    unregister per-SoC low-level data & function pointers

    :param struct cm_ll_data \*cld:
        low-level per-SoC OMAP CM data & function pointers to unregister

.. _`cm_unregister.description`:

Description
-----------

Unregister per-SoC low-level OMAP CM data and function pointers
that were previously registered with \ :c:func:`cm_register`\ .  The
caller may not destroy any of the data pointed to by \ ``cld``\  until
this function returns successfully.  Returns 0 upon success, or
-EINVAL if \ ``cld``\  is NULL or if \ ``cld``\  does not match the struct
cm_ll_data \* previously registered by \ :c:func:`cm_register`\ .

.. _`omap2_cm_base_init`:

omap2_cm_base_init
==================

.. c:function:: int omap2_cm_base_init( void)

    initialize iomappings for the CM drivers

    :param  void:
        no arguments

.. _`omap2_cm_base_init.description`:

Description
-----------

Detects and initializes the iomappings for the CM driver, based
on the DT data. Returns 0 in success, negative error value
otherwise.

.. _`omap_cm_init`:

omap_cm_init
============

.. c:function:: int omap_cm_init( void)

    low level init for the CM drivers

    :param  void:
        no arguments

.. _`omap_cm_init.description`:

Description
-----------

Initializes the low level clock infrastructure for CM drivers.
Returns 0 in success, negative error value in failure.

.. This file was automatic generated / don't edit.

