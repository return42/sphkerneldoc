.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/sunxi/clk-sun9i-core.c

.. _`sun9i_a80_get_pll4_factors`:

sun9i_a80_get_pll4_factors
==========================

.. c:function:: void sun9i_a80_get_pll4_factors(struct factors_request *req)

    calculates n, p, m factors for PLL4 PLL4 rate is calculated as follows rate = (parent_rate \* n >> p) / (m + 1); parent_rate is always 24MHz

    :param struct factors_request \*req:
        *undescribed*

.. _`sun9i_a80_get_pll4_factors.description`:

Description
-----------

p and m are named div1 and div2 in Allwinner's SDK

.. _`sun9i_a80_get_gt_factors`:

sun9i_a80_get_gt_factors
========================

.. c:function:: void sun9i_a80_get_gt_factors(struct factors_request *req)

    calculates m factor for GT GT rate is calculated as follows rate = parent_rate / (m + 1);

    :param struct factors_request \*req:
        *undescribed*

.. _`sun9i_a80_get_ahb_factors`:

sun9i_a80_get_ahb_factors
=========================

.. c:function:: void sun9i_a80_get_ahb_factors(struct factors_request *req)

    calculates p factor for AHB0/1/2 AHB rate is calculated as follows rate = parent_rate >> p;

    :param struct factors_request \*req:
        *undescribed*

.. _`sun9i_a80_get_apb1_factors`:

sun9i_a80_get_apb1_factors
==========================

.. c:function:: void sun9i_a80_get_apb1_factors(struct factors_request *req)

    calculates m, p factors for APB1 APB1 rate is calculated as follows rate = (parent_rate >> p) / (m + 1);

    :param struct factors_request \*req:
        *undescribed*

.. This file was automatic generated / don't edit.

