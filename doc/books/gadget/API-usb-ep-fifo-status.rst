.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-ep-fifo-status:

==================
usb_ep_fifo_status
==================

*man usb_ep_fifo_status(9)*

*4.6.0-rc5*

returns number of bytes in fifo, or error


Synopsis
========

.. c:function:: int usb_ep_fifo_status( struct usb_ep * ep )

Arguments
=========

``ep``
    the endpoint whose fifo status is being checked.


Description
===========

FIFO endpoints may have “unclaimed data” in them in certain cases, such
as after aborted transfers. Hosts may not have collected all the IN data
written by the gadget driver (and reported by a request completion). The
gadget driver may not have collected all the data written OUT to it by
the host. Drivers that need precise handling for fault reporting or
recovery may need to use this call.

This returns the number of such bytes in the fifo, or a negative errno
if the endpoint doesn't use a FIFO or doesn't support such precise
handling.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
