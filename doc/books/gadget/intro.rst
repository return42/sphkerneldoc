.. -*- coding: utf-8; mode: rst -*-

.. _intro:

============
Introduction
============

This document presents a Linux-USB "Gadget" kernel mode API, for use
within peripherals and other USB devices that embed Linux. It provides
an overview of the API structure, and shows how that fits into a system
development project. This is the first such API released on Linux to
address a number of important problems, including:

-  Supports USB 2.0, for high speed devices which can stream data at
   several dozen megabytes per second.

-  Handles devices with dozens of endpoints just as well as ones with
   just two fixed-function ones. Gadget drivers can be written so
   they're easy to port to new hardware.

-  Flexible enough to expose more complex USB device capabilities such
   as multiple configurations, multiple interfaces, composite devices,
   and alternate interface settings.

-  USB "On-The-Go" (OTG) support, in conjunction with updates to the
   Linux-USB host side.

-  Sharing data structures and API models with the Linux-USB host side
   API. This helps the OTG support, and looks forward to more-symmetric
   frameworks (where the same I/O model is used by both host and device
   side drivers).

-  Minimalist, so it's easier to support new device controller hardware.
   I/O processing doesn't imply large demands for memory or CPU
   resources.

Most Linux developers will not be able to use this API, since they have
USB "host" hardware in a PC, workstation, or server. Linux users with
embedded systems are more likely to have USB peripheral hardware. To
distinguish drivers running inside such hardware from the more familiar
Linux "USB device drivers", which are host side proxies for the real USB
devices, a different term is used: the drivers inside the peripherals
are "USB gadget drivers". In USB protocol interactions, the device
driver is the master (or "client driver") and the gadget driver is the
slave (or "function driver").

The gadget API resembles the host side Linux-USB API in that both use
queues of request objects to package I/O buffers, and those requests may
be submitted or canceled. They share common definitions for the standard
USB *Chapter 9* messages, structures, and constants. Also, both APIs
bind and unbind drivers to devices. The APIs differ in detail, since the
host side's current URB framework exposes a number of implementation
details and assumptions that are inappropriate for a gadget API. While
the model for control transfers and configuration management is
necessarily different (one side is a hardware-neutral master, the other
is a hardware-aware slave), the endpoint I/0 API used here should also
be usable for an overhead-reduced host side API.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
