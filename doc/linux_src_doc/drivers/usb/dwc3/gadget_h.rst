.. -*- coding: utf-8; mode: rst -*-

========
gadget.h
========


.. _`__drivers_usb_dwc3_gadget_h`:

__DRIVERS_USB_DWC3_GADGET_H
===========================

.. c:function:: __DRIVERS_USB_DWC3_GADGET_H ()

    DesignWare USB3 DRD Gadget Header



.. _`__drivers_usb_dwc3_gadget_h.description`:

Description
-----------


Copyright (C) 2010-2011 Texas Instruments Incorporated - http://www.ti.com



.. _`__drivers_usb_dwc3_gadget_h.authors`:

Authors
-------

Felipe Balbi <balbi\ ``ti``\ .com>,
Sebastian Andrzej Siewior <bigeasy\ ``linutronix``\ .de>



.. _`__drivers_usb_dwc3_gadget_h.this-program-is-free-software`:

This program is free software
-----------------------------

you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2  of
the License as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.



.. _`dwc3_gadget_ep_get_transfer_index`:

dwc3_gadget_ep_get_transfer_index
=================================

.. c:function:: u32 dwc3_gadget_ep_get_transfer_index (struct dwc3 *dwc, u8 number)

    Gets transfer index from HW

    :param struct dwc3 \*dwc:
        DesignWare USB3 Pointer

    :param u8 number:
        DWC endpoint number



.. _`dwc3_gadget_ep_get_transfer_index.description`:

Description
-----------

Caller should take care of locking

