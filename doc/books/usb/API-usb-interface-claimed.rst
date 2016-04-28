.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-interface-claimed:

=====================
usb_interface_claimed
=====================

*man usb_interface_claimed(9)*

*4.6.0-rc5*

returns true iff an interface is claimed


Synopsis
========

.. c:function:: int usb_interface_claimed( struct usb_interface * iface )

Arguments
=========

``iface``
    the interface being checked


Return
======

``true`` (nonzero) iff the interface is claimed, else ``false`` (zero).


Note
====

Callers must own the driver model's usb bus readlock. So driver
``probe`` entries don't need extra locking, but other call contexts may
need to explicitly claim that lock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
