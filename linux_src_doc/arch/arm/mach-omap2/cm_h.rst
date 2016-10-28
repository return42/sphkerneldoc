.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/cm.h

.. _`cm_ll_data`:

struct cm_ll_data
=================

.. c:type:: struct cm_ll_data

    fn ptrs to per-SoC CM function implementations

.. _`cm_ll_data.definition`:

Definition
----------

.. code-block:: c

    struct cm_ll_data {
        int (*split_idlest_reg)(void __iomem *idlest_reg, s16 *prcm_inst,u8 *idlest_reg_id);
        int (*wait_module_ready)(u8 part, s16 prcm_mod, u16 idlest_reg,u8 idlest_shift);
        int (*wait_module_idle)(u8 part, s16 prcm_mod, u16 idlest_reg,u8 idlest_shift);
        void (*module_enable)(u8 mode, u8 part, u16 inst, u16 clkctrl_offs);
        void (*module_disable)(u8 part, u16 inst, u16 clkctrl_offs);
    }

.. _`cm_ll_data.members`:

Members
-------

split_idlest_reg
    ptr to the SoC CM-specific split_idlest_reg impl

wait_module_ready
    ptr to the SoC CM-specific wait_module_ready impl

wait_module_idle
    ptr to the SoC CM-specific wait_module_idle impl

module_enable
    ptr to the SoC CM-specific module_enable impl

module_disable
    ptr to the SoC CM-specific module_disable impl

.. This file was automatic generated / don't edit.

