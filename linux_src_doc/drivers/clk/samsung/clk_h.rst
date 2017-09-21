.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/samsung/clk.h

.. _`samsung_clk_provider`:

struct samsung_clk_provider
===========================

.. c:type:: struct samsung_clk_provider

    information about clock provider

.. _`samsung_clk_provider.definition`:

Definition
----------

.. code-block:: c

    struct samsung_clk_provider {
        void __iomem *reg_base;
        spinlock_t lock;
        struct clk_hw_onecell_data clk_data;
    }

.. _`samsung_clk_provider.members`:

Members
-------

reg_base
    virtual address for the register base.

lock
    maintains exclusion between callbacks for a given clock-provider.

clk_data
    holds clock related data like clk_hw\* and number of clocks.

.. _`samsung_clock_alias`:

struct samsung_clock_alias
==========================

.. c:type:: struct samsung_clock_alias

    information about mux clock

.. _`samsung_clock_alias.definition`:

Definition
----------

.. code-block:: c

    struct samsung_clock_alias {
        unsigned int id;
        const char *dev_name;
        const char *alias;
    }

.. _`samsung_clock_alias.members`:

Members
-------

id
    platform specific id of the clock.

dev_name
    name of the device to which this clock belongs.

alias
    optional clock alias name to be assigned to this clock.

.. _`samsung_fixed_rate_clock`:

struct samsung_fixed_rate_clock
===============================

.. c:type:: struct samsung_fixed_rate_clock

    information about fixed-rate clock

.. _`samsung_fixed_rate_clock.definition`:

Definition
----------

.. code-block:: c

    struct samsung_fixed_rate_clock {
        unsigned int id;
        char *name;
        const char *parent_name;
        unsigned long flags;
        unsigned long fixed_rate;
    }

.. _`samsung_fixed_rate_clock.members`:

Members
-------

id
    platform specific id of the clock.

name
    name of this fixed-rate clock.

parent_name
    optional parent clock name.

flags
    optional fixed-rate clock flags.

fixed_rate
    *undescribed*

.. _`samsung_mux_clock`:

struct samsung_mux_clock
========================

.. c:type:: struct samsung_mux_clock

    information about mux clock

.. _`samsung_mux_clock.definition`:

Definition
----------

.. code-block:: c

    struct samsung_mux_clock {
        unsigned int id;
        const char *dev_name;
        const char *name;
        const char *const *parent_names;
        u8 num_parents;
        unsigned long flags;
        unsigned long offset;
        u8 shift;
        u8 width;
        u8 mux_flags;
        const char *alias;
    }

.. _`samsung_mux_clock.members`:

Members
-------

id
    platform specific id of the clock.

dev_name
    name of the device to which this clock belongs.

name
    name of this mux clock.

parent_names
    array of pointer to parent clock names.

num_parents
    number of parents listed in \ ``parent_names``\ .

flags
    optional flags for basic clock.

offset
    offset of the register for configuring the mux.

shift
    starting bit location of the mux control bit-field in \ ``reg``\ .

width
    width of the mux control bit-field in \ ``reg``\ .

mux_flags
    flags for mux-type clock.

alias
    optional clock alias name to be assigned to this clock.

.. _`samsung_gate_clock`:

struct samsung_gate_clock
=========================

.. c:type:: struct samsung_gate_clock

    information about gate clock

.. _`samsung_gate_clock.definition`:

Definition
----------

.. code-block:: c

    struct samsung_gate_clock {
        unsigned int id;
        const char *dev_name;
        const char *name;
        const char *parent_name;
        unsigned long flags;
        unsigned long offset;
        u8 bit_idx;
        u8 gate_flags;
        const char *alias;
    }

.. _`samsung_gate_clock.members`:

Members
-------

id
    platform specific id of the clock.

dev_name
    name of the device to which this clock belongs.

name
    name of this gate clock.

parent_name
    name of the parent clock.

flags
    optional flags for basic clock.

offset
    offset of the register for configuring the gate.

bit_idx
    bit index of the gate control bit-field in \ ``reg``\ .

gate_flags
    flags for gate-type clock.

alias
    optional clock alias name to be assigned to this clock.

.. _`samsung_clk_reg_dump`:

struct samsung_clk_reg_dump
===========================

.. c:type:: struct samsung_clk_reg_dump

    register dump of clock controller registers.

.. _`samsung_clk_reg_dump.definition`:

Definition
----------

.. code-block:: c

    struct samsung_clk_reg_dump {
        u32 offset;
        u32 value;
    }

.. _`samsung_clk_reg_dump.members`:

Members
-------

offset
    clock register offset from the controller base address.

value
    the value to be register at offset.

.. _`samsung_pll_clock`:

struct samsung_pll_clock
========================

.. c:type:: struct samsung_pll_clock

    information about pll clock

.. _`samsung_pll_clock.definition`:

Definition
----------

.. code-block:: c

    struct samsung_pll_clock {
        unsigned int id;
        const char *dev_name;
        const char *name;
        const char *parent_name;
        unsigned long flags;
        int con_offset;
        int lock_offset;
        enum samsung_pll_type type;
        const struct samsung_pll_rate_table *rate_table;
        const char *alias;
    }

.. _`samsung_pll_clock.members`:

Members
-------

id
    platform specific id of the clock.

dev_name
    name of the device to which this clock belongs.

name
    name of this pll clock.

parent_name
    name of the parent clock.

flags
    optional flags for basic clock.

con_offset
    offset of the register for configuring the PLL.

lock_offset
    offset of the register for locking the PLL.

type
    Type of PLL to be registered.

rate_table
    *undescribed*

alias
    optional clock alias name to be assigned to this clock.

.. This file was automatic generated / don't edit.

