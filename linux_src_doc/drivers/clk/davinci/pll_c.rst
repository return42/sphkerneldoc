.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/davinci/pll.c

.. _`davinci_pll_clk`:

struct davinci_pll_clk
======================

.. c:type:: struct davinci_pll_clk

    Main PLL clock (aka PLLOUT)

.. _`davinci_pll_clk.definition`:

Definition
----------

.. code-block:: c

    struct davinci_pll_clk {
        struct clk_hw hw;
        void __iomem *base;
        u32 pllm_min;
        u32 pllm_max;
        u32 pllm_mask;
    }

.. _`davinci_pll_clk.members`:

Members
-------

hw
    clk_hw for the pll

base
    Base memory address

pllm_min
    The minimum allowable PLLM[PLLM] value

pllm_max
    The maxiumum allowable PLLM[PLLM] value

pllm_mask
    Bitmask for PLLM[PLLM] value

.. _`davinci_pll_div_register`:

davinci_pll_div_register
========================

.. c:function:: struct clk *davinci_pll_div_register(struct device *dev, const char *name, const char *parent_name, void __iomem *reg, bool fixed, u32 flags)

    common \*DIV clock implementation

    :param dev:
        The PLL platform device or NULL
    :type dev: struct device \*

    :param name:
        the clock name
    :type name: const char \*

    :param parent_name:
        the parent clock name
    :type parent_name: const char \*

    :param reg:
        the \*DIV register
    :type reg: void __iomem \*

    :param fixed:
        if true, the divider is a fixed value
    :type fixed: bool

    :param flags:
        bitmap of CLK\_\* flags from clock-provider.h
    :type flags: u32

.. _`davinci_pll_clk_register`:

davinci_pll_clk_register
========================

.. c:function:: struct clk *davinci_pll_clk_register(struct device *dev, const struct davinci_pll_clk_info *info, const char *parent_name, void __iomem *base, struct regmap *cfgchip)

    Register a PLL clock

    :param dev:
        The PLL platform device or NULL
    :type dev: struct device \*

    :param info:
        The device-specific clock info
    :type info: const struct davinci_pll_clk_info \*

    :param parent_name:
        The parent clock name
    :type parent_name: const char \*

    :param base:
        The PLL's memory region
    :type base: void __iomem \*

    :param cfgchip:
        CFGCHIP syscon regmap for info->unlock_reg or NULL
    :type cfgchip: struct regmap \*

.. _`davinci_pll_clk_register.description`:

Description
-----------

This creates a series of clocks that represent the PLL.

OSCIN > [PREDIV >] PLL > [POSTDIV >] PLLEN

- OSCIN is the parent clock (on secondary PLL, may come from primary PLL)
- PREDIV and POSTDIV are optional (depends on the PLL controller)
- PLL is the PLL output (aka PLLOUT)
- PLLEN is the bypass multiplexer

.. _`davinci_pll_clk_register.return`:

Return
------

The PLLOUT clock or a negative error code.

.. _`davinci_pll_auxclk_register`:

davinci_pll_auxclk_register
===========================

.. c:function:: struct clk *davinci_pll_auxclk_register(struct device *dev, const char *name, void __iomem *base)

    Register bypass clock (AUXCLK)

    :param dev:
        The PLL platform device or NULL
    :type dev: struct device \*

    :param name:
        The clock name
    :type name: const char \*

    :param base:
        The PLL memory region
    :type base: void __iomem \*

.. _`davinci_pll_sysclkbp_clk_register`:

davinci_pll_sysclkbp_clk_register
=================================

.. c:function:: struct clk *davinci_pll_sysclkbp_clk_register(struct device *dev, const char *name, void __iomem *base)

    Register bypass divider clock (SYSCLKBP)

    :param dev:
        The PLL platform device or NULL
    :type dev: struct device \*

    :param name:
        The clock name
    :type name: const char \*

    :param base:
        The PLL memory region
    :type base: void __iomem \*

.. _`davinci_pll_obsclk_register`:

davinci_pll_obsclk_register
===========================

.. c:function:: struct clk *davinci_pll_obsclk_register(struct device *dev, const struct davinci_pll_obsclk_info *info, void __iomem *base)

    Register oscillator divider clock (OBSCLK)

    :param dev:
        The PLL platform device or NULL
    :type dev: struct device \*

    :param info:
        The clock info
    :type info: const struct davinci_pll_obsclk_info \*

    :param base:
        The PLL memory region
    :type base: void __iomem \*

.. _`davinci_pll_sysclk_register`:

davinci_pll_sysclk_register
===========================

.. c:function:: struct clk *davinci_pll_sysclk_register(struct device *dev, const struct davinci_pll_sysclk_info *info, void __iomem *base)

    Register divider clocks (SYSCLKn)

    :param dev:
        The PLL platform device or NULL
    :type dev: struct device \*

    :param info:
        The clock info
    :type info: const struct davinci_pll_sysclk_info \*

    :param base:
        The PLL memory region
    :type base: void __iomem \*

.. This file was automatic generated / don't edit.

