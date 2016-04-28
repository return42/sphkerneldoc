.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-composite-probe:

===================
usb_composite_probe
===================

*man usb_composite_probe(9)*

*4.6.0-rc5*

register a composite driver


Synopsis
========

.. c:function:: int usb_composite_probe( struct usb_composite_driver * driver )

Arguments
=========

``driver``
    the driver to register


Context
=======

single threaded during gadget setup


Description
===========

This function is used to register drivers using the composite driver
framework. The return value is zero, or a negative errno value. Those
values normally come from the driver's ``bind`` method, which does all
the work of setting up the driver to match the hardware.

On successful return, the gadget is ready to respond to requests from
the host, unless one of its components invokes ``usb_gadget_disconnect``
while it was binding. That would usually be done in order to wait for
some userspace participation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
