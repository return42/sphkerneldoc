.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-state-string:

================
usb_state_string
================

*man usb_state_string(9)*

*4.6.0-rc5*

Returns human readable name for the state.


Synopsis
========

.. c:function:: const char * usb_state_string( enum usb_device_state state )

Arguments
=========

``state``
    The state to return a human-readable name for. If it's not any of
    the states devices in usb_device_state_string enum, the string
    UNKNOWN will be returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
