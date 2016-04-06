
.. _api:

======================
Kernel Mode Gadget API
======================

Gadget drivers declare themselves through a *struct usb_gadget_driver*, which is responsible for most parts of enumeration for a *struct usb_gadget*. The response to a
set_configuration usually involves enabling one or more of the *struct usb_ep* objects exposed by the gadget, and submitting one or more *struct usb_request* buffers to transfer
data. Understand those four data types, and their operations, and you will understand how this API works.

    **Note**

    This documentation was prepared using the standard Linux kernel ``docproc`` tool, which turns text and in-code comments into SGML DocBook and then into usable formats such as
    HTML or PDF. Other than the "Chapter 9" data types, most of the significant data types and functions are described here.

    However, docproc does not understand all the C constructs that are used, so some relevant information is likely omitted from what you are reading. One example of such
    information is endpoint autoconfiguration. You'll have to read the header file, and use example source code (such as that for "Gadget Zero"), to fully understand the API.

    The part of the API implementing some basic driver capabilities is specific to the version of the Linux kernel that's in use. The 2.6 kernel includes a *driver model* framework
    that has no analogue on earlier kernels; so those parts of the gadget API are not fully portable. (They are implemented on 2.4 kernels, but in a different way.) The driver
    model state is another part of this API that is ignored by the kerneldoc tools.

The core API does not expose every possible hardware feature, only the most widely available ones. There are significant hardware features, such as device-to-device DMA (without
temporary storage in a memory buffer) that would be added using hardware-specific APIs.

This API allows drivers to use conditional compilation to handle endpoint capabilities of different hardware, but doesn't require that. Hardware tends to have arbitrary
restrictions, relating to transfer types, addressing, packet sizes, buffering, and availability. As a rule, such differences only matter for "endpoint zero" logic that handles
device configuration and management. The API supports limited run-time detection of capabilities, through naming conventions for endpoints. Many drivers will be able to at least
partially autoconfigure themselves. In particular, driver init sections will often have endpoint autoconfiguration logic that scans the hardware's list of endpoints to find ones
matching the driver requirements (relying on those conventions), to eliminate some of the most common reasons for conditional compilation.

Like the Linux-USB host side API, this API exposes the "chunky" nature of USB messages: I/O requests are in terms of one or more "packets", and packet boundaries are visible to
drivers. Compared to RS-232 serial protocols, USB resembles synchronous protocols like HDLC (N bytes per frame, multipoint addressing, host as the primary station and devices as
secondary stations) more than asynchronous ones (tty style: 8 data bits per frame, no parity, one stop bit). So for example the controller drivers won't buffer two single byte
writes into a single two-byte USB IN packet, although gadget drivers may do so when they implement protocols where packet boundaries (and "short packets") are not significant.


.. _lifecycle:

Driver Life Cycle
=================

Gadget drivers make endpoint I/O requests to hardware without needing to know many details of the hardware, but driver setup/configuration code needs to handle some differences.
Use the API like this:

1. Register a driver for the particular device side usb controller hardware, such as the net2280 on PCI (USB 2.0), sa11x0 or pxa25x as found in Linux PDAs, and so on. At this point
   the device is logically in the USB ch9 initial state ("attached"), drawing no power and not usable (since it does not yet support enumeration). Any host should not see the
   device, since it's not activated the data line pullup used by the host to detect a device, even if VBUS power is available.

2. Register a gadget driver that implements some higher level device function. That will then bind() to a usb_gadget, which activates the data line pullup sometime after detecting
   VBUS.

3. The hardware driver can now start enumerating. The steps it handles are to accept USB power and set_address requests. Other steps are handled by the gadget driver. If the
   gadget driver module is unloaded before the host starts to enumerate, steps before step 7 are skipped.

4. The gadget driver's setup() call returns usb descriptors, based both on what the bus interface hardware provides and on the functionality being implemented. That can involve
   alternate settings or configurations, unless the hardware prevents such operation. For OTG devices, each configuration descriptor includes an OTG descriptor.

