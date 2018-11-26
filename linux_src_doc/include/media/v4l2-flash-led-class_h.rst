.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-flash-led-class.h

.. _`v4l2_flash_ctrl_data`:

struct v4l2_flash_ctrl_data
===========================

.. c:type:: struct v4l2_flash_ctrl_data

    flash control initialization data, filled basing on the features declared by the LED flash class driver in the v4l2_flash_config

.. _`v4l2_flash_ctrl_data.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_flash_ctrl_data {
        struct v4l2_ctrl_config config;
        u32 cid;
    }

.. _`v4l2_flash_ctrl_data.members`:

Members
-------

config
    initialization data for a control

cid
    contains v4l2 flash control id if the config
    field was initialized, 0 otherwise

.. _`v4l2_flash_ops`:

struct v4l2_flash_ops
=====================

.. c:type:: struct v4l2_flash_ops

    V4L2 flash operations

.. _`v4l2_flash_ops.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_flash_ops {
        int (*external_strobe_set)(struct v4l2_flash *v4l2_flash, bool enable);
        enum led_brightness (*intensity_to_led_brightness) (struct v4l2_flash *v4l2_flash, s32 intensity);
        s32 (*led_brightness_to_intensity) (struct v4l2_flash *v4l2_flash, enum led_brightness);
    }

.. _`v4l2_flash_ops.members`:

Members
-------

external_strobe_set
    Setup strobing the flash by hardware pin state
    assertion.

intensity_to_led_brightness
    Convert intensity to brightness in a device
    specific manner

led_brightness_to_intensity
    convert brightness to intensity in a device
    specific manner.

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
        struct led_flash_setting intensity;
        u32 flash_faults;
        unsigned int has_external_strobe:1;
    }

.. _`v4l2_flash_config.members`:

Members
-------

dev_name
    the name of the media entity,
    unique in the system

intensity
    non-flash strobe constraints for the LED

flash_faults
    bitmask of flash faults that the LED flash class
    device can report; corresponding LED_FAULT* bit
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
        struct led_classdev *iled_cdev;
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

.. _`v4l2_subdev_to_v4l2_flash`:

v4l2_subdev_to_v4l2_flash
=========================

.. c:function:: struct v4l2_flash *v4l2_subdev_to_v4l2_flash(struct v4l2_subdev *sd)

    Returns a \ :c:type:`struct v4l2_flash <v4l2_flash>`\  from the \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\  embedded on it.

    :param sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
    :type sd: struct v4l2_subdev \*

.. _`v4l2_ctrl_to_v4l2_flash`:

v4l2_ctrl_to_v4l2_flash
=======================

.. c:function:: struct v4l2_flash *v4l2_ctrl_to_v4l2_flash(struct v4l2_ctrl *c)

    Returns a \ :c:type:`struct v4l2_flash <v4l2_flash>`\  from the \ :c:type:`struct v4l2_ctrl <v4l2_ctrl>`\  embedded on it.

    :param c:
        pointer to \ :c:type:`struct v4l2_ctrl <v4l2_ctrl>`\ 
    :type c: struct v4l2_ctrl \*

.. _`v4l2_flash_init`:

v4l2_flash_init
===============

.. c:function:: struct v4l2_flash *v4l2_flash_init(struct device *dev, struct fwnode_handle *fwn, struct led_classdev_flash *fled_cdev, const struct v4l2_flash_ops *ops, struct v4l2_flash_config *config)

    initialize V4L2 flash led sub-device

    :param dev:
        flash device, e.g. an I2C device
    :type dev: struct device \*

    :param fwn:
        fwnode_handle of the LED, may be NULL if the same as device's
    :type fwn: struct fwnode_handle \*

    :param fled_cdev:
        LED flash class device to wrap
    :type fled_cdev: struct led_classdev_flash \*

    :param ops:
        V4L2 Flash device ops
    :type ops: const struct v4l2_flash_ops \*

    :param config:
        initialization data for V4L2 Flash sub-device
    :type config: struct v4l2_flash_config \*

.. _`v4l2_flash_init.description`:

Description
-----------

Create V4L2 Flash sub-device wrapping given LED subsystem device.
The ops pointer is stored by the V4L2 flash framework. No
references are held to config nor its contents once this function
has returned.

.. _`v4l2_flash_init.return`:

Return
------

A valid pointer, or, when an error occurs, the return
value is encoded using \ :c:func:`ERR_PTR`\ . Use \ :c:func:`IS_ERR`\  to check and
\ :c:func:`PTR_ERR`\  to obtain the numeric return value.

.. _`v4l2_flash_indicator_init`:

v4l2_flash_indicator_init
=========================

.. c:function:: struct v4l2_flash *v4l2_flash_indicator_init(struct device *dev, struct fwnode_handle *fwn, struct led_classdev *iled_cdev, struct v4l2_flash_config *config)

    initialize V4L2 indicator sub-device

    :param dev:
        flash device, e.g. an I2C device
    :type dev: struct device \*

    :param fwn:
        fwnode_handle of the LED, may be NULL if the same as device's
    :type fwn: struct fwnode_handle \*

    :param iled_cdev:
        LED flash class device representing the indicator LED
    :type iled_cdev: struct led_classdev \*

    :param config:
        initialization data for V4L2 Flash sub-device
    :type config: struct v4l2_flash_config \*

.. _`v4l2_flash_indicator_init.description`:

Description
-----------

Create V4L2 Flash sub-device wrapping given LED subsystem device.
The ops pointer is stored by the V4L2 flash framework. No
references are held to config nor its contents once this function
has returned.

.. _`v4l2_flash_indicator_init.return`:

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

    :param v4l2_flash:
        the V4L2 Flash sub-device to release
    :type v4l2_flash: struct v4l2_flash \*

.. _`v4l2_flash_release.description`:

Description
-----------

Release V4L2 Flash sub-device.

.. This file was automatic generated / don't edit.

