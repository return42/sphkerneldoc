
.. _API-gadget-is-dualspeed:

===================
gadget_is_dualspeed
===================

*man gadget_is_dualspeed(9)*

*4.6.0-rc1*

return true iff the hardware handles high speed


Synopsis
========

.. c:function:: int gadget_is_dualspeed( struct usb_gadget * g )

Arguments
=========

``g``
    controller that might support both high and full speeds
