.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/qcom/clk-regmap.h

.. _`clk_regmap`:

struct clk_regmap
=================

.. c:type:: struct clk_regmap

    regmap supporting clock

.. _`clk_regmap.definition`:

Definition
----------

.. code-block:: c

    struct clk_regmap {
        struct clk_hw hw;
        struct regmap *regmap;
        unsigned int enable_reg;
        unsigned int enable_mask;
        bool enable_is_inverted;
    }

.. _`clk_regmap.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

regmap
    regmap to use for regmap helpers and/or by providers

enable_reg
    register when using regmap enable/disable ops

enable_mask
    mask when using regmap enable/disable ops

enable_is_inverted
    flag to indicate set enable_mask bits to disable
    when using clock_enable_regmap and friends APIs.

.. This file was automatic generated / don't edit.

