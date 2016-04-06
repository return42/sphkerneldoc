
.. _API-usb-speed-string:

================
usb_speed_string
================

*man usb_speed_string(9)*

*4.6.0-rc1*

Returns human readable-name of the speed.


Synopsis
========

.. c:function:: const char ⋆ usb_speed_string( enum usb_device_speed speed )

Arguments
=========

``speed``
    The speed to return human-readable name for. If it's not any of the speeds defined in usb_device_speed enum, string for USB_SPEED_UNKNOWN will be returned.
