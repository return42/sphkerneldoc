.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/usbip/stub_tx.c

.. _`stub_complete`:

stub_complete
=============

.. c:function:: void stub_complete(struct urb *urb)

    completion handler of a usbip urb

    :param urb:
        pointer to the urb completed
    :type urb: struct urb \*

.. _`stub_complete.description`:

Description
-----------

When a urb has completed, the USB core driver calls this function mostly in
the interrupt context. To return the result of a urb, the completed urb is
linked to the pending list of returning.

.. This file was automatic generated / don't edit.

