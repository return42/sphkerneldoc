
.. _API-usb-scuttle-anchored-urbs:

=========================
usb_scuttle_anchored_urbs
=========================

*man usb_scuttle_anchored_urbs(9)*

*4.6.0-rc1*

unanchor all an anchor's urbs


Synopsis
========

.. c:function:: void usb_scuttle_anchored_urbs( struct usb_anchor * anchor )

Arguments
=========

``anchor``
    the anchor whose urbs you want to unanchor


Description
===========

use this to get rid of all an anchor's urbs
