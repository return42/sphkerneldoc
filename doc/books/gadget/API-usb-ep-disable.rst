
.. _API-usb-ep-disable:

==============
usb_ep_disable
==============

*man usb_ep_disable(9)*

*4.6.0-rc1*

endpoint is no longer usable


Synopsis
========

.. c:function:: int usb_ep_disable( struct usb_ep * ep )

Arguments
=========

``ep``
    the endpoint being unconfigured. may not be the endpoint named “ep0”.


Description
===========

no other task may be using this endpoint when this is called. any pending and uncompleted requests will complete with status indicating disconnect (-ESHUTDOWN) before this call
returns. gadget drivers must call ``usb_ep_enable`` again before queueing requests to the endpoint.

returns zero, or a negative error code.
