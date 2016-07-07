.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/qcom/clk-pll.h

.. _`pll_freq_tbl`:

struct pll_freq_tbl
===================

.. c:type:: struct pll_freq_tbl

    PLL frequency table

.. _`pll_freq_tbl.definition`:

Definition
----------

.. code-block:: c

    struct pll_freq_tbl {
        unsigned long freq;
        u16 l;
        u16 m;
        u16 n;
        u32 ibits;
    }

.. _`pll_freq_tbl.members`:

Members
-------

freq
    *undescribed*

l
    L value

m
    M value

n
    N value

ibits
    internal values

.. _`clk_pll`:

struct clk_pll
==============

.. c:type:: struct clk_pll

    phase locked loop (PLL)

.. _`clk_pll.definition`:

Definition
----------

.. code-block:: c

    struct clk_pll {
        u32 l_reg;
        u32 m_reg;
        u32 n_reg;
        u32 config_reg;
        u32 mode_reg;
        u32 status_reg;
        u8 status_bit;
        u8 post_div_width;
        u8 post_div_shift;
        const struct pll_freq_tbl *freq_tbl;
        struct clk_regmap clkr;
    }

.. _`clk_pll.members`:

Members
-------

l_reg
    L register

m_reg
    M register

n_reg
    N register

config_reg
    config register

mode_reg
    mode register

status_reg
    status register

status_bit
    ANDed with \ ``status_reg``\  to determine if PLL is enabled

post_div_width
    *undescribed*

post_div_shift
    *undescribed*

freq_tbl
    PLL frequency table

clkr
    *undescribed*

.. This file was automatic generated / don't edit.

