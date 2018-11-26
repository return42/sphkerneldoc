.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/rockchip/clk.c

.. _`rockchip_clk_register_branch`:

rockchip_clk_register_branch
============================

.. c:function:: struct clk *rockchip_clk_register_branch(const char *name, const char *const *parent_names, u8 num_parents, void __iomem *base, int muxdiv_offset, u8 mux_shift, u8 mux_width, u8 mux_flags, u8 div_shift, u8 div_width, u8 div_flags, struct clk_div_table *div_table, int gate_offset, u8 gate_shift, u8 gate_flags, unsigned long flags, spinlock_t *lock)

    Most clock branches have a form like

    :param name:
        *undescribed*
    :type name: const char \*

    :param parent_names:
        *undescribed*
    :type parent_names: const char \*const \*

    :param num_parents:
        *undescribed*
    :type num_parents: u8

    :param base:
        *undescribed*
    :type base: void __iomem \*

    :param muxdiv_offset:
        *undescribed*
    :type muxdiv_offset: int

    :param mux_shift:
        *undescribed*
    :type mux_shift: u8

    :param mux_width:
        *undescribed*
    :type mux_width: u8

    :param mux_flags:
        *undescribed*
    :type mux_flags: u8

    :param div_shift:
        *undescribed*
    :type div_shift: u8

    :param div_width:
        *undescribed*
    :type div_width: u8

    :param div_flags:
        *undescribed*
    :type div_flags: u8

    :param div_table:
        *undescribed*
    :type div_table: struct clk_div_table \*

    :param gate_offset:
        *undescribed*
    :type gate_offset: int

    :param gate_shift:
        *undescribed*
    :type gate_shift: u8

    :param gate_flags:
        *undescribed*
    :type gate_flags: u8

    :param flags:
        *undescribed*
    :type flags: unsigned long

    :param lock:
        *undescribed*
    :type lock: spinlock_t \*

.. _`rockchip_clk_register_branch.description`:

Description
-----------

src1 --\|--\
\|M \|--[GATE]-[DIV]-
src2 --\|--/

sometimes without one of those components.

.. _`rockchip_fractional_approximation`:

rockchip_fractional_approximation
=================================

.. c:function:: void rockchip_fractional_approximation(struct clk_hw *hw, unsigned long rate, unsigned long *parent_rate, unsigned long *m, unsigned long *n)

    numerator to generate precise clock frequency.

    :param hw:
        *undescribed*
    :type hw: struct clk_hw \*

    :param rate:
        *undescribed*
    :type rate: unsigned long

    :param parent_rate:
        *undescribed*
    :type parent_rate: unsigned long \*

    :param m:
        *undescribed*
    :type m: unsigned long \*

    :param n:
        *undescribed*
    :type n: unsigned long \*

.. This file was automatic generated / don't edit.

