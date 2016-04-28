.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-unanchor-urb:

================
usb_unanchor_urb
================

*man usb_unanchor_urb(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
