.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-unpoison-anchored-urbs:

==========================
usb_unpoison_anchored_urbs
==========================

*man usb_unpoison_anchored_urbs(9)*

*4.6.0-rc5*

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

Reverses the effect of usb_poison_anchored_urbs the anchor can be
used normally after it returns


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
