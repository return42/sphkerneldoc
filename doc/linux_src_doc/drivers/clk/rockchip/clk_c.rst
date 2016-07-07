.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/rockchip/clk.c

.. _`rockchip_clk_register_branch`:

rockchip_clk_register_branch
============================

.. c:function:: struct clk *rockchip_clk_register_branch(const char *name, const char *const *parent_names, u8 num_parents, void __iomem *base, int muxdiv_offset, u8 mux_shift, u8 mux_width, u8 mux_flags, u8 div_shift, u8 div_width, u8 div_flags, struct clk_div_table *div_table, int gate_offset, u8 gate_shift, u8 gate_flags, unsigned long flags, spinlock_t *lock)

    Most clock branches have a form like

    :param const char \*name:
        *undescribed*

    :param const char \*const \*parent_names:
        *undescribed*

    :param u8 num_parents:
        *undescribed*

    :param void __iomem \*base:
        *undescribed*

    :param int muxdiv_offset:
        *undescribed*

    :param u8 mux_shift:
        *undescribed*

    :param u8 mux_width:
        *undescribed*

    :param u8 mux_flags:
        *undescribed*

    :param u8 div_shift:
        *undescribed*

    :param u8 div_width:
        *undescribed*

    :param u8 div_flags:
        *undescribed*

    :param struct clk_div_table \*div_table:
        *undescribed*

    :param int gate_offset:
        *undescribed*

    :param u8 gate_shift:
        *undescribed*

    :param u8 gate_flags:
        *undescribed*

    :param unsigned long flags:
        *undescribed*

    :param spinlock_t \*lock:
        *undescribed*

.. _`rockchip_clk_register_branch.description`:

Description
-----------

src1 --\|--\
\|M \|--[GATE]-[DIV]-
src2 --\|--/

sometimes without one of those components.

.. This file was automatic generated / don't edit.

