.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/mouse/elantech.c

.. _`elantech_setup_smbus`:

elantech_setup_smbus
====================

.. c:function:: int elantech_setup_smbus(struct psmouse *psmouse, struct elantech_device_info *info, bool leave_breadcrumbs)

    called once the PS/2 devices are enumerated and decides to instantiate a SMBus InterTouch device.

    :param psmouse:
        *undescribed*
    :type psmouse: struct psmouse \*

    :param info:
        *undescribed*
    :type info: struct elantech_device_info \*

    :param leave_breadcrumbs:
        *undescribed*
    :type leave_breadcrumbs: bool

.. This file was automatic generated / don't edit.

