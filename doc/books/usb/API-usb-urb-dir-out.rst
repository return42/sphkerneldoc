
.. _API-usb-urb-dir-out:

===============
usb_urb_dir_out
===============

*man usb_urb_dir_out(9)*

*4.6.0-rc1*

check if an URB describes an OUT transfer


Synopsis
========

.. c:function:: int usb_urb_dir_out( struct urb * urb )

Arguments
=========

``urb``
    URB to be checked


Return
======

1 if ``urb`` describes an OUT transfer (host-to-device), otherwise 0.
