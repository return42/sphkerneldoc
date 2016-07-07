.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-axm5516.c

.. _`axxia_clk`:

struct axxia_clk
================

.. c:type:: struct axxia_clk

    Common struct to all Axxia clocks.

.. _`axxia_clk.definition`:

Definition
----------

.. code-block:: c

    struct axxia_clk {
        struct clk_hw hw;
        struct regmap *regmap;
    }

.. _`axxia_clk.members`:

Members
-------

hw
    clk_hw for the common clk framework

regmap
    Regmap for the clock control registers

.. _`axxia_pllclk`:

struct axxia_pllclk
===================

.. c:type:: struct axxia_pllclk

    Axxia PLL generated clock.

.. _`axxia_pllclk.definition`:

Definition
----------

.. code-block:: c

    struct axxia_pllclk {
        struct axxia_clk aclk;
        u32 reg;
    }

.. _`axxia_pllclk.members`:

Members
-------

aclk
    Common struct

reg
    Offset into regmap for PLL control register

.. _`axxia_pllclk_recalc`:

axxia_pllclk_recalc
===================

.. c:function:: unsigned long axxia_pllclk_recalc(struct clk_hw *hw, unsigned long parent_rate)

    Calculate the PLL generated clock rate given the parent clock rate.

    :param struct clk_hw \*hw:
        *undescribed*

    :param unsigned long parent_rate:
        *undescribed*

.. _`axxia_divclk`:

struct axxia_divclk
===================

.. c:type:: struct axxia_divclk

    Axxia clock divider

.. _`axxia_divclk.definition`:

Definition
----------

.. code-block:: c

    struct axxia_divclk {
        struct axxia_clk aclk;
        u32 reg;
        u32 shift;
        u32 width;
    }

.. _`axxia_divclk.members`:

Members
-------

aclk
    Common struct

reg
    Offset into regmap for PLL control register

shift
    Bit position for divider value

width
    Number of bits in divider value

.. _`axxia_divclk_recalc_rate`:

axxia_divclk_recalc_rate
========================

.. c:function:: unsigned long axxia_divclk_recalc_rate(struct clk_hw *hw, unsigned long parent_rate)

    Calculate clock divider output rage

    :param struct clk_hw \*hw:
        *undescribed*

    :param unsigned long parent_rate:
        *undescribed*

.. _`axxia_clkmux`:

struct axxia_clkmux
===================

.. c:type:: struct axxia_clkmux

    Axxia clock mux

.. _`axxia_clkmux.definition`:

Definition
----------

.. code-block:: c

    struct axxia_clkmux {
        struct axxia_clk aclk;
        u32 reg;
        u32 shift;
        u32 width;
    }

.. _`axxia_clkmux.members`:

Members
-------

aclk
    Common struct

reg
    Offset into regmap for PLL control register

shift
    Bit position for selection value

width
    Number of bits in selection value

.. _`axxia_clkmux_get_parent`:

axxia_clkmux_get_parent
=======================

.. c:function:: u8 axxia_clkmux_get_parent(struct clk_hw *hw)

    Return the index of selected parent clock

    :param struct clk_hw \*hw:
        *undescribed*

.. This file was automatic generated / don't edit.

