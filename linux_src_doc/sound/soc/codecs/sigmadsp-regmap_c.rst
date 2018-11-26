.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/codecs/sigmadsp-regmap.c

.. _`devm_sigmadsp_init_regmap`:

devm_sigmadsp_init_regmap
=========================

.. c:function:: struct sigmadsp *devm_sigmadsp_init_regmap(struct device *dev, struct regmap *regmap, const struct sigmadsp_ops *ops, const char *firmware_name)

    Initialize SigmaDSP instance

    :param dev:
        The parent device
    :type dev: struct device \*

    :param regmap:
        Regmap instance to use
    :type regmap: struct regmap \*

    :param ops:
        The sigmadsp_ops to use for this instance
    :type ops: const struct sigmadsp_ops \*

    :param firmware_name:
        Name of the firmware file to load
    :type firmware_name: const char \*

.. _`devm_sigmadsp_init_regmap.description`:

Description
-----------

Allocates a SigmaDSP instance and loads the specified firmware file.

Returns a pointer to a struct sigmadsp on success, or a \ :c:func:`PTR_ERR`\  on error.

.. This file was automatic generated / don't edit.