5. The gadget driver handles the last step of enumeration, when the USB host issues a set_configuration call. It enables all endpoints used in that configuration, with all
   interfaces in their default settings. That involves using a list of the hardware's endpoints, enabling each endpoint according to its descriptor. It may also involve using
   ``usb_gadget_vbus_draw`` to let more power be drawn from VBUS, as allowed by that configuration. For OTG devices, setting a configuration may also involve reporting HNP
   capabilities through a user interface.

6. Do real work and perform data transfers, possibly involving changes to interface settings or switching to new configurations, until the device is disconnect()ed from the host.
   Queue any number of transfer requests to each endpoint. It may be suspended and resumed several times before being disconnected. On disconnect, the drivers go back to step 3
   (above).

7. When the gadget driver module is being unloaded, the driver unbind() callback is issued. That lets the controller driver be unloaded.

Drivers will normally be arranged so that just loading the gadget driver module (or statically linking it into a Linux kernel) allows the peripheral device to be enumerated, but
some drivers will defer enumeration until some higher level component (like a user mode daemon) enables it. Note that at this lowest level there are no policies about how ep0
configuration logic is implemented, except that it should obey USB specifications. Such issues are in the domain of gadget drivers, including knowing about implementation
constraints imposed by some USB controllers or understanding that composite devices might happen to be built by integrating reusable components.

Note that the lifecycle above can be slightly different for OTG devices. Other than providing an additional OTG descriptor in each configuration, only the HNP-related differences
are particularly visible to driver code. They involve reporting requirements during the SET_CONFIGURATION request, and the option to invoke HNP during some suspend callbacks.
Also, SRP changes the semantics of ``usb_gadget_wakeup`` slightly.


.. _ch9:

USB 2.0 Chapter 9 Types and Constants
=====================================

Gadget drivers rely on common USB structures and constants defined in the ``<linux/usb/ch9.h>`` header file, which is standard in Linux 2.6 kernels. These are the same types and
constants used by host side drivers (and usbcore).


.. toctree::
    :maxdepth: 1

    API-usb-speed-string
    API-usb-get-maximum-speed
    API-usb-state-string

.. _core:

Core Objects and Methods
========================

These are declared in ``<linux/usb/gadget.h>``, and are used by gadget drivers to interact with USB peripheral controller drivers.


.. toctree::
    :maxdepth: 1

    API-struct-usb-request
    API-struct-usb-ep-caps
    API-struct-usb-ep
    API-usb-ep-set-maxpacket-limit
    API-usb-ep-enable
    API-usb-ep-disable
    API-usb-ep-alloc-request
    API-usb-ep-free-request
    API-usb-ep-queue
    API-usb-ep-dequeue
    API-usb-ep-set-halt
    API-usb-ep-clear-halt
    API-usb-ep-set-wedge
    API-usb-ep-fifo-status
    API-usb-ep-fifo-flush
    API-struct-usb-gadget
    API-usb-ep-align-maybe
    API-gadget-is-altset-supported
    API-gadget-is-stall-supported
    API-gadget-is-zlp-supported
    API-gadget-is-dualspeed
    API-gadget-is-superspeed
    API-gadget-is-superspeed-plus
    API-gadget-is-otg
    API-usb-gadget-frame-number
    API-usb-gadget-wakeup
    API-usb-gadget-set-selfpowered
    API-usb-gadget-clear-selfpowered
    API-usb-gadget-vbus-connect
    API-usb-gadget-vbus-draw
    API-usb-gadget-vbus-disconnect
    API-usb-gadget-connect
    API-usb-gadget-disconnect
    API-usb-gadget-deactivate
    API-usb-gadget-activate
    API-struct-usb-gadget-driver
    API-usb-gadget-probe-driver
    API-usb-gadget-unregister-driver
    API-struct-usb-string
    API-struct-usb-gadget-strings
    API-usb-free-descriptors

