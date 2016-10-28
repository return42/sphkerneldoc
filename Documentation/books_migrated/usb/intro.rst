.. -*- coding: utf-8; mode: rst -*-

.. _intro:

****************************
Introduction to USB on Linux
****************************

A Universal Serial Bus (USB) is used to connect a host, such as a PC or
workstation, to a number of peripheral devices. USB uses a tree
structure, with the host as the root (the system's master), hubs as
interior nodes, and peripherals as leaves (and slaves). Modern PCs
support several such trees of USB devices, usually a few USB 3.0 (5
GBit/s) or USB 3.1 (10 GBit/s) and some legacy USB 2.0 (480 MBit/s)
busses just in case.

That master/slave asymmetry was designed-in for a number of reasons, one
being ease of use. It is not physically possible to mistake upstream and
downstream or it does not matter with a type C plug (or they are built
into the peripheral). Also, the host software doesn't need to deal with
distributed auto-configuration since the pre-designated master node
manages all that.

Kernel developers added USB support to Linux early in the 2.2 kernel
series and have been developing it further since then. Besides support
for each new generation of USB, various host controllers gained support,
new drivers for peripherals have been added and advanced features for
latency measurement and improved power management introduced.

Linux can run inside USB devices as well as on the hosts that control
the devices. But USB device drivers running inside those peripherals
don't do the same things as the ones running inside hosts, so they've
been given a different name: *gadget drivers*. This document does not
cover gadget drivers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
