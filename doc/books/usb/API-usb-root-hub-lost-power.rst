
.. _API-usb-root-hub-lost-power:

=======================
usb_root_hub_lost_power
=======================

*man usb_root_hub_lost_power(9)*

*4.6.0-rc1*

called by HCD if the root hub lost Vbus power


Synopsis
========

.. c:function:: void usb_root_hub_lost_power( struct usb_device * rhdev )

Arguments
=========

``rhdev``
    struct usb_device for the root hub


Description
===========

The USB host controller driver calls this function when its root hub is resumed and Vbus power has been interrupted or the controller has been reset. The routine marks ``rhdev`` as
having lost power. When the hub driver is resumed it will take notice and carry out power-session recovery for all the “USB-PERSIST”-enabled child devices; the others will be
disconnected.
