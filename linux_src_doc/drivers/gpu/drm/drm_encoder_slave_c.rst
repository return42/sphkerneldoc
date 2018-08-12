.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_encoder_slave.c

.. _`drm_i2c_encoder_init`:

drm_i2c_encoder_init
====================

.. c:function:: int drm_i2c_encoder_init(struct drm_device *dev, struct drm_encoder_slave *encoder, struct i2c_adapter *adap, const struct i2c_board_info *info)

    Initialize an I2C slave encoder

    :param struct drm_device \*dev:
        DRM device.

    :param struct drm_encoder_slave \*encoder:
        Encoder to be attached to the I2C device. You aren't
        required to have called \ :c:func:`drm_encoder_init`\  before.

    :param struct i2c_adapter \*adap:
        I2C adapter that will be used to communicate with
        the device.

    :param const struct i2c_board_info \*info:
        Information that will be used to create the I2C device.
        Required fields are \ ``addr``\  and \ ``type``\ .

.. _`drm_i2c_encoder_init.description`:

Description
-----------

Create an I2C device on the specified bus (the module containing its
driver is transparently loaded) and attach it to the specified
\ :c:type:`struct drm_encoder_slave <drm_encoder_slave>`\ . The \ ``slave_funcs``\  field will be initialized with
the hooks provided by the slave driver.

If \ ``info.platform_data``\  is non-NULL it will be used as the initial
slave config.

Returns 0 on success or a negative errno on failure, in particular,
-ENODEV is returned when no matching driver is found.

.. _`drm_i2c_encoder_destroy`:

drm_i2c_encoder_destroy
=======================

.. c:function:: void drm_i2c_encoder_destroy(struct drm_encoder *drm_encoder)

    Unregister the I2C device backing an encoder

    :param struct drm_encoder \*drm_encoder:
        Encoder to be unregistered.

.. _`drm_i2c_encoder_destroy.description`:

Description
-----------

This should be called from the \ ``destroy``\  method of an I2C slave
encoder driver once I2C access is no longer needed.

.. This file was automatic generated / don't edit.

