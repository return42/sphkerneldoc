
.. _API-usb-function-activate:

=====================
usb_function_activate
=====================

*man usb_function_activate(9)*

*4.6.0-rc1*

allow function and gadget enumeration


Synopsis
========

.. c:function:: int usb_function_activate( struct usb_function * function )

Arguments
=========

``function``
    function on which ``usb_function_activate`` was called


Description
===========

Reverses effect of ``usb_function_deactivate``. If no more functions are delaying their activation, the gadget driver will respond to host enumeration procedures.

Returns zero on success, else negative errno.
