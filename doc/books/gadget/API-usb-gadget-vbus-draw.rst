
.. _API-usb-gadget-vbus-draw:

====================
usb_gadget_vbus_draw
====================

*man usb_gadget_vbus_draw(9)*

*4.6.0-rc1*

constrain controller's VBUS power usage


Synopsis
========

.. c:function:: int usb_gadget_vbus_draw( struct usb_gadget * gadget, unsigned mA )

Arguments
=========

``gadget``
    The device whose VBUS usage is being described

``mA``
    How much current to draw, in milliAmperes. This should be twice the value listed in the configuration descriptor bMaxPower field.


Description
===========

This call is used by gadget drivers during SET_CONFIGURATION calls, reporting how much power the device may consume. For example, this could affect how quickly batteries are
recharged.

Returns zero on success, else negative errno.
