
.. _API-usb-composite-setup-continue:

============================
usb_composite_setup_continue
============================

*man usb_composite_setup_continue(9)*

*4.6.0-rc1*

Continue with the control transfer


Synopsis
========

.. c:function:: void usb_composite_setup_continue( struct usb_composite_dev * cdev )

Arguments
=========

``cdev``
    the composite device who's control transfer was kept waiting


Description
===========

This function must be called by the USB function driver to continue with the control transfer's data/status stage in case it had requested to delay the data/status stages. A USB
function's setup handler (e.g. ``set_alt``) can request the composite framework to delay the setup request's data/status stages by returning USB_GADGET_DELAYED_STATUS.
