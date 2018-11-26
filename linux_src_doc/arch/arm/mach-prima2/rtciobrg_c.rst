.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-prima2/rtciobrg.c

.. _`devm_regmap_init_iobg`:

devm_regmap_init_iobg
=====================

.. c:function:: struct regmap *devm_regmap_init_iobg(struct device *dev, const struct regmap_config *config)

    Initialise managed register map

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param config:
        Configuration for register map
    :type config: const struct regmap_config \*

.. _`devm_regmap_init_iobg.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The regmap will be automatically freed by the
device management code.

.. This file was automatic generated / don't edit.

