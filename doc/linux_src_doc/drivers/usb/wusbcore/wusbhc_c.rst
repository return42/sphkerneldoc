.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/wusbcore/wusbhc.c

.. _`usbhc_dev_to_wusbhc`:

usbhc_dev_to_wusbhc
===================

.. c:function:: struct wusbhc *usbhc_dev_to_wusbhc(struct device *dev)

    :param struct device \*dev:
        *undescribed*

.. _`usbhc_dev_to_wusbhc.description`:

Description
-----------

WARNING! Apply only if \ ``dev``\  is that of a
wusbhc.usb_hcd.self->class_dev; otherwise, you loose.

.. _`wusbhc_giveback_urb`:

wusbhc_giveback_urb
===================

.. c:function:: void wusbhc_giveback_urb(struct wusbhc *wusbhc, struct urb *urb, int status)

    return an URB to the USB core

    :param struct wusbhc \*wusbhc:
        the host controller the URB is from.

    :param struct urb \*urb:
        the URB.

    :param int status:
        the URB's status.

.. _`wusbhc_giveback_urb.description`:

Description
-----------

Return an URB to the USB core doing some additional WUSB specific
processing.

- After a successful transfer, update the trust timeout timestamp
for the WUSB device.

- [WUSB] sections 4.13 and 7.5.1 specify the stop retransmission
condition for the WCONNECTACK_IE is that the host has observed
the associated device responding to a control transfer.

.. _`wusbhc_reset_all`:

wusbhc_reset_all
================

.. c:function:: void wusbhc_reset_all(struct wusbhc *wusbhc)

    reset the HC hardware

    :param struct wusbhc \*wusbhc:
        the host controller to reset.

.. _`wusbhc_reset_all.description`:

Description
-----------

Request a full hardware reset of the chip.  This will also reset
the radio controller and any other PALs.

.. This file was automatic generated / don't edit.

