.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/qcom/clk-alpha-pll.h

.. _`clk_alpha_pll`:

struct clk_alpha_pll
====================

.. c:type:: struct clk_alpha_pll

    phase locked loop (PLL)

.. _`clk_alpha_pll.definition`:

Definition
----------

.. code-block:: c

    struct clk_alpha_pll {
        u32 offset;
        const struct pll_vco *vco_table;
        size_t num_vco;
    #define SUPPORTS_OFFLINE_REQ BIT(0)
    #define SUPPORTS_16BIT_ALPHA BIT(1)
    #define SUPPORTS_FSM_MODE BIT(2)
        u8 flags;
        struct clk_regmap clkr;
    }

.. _`clk_alpha_pll.members`:

Members
-------

offset
    base address of registers

vco_table
    array of VCO settings

num_vco
    *undescribed*

flags
    *undescribed*

clkr
    regmap clock handle

.. _`clk_alpha_pll_postdiv`:

struct clk_alpha_pll_postdiv
============================

.. c:type:: struct clk_alpha_pll_postdiv

    phase locked loop (PLL) post-divider

.. _`clk_alpha_pll_postdiv.definition`:

Definition
----------

.. code-block:: c

    struct clk_alpha_pll_postdiv {
        u32 offset;
        u8 width;
        struct clk_regmap clkr;
    }

.. _`clk_alpha_pll_postdiv.members`:

Members
-------

offset
    base address of registers

width
    width of post-divider

clkr
    regmap clock handle

.. This file was automatic generated / don't edit.

