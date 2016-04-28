.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-copy-descriptors:

====================
usb_copy_descriptors
====================

*man usb_copy_descriptors(9)*

*4.6.0-rc5*

copy a vector of USB descriptors


Synopsis
========

.. c:function:: struct usb_descriptor_header ** usb_copy_descriptors( struct usb_descriptor_header ** src )

Arguments
=========

``src``
    null-terminated vector to copy


Context
=======

initialization code, which may sleep


Description
===========

This makes a copy of a vector of USB descriptors. Its primary use is to
support usb_function objects which can have multiple copies, each
needing different descriptors. Functions may have static tables of
descriptors, which are used as templates and customized with identifiers
(for interfaces, strings, endpoints, and more) as needed by a given
function instance.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
