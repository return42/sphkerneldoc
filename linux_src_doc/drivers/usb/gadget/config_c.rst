.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/config.c

.. _`usb_descriptor_fillbuf`:

usb_descriptor_fillbuf
======================

.. c:function:: int usb_descriptor_fillbuf(void *buf, unsigned buflen, const struct usb_descriptor_header **src)

    fill buffer with descriptors

    :param buf:
        Buffer to be filled
    :type buf: void \*

    :param buflen:
        Size of buf
    :type buflen: unsigned

    :param src:
        Array of descriptor pointers, terminated by null pointer.
    :type src: const struct usb_descriptor_header \*\*

.. _`usb_descriptor_fillbuf.description`:

Description
-----------

Copies descriptors into the buffer, returning the length or a
negative error code if they can't all be copied.  Useful when
assembling descriptors for an associated set of interfaces used
as part of configuring a composite device; or in other cases where
sets of descriptors need to be marshaled.

.. _`usb_gadget_config_buf`:

usb_gadget_config_buf
=====================

.. c:function:: int usb_gadget_config_buf(const struct usb_config_descriptor *config, void *buf, unsigned length, const struct usb_descriptor_header **desc)

    builts a complete configuration descriptor

    :param config:
        Header for the descriptor, including characteristics such
        as power requirements and number of interfaces.
    :type config: const struct usb_config_descriptor \*

    :param buf:
        Buffer for the resulting configuration descriptor.
    :type buf: void \*

    :param length:
        Length of buffer.  If this is not big enough to hold the
        entire configuration descriptor, an error code will be returned.
    :type length: unsigned

    :param desc:
        Null-terminated vector of pointers to the descriptors (interface,
        endpoint, etc) defining all functions in this device configuration.
    :type desc: const struct usb_descriptor_header \*\*

.. _`usb_gadget_config_buf.description`:

Description
-----------

This copies descriptors into the response buffer, building a descriptor
for that configuration.  It returns the buffer length or a negative
status code.  The config.wTotalLength field is set to match the length
of the result, but other descriptor fields (including power usage and
interface count) must be set by the caller.

Gadget drivers could use this when constructing a config descriptor
in response to USB_REQ_GET_DESCRIPTOR.  They will need to patch the
resulting bDescriptorType value if USB_DT_OTHER_SPEED_CONFIG is needed.

.. _`usb_copy_descriptors`:

usb_copy_descriptors
====================

.. c:function:: struct usb_descriptor_header **usb_copy_descriptors(struct usb_descriptor_header **src)

    copy a vector of USB descriptors

    :param src:
        null-terminated vector to copy
    :type src: struct usb_descriptor_header \*\*

.. _`usb_copy_descriptors.context`:

Context
-------

initialization code, which may sleep

.. _`usb_copy_descriptors.description`:

Description
-----------

This makes a copy of a vector of USB descriptors.  Its primary use
is to support usb_function objects which can have multiple copies,
each needing different descriptors.  Functions may have static
tables of descriptors, which are used as templates and customized
with identifiers (for interfaces, strings, endpoints, and more)
as needed by a given function instance.

.. This file was automatic generated / don't edit.

