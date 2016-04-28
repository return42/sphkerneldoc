.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-wait-anchor-empty-timeout:

=============================
usb_wait_anchor_empty_timeout
=============================

*man usb_wait_anchor_empty_timeout(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
