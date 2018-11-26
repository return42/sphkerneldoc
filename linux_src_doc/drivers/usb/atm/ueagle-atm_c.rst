.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/atm/ueagle-atm.c

.. _`uea_send_modem_cmd`:

uea_send_modem_cmd
==================

.. c:function:: int uea_send_modem_cmd(struct usb_device *usb, u16 addr, u16 size, const u8 *buff)

    Send a command for pre-firmware devices.

    :param usb:
        *undescribed*
    :type usb: struct usb_device \*

    :param addr:
        *undescribed*
    :type addr: u16

    :param size:
        *undescribed*
    :type size: u16

    :param buff:
        *undescribed*
    :type buff: const u8 \*

.. _`uea_load_firmware`:

uea_load_firmware
=================

.. c:function:: int uea_load_firmware(struct usb_device *usb, unsigned int ver)

    Load usb firmware for pre-firmware devices.

    :param usb:
        *undescribed*
    :type usb: struct usb_device \*

    :param ver:
        *undescribed*
    :type ver: unsigned int

.. This file was automatic generated / don't edit.

