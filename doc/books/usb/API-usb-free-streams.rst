.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-free-streams:

================
usb_free_streams
================

*man usb_free_streams(9)*

*4.6.0-rc5*

free bulk endpoint stream IDs.


Synopsis
========

.. c:function:: int usb_free_streams( struct usb_interface * interface, struct usb_host_endpoint ** eps, unsigned int num_eps, gfp_t mem_flags )

Arguments
=========

``interface``
    alternate setting that includes all endpoints.

``eps``
    array of endpoints to remove streams from.

``num_eps``
    number of endpoints in the array.

``mem_flags``
    flags hcd should use to allocate memory.


Description
===========

Reverts a group of bulk endpoints back to not using stream IDs. Can fail
if we are given bad arguments, or HCD is broken.


Return
======

0 on success. On failure, a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
