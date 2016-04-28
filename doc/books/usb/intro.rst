.. -*- coding: utf-8; mode: rst -*-

.. _intro:

============================
Introduction to USB on Linux
============================

A Universal Serial Bus (USB) is used to connect a host, such as a PC or
workstation, to a number of peripheral devices. USB uses a tree
structure, with the host as the root (the system's master), hubs as
interior nodes, and peripherals as leaves (and slaves). Modern PCs
support several such trees of USB devices, usually one USB 2.0 tree (480
Mbit/sec each) with a few USB 1.1 trees (12 Mbit/sec each) that are used
when you connect a USB 1.1 device directly to the machine's "root hub".

That master/slave asymmetry was designed-in for a number of reasons, one
being ease of use. It is not physically possible to assemble (legal) USB
cables incorrectly: all upstream "to the host" connectors are the
rectangular type (matching the sockets on root hubs), and all downstream
connectors are the squarish type (or they are built into the
peripheral). Also, the host software doesn't need to deal with
distributed auto-configuration since the pre-designated master node
manages all that. And finally, at the electrical level, bus protocol
overhead is reduced by eliminating arbitration and moving scheduling
into the host software.

USB 1.0 was announced in January 1996 and was revised as USB 1.1 (with
improvements in hub specification and support for interrupt-out
transfers) in September 1998. USB 2.0 was released in April 2000, adding
high-speed transfers and transaction-translating hubs (used for USB 1.1
and 1.0 backward compatibility).

Kernel developers added USB support to Linux early in the 2.2 kernel
series, shortly before 2.3 development forked. Updates from 2.3 were
regularly folded back into 2.2 releases, which improved reliability and
brought ``/sbin/hotplug`` support as well more drivers. Such
improvements were continued in the 2.5 kernel series, where they added
USB 2.0 support, improved performance, and made the host controller
drivers (HCDs) more consistent. They also simplified the API (to make
bugs less likely) and added internal "kerneldoc" documentation.

Linux can run inside USB devices as well as on the hosts that control
the devices. But USB device drivers running inside those peripherals
don't do the same things as the ones running inside hosts, so they've
been given a different name: *gadget drivers*. This document does not
cover gadget drivers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
