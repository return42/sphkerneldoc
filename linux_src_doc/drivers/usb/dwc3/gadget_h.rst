.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc3/gadget.h

.. _`dwc3_gadget_ep_get_transfer_index`:

dwc3_gadget_ep_get_transfer_index
=================================

.. c:function:: u32 dwc3_gadget_ep_get_transfer_index(struct dwc3 *dwc, u8 number)

    Gets transfer index from HW

    :param struct dwc3 \*dwc:
        DesignWare USB3 Pointer

    :param u8 number:
        DWC endpoint number

.. _`dwc3_gadget_ep_get_transfer_index.description`:

Description
-----------

Caller should take care of locking

.. This file was automatic generated / don't edit.

