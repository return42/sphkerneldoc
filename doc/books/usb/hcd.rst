.. -*- coding: utf-8; mode: rst -*-

.. _hcd:

====================
Host Controller APIs
====================

These APIs are only for use by host controller drivers, most of which
implement standard register interfaces such as EHCI, OHCI, or UHCI. UHCI
was one of the first interfaces, designed by Intel and also used by VIA;
it doesn't do much in hardware. OHCI was designed later, to have the
hardware do more work (bigger transfers, tracking protocol state, and so
on). EHCI was designed with USB 2.0; its design has features that
resemble OHCI (hardware does much more work) as well as UHCI (some parts
of ISO support, TD list processing).

There are host controllers other than the "big three", although most PCI
based controllers (and a few non-PCI based ones) use one of those
interfaces. Not all host controllers use DMA; some use PIO, and there is
also a simulator.

The same basic APIs are available to drivers for all those controllers.
For historical reasons they are in two layers: ``struct usb_bus`` is a
rather thin layer that became available in the 2.2 kernels, while
``struct usb_hcd`` is a more featureful layer (available in later 2.4
kernels and in 2.5) that lets HCDs share common code, to shrink driver
size and significantly reduce hcd-specific behaviors.


.. toctree::
    :maxdepth: 1

    API-usb-calc-bus-time
    API-usb-hcd-link-urb-to-ep
    API-usb-hcd-check-unlink-urb
    API-usb-hcd-unlink-urb-from-ep
    API-usb-hcd-giveback-urb
    API-usb-alloc-streams
    API-usb-free-streams
    API-usb-hcd-resume-root-hub
    API-usb-bus-start-enum
    API-usb-hcd-irq
    API-usb-hc-died
    API-usb-create-shared-hcd
    API-usb-create-hcd
    API-usb-add-hcd
    API-usb-remove-hcd
    API-usb-hcd-pci-probe
    API-usb-hcd-pci-remove
    API-usb-hcd-pci-shutdown
    API-hcd-buffer-create
    API-hcd-buffer-destroy




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
