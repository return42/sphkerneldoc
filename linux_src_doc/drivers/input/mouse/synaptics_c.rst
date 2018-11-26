.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/mouse/synaptics.c

.. _`synaptics_setup_intertouch`:

synaptics_setup_intertouch
==========================

.. c:function:: int synaptics_setup_intertouch(struct psmouse *psmouse, struct synaptics_device_info *info, bool leave_breadcrumbs)

    called once the PS/2 devices are enumerated and decides to instantiate a SMBus InterTouch device.

    :param psmouse:
        *undescribed*
    :type psmouse: struct psmouse \*

    :param info:
        *undescribed*
    :type info: struct synaptics_device_info \*

    :param leave_breadcrumbs:
        *undescribed*
    :type leave_breadcrumbs: bool

.. This file was automatic generated / don't edit.

