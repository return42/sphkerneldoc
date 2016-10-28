.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/fixed.c

.. _`of_get_fixed_voltage_config`:

of_get_fixed_voltage_config
===========================

.. c:function:: struct fixed_voltage_config *of_get_fixed_voltage_config(struct device *dev, const struct regulator_desc *desc)

    extract fixed_voltage_config structure info

    :param struct device \*dev:
        device requesting for fixed_voltage_config

    :param const struct regulator_desc \*desc:
        regulator description

.. _`of_get_fixed_voltage_config.description`:

Description
-----------

Populates fixed_voltage_config structure by extracting data from device
tree node, returns a pointer to the populated structure of NULL if memory
alloc fails.

.. This file was automatic generated / don't edit.

