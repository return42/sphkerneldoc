
.. _API-usb-ep-alloc-request:

====================
usb_ep_alloc_request
====================

*man usb_ep_alloc_request(9)*

*4.6.0-rc1*

allocate a request object to use with this endpoint


Synopsis
========

.. c:function:: struct usb_request ⋆ usb_ep_alloc_request( struct usb_ep * ep, gfp_t gfp_flags )

Arguments
=========

``ep``
    the endpoint to be used with with the request

``gfp_flags``
    GFP_⋆ flags to use


Description
===========

Request objects must be allocated with this call, since they normally need controller-specific setup and may even need endpoint-specific resources such as allocation of DMA
descriptors. Requests may be submitted with ``usb_ep_queue``, and receive a single completion callback. Free requests with ``usb_ep_free_request``, when they are no longer needed.

Returns the request, or null if one could not be allocated.
