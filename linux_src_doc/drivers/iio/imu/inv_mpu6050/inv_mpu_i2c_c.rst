.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/imu/inv_mpu6050/inv_mpu_i2c.c

.. _`inv_mpu_probe`:

inv_mpu_probe
=============

.. c:function:: int inv_mpu_probe(struct i2c_client *client, const struct i2c_device_id *id)

    probe function.

    :param client:
        i2c client.
    :type client: struct i2c_client \*

    :param id:
        i2c device id.
    :type id: const struct i2c_device_id \*

.. _`inv_mpu_probe.description`:

Description
-----------

Returns 0 on success, a negative error code otherwise.

.. This file was automatic generated / don't edit.

