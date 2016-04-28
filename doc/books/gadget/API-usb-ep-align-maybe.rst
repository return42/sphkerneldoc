.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-ep-align-maybe:

==================
usb_ep_align_maybe
==================

*man usb_ep_align_maybe(9)*

*4.6.0-rc5*

returns ``len`` aligned to ep's maxpacketsize if gadget requires
quirk_ep_out_aligned_size, otherwise reguens len.


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

This helper is used in case it's required for any reason to check and
maybe align buffer's size to an ep's maxpacketsize.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