.. _utils:

Optional Utilities
==================

The core API is sufficient for writing a USB Gadget Driver, but some optional utilities are provided to simplify common tasks. These utilities include endpoint autoconfiguration.


.. toctree::
    :maxdepth: 1

    API-usb-gadget-get-string
    API-usb-descriptor-fillbuf
    API-usb-gadget-config-buf
    API-usb-copy-descriptors

.. _composite:

Composite Device Framework
==========================

The core API is sufficient for writing drivers for composite USB devices (with more than one function in a given configuration), and also multi-configuration devices (also more
than one function, but not necessarily sharing a given configuration). There is however an optional framework which makes it easier to reuse and combine functions.

Devices using this framework provide a *struct usb_composite_driver*, which in turn provides one or more *struct usb_configuration* instances. Each such configuration includes
at least one *struct usb_function*, which packages a user visible role such as "network link" or "mass storage device". Management functions may also exist, such as "Device
Firmware Upgrade".


.. toctree::
    :maxdepth: 1

    API-struct-usb-os-desc-ext-prop
    API-struct-usb-os-desc
    API-struct-usb-os-desc-table
    API-struct-usb-function
    API-struct-usb-configuration
    API-struct-usb-composite-driver
    API-module-usb-composite-driver
    API-struct-usb-composite-dev
    API-config-ep-by-speed
    API-usb-add-function
    API-usb-function-deactivate
    API-usb-function-activate
    API-usb-interface-id
    API-usb-add-config
    API-usb-string-id
    API-usb-string-ids-tab
    API-usb-gstrings-attach
    API-usb-string-ids-n
    API-usb-composite-probe
    API-usb-composite-unregister
    API-usb-composite-setup-continue

.. _functions:

Composite Device Functions
==========================

At this writing, a few of the current gadget drivers have been converted to this framework. Near-term plans include converting all of them, except for "gadgetfs".



===================================
drivers/usb/gadget/function/f_acm.c
===================================

*man drivers/usb/gadget/function/f_acm.c(None)*

Document generation inconsistency


Oops
====

    **Warning**

    The template for this document tried to insert the structured comment from the file ``drivers/usb/gadget/function/f_acm.c`` at this point, but none was found. This dummy
    section is inserted to allow generation to continue.



===================================
drivers/usb/gadget/function/f_ecm.c
===================================

*man drivers/usb/gadget/function/f_ecm.c(None)*

Document generation inconsistency


Oops
====

    **Warning**

    The template for this document tried to insert the structured comment from the file ``drivers/usb/gadget/function/f_ecm.c`` at this point, but none was found. This dummy
    section is inserted to allow generation to continue.



======================================
drivers/usb/gadget/function/f_subset.c
======================================

*man drivers/usb/gadget/function/f_subset.c(None)*

Document generation inconsistency


Oops
====

    **Warning**

    The template for this document tried to insert the structured comment from the file ``drivers/usb/gadget/function/f_subset.c`` at this point, but none was found. This dummy
    section is inserted to allow generation to continue.



====================================
drivers/usb/gadget/function/f_obex.c
====================================

*man drivers/usb/gadget/function/f_obex.c(None)*

Document generation inconsistency


Oops
====

    **Warning**

    The template for this document tried to insert the structured comment from the file ``drivers/usb/gadget/function/f_obex.c`` at this point, but none was found. This dummy
    section is inserted to allow generation to continue.



======================================
drivers/usb/gadget/function/f_serial.c
======================================

*man drivers/usb/gadget/function/f_serial.c(None)*

Document generation inconsistency


Oops
====

    **Warning**

    The template for this document tried to insert the structured comment from the file ``drivers/usb/gadget/function/f_serial.c`` at this point, but none was found. This dummy
    section is inserted to allow generation to continue.
