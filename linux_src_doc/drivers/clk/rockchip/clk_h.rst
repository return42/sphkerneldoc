.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/rockchip/clk.h

.. _`rockchip_clk_provider`:

struct rockchip_clk_provider
============================

.. c:type:: struct rockchip_clk_provider

    information about clock provider

.. _`rockchip_clk_provider.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_clk_provider {
        void __iomem *reg_base;
        struct clk_onecell_data clk_data;
        struct device_node *cru_node;
        struct regmap *grf;
        spinlock_t lock;
    }

.. _`rockchip_clk_provider.members`:

Members
-------

reg_base
    virtual address for the register base.

clk_data
    holds clock related data like clk\* and number of clocks.

cru_node
    device-node of the clock-provider

grf
    regmap of the general-register-files syscon

lock
    maintains exclusion between callbacks for a given clock-provider.

.. _`rockchip_pll_clock`:

struct rockchip_pll_clock
=========================

.. c:type:: struct rockchip_pll_clock

    information about pll clock

.. _`rockchip_pll_clock.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_pll_clock {
        unsigned int id;
        const char *name;
        const char *const *parent_names;
        u8 num_parents;
        unsigned long flags;
        int con_offset;
        int mode_offset;
        int mode_shift;
        int lock_shift;
        enum rockchip_pll_type type;
        u8 pll_flags;
        struct rockchip_pll_rate_table *rate_table;
    }

.. _`rockchip_pll_clock.members`:

Members
-------

id
    platform specific id of the clock.

name
    name of this pll clock.

parent_names
    name of the parent clock.

num_parents
    number of parents

flags
    optional flags for basic clock.

con_offset
    offset of the register for configuring the PLL.

mode_offset
    offset of the register for configuring the PLL-mode.

mode_shift
    offset inside the mode-register for the mode of this pll.

lock_shift
    offset inside the lock register for the lock status.

type
    Type of PLL to be registered.

pll_flags
    hardware-specific flags

rate_table
    Table of usable pll rates

.. _`rockchip_pll_clock.flags`:

Flags
-----

ROCKCHIP_PLL_SYNC_RATE - check rate parameters to match against the
rate_table parameters and ajust them if necessary.

.. _`rockchip_cpuclk_reg_data`:

struct rockchip_cpuclk_reg_data
===============================

.. c:type:: struct rockchip_cpuclk_reg_data

    register offsets and masks of the cpuclock

.. _`rockchip_cpuclk_reg_data.definition`:

Definition
----------

.. code-block:: c

    struct rockchip_cpuclk_reg_data {
        int core_reg;
        u8 div_core_shift;
        u32 div_core_mask;
        u8 mux_core_alt;
        u8 mux_core_main;
        u8 mux_core_shift;
        u32 mux_core_mask;
    }

.. _`rockchip_cpuclk_reg_data.members`:

Members
-------

core_reg
    register offset of the core settings register

div_core_shift
    core divider offset used to divide the pll value

div_core_mask
    core divider mask

mux_core_alt
    mux value to select alternate parent

mux_core_main
    mux value to select main parent of core

mux_core_shift
    offset of the core multiplexer

mux_core_mask
    core multiplexer mask

.. This file was automatic generated / don't edit.

