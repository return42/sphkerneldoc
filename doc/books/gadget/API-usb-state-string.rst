
.. _API-usb-state-string:

================
usb_state_string
================

*man usb_state_string(9)*

*4.6.0-rc1*

Returns human readable name for the state.


Synopsis
========

.. c:function:: const char ⋆ usb_state_string( enum usb_device_state state )

Arguments
=========

``state``
    The state to return a human-readable name for. If it's not any of the states devices in usb_device_state_string enum, the string UNKNOWN will be returned.
