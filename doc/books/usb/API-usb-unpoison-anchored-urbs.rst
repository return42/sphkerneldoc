
.. _API-usb-unpoison-anchored-urbs:

==========================
usb_unpoison_anchored_urbs
==========================

*man usb_unpoison_anchored_urbs(9)*

*4.6.0-rc1*

let an anchor be used successfully again


Synopsis
========

.. c:function:: void usb_unpoison_anchored_urbs( struct usb_anchor * anchor )

Arguments
=========

``anchor``
    anchor the requests are bound to


Description
===========

Reverses the effect of usb_poison_anchored_urbs the anchor can be used normally after it returns
