.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/atm/ueagle-atm.c

.. _`uea_send_modem_cmd`:

uea_send_modem_cmd
==================

.. c:function:: int uea_send_modem_cmd(struct usb_device *usb, u16 addr, u16 size, const u8 *buff)

    Send a command for pre-firmware devices.

    :param struct usb_device \*usb:
        *undescribed*

    :param u16 addr:
        *undescribed*

    :param u16 size:
        *undescribed*

    :param const u8 \*buff:
        *undescribed*

.. _`uea_load_firmware`:

uea_load_firmware
=================

.. c:function:: int uea_load_firmware(struct usb_device *usb, unsigned int ver)

    Load usb firmware for pre-firmware devices.

    :param struct usb_device \*usb:
        *undescribed*

    :param unsigned int ver:
        *undescribed*

.. This file was automatic generated / don't edit.

