.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-scuttle-anchored-urbs:

=========================
usb_scuttle_anchored_urbs
=========================

*man usb_scuttle_anchored_urbs(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
