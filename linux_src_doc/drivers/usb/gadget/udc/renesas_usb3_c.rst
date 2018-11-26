.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/udc/renesas_usb3.c

.. _`usb3_handle_standard_request`:

usb3_handle_standard_request
============================

.. c:function:: bool usb3_handle_standard_request(struct renesas_usb3 *usb3, struct usb_ctrlrequest *ctrl)

    handle some standard requests

    :param usb3:
        the renesas_usb3 pointer
    :type usb3: struct renesas_usb3 \*

    :param ctrl:
        a pointer of setup data
    :type ctrl: struct usb_ctrlrequest \*

.. _`usb3_handle_standard_request.description`:

Description
-----------

Returns true if this function handled a standard request

.. This file was automatic generated / don't edit.

