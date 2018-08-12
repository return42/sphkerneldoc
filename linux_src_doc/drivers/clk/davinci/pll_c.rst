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

    :param struct device \*dev:
        The PLL platform device or NULL

    :param const char \*name:
        the clock name

    :param const char \*parent_name:
        the parent clock name

    :param void __iomem \*reg:
        the \*DIV register

    :param bool fixed:
        if true, the divider is a fixed value

    :param u32 flags:
        bitmap of CLK\_\* flags from clock-provider.h

.. _`davinci_pll_clk_register`:

davinci_pll_clk_register
========================

.. c:function:: struct clk *davinci_pll_clk_register(struct device *dev, const struct davinci_pll_clk_info *info, const char *parent_name, void __iomem *base, struct regmap *cfgchip)

    Register a PLL clock

    :param struct device \*dev:
        The PLL platform device or NULL

    :param const struct davinci_pll_clk_info \*info:
        The device-specific clock info

    :param const char \*parent_name:
        The parent clock name

    :param void __iomem \*base:
        The PLL's memory region

    :param struct regmap \*cfgchip:
        CFGCHIP syscon regmap for info->unlock_reg or NULL

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

    :param struct device \*dev:
        The PLL platform device or NULL

    :param const char \*name:
        The clock name

    :param void __iomem \*base:
        The PLL memory region

.. _`davinci_pll_sysclkbp_clk_register`:

davinci_pll_sysclkbp_clk_register
=================================

.. c:function:: struct clk *davinci_pll_sysclkbp_clk_register(struct device *dev, const char *name, void __iomem *base)

    Register bypass divider clock (SYSCLKBP)

    :param struct device \*dev:
        The PLL platform device or NULL

    :param const char \*name:
        The clock name

    :param void __iomem \*base:
        The PLL memory region

.. _`davinci_pll_obsclk_register`:

davinci_pll_obsclk_register
===========================

.. c:function:: struct clk *davinci_pll_obsclk_register(struct device *dev, const struct davinci_pll_obsclk_info *info, void __iomem *base)

    Register oscillator divider clock (OBSCLK)

    :param struct device \*dev:
        The PLL platform device or NULL

    :param const struct davinci_pll_obsclk_info \*info:
        The clock info

    :param void __iomem \*base:
        The PLL memory region

.. _`davinci_pll_sysclk_register`:

davinci_pll_sysclk_register
===========================

.. c:function:: struct clk *davinci_pll_sysclk_register(struct device *dev, const struct davinci_pll_sysclk_info *info, void __iomem *base)

    Register divider clocks (SYSCLKn)

    :param struct device \*dev:
        The PLL platform device or NULL

    :param const struct davinci_pll_sysclk_info \*info:
        The clock info

    :param void __iomem \*base:
        The PLL memory region

.. This file was automatic generated / don't edit.

