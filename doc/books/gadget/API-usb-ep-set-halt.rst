.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-ep-set-halt:

===============
usb_ep_set_halt
===============

*man usb_ep_set_halt(9)*

*4.6.0-rc5*

sets the endpoint halt feature.


Synopsis
========

.. c:function:: int usb_ep_set_halt( struct usb_ep * ep )

Arguments
=========

``ep``
    the non-isochronous endpoint being stalled


Description
===========

Use this to stall an endpoint, perhaps as an error report. Except for
control endpoints, the endpoint stays halted (will not stream any data)
until the host clears this feature; drivers may need to empty the
endpoint's request queue first, to make sure no inappropriate transfers
happen.

Note that while an endpoint CLEAR_FEATURE will be invisible to the
gadget driver, a SET_INTERFACE will not be. To reset endpoints for the
current altsetting, see ``usb_ep_clear_halt``. When switching
altsettings, it's simplest to use ``usb_ep_enable`` or
``usb_ep_disable`` for the endpoints.

Returns zero, or a negative error code. On success, this call sets
underlying hardware state that blocks data transfers. Attempts to halt
IN endpoints will fail (returning -EAGAIN) if any transfer requests are
still queued, or if the controller hardware (usually a FIFO) still holds
bytes that the host hasn't collected.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
