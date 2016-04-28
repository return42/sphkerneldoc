.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-gadget-probe-driver:

=======================
usb_gadget_probe_driver
=======================

*man usb_gadget_probe_driver(9)*

*4.6.0-rc5*

probe a gadget driver


Synopsis
========

.. c:function:: int usb_gadget_probe_driver( struct usb_gadget_driver * driver )

Arguments
=========

``driver``
    the driver being registered


Context
=======

can sleep


Description
===========

Call this in your gadget driver's module initialization function, to
tell the underlying usb controller driver about your driver. The
``bind``\ () function will be called to bind it to a gadget before this
registration call returns. It's expected that the ``bind``\ () function
will be in init sections.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
