.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/misc/adutux.c

.. _`adu_abort_transfers`:

adu_abort_transfers
===================

.. c:function:: void adu_abort_transfers(struct adu_device *dev)

    aborts transfers and frees associated data structures

    :param dev:
        *undescribed*
    :type dev: struct adu_device \*

.. _`adu_probe`:

adu_probe
=========

.. c:function:: int adu_probe(struct usb_interface *interface, const struct usb_device_id *id)

    :param interface:
        *undescribed*
    :type interface: struct usb_interface \*

    :param id:
        *undescribed*
    :type id: const struct usb_device_id \*

.. _`adu_probe.description`:

Description
-----------

Called by the usb core when a new device is connected that it thinks
this driver might be interested in.

.. _`adu_disconnect`:

adu_disconnect
==============

.. c:function:: void adu_disconnect(struct usb_interface *interface)

    :param interface:
        *undescribed*
    :type interface: struct usb_interface \*

.. _`adu_disconnect.description`:

Description
-----------

Called by the usb core when the device is removed from the system.

.. This file was automatic generated / don't edit.

