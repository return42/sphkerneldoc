.. -*- coding: utf-8; mode: rst -*-

.. _hcd:

********************
Host Controller APIs
********************

These APIs are only for use by host controller drivers, most of which
implement standard register interfaces such as XHCI, EHCI, OHCI, or
UHCI. UHCI was one of the first interfaces, designed by Intel and also
used by VIA; it doesn't do much in hardware. OHCI was designed later, to
have the hardware do more work (bigger transfers, tracking protocol
state, and so on). EHCI was designed with USB 2.0; its design has
features that resemble OHCI (hardware does much more work) as well as
UHCI (some parts of ISO support, TD list processing). XHCI was designed
with USB 3.0. It continues to shift support for functionality into
hardware.

There are host controllers other than the "big three", although most PCI
based controllers (and a few non-PCI based ones) use one of those
interfaces. Not all host controllers use DMA; some use PIO, and there is
also a simulator and a virtual host controller to pipe USB over the
network.

The same basic APIs are available to drivers for all those controllers.
For historical reasons they are in two layers:
:c:type:`struct usb_bus` is a rather thin layer that became available
in the 2.2 kernels, while :c:type:`struct usb_hcd` is a more
featureful layer that lets HCDs share common code, to shrink driver size
and significantly reduce hcd-specific behaviors.


.. kernel-doc:: drivers/usb/core/hcd.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/usb/core/hcd-pci.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/usb/core/buffer.c
    :man-sect: 9
    :internal:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
