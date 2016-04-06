
.. _API-usb-urb-dir-in:

==============
usb_urb_dir_in
==============

*man usb_urb_dir_in(9)*

*4.6.0-rc1*

check if an URB describes an IN transfer


Synopsis
========

.. c:function:: int usb_urb_dir_in( struct urb * urb )

Arguments
=========

``urb``
    URB to be checked


Return
======

1 if ``urb`` describes an IN transfer (device-to-host), otherwise 0.
