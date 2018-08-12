.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/meson/clk-regmap.h

.. _`clk_regmap`:

struct clk_regmap
=================

.. c:type:: struct clk_regmap

    regmap backed clock

.. _`clk_regmap.definition`:

Definition
----------

.. code-block:: c

    struct clk_regmap {
        struct clk_hw hw;
        struct regmap *map;
        void *data;
    }

.. _`clk_regmap.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

map
    pointer to the regmap structure controlling the clock

data
    data specific to the clock type

.. _`clk_regmap.description`:

Description
-----------

Clock which is controlled by regmap backed registers. The actual type of
of the clock is controlled by the clock_ops and data.

.. _`clk_regmap_gate_data`:

struct clk_regmap_gate_data
===========================

.. c:type:: struct clk_regmap_gate_data

    regmap backed gate specific data

.. _`clk_regmap_gate_data.definition`:

Definition
----------

.. code-block:: c

    struct clk_regmap_gate_data {
        unsigned int offset;
        u8 bit_idx;
        u8 flags;
    }

.. _`clk_regmap_gate_data.members`:

Members
-------

offset
    offset of the register controlling gate

bit_idx
    single bit controlling gate

flags
    hardware-specific flags

.. _`clk_regmap_gate_data.flags`:

Flags
-----

Same as clk_gate except CLK_GATE_HIWORD_MASK which is ignored

.. _`clk_regmap_div_data`:

struct clk_regmap_div_data
==========================

.. c:type:: struct clk_regmap_div_data

    regmap backed adjustable divider specific data

.. _`clk_regmap_div_data.definition`:

Definition
----------

.. code-block:: c

    struct clk_regmap_div_data {
        unsigned int offset;
        u8 shift;
        u8 width;
        u8 flags;
        const struct clk_div_table *table;
    }

.. _`clk_regmap_div_data.members`:

Members
-------

offset
    offset of the register controlling the divider

shift
    shift to the divider bit field

width
    width of the divider bit field

flags
    *undescribed*

table
    array of value/divider pairs, last entry should have div = 0

.. _`clk_regmap_div_data.flags`:

Flags
-----

Same as clk_divider except CLK_DIVIDER_HIWORD_MASK which is ignored

.. _`clk_regmap_mux_data`:

struct clk_regmap_mux_data
==========================

.. c:type:: struct clk_regmap_mux_data

    regmap backed multiplexer clock specific data

.. _`clk_regmap_mux_data.definition`:

Definition
----------

.. code-block:: c

    struct clk_regmap_mux_data {
        unsigned int offset;
        u32 *table;
        u32 mask;
        u8 shift;
        u8 flags;
    }

.. _`clk_regmap_mux_data.members`:

Members
-------

offset
    offset of theregister controlling multiplexer

table
    array of parent indexed register values

mask
    mask of mutliplexer bit field

shift
    shift to multiplexer bit field

flags
    hardware-specific flags

.. _`clk_regmap_mux_data.flags`:

Flags
-----

Same as clk_divider except CLK_MUX_HIWORD_MASK which is ignored

.. This file was automatic generated / don't edit.

