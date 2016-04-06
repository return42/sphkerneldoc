
.. _API-gadget-is-stall-supported:

=========================
gadget_is_stall_supported
=========================

*man gadget_is_stall_supported(9)*

*4.6.0-rc1*

return true iff the hardware supports stalling


Synopsis
========

.. c:function:: int gadget_is_stall_supported( struct usb_gadget * g )

Arguments
=========

``g``
    controller to check for quirk
