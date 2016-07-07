.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/codecs/sigmadsp-regmap.c

.. _`devm_sigmadsp_init_regmap`:

devm_sigmadsp_init_regmap
=========================

.. c:function:: struct sigmadsp *devm_sigmadsp_init_regmap(struct device *dev, struct regmap *regmap, const struct sigmadsp_ops *ops, const char *firmware_name)

    Initialize SigmaDSP instance

    :param struct device \*dev:
        The parent device

    :param struct regmap \*regmap:
        Regmap instance to use

    :param const struct sigmadsp_ops \*ops:
        The sigmadsp_ops to use for this instance

    :param const char \*firmware_name:
        Name of the firmware file to load

.. _`devm_sigmadsp_init_regmap.description`:

Description
-----------

Allocates a SigmaDSP instance and loads the specified firmware file.

Returns a pointer to a struct sigmadsp on success, or a \ :c:func:`PTR_ERR`\  on error.

.. This file was automatic generated / don't edit.

