.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/tc35876x-dsi-lvds.c

.. _`tc35876x_regw`:

tc35876x_regw
=============

.. c:function:: int tc35876x_regw(struct i2c_client *client, u16 reg, u32 value)

    Write DSI-LVDS bridge register using I2C

    :param struct i2c_client \*client:
        struct i2c_client to use

    :param u16 reg:
        register address

    :param u32 value:
        value to write

.. _`tc35876x_regw.description`:

Description
-----------

Returns 0 on success, or a negative error value.

.. _`tc35876x_regr`:

tc35876x_regr
=============

.. c:function:: int tc35876x_regr(struct i2c_client *client, u16 reg, u32 *value)

    Read DSI-LVDS bridge register using I2C

    :param struct i2c_client \*client:
        struct i2c_client to use

    :param u16 reg:
        register address

    :param u32 \*value:
        pointer for storing the value

.. _`tc35876x_regr.description`:

Description
-----------

Returns 0 on success, or a negative error value.

.. This file was automatic generated / don't edit.

