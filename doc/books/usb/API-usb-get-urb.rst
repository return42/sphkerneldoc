.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-get-urb:

===========
usb_get_urb
===========

*man usb_get_urb(9)*

*4.6.0-rc5*

increments the reference count of the urb


Synopsis
========

.. c:function:: struct urb * usb_get_urb( struct urb * urb )

Arguments
=========

``urb``
    pointer to the urb to modify, may be NULL


Description
===========

This must be called whenever a urb is transferred from a device driver
to a host controller driver. This allows proper reference counting to
happen for urbs.


Return
======

A pointer to the urb with the incremented reference counter.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
