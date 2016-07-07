.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-flash-led-class.h

.. _`v4l2_flash_config`:

struct v4l2_flash_config
========================

.. c:type:: struct v4l2_flash_config

    V4L2 Flash sub-device initialization data

.. _`v4l2_flash_config.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_flash_config {
        char dev_name[32];
        struct led_flash_setting torch_intensity;
        struct led_flash_setting indicator_intensity;
        u32 flash_faults;
        unsigned int has_external_strobe:1;
    }

.. _`v4l2_flash_config.members`:

Members
-------

dev_name
    the name of the media entity,
    unique in the system

torch_intensity
    constraints for the LED in torch mode

indicator_intensity
    constraints for the indicator LED

flash_faults
    bitmask of flash faults that the LED flash class
    device can report; corresponding LED_FAULT\* bit
    definitions are available in the header file
    <linux/led-class-flash.h>

has_external_strobe
    external strobe capability

.. _`v4l2_flash`:

struct v4l2_flash
=================

.. c:type:: struct v4l2_flash

    Flash sub-device context

.. _`v4l2_flash.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_flash {
        struct led_classdev_flash *fled_cdev;
        struct led_classdev_flash *iled_cdev;
        const struct v4l2_flash_ops *ops;
        struct v4l2_subdev sd;
        struct v4l2_ctrl_handler hdl;
        struct v4l2_ctrl **ctrls;
    }

.. _`v4l2_flash.members`:

Members
-------

fled_cdev
    LED flash class device controlled by this sub-device

iled_cdev
    LED class device representing indicator LED associated
    with the LED flash class device

ops
    V4L2 specific flash ops

sd
    V4L2 sub-device

hdl
    flash controls handler

ctrls
    array of pointers to controls, whose values define
    the sub-device state

.. _`v4l2_flash_init`:

v4l2_flash_init
===============

.. c:function:: struct v4l2_flash *v4l2_flash_init(struct device *dev, struct device_node *of_node, struct led_classdev_flash *fled_cdev, struct led_classdev_flash *iled_cdev, const struct v4l2_flash_ops *ops, struct v4l2_flash_config *config)

    initialize V4L2 flash led sub-device

    :param struct device \*dev:
        flash device, e.g. an I2C device

    :param struct device_node \*of_node:
        of_node of the LED, may be NULL if the same as device's

    :param struct led_classdev_flash \*fled_cdev:
        LED flash class device to wrap

    :param struct led_classdev_flash \*iled_cdev:
        LED flash class device representing indicator LED associated
        with fled_cdev, may be NULL

    :param const struct v4l2_flash_ops \*ops:
        V4L2 Flash device ops

    :param struct v4l2_flash_config \*config:
        initialization data for V4L2 Flash sub-device

.. _`v4l2_flash_init.description`:

Description
-----------

Create V4L2 Flash sub-device wrapping given LED subsystem device.

.. _`v4l2_flash_init.return`:

Return
------

A valid pointer, or, when an error occurs, the return
value is encoded using \ :c:func:`ERR_PTR`\ . Use \ :c:func:`IS_ERR`\  to check and
\ :c:func:`PTR_ERR`\  to obtain the numeric return value.

.. _`v4l2_flash_release`:

v4l2_flash_release
==================

.. c:function:: void v4l2_flash_release(struct v4l2_flash *v4l2_flash)

    release V4L2 Flash sub-device

    :param struct v4l2_flash \*v4l2_flash:
        the V4L2 Flash sub-device to release

.. _`v4l2_flash_release.description`:

Description
-----------

Release V4L2 Flash sub-device.

.. This file was automatic generated / don't edit.

