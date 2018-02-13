.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/qcom/clk-regmap-mux-div.h

.. _`clk_regmap_mux_div`:

struct clk_regmap_mux_div
=========================

.. c:type:: struct clk_regmap_mux_div

    combined mux/divider clock

.. _`clk_regmap_mux_div.definition`:

Definition
----------

.. code-block:: c

    struct clk_regmap_mux_div {
        u32 reg_offset;
        u32 hid_width;
        u32 hid_shift;
        u32 src_width;
        u32 src_shift;
        u32 div;
        u32 src;
        const u32 *parent_map;
        struct clk_regmap clkr;
        struct clk *pclk;
        struct notifier_block clk_nb;
    }

.. _`clk_regmap_mux_div.members`:

Members
-------

reg_offset
    offset of the mux/divider register

hid_width
    number of bits in half integer divider

hid_shift
    lowest bit of hid value field

src_width
    number of bits in source select

src_shift
    lowest bit of source select field

div
    the divider raw configuration value

src
    the mux index which will be used if the clock is enabled

parent_map
    map from parent_names index to src_sel field

clkr
    handle between common and hardware-specific interfaces

pclk
    the input PLL clock

clk_nb
    clock notifier for rate changes of the input PLL

.. This file was automatic generated / don't edit.

