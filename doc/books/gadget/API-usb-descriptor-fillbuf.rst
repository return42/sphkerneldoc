
.. _API-usb-descriptor-fillbuf:

======================
usb_descriptor_fillbuf
======================

*man usb_descriptor_fillbuf(9)*

*4.6.0-rc1*

fill buffer with descriptors


Synopsis
========

.. c:function:: int usb_descriptor_fillbuf( void * buf, unsigned buflen, const struct usb_descriptor_header ** src )

Arguments
=========

``buf``
    Buffer to be filled

``buflen``
    Size of buf

``src``
    Array of descriptor pointers, terminated by null pointer.


Description
===========

Copies descriptors into the buffer, returning the length or a negative error code if they can't all be copied. Useful when assembling descriptors for an associated set of
interfaces used as part of configuring a composite device; or in other cases where sets of descriptors need to be marshaled.
