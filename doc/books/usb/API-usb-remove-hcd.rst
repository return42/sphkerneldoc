.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-remove-hcd:

==============
usb_remove_hcd
==============

*man usb_remove_hcd(9)*

*4.6.0-rc5*

shutdown processing for generic HCDs


Synopsis
========

.. c:function:: void usb_remove_hcd( struct usb_hcd * hcd )

Arguments
=========

``hcd``
    the usb_hcd structure to remove


Context
=======

!\ ``in_interrupt``


Description
===========

Disconnects the root hub, then reverses the effects of ``usb_add_hcd``,
invoking the HCD's ``stop`` method.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
