
.. _API-usb-unanchor-urb:

================
usb_unanchor_urb
================

*man usb_unanchor_urb(9)*

*4.6.0-rc1*

unanchors an URB


Synopsis
========

.. c:function:: void usb_unanchor_urb( struct urb * urb )

Arguments
=========

``urb``
    pointer to the urb to anchor


Description
===========

Call this to stop the system keeping track of this URB
