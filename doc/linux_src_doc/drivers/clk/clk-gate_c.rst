.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-gate.c

.. _`clk_hw_register_gate`:

clk_hw_register_gate
====================

.. c:function:: struct clk_hw *clk_hw_register_gate(struct device *dev, const char *name, const char *parent_name, unsigned long flags, void __iomem *reg, u8 bit_idx, u8 clk_gate_flags, spinlock_t *lock)

    register a gate clock with the clock framework

    :param struct device \*dev:
        device that is registering this clock

    :param const char \*name:
        name of this clock

    :param const char \*parent_name:
        name of this clock's parent

    :param unsigned long flags:
        framework-specific flags for this clock

    :param void __iomem \*reg:
        register address to control gating of this clock

    :param u8 bit_idx:
        which bit in the register controls gating of this clock

    :param u8 clk_gate_flags:
        gate-specific flags for this clock

    :param spinlock_t \*lock:
        shared register lock for this clock

.. This file was automatic generated / don't edit.

