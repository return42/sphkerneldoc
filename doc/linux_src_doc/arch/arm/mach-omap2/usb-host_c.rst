.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/usb-host.c

.. _`usbhs_add_regulator`:

usbhs_add_regulator
===================

.. c:function:: int usbhs_add_regulator(char *name, char *dev_id, char *dev_supply, int gpio, int polarity)

    Add a gpio based fixed voltage regulator device

    :param char \*name:
        name for the regulator

    :param char \*dev_id:
        device id of the device this regulator supplies power to

    :param char \*dev_supply:
        supply name that the device expects

    :param int gpio:
        GPIO number

    :param int polarity:
        1 - Active high, 0 - Active low

.. This file was automatic generated / don't edit.

