.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/core/ledtrig-usbport.c

.. _`usbport_trig_usb_dev_observed`:

usbport_trig_usb_dev_observed
=============================

.. c:function:: bool usbport_trig_usb_dev_observed(struct usbport_trig_data *usbport_data, struct usb_device *usb_dev)

    Check if dev is connected to observed port

    :param struct usbport_trig_data \*usbport_data:
        *undescribed*

    :param struct usb_device \*usb_dev:
        *undescribed*

.. _`usbport_trig_update_count`:

usbport_trig_update_count
=========================

.. c:function:: void usbport_trig_update_count(struct usbport_trig_data *usbport_data)

    Recalculate amount of connected matching devices

    :param struct usbport_trig_data \*usbport_data:
        *undescribed*

.. _`usbport_trig_port_observed`:

usbport_trig_port_observed
==========================

.. c:function:: bool usbport_trig_port_observed(struct usbport_trig_data *usbport_data, struct usb_device *usb_dev, int port1)

    Check if port should be observed

    :param struct usbport_trig_data \*usbport_data:
        *undescribed*

    :param struct usb_device \*usb_dev:
        *undescribed*

    :param int port1:
        *undescribed*

.. This file was automatic generated / don't edit.

