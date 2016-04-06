
.. _API-usb-ep-dequeue:

==============
usb_ep_dequeue
==============

*man usb_ep_dequeue(9)*

*4.6.0-rc1*

dequeues (cancels, unlinks) an I/O request from an endpoint


Synopsis
========

.. c:function:: int usb_ep_dequeue( struct usb_ep * ep, struct usb_request * req )

Arguments
=========

``ep``
    the endpoint associated with the request

``req``
    the request being canceled


Description
===========

If the request is still active on the endpoint, it is dequeued and its completion routine is called (with status -ECONNRESET); else a negative error code is returned. This is
guaranteed to happen before the call to ``usb_ep_dequeue`` returns.

Note that some hardware can't clear out write fifos (to unlink the request at the head of the queue) except as part of disconnecting from usb. Such restrictions prevent drivers
from supporting configuration changes, even to configuration zero (a “chapter 9” requirement).
