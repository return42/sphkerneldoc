
.. _API-usb-wait-anchor-empty-timeout:

=============================
usb_wait_anchor_empty_timeout
=============================

*man usb_wait_anchor_empty_timeout(9)*

*4.6.0-rc1*

wait for an anchor to be unused


Synopsis
========

.. c:function:: int usb_wait_anchor_empty_timeout( struct usb_anchor * anchor, unsigned int timeout )

Arguments
=========

``anchor``
    the anchor you want to become unused

``timeout``
    how long you are willing to wait in milliseconds


Description
===========

Call this is you want to be sure all an anchor's URBs have finished


Return
======

Non-zero if the anchor became unused. Zero on timeout.
