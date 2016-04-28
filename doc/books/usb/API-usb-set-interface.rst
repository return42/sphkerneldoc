.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-set-interface:

=================
usb_set_interface
=================

*man usb_set_interface(9)*

*4.6.0-rc5*

Makes a particular alternate setting be current


Synopsis
========

.. c:function:: int usb_set_interface( struct usb_device * dev, int interface, int alternate )

Arguments
=========

``dev``
    the device whose interface is being updated

``interface``
    the interface being updated

``alternate``
    the setting being chosen.


Context
=======

!in_interrupt ()


Description
===========

This is used to enable data transfers on interfaces that may not be
enabled by default. Not all devices support such configurability. Only
the driver bound to an interface may change its setting.

Within any given configuration, each interface may have several
alternative settings. These are often used to control levels of
bandwidth consumption. For example, the default setting for a high speed
interrupt endpoint may not send more than 64 bytes per microframe, while
interrupt transfers of up to 3KBytes per microframe are legal. Also,
isochronous endpoints may never be part of an interface's default
setting. To access such bandwidth, alternate interface settings must be
made current.

Note that in the Linux USB subsystem, bandwidth associated with an
endpoint in a given alternate setting is not reserved until an URB is
submitted that needs that bandwidth. Some other operating systems
allocate bandwidth early, when a configuration is chosen.

This call is synchronous, and may not be used in an interrupt context.
Also, drivers must not change altsettings while urbs are scheduled for
endpoints in that interface; all such urbs must first be completed
(perhaps forced by unlinking).


Return
======

Zero on success, or else the status code returned by the underlying
``usb_control_msg`` call.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
