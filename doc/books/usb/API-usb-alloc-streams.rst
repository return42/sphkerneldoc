
.. _API-usb-alloc-streams:

=================
usb_alloc_streams
=================

*man usb_alloc_streams(9)*

*4.6.0-rc1*

allocate bulk endpoint stream IDs.


Synopsis
========

.. c:function:: int usb_alloc_streams( struct usb_interface * interface, struct usb_host_endpoint ** eps, unsigned int num_eps, unsigned int num_streams, gfp_t mem_flags )

Arguments
=========

``interface``
    alternate setting that includes all endpoints.

``eps``
    array of endpoints that need streams.

``num_eps``
    number of endpoints in the array.

``num_streams``
    number of streams to allocate.

``mem_flags``
    flags hcd should use to allocate memory.


Description
===========

Sets up a group of bulk endpoints to have ``num_streams`` stream IDs available. Drivers may queue multiple transfers to different stream IDs, which may complete in a different
order than they were queued.


Return
======

On success, the number of allocated streams. On failure, a negative error code.
