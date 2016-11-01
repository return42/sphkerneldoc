.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/u_f.h

.. _`alloc_ep_req`:

alloc_ep_req
============

.. c:function:: struct usb_request *alloc_ep_req(struct usb_ep *ep, size_t len)

    returns a usb_request allocated by the gadget driver and allocates the request's buffer.

    :param struct usb_ep \*ep:
        the endpoint to allocate a usb_request

    :param size_t len:
        usb_requests's buffer suggested size

.. _`alloc_ep_req.description`:

Description
-----------

In case \ ``ep``\  direction is OUT, the \ ``len``\  will be aligned to ep's
wMaxPacketSize. In order to avoid memory leaks or drops, \*always\* use
usb_requests's length (req->length) to refer to the allocated buffer size.
Requests allocated via \ :c:func:`alloc_ep_req`\  \*must\* be freed by \ :c:func:`free_ep_req`\ .

.. This file was automatic generated / don't edit.

