
.. _API-usb-hc-died:

===========
usb_hc_died
===========

*man usb_hc_died(9)*

*4.6.0-rc1*

report abnormal shutdown of a host controller (bus glue)


Synopsis
========

.. c:function:: void usb_hc_died( struct usb_hcd * hcd )

Arguments
=========

``hcd``
    pointer to the HCD representing the controller


Description
===========

This is called by bus glue to report a USB host controller that died while operations may still have been pending. It's called automatically by the PCI glue, so only glue for
non-PCI busses should need to call it.

Only call this function with the primary HCD.
