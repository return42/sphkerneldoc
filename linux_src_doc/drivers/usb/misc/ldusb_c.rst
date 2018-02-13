.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/misc/ldusb.c

.. _`usb_vendor_id_ld`:

USB_VENDOR_ID_LD
================

.. c:function::  USB_VENDOR_ID_LD()

    like LD Didactic's USB devices. LD Didactic's USB devices are HID devices which do not use HID report definitons (they use raw interrupt in and our reports only for communication).

.. _`usb_vendor_id_ld.description`:

Description
-----------

This driver uses a ring buffer for time critical reading of
interrupt in reports and provides read and write methods for
raw interrupt reports (similar to the Windows HID driver).
Devices based on the book USB COMPLETE by Jan Axelson may need
such a compatibility to the Windows HID driver.

Copyright (C) 2005 Michael Hund <mhund@ld-didactic.de>

Derived from Lego USB Tower driver
Copyright (C) 2003 David Glance <advidgsf@sourceforge.net>
2001-2004 Juergen Stuber <starblue@users.sourceforge.net>

.. _`ld_usb_abort_transfers`:

ld_usb_abort_transfers
======================

.. c:function:: void ld_usb_abort_transfers(struct ld_usb *dev)

    aborts transfers and frees associated data structures

    :param struct ld_usb \*dev:
        *undescribed*

.. _`ld_usb_delete`:

ld_usb_delete
=============

.. c:function:: void ld_usb_delete(struct ld_usb *dev)

    :param struct ld_usb \*dev:
        *undescribed*

.. _`ld_usb_interrupt_in_callback`:

ld_usb_interrupt_in_callback
============================

.. c:function:: void ld_usb_interrupt_in_callback(struct urb *urb)

    :param struct urb \*urb:
        *undescribed*

.. _`ld_usb_interrupt_out_callback`:

ld_usb_interrupt_out_callback
=============================

.. c:function:: void ld_usb_interrupt_out_callback(struct urb *urb)

    :param struct urb \*urb:
        *undescribed*

.. _`ld_usb_open`:

ld_usb_open
===========

.. c:function:: int ld_usb_open(struct inode *inode, struct file *file)

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*file:
        *undescribed*

.. _`ld_usb_release`:

ld_usb_release
==============

.. c:function:: int ld_usb_release(struct inode *inode, struct file *file)

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*file:
        *undescribed*

.. _`ld_usb_poll`:

ld_usb_poll
===========

.. c:function:: __poll_t ld_usb_poll(struct file *file, poll_table *wait)

    :param struct file \*file:
        *undescribed*

    :param poll_table \*wait:
        *undescribed*

.. _`ld_usb_read`:

ld_usb_read
===========

.. c:function:: ssize_t ld_usb_read(struct file *file, char __user *buffer, size_t count, loff_t *ppos)

    :param struct file \*file:
        *undescribed*

    :param char __user \*buffer:
        *undescribed*

    :param size_t count:
        *undescribed*

    :param loff_t \*ppos:
        *undescribed*

.. _`ld_usb_write`:

ld_usb_write
============

.. c:function:: ssize_t ld_usb_write(struct file *file, const char __user *buffer, size_t count, loff_t *ppos)

    :param struct file \*file:
        *undescribed*

    :param const char __user \*buffer:
        *undescribed*

    :param size_t count:
        *undescribed*

    :param loff_t \*ppos:
        *undescribed*

.. _`ld_usb_probe`:

ld_usb_probe
============

.. c:function:: int ld_usb_probe(struct usb_interface *intf, const struct usb_device_id *id)

    :param struct usb_interface \*intf:
        *undescribed*

    :param const struct usb_device_id \*id:
        *undescribed*

.. _`ld_usb_probe.description`:

Description
-----------

Called by the usb core when a new device is connected that it thinks
this driver might be interested in.

.. _`ld_usb_disconnect`:

ld_usb_disconnect
=================

.. c:function:: void ld_usb_disconnect(struct usb_interface *intf)

    :param struct usb_interface \*intf:
        *undescribed*

.. _`ld_usb_disconnect.description`:

Description
-----------

Called by the usb core when the device is removed from the system.

.. This file was automatic generated / don't edit.

