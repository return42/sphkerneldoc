.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-usb-gadget:

=================
struct usb_gadget
=================

*man struct usb_gadget(9)*

*4.6.0-rc5*

represents a usb slave device


Synopsis
========

.. code-block:: c

    struct usb_gadget {
      struct work_struct work;
      struct usb_udc * udc;
      const struct usb_gadget_ops * ops;
      struct usb_ep * ep0;
      struct list_head ep_list;
      enum usb_device_speed speed;
      enum usb_device_speed max_speed;
      enum usb_device_state state;
      const char * name;
      struct device dev;
      unsigned out_epnum;
      unsigned in_epnum;
      struct usb_otg_caps * otg_caps;
      unsigned sg_supported:1;
      unsigned is_otg:1;
      unsigned is_a_peripheral:1;
      unsigned b_hnp_enable:1;
      unsigned a_hnp_support:1;
      unsigned a_alt_hnp_support:1;
      unsigned hnp_polling_support:1;
      unsigned host_request_flag:1;
      unsigned quirk_ep_out_aligned_size:1;
      unsigned is_selfpowered:1;
      unsigned deactivated:1;
      unsigned connected:1;
    };


Members
=======

work
    (internal use) Workqueue to be used for ``sysfs_notify``

udc
    struct usb_udc pointer for this gadget

ops
    Function pointers used to access hardware-specific operations.

ep0
    Endpoint zero, used when reading or writing responses to driver
    ``setup`` requests

ep_list
    List of other endpoints supported by the device.

speed
    Speed of current connection to USB host.

max_speed
    Maximal speed the UDC can handle. UDC must support this and all
    slower speeds.

state
    the state we are now (attached, suspended, configured, etc)

name
    Identifies the controller hardware type. Used in diagnostics and
    sometimes configuration.

dev
    Driver model state for this abstract device.

out_epnum
    last used out ep number

in_epnum
    last used in ep number

otg_caps
    OTG capabilities of this gadget.

sg_supported
    true if we can handle scatter-gather

is_otg
    True if the USB device port uses a Mini-AB jack, so that the gadget
    driver must provide a USB OTG descriptor.

is_a_peripheral
    False unless is_otg, the “A” end of a USB cable is in the Mini-AB
    jack, and HNP has been used to switch roles so that the “A” device
    currently acts as A-Peripheral, not A-Host.

b_hnp_enable
    OTG device feature flag, indicating that the A-Host enabled HNP
    support.

a_hnp_support
    OTG device feature flag, indicating that the A-Host supports HNP at
    this port.

a_alt_hnp_support
    OTG device feature flag, indicating that the A-Host only supports
    HNP on a different root port.

hnp_polling_support
    OTG device feature flag, indicating if the OTG device in peripheral
    mode can support HNP polling.

host_request_flag
    OTG device feature flag, indicating if A-Peripheral or B-Peripheral
    wants to take host role.

quirk_ep_out_aligned_size
    epout requires buffer size to be aligned to MaxPacketSize.

is_selfpowered
    if the gadget is self-powered.

deactivated
    True if gadget is deactivated - in deactivated state it cannot be
    connected.

connected
    True if gadget is connected.


Description
===========

Gadgets have a mostly-portable “gadget driver” implementing device
functions, handling all usb configurations and interfaces. Gadget
drivers talk to hardware-specific code indirectly, through ops vectors.
That insulates the gadget driver from hardware details, and packages the
hardware endpoints through generic i/o queues. The “usb_gadget” and
“usb_ep” interfaces provide that insulation from the hardware.

Except for the driver data, all fields in this structure are read-only
to the gadget driver. That driver data is part of the “driver model”
infrastructure in 2.6 (and later) kernels, and for earlier systems is
grouped in a similar structure that's not known to the rest of the
kernel.

Values of the three OTG device feature flags are updated before the
``setup`` call corresponding to USB_REQ_SET_CONFIGURATION, and before
driver ``suspend`` calls. They are valid only when is_otg, and when the
device is acting as a B-Peripheral (so is_a_peripheral is false).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
