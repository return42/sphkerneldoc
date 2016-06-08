.. -*- coding: utf-8; mode: rst -*-

.. _structure:

***************************
Structure of Gadget Drivers
***************************

A system running inside a USB peripheral normally has at least three
layers inside the kernel to handle USB protocol processing, and may have
additional layers in user space code. The "gadget" API is used by the
middle layer to interact with the lowest level (which directly handles
hardware).

In Linux, from the bottom up, these layers are:

*USB Controller Driver*
    This is the lowest software level. It is the only layer that talks
    to hardware, through registers, fifos, dma, irqs, and the like. The
    ``<linux/usb/gadget.h>`` API abstracts the peripheral controller
    endpoint hardware. That hardware is exposed through endpoint
    objects, which accept streams of IN/OUT buffers, and through
    callbacks that interact with gadget drivers. Since normal USB
    devices only have one upstream port, they only have one of these
    drivers. The controller driver can support any number of different
    gadget drivers, but only one of them can be used at a time.

    Examples of such controller hardware include the PCI-based NetChip
    2280 USB 2.0 high speed controller, the SA-11x0 or PXA-25x UDC
    (found within many PDAs), and a variety of other products.

*Gadget Driver*
    The lower boundary of this driver implements hardware-neutral USB
    functions, using calls to the controller driver. Because such
    hardware varies widely in capabilities and restrictions, and is used
    in embedded environments where space is at a premium, the gadget
    driver is often configured at compile time to work with endpoints
    supported by one particular controller. Gadget drivers may be
    portable to several different controllers, using conditional
    compilation. (Recent kernels substantially simplify the work
    involved in supporting new hardware, by *autoconfiguring* endpoints
    automatically for many bulk-oriented drivers.) Gadget driver
    responsibilities include:

    -  handling setup requests (ep0 protocol responses) possibly
       including class-specific functionality

    -  returning configuration and string descriptors

    -  (re)setting configurations and interface altsettings, including
       enabling and configuring endpoints

    -  handling life cycle events, such as managing bindings to
       hardware, USB suspend/resume, remote wakeup, and disconnection
       from the USB host.

    -  managing IN and OUT transfers on all currently enabled endpoints

    Such drivers may be modules of proprietary code, although that
    approach is discouraged in the Linux community.

*Upper Level*
    Most gadget drivers have an upper boundary that connects to some
    Linux driver or framework in Linux. Through that boundary flows the
    data which the gadget driver produces and/or consumes through
    protocol transfers over USB. Examples include:

    -  user mode code, using generic (gadgetfs) or application specific
       files in ``/dev``

    -  networking subsystem (for network gadgets, like the CDC Ethernet
       Model gadget driver)

    -  data capture drivers, perhaps video4Linux or a scanner driver; or
       test and measurement hardware.

    -  input subsystem (for HID gadgets)

    -  sound subsystem (for audio gadgets)

    -  file system (for PTP gadgets)

    -  block i/o subsystem (for usb-storage gadgets)

    -  ... and more

*Additional Layers*
    Other layers may exist. These could include kernel layers, such as
    network protocol stacks, as well as user mode applications building
    on standard POSIX system call APIs such as *open()*, *close()*,
    *read()* and *write()*. On newer systems, POSIX Async I/O calls may
    be an option. Such user mode code will not necessarily be subject to
    the GNU General Public License (GPL).

OTG-capable systems will also need to include a standard Linux-USB host
side stack, with *usbcore*, one or more *Host Controller Drivers*
(HCDs), *USB Device Drivers* to support the OTG "Targeted Peripheral
List", and so forth. There will also be an *OTG Controller Driver*,
which is visible to gadget and device driver developers only indirectly.
That helps the host and device side USB controllers implement the two
new OTG protocols (HNP and SRP). Roles switch (host to peripheral, or
vice versa) using HNP during USB suspend processing, and SRP can be
viewed as a more battery-friendly kind of device wakeup protocol.

Over time, reusable utilities are evolving to help make some gadget
driver tasks simpler. For example, building configuration descriptors
from vectors of descriptors for the configurations interfaces and
endpoints is now automated, and many drivers now use autoconfiguration
to choose hardware endpoints and initialize their descriptors. A
potential example of particular interest is code implementing standard
USB-IF protocols for HID, networking, storage, or audio classes. Some
developers are interested in KDB or KGDB hooks, to let target hardware
be remotely debugged. Most such USB protocol code doesn't need to be
hardware-specific, any more than network protocols like X11, HTTP, or
NFS are. Such gadget-side interface drivers should eventually be
combined, to implement composite devices.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
