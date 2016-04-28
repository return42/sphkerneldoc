.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-ep-disable:

==============
usb_ep_disable
==============

*man usb_ep_disable(9)*

*4.6.0-rc5*

endpoint is no longer usable


Synopsis
========

.. c:function:: int usb_ep_disable( struct usb_ep * ep )

Arguments
=========

``ep``
    the endpoint being unconfigured. may not be the endpoint named
    “ep0”.


Description
===========

no other task may be using this endpoint when this is called. any
pending and uncompleted requests will complete with status indicating
disconnect (-ESHUTDOWN) before this call returns. gadget drivers must
call ``usb_ep_enable`` again before queueing requests to the endpoint.

returns zero, or a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
