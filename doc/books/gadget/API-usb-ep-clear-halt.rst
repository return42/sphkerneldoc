.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-ep-clear-halt:

=================
usb_ep_clear_halt
=================

*man usb_ep_clear_halt(9)*

*4.6.0-rc5*

clears endpoint halt, and resets toggle


Synopsis
========

.. c:function:: int usb_ep_clear_halt( struct usb_ep * ep )

Arguments
=========

``ep``
    the bulk or interrupt endpoint being reset


Description
===========

Use this when responding to the standard usb “set interface” request,
for endpoints that aren't reconfigured, after clearing any other state
in the endpoint's i/o queue.

Returns zero, or a negative error code. On success, this call clears the
underlying hardware state reflecting endpoint halt and data toggle. Note
that some hardware can't support this request (like pxa2xx_udc), and
accordingly can't correctly implement interface altsettings.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
