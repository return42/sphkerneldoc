.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-common.h

.. _`v4l2_ctrl_query_fill`:

v4l2_ctrl_query_fill
====================

.. c:function:: int v4l2_ctrl_query_fill(struct v4l2_queryctrl *qctrl, s32 min, s32 max, s32 step, s32 def)

    Fill in a struct v4l2_queryctrl

    :param struct v4l2_queryctrl \*qctrl:
        pointer to the \ :c:type:`struct v4l2_queryctrl <v4l2_queryctrl>`\  to be filled

    :param s32 min:
        minimum value for the control

    :param s32 max:
        maximum value for the control

    :param s32 step:
        control step

    :param s32 def:
        default value for the control

.. _`v4l2_ctrl_query_fill.description`:

Description
-----------

Fills the \ :c:type:`struct v4l2_queryctrl <v4l2_queryctrl>`\  fields for the query control.

.. note::

   This function assumes that the \ ``qctrl``\ ->id field is filled.

Returns -EINVAL if the control is not known by the V4L2 core, 0 on success.

.. _`v4l2_i2c_new_subdev`:

v4l2_i2c_new_subdev
===================

.. c:function:: struct v4l2_subdev *v4l2_i2c_new_subdev(struct v4l2_device *v4l2_dev, struct i2c_adapter *adapter, const char *client_type, u8 addr, const unsigned short *probe_addrs)

    Load an i2c module and return an initialized \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ .

    :param struct v4l2_device \*v4l2_dev:
        pointer to \ :c:type:`struct v4l2_device <v4l2_device>`\ 

    :param struct i2c_adapter \*adapter:
        pointer to struct i2c_adapter

    :param const char \*client_type:
        name of the chip that's on the adapter.

    :param u8 addr:
        I2C address. If zero, it will use \ ``probe_addrs``\ 

    :param const unsigned short \*probe_addrs:
        array with a list of address. The last entry at such
        array should be \ ``I2C_CLIENT_END``\ .

.. _`v4l2_i2c_new_subdev.description`:

Description
-----------

returns a \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\  pointer.

.. _`v4l2_i2c_new_subdev_board`:

v4l2_i2c_new_subdev_board
=========================

.. c:function:: struct v4l2_subdev *v4l2_i2c_new_subdev_board(struct v4l2_device *v4l2_dev, struct i2c_adapter *adapter, struct i2c_board_info *info, const unsigned short *probe_addrs)

    Load an i2c module and return an initialized \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ .

    :param struct v4l2_device \*v4l2_dev:
        pointer to \ :c:type:`struct v4l2_device <v4l2_device>`\ 

    :param struct i2c_adapter \*adapter:
        pointer to struct i2c_adapter

    :param struct i2c_board_info \*info:
        pointer to struct i2c_board_info used to replace the irq,
        platform_data and addr arguments.

    :param const unsigned short \*probe_addrs:
        array with a list of address. The last entry at such
        array should be \ ``I2C_CLIENT_END``\ .

.. _`v4l2_i2c_new_subdev_board.description`:

Description
-----------

returns a \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\  pointer.

.. _`v4l2_i2c_subdev_init`:

v4l2_i2c_subdev_init
====================

.. c:function:: void v4l2_i2c_subdev_init(struct v4l2_subdev *sd, struct i2c_client *client, const struct v4l2_subdev_ops *ops)

    Initializes a \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\  with data from an i2c_client struct.

    :param struct v4l2_subdev \*sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 

    :param struct i2c_client \*client:
        pointer to struct i2c_client

    :param const struct v4l2_subdev_ops \*ops:
        pointer to \ :c:type:`struct v4l2_subdev_ops <v4l2_subdev_ops>`\ 

.. _`v4l2_i2c_subdev_addr`:

v4l2_i2c_subdev_addr
====================

.. c:function:: unsigned short v4l2_i2c_subdev_addr(struct v4l2_subdev *sd)

    returns i2c client address of \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ .

    :param struct v4l2_subdev \*sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 

.. _`v4l2_i2c_subdev_addr.description`:

Description
-----------

Returns the address of an I2C sub-device

.. _`v4l2_spi_new_subdev`:

v4l2_spi_new_subdev
===================

.. c:function:: struct v4l2_subdev *v4l2_spi_new_subdev(struct v4l2_device *v4l2_dev, struct spi_master *master, struct spi_board_info *info)

    Load an spi module and return an initialized \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ .

    :param struct v4l2_device \*v4l2_dev:
        pointer to \ :c:type:`struct v4l2_device <v4l2_device>`\ .

    :param struct spi_master \*master:
        pointer to struct spi_master.

    :param struct spi_board_info \*info:
        pointer to struct spi_board_info.

.. _`v4l2_spi_new_subdev.description`:

Description
-----------

returns a \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\  pointer.

.. _`v4l2_spi_subdev_init`:

v4l2_spi_subdev_init
====================

.. c:function:: void v4l2_spi_subdev_init(struct v4l2_subdev *sd, struct spi_device *spi, const struct v4l2_subdev_ops *ops)

    Initialize a v4l2_subdev with data from an spi_device struct.

    :param struct v4l2_subdev \*sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 

    :param struct spi_device \*spi:
        pointer to struct spi_device.

    :param const struct v4l2_subdev_ops \*ops:
        pointer to \ :c:type:`struct v4l2_subdev_ops <v4l2_subdev_ops>`\ 

.. This file was automatic generated / don't edit.

