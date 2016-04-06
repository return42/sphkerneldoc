
.. _API-struct-usb-gadget-driver:

========================
struct usb_gadget_driver
========================

*man struct usb_gadget_driver(9)*

*4.6.0-rc1*

driver for usb 'slave' devices


Synopsis
========

.. code-block:: c

    struct usb_gadget_driver {
      char * function;
      enum usb_device_speed max_speed;
      int (* bind) (struct usb_gadget *gadget,struct usb_gadget_driver *driver);
      void (* unbind) (struct usb_gadget *);
      int (* setup) (struct usb_gadget *,const struct usb_ctrlrequest *);
      void (* disconnect) (struct usb_gadget *);
      void (* suspend) (struct usb_gadget *);
      void (* resume) (struct usb_gadget *);
      void (* reset) (struct usb_gadget *);
      struct device_driver driver;
      char * udc_name;
      struct list_head pending;
    };


Members
=======

function
    String describing the gadget's function

max_speed
    Highest speed the driver handles.

bind
    the driver's bind callback

unbind
    Invoked when the driver is unbound from a gadget, usually from rmmod (after a disconnect is reported). Called in a context that permits sleeping.

setup
    Invoked for ep0 control requests that aren't handled by the hardware level driver. Most calls must be handled by the gadget driver, including descriptor and configuration
    management. The 16 bit members of the setup data are in USB byte order. Called in_interrupt; this may not sleep. Driver queues a response to ep0, or returns negative to stall.

disconnect
    Invoked after all transfers have been stopped, when the host is disconnected. May be called in_interrupt; this may not sleep. Some devices can't detect disconnect, so this
    might not be called except as part of controller shutdown.

suspend
    Invoked on USB suspend. May be called in_interrupt.

resume
    Invoked on USB resume. May be called in_interrupt.

reset
    Invoked on USB bus reset. It is mandatory for all gadget drivers and should be called in_interrupt.

driver
    Driver model state for this driver.

udc_name
    A name of UDC this driver should be bound to. If udc_name is NULL, this driver will be bound to any available UDC.

pending
    UDC core private data used for deferred probe of this driver.


Description
===========

Devices are disabled till a gadget driver successfully ``bind``\ s, which means the driver will handle ``setup`` requests needed to enumerate (and meet “chapter 9” requirements)
then do some useful work.

If gadget->is_otg is true, the gadget driver must provide an OTG descriptor during enumeration, or else fail the ``bind`` call. In such cases, no USB traffic may flow until both
``bind`` returns without having called ``usb_gadget_disconnect``, and the USB host stack has initialized.

Drivers use hardware-specific knowledge to configure the usb hardware. endpoint addressing is only one of several hardware characteristics that are in descriptors the ep0
implementation returns from ``setup`` calls.

Except for ep0 implementation, most driver code shouldn't need change to run on top of different usb controllers. It'll use endpoints set up by that ep0 implementation.

The usb controller driver handles a few standard usb requests. Those include set_address, and feature flags for devices, interfaces, and endpoints (the get_status, set_feature,
and clear_feature requests).

Accordingly, the driver's ``setup`` callback must always implement all get_descriptor requests, returning at least a device descriptor and a configuration descriptor. Drivers must
make sure the endpoint descriptors match any hardware constraints. Some hardware also constrains other descriptors. (The pxa250 allows only configurations 1, 2, or 3).

The driver's ``setup`` callback must also implement set_configuration, and should also implement set_interface, get_configuration, and get_interface. Setting a configuration
(or interface) is where endpoints should be activated or (config 0) shut down.

(Note that only the default control endpoint is supported. Neither hosts nor devices generally support control traffic except to ep0.)

Most devices will ignore USB suspend/resume operations, and so will not provide those callbacks. However, some may need to change modes when the host is not longer directing those
activities. For example, local controls (buttons, dials, etc) may need to be re-enabled since the (remote) host can't do that any longer; or an error state might be cleared, to
make the device behave identically whether or not power is maintained.
