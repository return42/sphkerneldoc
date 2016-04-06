
.. _API-v4l2-flash-init:

===============
v4l2_flash_init
===============

*man v4l2_flash_init(9)*

*4.6.0-rc1*

initialize V4L2 flash led sub-device


Synopsis
========

.. c:function:: struct v4l2_flash ⋆ v4l2_flash_init( struct device * dev, struct device_node * of_node, struct led_classdev_flash * fled_cdev, struct led_classdev_flash * iled_cdev, const struct v4l2_flash_ops * ops, struct v4l2_flash_config * config )

Arguments
=========

``dev``
    flash device, e.g. an I2C device

``of_node``
    of_node of the LED, may be NULL if the same as device's

``fled_cdev``
    LED flash class device to wrap

``iled_cdev``
    LED flash class device representing indicator LED associated with fled_cdev, may be NULL

``ops``
    V4L2 Flash device ops

``config``
    initialization data for V4L2 Flash sub-device


Description
===========

Create V4L2 Flash sub-device wrapping given LED subsystem device.


Returns
=======

A valid pointer, or, when an error occurs, the return value is encoded using ``ERR_PTR``. Use ``IS_ERR`` to check and ``PTR_ERR`` to obtain the numeric return value.
