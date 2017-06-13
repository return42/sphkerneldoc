.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-tegra-bpmp.c

.. _`tegra_bpmp_serialize_i2c_msg`:

tegra_bpmp_serialize_i2c_msg
============================

.. c:function:: int tegra_bpmp_serialize_i2c_msg(struct tegra_bpmp_i2c *i2c, struct mrq_i2c_request *request, struct i2c_msg *msgs, unsigned int num)

    [addr little-endian][flags little-endian][len little-endian][data if write] [addr little-endian][flags little-endian][len little-endian][data if write] ...

    :param struct tegra_bpmp_i2c \*i2c:
        *undescribed*

    :param struct mrq_i2c_request \*request:
        *undescribed*

    :param struct i2c_msg \*msgs:
        *undescribed*

    :param unsigned int num:
        *undescribed*

.. _`tegra_bpmp_serialize_i2c_msg.description`:

Description
-----------

The flags are translated from Linux kernel representation to seriali2c
representation. Any undefined flag being set causes an error.

The data is there only for writes. Reads have the data transferred in the
other direction, and thus data is not present.

See deserialize_i2c documentation for the data format in the other direction.

.. _`tegra_bpmp_i2c_deserialize`:

tegra_bpmp_i2c_deserialize
==========================

.. c:function:: int tegra_bpmp_i2c_deserialize(struct tegra_bpmp_i2c *i2c, struct mrq_i2c_response *response, struct i2c_msg *msgs, unsigned int num)

    > CPU direction is composed of sequential blocks for those messages that have I2C_M_RD. So, for example, if you have:

    :param struct tegra_bpmp_i2c \*i2c:
        *undescribed*

    :param struct mrq_i2c_response \*response:
        *undescribed*

    :param struct i2c_msg \*msgs:
        *undescribed*

    :param unsigned int num:
        *undescribed*

.. _`tegra_bpmp_i2c_deserialize.description`:

Description
-----------

- !I2C_M_RD, len == 5, data == a0 01 02 03 04
- !I2C_M_RD, len == 1, data == a0
- I2C_M_RD, len == 2, data == [uninitialized buffer 1]
- !I2C_M_RD, len == 1, data == a2
- I2C_M_RD, len == 2, data == [uninitialized buffer 2]

...then the data in the BPMP -> CPU direction would be 4 bytes total, and
would contain 2 bytes that will go to uninitialized buffer 1, and 2 bytes
that will go to uninitialized buffer 2.

.. This file was automatic generated / don't edit.

