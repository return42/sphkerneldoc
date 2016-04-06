
.. _API-struct-usb-composite-driver:

===========================
struct usb_composite_driver
===========================

*man struct usb_composite_driver(9)*

*4.6.0-rc1*

groups configurations into a gadget


Synopsis
========

.. code-block:: c

    struct usb_composite_driver {
      const char * name;
      const struct usb_device_descriptor * dev;
      struct usb_gadget_strings ** strings;
      enum usb_device_speed max_speed;
      unsigned needs_serial:1;
      int (* bind) (struct usb_composite_dev *cdev);
      int (* unbind) (struct usb_composite_dev *);
      void (* disconnect) (struct usb_composite_dev *);
      void (* suspend) (struct usb_composite_dev *);
      void (* resume) (struct usb_composite_dev *);
      struct usb_gadget_driver gadget_driver;
    };


Members
=======

name
    For diagnostics, identifies the driver.

dev
    Template descriptor for the device, including default device identifiers.

strings
    tables of strings, keyed by identifiers assigned during ``bind`` and language IDs provided in control requests. Note: The first entries are predefined. The first entry that may
    be used is USB_GADGET_FIRST_AVAIL_IDX

max_speed
    Highest speed the driver supports.

needs_serial
    set to 1 if the gadget needs userspace to provide a serial number. If one is not provided, warning will be printed.

bind
    (REQUIRED) Used to allocate resources that are shared across the whole device, such as string IDs, and add its configurations using ``usb_add_config``\ (). This may fail by
    returning a negative errno value; it should return zero on successful initialization.

unbind
    Reverses ``bind``; called as a side effect of unregistering this driver.

disconnect
    optional driver disconnect method

suspend
    Notifies when the host stops sending USB traffic, after function notifications

resume
    Notifies configuration when the host restarts USB traffic, before function notifications

gadget_driver
    Gadget driver controlling this driver


Description
===========

Devices default to reporting self powered operation. Devices which rely on bus powered operation should report this in their ``bind`` method.

Before returning from ``bind``, various fields in the template descriptor may be overridden. These include the idVendor/idProduct/bcdDevice values normally to bind the appropriate
host side driver, and the three strings (iManufacturer, iProduct, iSerialNumber) normally used to provide user meaningful device identifiers. (The strings will not be defined
unless they are defined in ``dev`` and ``strings``.) The correct ep0 maxpacket size is also reported, as defined by the underlying controller driver.
