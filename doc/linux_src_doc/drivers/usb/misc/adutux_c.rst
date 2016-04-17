.. -*- coding: utf-8; mode: rst -*-

========
adutux.c
========


.. _`adu_abort_transfers`:

adu_abort_transfers
===================

.. c:function:: void adu_abort_transfers (struct adu_device *dev)

    :param struct adu_device \*dev:

        *undescribed*



.. _`adu_abort_transfers.description`:

Description
-----------

aborts transfers and frees associated data structures



.. _`adu_probe`:

adu_probe
=========

.. c:function:: int adu_probe (struct usb_interface *interface, const struct usb_device_id *id)

    :param struct usb_interface \*interface:

        *undescribed*

    :param const struct usb_device_id \*id:

        *undescribed*



.. _`adu_probe.description`:

Description
-----------


Called by the usb core when a new device is connected that it thinks
this driver might be interested in.



.. _`adu_disconnect`:

adu_disconnect
==============

.. c:function:: void adu_disconnect (struct usb_interface *interface)

    :param struct usb_interface \*interface:

        *undescribed*



.. _`adu_disconnect.description`:

Description
-----------


Called by the usb core when the device is removed from the system.

