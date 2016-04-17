.. -*- coding: utf-8; mode: rst -*-

==============
renesas_usb3.c
==============


.. _`usb3_handle_standard_request`:

usb3_handle_standard_request
============================

.. c:function:: bool usb3_handle_standard_request (struct renesas_usb3 *usb3, struct usb_ctrlrequest *ctrl)

    handle some standard requests

    :param struct renesas_usb3 \*usb3:
        the renesas_usb3 pointer

    :param struct usb_ctrlrequest \*ctrl:
        a pointer of setup data



.. _`usb3_handle_standard_request.description`:

Description
-----------

Returns true if this function handled a standard request

