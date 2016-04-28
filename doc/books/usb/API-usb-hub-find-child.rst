.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-hub-find-child:

==================
usb_hub_find_child
==================

*man usb_hub_find_child(9)*

*4.6.0-rc5*

Get the pointer of child device attached to the port which is specified
by ``port1``.


Synopsis
========

.. c:function:: struct usb_device * usb_hub_find_child( struct usb_device * hdev, int port1 )

Arguments
=========

``hdev``
    USB device belonging to the usb hub

``port1``
    port num to indicate which port the child device is attached to.


Description
===========

USB drivers call this function to get hub's child device pointer.


Return
======

``NULL`` if input param is invalid and child's usb_device pointer if
non-NULL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
