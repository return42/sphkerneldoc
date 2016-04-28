.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-autopm-get-interface:

========================
usb_autopm_get_interface
========================

*man usb_autopm_get_interface(9)*

*4.6.0-rc5*

increment a USB interface's PM-usage counter


Synopsis
========

.. c:function:: int usb_autopm_get_interface( struct usb_interface * intf )

Arguments
=========

``intf``
    the usb_interface whose counter should be incremented


Description
===========

This routine should be called by an interface driver when it wants to
use ``intf`` and needs to guarantee that it is not suspended. In
addition, the routine prevents ``intf`` from being autosuspended
subsequently. (Note that this will not prevent suspend events
originating in the PM core.) This prevention will persist until
``usb_autopm_put_interface`` is called or ``intf`` is unbound. A typical
example would be a character-device driver when its device file is
opened.

``intf``'s usage counter is incremented to prevent subsequent
autosuspends. However if the autoresume fails then the counter is
re-decremented.

This routine can run only in process context.


Return
======

0 on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
