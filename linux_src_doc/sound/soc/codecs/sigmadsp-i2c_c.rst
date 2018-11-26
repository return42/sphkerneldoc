.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/codecs/sigmadsp-i2c.c

.. _`devm_sigmadsp_init_i2c`:

devm_sigmadsp_init_i2c
======================

.. c:function:: struct sigmadsp *devm_sigmadsp_init_i2c(struct i2c_client *client, const struct sigmadsp_ops *ops, const char *firmware_name)

    Initialize SigmaDSP instance

    :param client:
        The parent I2C device
    :type client: struct i2c_client \*

    :param ops:
        The sigmadsp_ops to use for this instance
    :type ops: const struct sigmadsp_ops \*

    :param firmware_name:
        Name of the firmware file to load
    :type firmware_name: const char \*

.. _`devm_sigmadsp_init_i2c.description`:

Description
-----------

Allocates a SigmaDSP instance and loads the specified firmware file.

Returns a pointer to a struct sigmadsp on success, or a \ :c:func:`PTR_ERR`\  on error.

.. This file was automatic generated / don't edit.

