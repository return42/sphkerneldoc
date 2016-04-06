
.. _API-usb-ep-fifo-flush:

=================
usb_ep_fifo_flush
=================

*man usb_ep_fifo_flush(9)*

*4.6.0-rc1*

flushes contents of a fifo


Synopsis
========

.. c:function:: void usb_ep_fifo_flush( struct usb_ep * ep )

Arguments
=========

``ep``
    the endpoint whose fifo is being flushed.


Description
===========

This call may be used to flush the “unclaimed data” that may exist in an endpoint fifo after abnormal transaction terminations. The call must never be used except when endpoint is
not being used for any protocol translation.
