.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/pcwd_usb.c

.. _`usb_pcwd_delete`:

usb_pcwd_delete
===============

.. c:function:: void usb_pcwd_delete(struct usb_pcwd_private *usb_pcwd)

    :param struct usb_pcwd_private \*usb_pcwd:
        *undescribed*

.. _`usb_pcwd_probe`:

usb_pcwd_probe
==============

.. c:function:: int usb_pcwd_probe(struct usb_interface *interface, const struct usb_device_id *id)

    :param struct usb_interface \*interface:
        *undescribed*

    :param const struct usb_device_id \*id:
        *undescribed*

.. _`usb_pcwd_probe.description`:

Description
-----------

Called by the usb core when a new device is connected that it thinks
this driver might be interested in.

.. _`usb_pcwd_disconnect`:

usb_pcwd_disconnect
===================

.. c:function:: void usb_pcwd_disconnect(struct usb_interface *interface)

    :param struct usb_interface \*interface:
        *undescribed*

.. _`usb_pcwd_disconnect.description`:

Description
-----------

Called by the usb core when the device is removed from the system.

This routine guarantees that the driver will not submit any more urbs
by clearing dev->udev.

.. This file was automatic generated / don't edit.

