.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/sunxi/clk-sun6i-ar100.c

.. _`sun6i_get_ar100_factors`:

sun6i_get_ar100_factors
=======================

.. c:function:: void sun6i_get_ar100_factors(struct factors_request *req)

    Calculates factors p, m for AR100

    :param struct factors_request \*req:
        *undescribed*

.. _`sun6i_get_ar100_factors.description`:

Description
-----------

AR100 rate is calculated as follows
rate = (parent_rate >> p) / (m + 1);

.. This file was automatic generated / don't edit.

