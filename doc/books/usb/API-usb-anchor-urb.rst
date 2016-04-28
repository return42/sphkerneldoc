.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-anchor-urb:

==============
usb_anchor_urb
==============

*man usb_anchor_urb(9)*

*4.6.0-rc5*

anchors an URB while it is processed


Synopsis
========

.. c:function:: void usb_anchor_urb( struct urb * urb, struct usb_anchor * anchor )

Arguments
=========

``urb``
    pointer to the urb to anchor

``anchor``
    pointer to the anchor


Description
===========

This can be called to have access to URBs which are to be executed
without bothering to track them


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
