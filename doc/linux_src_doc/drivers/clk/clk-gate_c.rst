.. -*- coding: utf-8; mode: rst -*-

==========
clk-gate.c
==========


.. _`basic-gatable-clock-which-can-gate-and-ungate-it-s-ouput`:

basic gatable clock which can gate and ungate it's ouput
========================================================

Traits of this clock:
prepare - clk_(un)prepare only ensures parent is (un)prepared
enable - clk_enable and clk_disable are functional & control gating
rate - inherits rate from parent.  No clk_set_rate support
parent - fixed parent.  No clk_set_parent support



.. _`clk_register_gate`:

clk_register_gate
=================

.. c:function:: struct clk *clk_register_gate (struct device *dev, const char *name, const char *parent_name, unsigned long flags, void __iomem *reg, u8 bit_idx, u8 clk_gate_flags, spinlock_t *lock)

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

