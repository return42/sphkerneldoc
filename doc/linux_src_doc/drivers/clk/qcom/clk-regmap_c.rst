.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/qcom/clk-regmap.c

.. _`clk_is_enabled_regmap`:

clk_is_enabled_regmap
=====================

.. c:function:: int clk_is_enabled_regmap(struct clk_hw *hw)

    standard \ :c:func:`is_enabled`\  for regmap users

    :param struct clk_hw \*hw:
        clk to operate on

.. _`clk_is_enabled_regmap.description`:

Description
-----------

Clocks that use regmap for their register I/O can set the
enable_reg and enable_mask fields in their struct clk_regmap and then use
this as their is_enabled operation, saving some code.

.. _`clk_enable_regmap`:

clk_enable_regmap
=================

.. c:function:: int clk_enable_regmap(struct clk_hw *hw)

    standard \ :c:func:`enable`\  for regmap users

    :param struct clk_hw \*hw:
        clk to operate on

.. _`clk_enable_regmap.description`:

Description
-----------

Clocks that use regmap for their register I/O can set the
enable_reg and enable_mask fields in their struct clk_regmap and then use
this as their \ :c:func:`enable`\  operation, saving some code.

.. _`clk_disable_regmap`:

clk_disable_regmap
==================

.. c:function:: void clk_disable_regmap(struct clk_hw *hw)

    standard \ :c:func:`disable`\  for regmap users

    :param struct clk_hw \*hw:
        clk to operate on

.. _`clk_disable_regmap.description`:

Description
-----------

Clocks that use regmap for their register I/O can set the
enable_reg and enable_mask fields in their struct clk_regmap and then use
this as their \ :c:func:`disable`\  operation, saving some code.

.. _`devm_clk_register_regmap`:

devm_clk_register_regmap
========================

.. c:function:: struct clk *devm_clk_register_regmap(struct device *dev, struct clk_regmap *rclk)

    register a clk_regmap clock

    :param struct device \*dev:
        *undescribed*

    :param struct clk_regmap \*rclk:
        clk to operate on

.. _`devm_clk_register_regmap.description`:

Description
-----------

Clocks that use regmap for their register I/O should register their
clk_regmap struct via this function so that the regmap is initialized
and so that the clock is registered with the common clock framework.

.. This file was automatic generated / don't edit.

