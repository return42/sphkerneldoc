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

    :param dev:
        *undescribed*
    :type dev: struct ld_usb \*

.. _`ld_usb_delete`:

ld_usb_delete
=============

.. c:function:: void ld_usb_delete(struct ld_usb *dev)

    :param dev:
        *undescribed*
    :type dev: struct ld_usb \*

.. _`ld_usb_interrupt_in_callback`:

ld_usb_interrupt_in_callback
============================

.. c:function:: void ld_usb_interrupt_in_callback(struct urb *urb)

    :param urb:
        *undescribed*
    :type urb: struct urb \*

.. _`ld_usb_interrupt_out_callback`:

ld_usb_interrupt_out_callback
=============================

.. c:function:: void ld_usb_interrupt_out_callback(struct urb *urb)

    :param urb:
        *undescribed*
    :type urb: struct urb \*

.. _`ld_usb_open`:

ld_usb_open
===========

.. c:function:: int ld_usb_open(struct inode *inode, struct file *file)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param file:
        *undescribed*
    :type file: struct file \*

.. _`ld_usb_release`:

ld_usb_release
==============

.. c:function:: int ld_usb_release(struct inode *inode, struct file *file)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param file:
        *undescribed*
    :type file: struct file \*

.. _`ld_usb_poll`:

ld_usb_poll
===========

.. c:function:: __poll_t ld_usb_poll(struct file *file, poll_table *wait)

    :param file:
        *undescribed*
    :type file: struct file \*

    :param wait:
        *undescribed*
    :type wait: poll_table \*

.. _`ld_usb_read`:

ld_usb_read
===========

.. c:function:: ssize_t ld_usb_read(struct file *file, char __user *buffer, size_t count, loff_t *ppos)

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buffer:
        *undescribed*
    :type buffer: char __user \*

    :param count:
        *undescribed*
    :type count: size_t

    :param ppos:
        *undescribed*
    :type ppos: loff_t \*

.. _`ld_usb_write`:

ld_usb_write
============

.. c:function:: ssize_t ld_usb_write(struct file *file, const char __user *buffer, size_t count, loff_t *ppos)

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buffer:
        *undescribed*
    :type buffer: const char __user \*

    :param count:
        *undescribed*
    :type count: size_t

    :param ppos:
        *undescribed*
    :type ppos: loff_t \*

.. _`ld_usb_probe`:

ld_usb_probe
============

.. c:function:: int ld_usb_probe(struct usb_interface *intf, const struct usb_device_id *id)

    :param intf:
        *undescribed*
    :type intf: struct usb_interface \*

    :param id:
        *undescribed*
    :type id: const struct usb_device_id \*

.. _`ld_usb_probe.description`:

Description
-----------

Called by the usb core when a new device is connected that it thinks
this driver might be interested in.

.. _`ld_usb_disconnect`:

ld_usb_disconnect
=================

.. c:function:: void ld_usb_disconnect(struct usb_interface *intf)

    :param intf:
        *undescribed*
    :type intf: struct usb_interface \*

.. _`ld_usb_disconnect.description`:

Description
-----------

Called by the usb core when the device is removed from the system.

.. This file was automatic generated / don't edit.

