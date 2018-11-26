.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/misc/legousbtower.c

.. _`lego_usb_tower_debug_data`:

lego_usb_tower_debug_data
=========================

.. c:function:: void lego_usb_tower_debug_data(struct device *dev, const char *function, int size, const unsigned char *data)

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param function:
        *undescribed*
    :type function: const char \*

    :param size:
        *undescribed*
    :type size: int

    :param data:
        *undescribed*
    :type data: const unsigned char \*

.. _`tower_delete`:

tower_delete
============

.. c:function:: void tower_delete(struct lego_usb_tower *dev)

    :param dev:
        *undescribed*
    :type dev: struct lego_usb_tower \*

.. _`tower_open`:

tower_open
==========

.. c:function:: int tower_open(struct inode *inode, struct file *file)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param file:
        *undescribed*
    :type file: struct file \*

.. _`tower_release`:

tower_release
=============

.. c:function:: int tower_release(struct inode *inode, struct file *file)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param file:
        *undescribed*
    :type file: struct file \*

.. _`tower_abort_transfers`:

tower_abort_transfers
=====================

.. c:function:: void tower_abort_transfers(struct lego_usb_tower *dev)

    aborts transfers and frees associated data structures

    :param dev:
        *undescribed*
    :type dev: struct lego_usb_tower \*

.. _`tower_check_for_read_packet`:

tower_check_for_read_packet
===========================

.. c:function:: void tower_check_for_read_packet(struct lego_usb_tower *dev)

    :param dev:
        *undescribed*
    :type dev: struct lego_usb_tower \*

.. _`tower_check_for_read_packet.description`:

Description
-----------

To get correct semantics for signals and non-blocking I/O
with packetizing we pretend not to see any data in the read buffer
until it has been there unchanged for at least
dev->packet_timeout_jiffies, or until the buffer is full.

.. _`tower_poll`:

tower_poll
==========

.. c:function:: __poll_t tower_poll(struct file *file, poll_table *wait)

    :param file:
        *undescribed*
    :type file: struct file \*

    :param wait:
        *undescribed*
    :type wait: poll_table \*

.. _`tower_llseek`:

tower_llseek
============

.. c:function:: loff_t tower_llseek(struct file *file, loff_t off, int whence)

    :param file:
        *undescribed*
    :type file: struct file \*

    :param off:
        *undescribed*
    :type off: loff_t

    :param whence:
        *undescribed*
    :type whence: int

.. _`tower_read`:

tower_read
==========

.. c:function:: ssize_t tower_read(struct file *file, char __user *buffer, size_t count, loff_t *ppos)

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

.. _`tower_write`:

tower_write
===========

.. c:function:: ssize_t tower_write(struct file *file, const char __user *buffer, size_t count, loff_t *ppos)

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

.. _`tower_interrupt_in_callback`:

tower_interrupt_in_callback
===========================

.. c:function:: void tower_interrupt_in_callback(struct urb *urb)

    :param urb:
        *undescribed*
    :type urb: struct urb \*

.. _`tower_interrupt_out_callback`:

tower_interrupt_out_callback
============================

.. c:function:: void tower_interrupt_out_callback(struct urb *urb)

    :param urb:
        *undescribed*
    :type urb: struct urb \*

.. _`tower_probe`:

tower_probe
===========

.. c:function:: int tower_probe(struct usb_interface *interface, const struct usb_device_id *id)

    :param interface:
        *undescribed*
    :type interface: struct usb_interface \*

    :param id:
        *undescribed*
    :type id: const struct usb_device_id \*

.. _`tower_probe.description`:

Description
-----------

Called by the usb core when a new device is connected that it thinks
this driver might be interested in.

.. _`tower_disconnect`:

tower_disconnect
================

.. c:function:: void tower_disconnect(struct usb_interface *interface)

    :param interface:
        *undescribed*
    :type interface: struct usb_interface \*

.. _`tower_disconnect.description`:

Description
-----------

Called by the usb core when the device is removed from the system.

.. This file was automatic generated / don't edit.

