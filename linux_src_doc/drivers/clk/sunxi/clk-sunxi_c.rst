.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/sunxi/clk-sunxi.c

.. _`sun4i_get_pll1_factors`:

sun4i_get_pll1_factors
======================

.. c:function:: void sun4i_get_pll1_factors(struct factors_request *req)

    calculates n, k, m, p factors for PLL1 PLL1 rate is calculated as follows rate = (parent_rate \* n \* (k + 1) >> p) / (m + 1); parent_rate is always 24Mhz

    :param req:
        *undescribed*
    :type req: struct factors_request \*

.. _`sun6i_a31_get_pll1_factors`:

sun6i_a31_get_pll1_factors
==========================

.. c:function:: void sun6i_a31_get_pll1_factors(struct factors_request *req)

    calculates n, k and m factors for PLL1 PLL1 rate is calculated as follows rate = parent_rate \* (n + 1) \* (k + 1) / (m + 1); parent_rate should always be 24MHz

    :param req:
        *undescribed*
    :type req: struct factors_request \*

.. _`sun8i_a23_get_pll1_factors`:

sun8i_a23_get_pll1_factors
==========================

.. c:function:: void sun8i_a23_get_pll1_factors(struct factors_request *req)

    calculates n, k, m, p factors for PLL1 PLL1 rate is calculated as follows rate = (parent_rate \* (n + 1) \* (k + 1) >> p) / (m + 1); parent_rate is always 24Mhz

    :param req:
        *undescribed*
    :type req: struct factors_request \*

.. _`sun4i_get_pll5_factors`:

sun4i_get_pll5_factors
======================

.. c:function:: void sun4i_get_pll5_factors(struct factors_request *req)

    calculates n, k factors for PLL5 PLL5 rate is calculated as follows rate = parent_rate \* n \* (k + 1) parent_rate is always 24Mhz

    :param req:
        *undescribed*
    :type req: struct factors_request \*

.. _`sun6i_a31_get_pll6_factors`:

sun6i_a31_get_pll6_factors
==========================

.. c:function:: void sun6i_a31_get_pll6_factors(struct factors_request *req)

    calculates n, k factors for A31 PLL6x2 PLL6x2 rate is calculated as follows rate = parent_rate \* (n + 1) \* (k + 1) parent_rate is always 24Mhz

    :param req:
        *undescribed*
    :type req: struct factors_request \*

.. _`sun5i_a13_get_ahb_factors`:

sun5i_a13_get_ahb_factors
=========================

.. c:function:: void sun5i_a13_get_ahb_factors(struct factors_request *req)

    calculates m, p factors for AHB AHB rate is calculated as follows rate = parent_rate >> p

    :param req:
        *undescribed*
    :type req: struct factors_request \*

.. _`sun6i_get_ahb1_factors`:

sun6i_get_ahb1_factors
======================

.. c:function:: void sun6i_get_ahb1_factors(struct factors_request *req)

    calculates m, p factors for AHB AHB rate is calculated as follows rate = parent_rate >> p

    :param req:
        *undescribed*
    :type req: struct factors_request \*

.. _`sun6i_get_ahb1_factors.description`:

Description
-----------

if parent is pll6, then
parent_rate = pll6 rate / (m + 1)

.. _`sun6i_ahb1_recalc`:

sun6i_ahb1_recalc
=================

.. c:function:: void sun6i_ahb1_recalc(struct factors_request *req)

    calculates AHB clock rate from m, p factors and parent index

    :param req:
        *undescribed*
    :type req: struct factors_request \*

.. _`sun4i_get_apb1_factors`:

sun4i_get_apb1_factors
======================

.. c:function:: void sun4i_get_apb1_factors(struct factors_request *req)

    calculates m, p factors for APB1 APB1 rate is calculated as follows rate = (parent_rate >> p) / (m + 1);

    :param req:
        *undescribed*
    :type req: struct factors_request \*

.. _`sun7i_a20_get_out_factors`:

sun7i_a20_get_out_factors
=========================

.. c:function:: void sun7i_a20_get_out_factors(struct factors_request *req)

    calculates m, p factors for CLK_OUT_A/B CLK_OUT rate is calculated as follows rate = (parent_rate >> p) / (m + 1);

    :param req:
        *undescribed*
    :type req: struct factors_request \*

.. _`sunxi_mux_gate_width`:

SUNXI_MUX_GATE_WIDTH
====================

.. c:function::  SUNXI_MUX_GATE_WIDTH()

    Setup function for muxes

.. _`sunxi_gates_max_size`:

SUNXI_GATES_MAX_SIZE
====================

.. c:function::  SUNXI_GATES_MAX_SIZE()

    Setup function for leaf gates on clocks

.. _`sunxi_divs_max_qty`:

SUNXI_DIVS_MAX_QTY
==================

.. c:function::  SUNXI_DIVS_MAX_QTY()

.. _`sunxi_divs_clk_setup`:

sunxi_divs_clk_setup
====================

.. c:function:: struct clk **sunxi_divs_clk_setup(struct device_node *node, const struct divs_data *data)

    Setup function for leaf divisors on clocks

    :param node:
        *undescribed*
    :type node: struct device_node \*

    :param data:
        *undescribed*
    :type data: const struct divs_data \*

.. _`sunxi_divs_clk_setup.description`:

Description
-----------

These clocks look something like this
\________________________
\|         \___divisor 1---\|----> to consumer
parent >--\|  pll___/___divisor 2---\|----> to consumer
\|        \_______________\|____> to consumer
\|________________________\|

.. This file was automatic generated / don't edit.

