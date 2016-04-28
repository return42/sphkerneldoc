.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-interface-id:

================
usb_interface_id
================

*man usb_interface_id(9)*

*4.6.0-rc5*

allocate an unused interface ID


Synopsis
========

.. c:function:: int usb_interface_id( struct usb_configuration * config, struct usb_function * function )

Arguments
=========

``config``
    configuration associated with the interface

``function``
    function handling the interface


Context
=======

single threaded during gadget setup


Description
===========

``usb_interface_id`` is called from usb_function. ``bind`` callbacks
to allocate new interface IDs. The function driver will then store that
ID in interface, association, CDC union, and other descriptors. It will
also handle any control requests targeted at that interface,
particularly changing its altsetting via ``set_alt``. There may also be
class-specific or vendor-specific requests to handle.

All interface identifier should be allocated using this routine, to
ensure that for example different functions don't wrongly assign
different meanings to the same identifier. Note that since interface
identifiers are configuration-specific, functions used in more than one
configuration (or more than once in a given configuration) need multiple
versions of the relevant descriptors.

Returns the interface ID which was allocated; or -ENODEV if no more
interface IDs can be allocated.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
