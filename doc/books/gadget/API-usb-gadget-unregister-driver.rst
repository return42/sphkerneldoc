.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-gadget-unregister-driver:

============================
usb_gadget_unregister_driver
============================

*man usb_gadget_unregister_driver(9)*

*4.6.0-rc5*

unregister a gadget driver


Synopsis
========

.. c:function:: int usb_gadget_unregister_driver( struct usb_gadget_driver * driver )

Arguments
=========

``driver``
    the driver being unregistered


Context
=======

can sleep


Description
===========

Call this in your gadget driver's module cleanup function, to tell the
underlying usb controller that your driver is going away. If the
controller is connected to a USB host, it will first ``disconnect``. The
driver is also requested to ``unbind`` and clean up any device state,
before this procedure finally returns. It's expected that the ``unbind``
functions will in in exit sections, so may not be linked in some
kernels.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
