.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/ch9.h

.. _`usb_speed_string`:

usb_speed_string
================

.. c:function:: const char *usb_speed_string(enum usb_device_speed speed)

    Returns human readable-name of the speed.

    :param speed:
        The speed to return human-readable name for.  If it's not
        any of the speeds defined in usb_device_speed enum, string for
        USB_SPEED_UNKNOWN will be returned.
    :type speed: enum usb_device_speed

.. _`usb_get_maximum_speed`:

usb_get_maximum_speed
=====================

.. c:function:: enum usb_device_speed usb_get_maximum_speed(struct device *dev)

    Get maximum requested speed for a given USB controller.

    :param dev:
        Pointer to the given USB controller device
    :type dev: struct device \*

.. _`usb_get_maximum_speed.description`:

Description
-----------

The function gets the maximum speed string from property "maximum-speed",
and returns the corresponding enum usb_device_speed.

.. _`usb_state_string`:

usb_state_string
================

.. c:function:: const char *usb_state_string(enum usb_device_state state)

    Returns human readable name for the state.

    :param state:
        The state to return a human-readable name for. If it's not
        any of the states devices in usb_device_state_string enum,
        the string UNKNOWN will be returned.
    :type state: enum usb_device_state

.. This file was automatic generated / don't edit.

