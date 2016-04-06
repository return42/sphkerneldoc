
.. _API-gadget-is-zlp-supported:

=======================
gadget_is_zlp_supported
=======================

*man gadget_is_zlp_supported(9)*

*4.6.0-rc1*

return true iff the hardware supports zlp


Synopsis
========

.. c:function:: int gadget_is_zlp_supported( struct usb_gadget * g )

Arguments
=========

``g``
    controller to check for quirk
