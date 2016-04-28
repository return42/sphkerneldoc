.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-ep-free-request:

===================
usb_ep_free_request
===================

*man usb_ep_free_request(9)*

*4.6.0-rc5*

frees a request object


Synopsis
========

.. c:function:: void usb_ep_free_request( struct usb_ep * ep, struct usb_request * req )

Arguments
=========

``ep``
    the endpoint associated with the request

``req``
    the request being freed


Description
===========

Reverses the effect of ``usb_ep_alloc_request``. Caller guarantees the
request is not queued, and that it will no longer be requeued (or
otherwise used).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
