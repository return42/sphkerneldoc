
.. _API-struct-usb-host-config:

======================
struct usb_host_config
======================

*man struct usb_host_config(9)*

*4.6.0-rc1*

representation of a device's configuration


Synopsis
========

.. code-block:: c

    struct usb_host_config {
      struct usb_config_descriptor desc;
      char * string;
      struct usb_interface_assoc_descriptor * intf_assoc[USB_MAXIADS];
      struct usb_interface * interface[USB_MAXINTERFACES];
      struct usb_interface_cache * intf_cache[USB_MAXINTERFACES];
      unsigned char * extra;
      int extralen;
    };


Members
=======

desc
    the device's configuration descriptor.

string
    pointer to the cached version of the iConfiguration string, if present for this configuration.

intf_assoc[USB_MAXIADS]
    list of any interface association descriptors in this config

interface[USB_MAXINTERFACES]
    array of pointers to usb_interface structures, one for each interface in the configuration. The number of interfaces is stored in desc.bNumInterfaces. These pointers are valid
    only while the the configuration is active.

intf_cache[USB_MAXINTERFACES]
    array of pointers to usb_interface_cache structures, one for each interface in the configuration. These structures exist for the entire life of the device.

extra
    pointer to buffer containing all extra descriptors associated with this configuration (those preceding the first interface descriptor).

extralen
    length of the extra descriptors buffer.


Description
===========

USB devices may have multiple configurations, but only one can be active at any time. Each encapsulates a different operational environment; for example, a dual-speed device would
have separate configurations for full-speed and high-speed operation. The number of configurations available is stored in the device descriptor as bNumConfigurations.

A configuration can contain multiple interfaces. Each corresponds to a different function of the USB device, and all are available whenever the configuration is active. The USB
standard says that interfaces are supposed to be numbered from 0 to desc.bNumInterfaces-1, but a lot of devices get this wrong. In addition, the interface array is not guaranteed
to be sorted in numerical order. Use ``usb_ifnum_to_if`` to look up an interface entry based on its number.

Device drivers should not attempt to activate configurations. The choice of which configuration to install is a policy decision based on such considerations as available power,
functionality provided, and the user's desires (expressed through userspace tools). However, drivers can call ``usb_reset_configuration`` to reinitialize the current configuration
and all its interfaces.
