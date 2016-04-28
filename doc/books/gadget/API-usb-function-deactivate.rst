.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-function-deactivate:

=======================
usb_function_deactivate
=======================

*man usb_function_deactivate(9)*

*4.6.0-rc5*

prevent function and gadget enumeration


Synopsis
========

.. c:function:: int usb_function_deactivate( struct usb_function * function )

Arguments
=========

``function``
    the function that isn't yet ready to respond


Description
===========

Blocks response of the gadget driver to host enumeration by preventing
the data line pullup from being activated. This is normally called
during ``bind``\ () processing to change from the initial “ready to
respond” state, or when a required resource becomes available.

For example, drivers that serve as a passthrough to a userspace daemon
can block enumeration unless that daemon (such as an OBEX, MTP, or print
server) is ready to handle host requests.

Not all systems support software control of their USB peripheral data
pullups.

Returns zero on success, else negative errno.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
