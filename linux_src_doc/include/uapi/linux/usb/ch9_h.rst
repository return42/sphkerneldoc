.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/usb/ch9.h

.. _`usb_ctrlrequest`:

struct usb_ctrlrequest
======================

.. c:type:: struct usb_ctrlrequest

    SETUP data for a USB device control request

.. _`usb_ctrlrequest.definition`:

Definition
----------

.. code-block:: c

    struct usb_ctrlrequest {
        __u8 bRequestType;
        __u8 bRequest;
        __le16 wValue;
        __le16 wIndex;
        __le16 wLength;
    }

.. _`usb_ctrlrequest.members`:

Members
-------

bRequestType
    matches the USB bmRequestType field

bRequest
    matches the USB bRequest field

wValue
    matches the USB wValue field (le16 byte order)

wIndex
    matches the USB wIndex field (le16 byte order)

wLength
    matches the USB wLength field (le16 byte order)

.. _`usb_ctrlrequest.description`:

Description
-----------

This structure is used to send control requests to a USB device.  It matches
the different fields of the USB 2.0 Spec section 9.3, table 9-2.  See the
USB spec for a fuller description of the different fields, and what they are
used for.

Note that the driver for any interface can issue control requests.
For most devices, interfaces don't coordinate with each other, so
such requests may be made at any time.

.. _`usb_endpoint_num`:

usb_endpoint_num
================

.. c:function:: int usb_endpoint_num(const struct usb_endpoint_descriptor *epd)

    get the endpoint's number

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_num.description`:

Description
-----------

Returns \ ``epd``\ 's number: 0 to 15.

.. _`usb_endpoint_type`:

usb_endpoint_type
=================

.. c:function:: int usb_endpoint_type(const struct usb_endpoint_descriptor *epd)

    get the endpoint's transfer type

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_type.description`:

Description
-----------

Returns one of USB_ENDPOINT_XFER_{CONTROL, ISOC, BULK, INT} according
to \ ``epd``\ 's transfer type.

.. _`usb_endpoint_dir_in`:

usb_endpoint_dir_in
===================

.. c:function:: int usb_endpoint_dir_in(const struct usb_endpoint_descriptor *epd)

    check if the endpoint has IN direction

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_dir_in.description`:

Description
-----------

Returns true if the endpoint is of type IN, otherwise it returns false.

.. _`usb_endpoint_dir_out`:

usb_endpoint_dir_out
====================

.. c:function:: int usb_endpoint_dir_out(const struct usb_endpoint_descriptor *epd)

    check if the endpoint has OUT direction

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_dir_out.description`:

Description
-----------

Returns true if the endpoint is of type OUT, otherwise it returns false.

.. _`usb_endpoint_xfer_bulk`:

usb_endpoint_xfer_bulk
======================

.. c:function:: int usb_endpoint_xfer_bulk(const struct usb_endpoint_descriptor *epd)

    check if the endpoint has bulk transfer type

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_xfer_bulk.description`:

Description
-----------

Returns true if the endpoint is of type bulk, otherwise it returns false.

.. _`usb_endpoint_xfer_control`:

usb_endpoint_xfer_control
=========================

.. c:function:: int usb_endpoint_xfer_control(const struct usb_endpoint_descriptor *epd)

    check if the endpoint has control transfer type

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_xfer_control.description`:

Description
-----------

Returns true if the endpoint is of type control, otherwise it returns false.

.. _`usb_endpoint_xfer_int`:

usb_endpoint_xfer_int
=====================

.. c:function:: int usb_endpoint_xfer_int(const struct usb_endpoint_descriptor *epd)

    check if the endpoint has interrupt transfer type

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_xfer_int.description`:

Description
-----------

Returns true if the endpoint is of type interrupt, otherwise it returns
false.

.. _`usb_endpoint_xfer_isoc`:

usb_endpoint_xfer_isoc
======================

.. c:function:: int usb_endpoint_xfer_isoc(const struct usb_endpoint_descriptor *epd)

    check if the endpoint has isochronous transfer type

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_xfer_isoc.description`:

Description
-----------

Returns true if the endpoint is of type isochronous, otherwise it returns
false.

.. _`usb_endpoint_is_bulk_in`:

usb_endpoint_is_bulk_in
=======================

.. c:function:: int usb_endpoint_is_bulk_in(const struct usb_endpoint_descriptor *epd)

    check if the endpoint is bulk IN

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_is_bulk_in.description`:

Description
-----------

Returns true if the endpoint has bulk transfer type and IN direction,
otherwise it returns false.

.. _`usb_endpoint_is_bulk_out`:

usb_endpoint_is_bulk_out
========================

.. c:function:: int usb_endpoint_is_bulk_out(const struct usb_endpoint_descriptor *epd)

    check if the endpoint is bulk OUT

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_is_bulk_out.description`:

Description
-----------

Returns true if the endpoint has bulk transfer type and OUT direction,
otherwise it returns false.

.. _`usb_endpoint_is_int_in`:

usb_endpoint_is_int_in
======================

.. c:function:: int usb_endpoint_is_int_in(const struct usb_endpoint_descriptor *epd)

    check if the endpoint is interrupt IN

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_is_int_in.description`:

Description
-----------

Returns true if the endpoint has interrupt transfer type and IN direction,
otherwise it returns false.

.. _`usb_endpoint_is_int_out`:

usb_endpoint_is_int_out
=======================

.. c:function:: int usb_endpoint_is_int_out(const struct usb_endpoint_descriptor *epd)

    check if the endpoint is interrupt OUT

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_is_int_out.description`:

Description
-----------

Returns true if the endpoint has interrupt transfer type and OUT direction,
otherwise it returns false.

.. _`usb_endpoint_is_isoc_in`:

usb_endpoint_is_isoc_in
=======================

.. c:function:: int usb_endpoint_is_isoc_in(const struct usb_endpoint_descriptor *epd)

    check if the endpoint is isochronous IN

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_is_isoc_in.description`:

Description
-----------

Returns true if the endpoint has isochronous transfer type and IN direction,
otherwise it returns false.

.. _`usb_endpoint_is_isoc_out`:

usb_endpoint_is_isoc_out
========================

.. c:function:: int usb_endpoint_is_isoc_out(const struct usb_endpoint_descriptor *epd)

    check if the endpoint is isochronous OUT

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_is_isoc_out.description`:

Description
-----------

Returns true if the endpoint has isochronous transfer type and OUT direction,
otherwise it returns false.

.. _`usb_endpoint_maxp`:

usb_endpoint_maxp
=================

.. c:function:: int usb_endpoint_maxp(const struct usb_endpoint_descriptor *epd)

    get endpoint's max packet size

    :param const struct usb_endpoint_descriptor \*epd:
        endpoint to be checked

.. _`usb_endpoint_maxp.description`:

Description
-----------

Returns \ ``epd``\ 's max packet

.. This file was automatic generated / don't edit.

