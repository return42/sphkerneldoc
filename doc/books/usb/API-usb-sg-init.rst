
.. _API-usb-sg-init:

===========
usb_sg_init
===========

*man usb_sg_init(9)*

*4.6.0-rc1*

initializes scatterlist-based bulk/interrupt I/O request


Synopsis
========

.. c:function:: int usb_sg_init( struct usb_sg_request * io, struct usb_device * dev, unsigned pipe, unsigned period, struct scatterlist * sg, int nents, size_t length, gfp_t mem_flags )

Arguments
=========

``io``
    request block being initialized. until ``usb_sg_wait`` returns, treat this as a pointer to an opaque block of memory,

``dev``
    the usb device that will send or receive the data

``pipe``
    endpoint “pipe” used to transfer the data

``period``
    polling rate for interrupt endpoints, in frames or (for high speed endpoints) microframes; ignored for bulk

``sg``
    scatterlist entries

``nents``
    how many entries in the scatterlist

``length``
    how many bytes to send from the scatterlist, or zero to send every byte identified in the list.

``mem_flags``
    SLAB_⋆ flags affecting memory allocations in this call


Description
===========

This initializes a scatter/gather request, allocating resources such as I/O mappings and urb memory (except maybe memory used by USB controller drivers).

The request must be issued using ``usb_sg_wait``, which waits for the I/O to complete (or to be canceled) and then cleans up all resources allocated by ``usb_sg_init``.

The request may be canceled with ``usb_sg_cancel``, either before or after ``usb_sg_wait`` is called.


Return
======

Zero for success, else a negative errno value.
