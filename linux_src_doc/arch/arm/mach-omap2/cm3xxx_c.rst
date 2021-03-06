.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/cm3xxx.c

.. _`omap3xxx_cm_wait_module_ready`:

omap3xxx_cm_wait_module_ready
=============================

.. c:function:: int omap3xxx_cm_wait_module_ready(u8 part, s16 prcm_mod, u16 idlest_id, u8 idlest_shift)

    wait for a module to leave idle or standby

    :param part:
        PRCM partition, ignored for OMAP3
    :type part: u8

    :param prcm_mod:
        PRCM module offset
    :type prcm_mod: s16

    :param idlest_id:
        CM_IDLESTx register ID (i.e., x = 1, 2, 3)
    :type idlest_id: u16

    :param idlest_shift:
        shift of the bit in the CM_IDLEST\* register to check
    :type idlest_shift: u8

.. _`omap3xxx_cm_wait_module_ready.description`:

Description
-----------

Wait for the PRCM to indicate that the module identified by
(@prcm_mod, \ ``idlest_id``\ , \ ``idlest_shift``\ ) is clocked.  Return 0 upon
success or -EBUSY if the module doesn't enable in time.

.. _`omap3xxx_cm_split_idlest_reg`:

omap3xxx_cm_split_idlest_reg
============================

.. c:function:: int omap3xxx_cm_split_idlest_reg(struct clk_omap_reg *idlest_reg, s16 *prcm_inst, u8 *idlest_reg_id)

    split CM_IDLEST reg addr into its components

    :param idlest_reg:
        CM_IDLEST\* virtual address
    :type idlest_reg: struct clk_omap_reg \*

    :param prcm_inst:
        pointer to an s16 to return the PRCM instance offset
    :type prcm_inst: s16 \*

    :param idlest_reg_id:
        pointer to a u8 to return the CM_IDLESTx register ID
    :type idlest_reg_id: u8 \*

.. _`omap3xxx_cm_split_idlest_reg.description`:

Description
-----------

XXX This function is only needed until absolute register addresses are
removed from the OMAP struct clk records.

.. This file was automatic generated / don't edit.

