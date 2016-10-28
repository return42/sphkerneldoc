.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/rockchip/clk-cpu.c

.. _`rockchip_cpuclk`:

struct rockchip_cpuclk
======================

.. c:type:: struct rockchip_cpuclk

    information about clock supplied to a CPU core.

.. _`rockchip_cpuclk.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_cpuclk {
        struct clk_hw hw;
        struct clk_mux cpu_mux;
        const struct clk_ops *cpu_mux_ops;
        struct clk *alt_parent;
        void __iomem *reg_base;
        struct notifier_block clk_nb;
        unsigned int rate_count;
        struct rockchip_cpuclk_rate_table *rate_table;
        const struct rockchip_cpuclk_reg_data *reg_data;
        spinlock_t *lock;
    }

.. _`rockchip_cpuclk.members`:

Members
-------

hw
    handle between ccf and cpu clock.

cpu_mux
    *undescribed*

cpu_mux_ops
    *undescribed*

alt_parent
    alternate parent clock to use when switching the speed
    of the primary parent clock.

reg_base
    base register for cpu-clock values.

clk_nb
    clock notifier registered for changes in clock speed of the
    primary parent clock.

rate_count
    number of rates in the rate_table

rate_table
    pll-rates and their associated dividers

reg_data
    cpu-specific register settings

lock
    clock lock

.. This file was automatic generated / don't edit.

