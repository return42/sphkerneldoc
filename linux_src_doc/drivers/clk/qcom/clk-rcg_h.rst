.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/qcom/clk-rcg.h

.. _`mn`:

struct mn
=========

.. c:type:: struct mn

    M/N:D counter

.. _`mn.definition`:

Definition
----------

.. code-block:: c

    struct mn {
        u8 mnctr_en_bit;
        u8 mnctr_reset_bit;
        u8 mnctr_mode_shift;
    #define MNCTR_MODE_DUAL 0x2
    #define MNCTR_MODE_MASK 0x3
        u8 n_val_shift;
        u8 m_val_shift;
        u8 width;
        bool reset_in_cc;
    }

.. _`mn.members`:

Members
-------

mnctr_en_bit
    bit to enable mn counter

mnctr_reset_bit
    bit to assert mn counter reset

mnctr_mode_shift
    lowest bit of mn counter mode field

n_val_shift
    lowest bit of n value field

m_val_shift
    lowest bit of m value field

width
    number of bits in m/n/d values

reset_in_cc
    true if the mnctr_reset_bit is in the CC register

.. _`pre_div`:

struct pre_div
==============

.. c:type:: struct pre_div

    pre-divider

.. _`pre_div.definition`:

Definition
----------

.. code-block:: c

    struct pre_div {
        u8 pre_div_shift;
        u8 pre_div_width;
    }

.. _`pre_div.members`:

Members
-------

pre_div_shift
    lowest bit of pre divider field

pre_div_width
    number of bits in predivider

.. _`src_sel`:

struct src_sel
==============

.. c:type:: struct src_sel

    source selector

.. _`src_sel.definition`:

Definition
----------

.. code-block:: c

    struct src_sel {
        u8 src_sel_shift;
    #define SRC_SEL_MASK 0x7
        const struct parent_map *parent_map;
    }

.. _`src_sel.members`:

Members
-------

src_sel_shift
    lowest bit of source selection field

parent_map
    map from software's parent index to hardware's src_sel field

.. _`clk_rcg`:

struct clk_rcg
==============

.. c:type:: struct clk_rcg

    root clock generator

.. _`clk_rcg.definition`:

Definition
----------

.. code-block:: c

    struct clk_rcg {
        u32 ns_reg;
        u32 md_reg;
        struct mn mn;
        struct pre_div p;
        struct src_sel s;
        const struct freq_tbl *freq_tbl;
        struct clk_regmap clkr;
    }

.. _`clk_rcg.members`:

Members
-------

ns_reg
    NS register

md_reg
    MD register

mn
    mn counter

p
    pre divider

s
    source selector

freq_tbl
    frequency table

clkr
    regmap clock handle

.. _`clk_dyn_rcg`:

struct clk_dyn_rcg
==================

.. c:type:: struct clk_dyn_rcg

    root clock generator with glitch free mux

.. _`clk_dyn_rcg.definition`:

Definition
----------

.. code-block:: c

    struct clk_dyn_rcg {
        u32 ns_reg[2];
        u32 md_reg[2];
        u32 bank_reg;
        u8 mux_sel_bit;
        struct mn mn[2];
        struct pre_div p[2];
        struct src_sel s[2];
        const struct freq_tbl *freq_tbl;
        struct clk_regmap clkr;
    }

.. _`clk_dyn_rcg.members`:

Members
-------

ns_reg
    NS0 and NS1 register

md_reg
    MD0 and MD1 register

bank_reg
    register to XOR \ ``mux_sel_bit``\  into to switch glitch free mux

mux_sel_bit
    bit to switch glitch free mux

mn
    mn counter (banked)

p
    *undescribed*

s
    source selector (banked)

freq_tbl
    frequency table

clkr
    regmap clock handle

.. _`clk_rcg2`:

struct clk_rcg2
===============

.. c:type:: struct clk_rcg2

    root clock generator

.. _`clk_rcg2.definition`:

Definition
----------

.. code-block:: c

    struct clk_rcg2 {
        u32 cmd_rcgr;
        u8 mnd_width;
        u8 hid_width;
        u8 safe_src_index;
        const struct parent_map *parent_map;
        const struct freq_tbl *freq_tbl;
        struct clk_regmap clkr;
    }

.. _`clk_rcg2.members`:

Members
-------

cmd_rcgr
    corresponds to \*\_CMD_RCGR

mnd_width
    number of bits in m/n/d values

hid_width
    number of bits in half integer divider

safe_src_index
    safe src index value

parent_map
    map from software's parent index to hardware's src_sel field

freq_tbl
    frequency table

clkr
    regmap clock handle

.. This file was automatic generated / don't edit.

