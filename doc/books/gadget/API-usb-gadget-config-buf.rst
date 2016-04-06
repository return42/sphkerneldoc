
.. _API-usb-gadget-config-buf:

=====================
usb_gadget_config_buf
=====================

*man usb_gadget_config_buf(9)*

*4.6.0-rc1*

builts a complete configuration descriptor


Synopsis
========

.. c:function:: int usb_gadget_config_buf( const struct usb_config_descriptor * config, void * buf, unsigned length, const struct usb_descriptor_header ** desc )

Arguments
=========

``config``
    Header for the descriptor, including characteristics such as power requirements and number of interfaces.

``buf``
    Buffer for the resulting configuration descriptor.

``length``
    Length of buffer. If this is not big enough to hold the entire configuration descriptor, an error code will be returned.

``desc``
    Null-terminated vector of pointers to the descriptors (interface, endpoint, etc) defining all functions in this device configuration.


Description
===========

This copies descriptors into the response buffer, building a descriptor for that configuration. It returns the buffer length or a negative status code. The config.wTotalLength
field is set to match the length of the result, but other descriptor fields (including power usage and interface count) must be set by the caller.

Gadget drivers could use this when constructing a config descriptor in response to USB_REQ_GET_DESCRIPTOR. They will need to patch the resulting bDescriptorType value if
USB_DT_OTHER_SPEED_CONFIG is needed.
