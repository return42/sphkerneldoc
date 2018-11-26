.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/core/ledtrig-usbport.c

.. _`usbport_trig_usb_dev_observed`:

usbport_trig_usb_dev_observed
=============================

.. c:function:: bool usbport_trig_usb_dev_observed(struct usbport_trig_data *usbport_data, struct usb_device *usb_dev)

    Check if dev is connected to observed port

    :param usbport_data:
        *undescribed*
    :type usbport_data: struct usbport_trig_data \*

    :param usb_dev:
        *undescribed*
    :type usb_dev: struct usb_device \*

.. _`usbport_trig_update_count`:

usbport_trig_update_count
=========================

.. c:function:: void usbport_trig_update_count(struct usbport_trig_data *usbport_data)

    Recalculate amount of connected matching devices

    :param usbport_data:
        *undescribed*
    :type usbport_data: struct usbport_trig_data \*

.. _`usbport_trig_port_observed`:

usbport_trig_port_observed
==========================

.. c:function:: bool usbport_trig_port_observed(struct usbport_trig_data *usbport_data, struct usb_device *usb_dev, int port1)

    Check if port should be observed

    :param usbport_data:
        *undescribed*
    :type usbport_data: struct usbport_trig_data \*

    :param usb_dev:
        *undescribed*
    :type usb_dev: struct usb_device \*

    :param port1:
        *undescribed*
    :type port1: int

.. This file was automatic generated / don't edit.

