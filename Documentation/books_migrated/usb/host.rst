.. -*- coding: utf-8; mode: rst -*-

.. _host:

***********************
USB Host-Side API Model
***********************

Host-side drivers for USB devices talk to the "usbcore" APIs. There are
two. One is intended for *general-purpose* drivers (exposed through
driver frameworks), and the other is for drivers that are *part of the
core*. Such core drivers include the *hub* driver (which manages trees
of USB devices) and several different kinds of *host controller
drivers*, which control individual busses.

The device model seen by USB drivers is relatively complex.

-  USB supports four kinds of data transfers (control, bulk, interrupt,
   and isochronous). Two of them (control and bulk) use bandwidth as
   it's available, while the other two (interrupt and isochronous) are
   scheduled to provide guaranteed bandwidth.

-  The device description model includes one or more "configurations"
   per device, only one of which is active at a time. Devices are
   supposed to be capable of operating at lower than their top speeds
   and may provide a BOS descriptor showing the lowest speed they remain
   fully operational at.

-  From USB 3.0 on configurations have one or more "functions", which
   provide a common functionality and are grouped together for purposes
   of power management.

-  Configurations or functions have one or more "interfaces", each of
   which may have "alternate settings". Interfaces may be standardized
   by USB "Class" specifications, or may be specific to a vendor or
   device.

   USB device drivers actually bind to interfaces, not devices. Think of
   them as "interface drivers", though you may not see many devices
   where the distinction is important. *Most USB devices are simple,
   with only one configuration, one function, one interface, and one
   alternate setting.*

-  Interfaces have one or more "endpoints", each of which supports one
   type and direction of data transfer such as "bulk out" or "interrupt
   in". The entire configuration may have up to sixteen endpoints in
   each direction, allocated as needed among all the interfaces.

-  Data transfer on USB is packetized; each endpoint has a maximum
   packet size. Drivers must often be aware of conventions such as
   flagging the end of bulk transfers using "short" (including zero
   length) packets.

-  The Linux USB API supports synchronous calls for control and bulk
   messages. It also supports asynchronous calls for all kinds of data
   transfer, using request structures called "URBs" (USB Request
   Blocks).

Accordingly, the USB Core API exposed to device drivers covers quite a
lot of territory. You'll probably need to consult the USB 3.0
specification, available online from www.usb.org at no cost, as well as
class or device specifications.

The only host-side drivers that actually touch hardware (reading/writing
registers, handling IRQs, and so on) are the HCDs. In theory, all HCDs
provide the same functionality through the same API. In practice, that's
becoming mostly true, but there are still differences that crop up
especially with fault handling on the less common controllers. Different
controllers don't necessarily report the same aspects of failures, and
recovery from faults (including software-induced ones like unlinking an
URB) isn't yet fully consistent. Device driver authors should make a
point of doing disconnect testing (while the device is active) with each
different host controller driver, to make sure drivers don't have bugs
of thei1r own as well as to make sure they aren't relying on some
HCD-specific behavior.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
