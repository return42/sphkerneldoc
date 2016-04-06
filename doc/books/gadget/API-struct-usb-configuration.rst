
.. _API-struct-usb-configuration:

========================
struct usb_configuration
========================

*man struct usb_configuration(9)*

*4.6.0-rc1*

represents one gadget configuration


Synopsis
========

.. code-block:: c

    struct usb_configuration {
      const char * label;
      struct usb_gadget_strings ** strings;
      const struct usb_descriptor_header ** descriptors;
      void (* unbind) (struct usb_configuration *);
      int (* setup) (struct usb_configuration *,const struct usb_ctrlrequest *);
      u8 bConfigurationValue;
      u8 iConfiguration;
      u8 bmAttributes;
      u16 MaxPower;
      struct usb_composite_dev * cdev;
    };


Members
=======

label
    For diagnostics, describes the configuration.

strings
    Tables of strings, keyed by identifiers assigned during ``bind``\ () and by language IDs provided in control requests.

descriptors
    Table of descriptors preceding all function descriptors. Examples include OTG and vendor-specific descriptors.

unbind
    Reverses ``bind``; called as a side effect of unregistering the driver which added this configuration.

setup
    Used to delegate control requests that aren't handled by standard device infrastructure or directed at a specific interface.

bConfigurationValue
    Copied into configuration descriptor.

iConfiguration
    Copied into configuration descriptor.

bmAttributes
    Copied into configuration descriptor.

MaxPower
    Power consumtion in mA. Used to compute bMaxPower in the configuration descriptor after considering the bus speed.

cdev
    assigned by ``usb_add_config``\ () before calling ``bind``\ (); this is the device associated with this configuration.


Description
===========

Configurations are building blocks for gadget drivers structured around function drivers. Simple USB gadgets require only one function and one configuration, and handle dual-speed
hardware by always providing the same functionality. Slightly more complex gadgets may have more than one single-function configuration at a given speed; or have configurations
that only work at one speed.

Composite devices are, by definition, ones with configurations which include more than one function.

The lifecycle of a usb_configuration includes allocation, initialization of the fields described above, and calling ``usb_add_config`` () to set up internal data and bind it to a
specific device. The configuration's ``bind``\ () method is then used to initialize all the functions and then call ``usb_add_function``\ () for them.

Those functions would normally be independent of each other, but that's not mandatory. CDC WMC devices are an example where functions often depend on other functions, with some
functions subsidiary to others. Such interdependency may be managed in any way, so long as all of the descriptors complete by the time the composite driver returns from its
``bind`` routine.
