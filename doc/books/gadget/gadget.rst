.. -*- coding: utf-8; mode: rst -*-

.. _gadget:

==============
Gadget Drivers
==============

In addition to *Gadget Zero* (used primarily for testing and development
with drivers for usb controller hardware), other gadget drivers exist.

There's an *ethernet* gadget driver, which implements one of the most
useful *Communications Device Class* (CDC) models. One of the standards
for cable modem interoperability even specifies the use of this ethernet
model as one of two mandatory options. Gadgets using this code look to a
USB host as if they're an Ethernet adapter. It provides access to a
network where the gadget's CPU is one host, which could easily be
bridging, routing, or firewalling access to other networks. Since some
hardware can't fully implement the CDC Ethernet requirements, this
driver also implements a "good parts only" subset of CDC Ethernet. (That
subset doesn't advertise itself as CDC Ethernet, to avoid creating
problems.)

Support for Microsoft's *RNDIS* protocol has been contributed by
Pengutronix and Auerswald GmbH. This is like CDC Ethernet, but it runs
on more slightly USB hardware (but less than the CDC subset). However,
its main claim to fame is being able to connect directly to recent
versions of Windows, using drivers that Microsoft bundles and supports,
making it much simpler to network with Windows.

There is also support for user mode gadget drivers, using *gadgetfs*.
This provides a *User Mode API* that presents each endpoint as a single
file descriptor. I/O is done using normal *read()* and *read()* calls.
Familiar tools like GDB and pthreads can be used to develop and debug
user mode drivers, so that once a robust controller driver is available
many applications for it won't require new kernel mode software. Linux
2.6 *Async I/O (AIO)* support is available, so that user mode software
can stream data with only slightly more overhead than a kernel driver.

There's a USB Mass Storage class driver, which provides a different
solution for interoperability with systems such as MS-Windows and MacOS.
That *Mass Storage* driver uses a file or block device as backing store
for a drive, like the ``loop`` driver. The USB host uses the BBB, CB, or
CBI versions of the mass storage class specification, using transparent
SCSI commands to access the data from the backing store.

There's a "serial line" driver, useful for TTY style operation over USB.
The latest version of that driver supports CDC ACM style operation, like
a USB modem, and so on most hardware it can interoperate easily with
MS-Windows. One interesting use of that driver is in boot firmware (like
a BIOS), which can sometimes use that model with very small systems
without real serial lines.

Support for other kinds of gadget is expected to be developed and
contributed over time, as this driver framework evolves.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
