
.. _API-usb-ep-align-maybe:

==================
usb_ep_align_maybe
==================

*man usb_ep_align_maybe(9)*

*4.6.0-rc1*

returns ``len`` aligned to ep's maxpacketsize if gadget requires quirk_ep_out_aligned_size, otherwise reguens len.


Synopsis
========

.. c:function:: size_t usb_ep_align_maybe( struct usb_gadget * g, struct usb_ep * ep, size_t len )

Arguments
=========

``g``
    controller to check for quirk

``ep``
    the endpoint whose maxpacketsize is used to align ``len``

``len``
    buffer size's length to align to ``ep``'s maxpacketsize


Description
===========

This helper is used in case it's required for any reason to check and maybe align buffer's size to an ep's maxpacketsize.
