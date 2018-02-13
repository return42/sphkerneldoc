.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/misc/legousbtower.c

.. _`lego_usb_tower_debug_data`:

lego_usb_tower_debug_data
=========================

.. c:function:: void lego_usb_tower_debug_data(struct device *dev, const char *function, int size, const unsigned char *data)

    :param struct device \*dev:
        *undescribed*

    :param const char \*function:
        *undescribed*

    :param int size:
        *undescribed*

    :param const unsigned char \*data:
        *undescribed*

.. _`tower_delete`:

tower_delete
============

.. c:function:: void tower_delete(struct lego_usb_tower *dev)

    :param struct lego_usb_tower \*dev:
        *undescribed*

.. _`tower_open`:

tower_open
==========

.. c:function:: int tower_open(struct inode *inode, struct file *file)

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*file:
        *undescribed*

.. _`tower_release`:

tower_release
=============

.. c:function:: int tower_release(struct inode *inode, struct file *file)

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*file:
        *undescribed*

.. _`tower_abort_transfers`:

tower_abort_transfers
=====================

.. c:function:: void tower_abort_transfers(struct lego_usb_tower *dev)

    aborts transfers and frees associated data structures

    :param struct lego_usb_tower \*dev:
        *undescribed*

.. _`tower_check_for_read_packet`:

tower_check_for_read_packet
===========================

.. c:function:: void tower_check_for_read_packet(struct lego_usb_tower *dev)

    :param struct lego_usb_tower \*dev:
        *undescribed*

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

    :param struct file \*file:
        *undescribed*

    :param poll_table \*wait:
        *undescribed*

.. _`tower_llseek`:

tower_llseek
============

.. c:function:: loff_t tower_llseek(struct file *file, loff_t off, int whence)

    :param struct file \*file:
        *undescribed*

    :param loff_t off:
        *undescribed*

    :param int whence:
        *undescribed*

.. _`tower_read`:

tower_read
==========

.. c:function:: ssize_t tower_read(struct file *file, char __user *buffer, size_t count, loff_t *ppos)

    :param struct file \*file:
        *undescribed*

    :param char __user \*buffer:
        *undescribed*

    :param size_t count:
        *undescribed*

    :param loff_t \*ppos:
        *undescribed*

.. _`tower_write`:

tower_write
===========

.. c:function:: ssize_t tower_write(struct file *file, const char __user *buffer, size_t count, loff_t *ppos)

    :param struct file \*file:
        *undescribed*

    :param const char __user \*buffer:
        *undescribed*

    :param size_t count:
        *undescribed*

    :param loff_t \*ppos:
        *undescribed*

.. _`tower_interrupt_in_callback`:

tower_interrupt_in_callback
===========================

.. c:function:: void tower_interrupt_in_callback(struct urb *urb)

    :param struct urb \*urb:
        *undescribed*

.. _`tower_interrupt_out_callback`:

tower_interrupt_out_callback
============================

.. c:function:: void tower_interrupt_out_callback(struct urb *urb)

    :param struct urb \*urb:
        *undescribed*

.. _`tower_probe`:

tower_probe
===========

.. c:function:: int tower_probe(struct usb_interface *interface, const struct usb_device_id *id)

    :param struct usb_interface \*interface:
        *undescribed*

    :param const struct usb_device_id \*id:
        *undescribed*

.. _`tower_probe.description`:

Description
-----------

Called by the usb core when a new device is connected that it thinks
this driver might be interested in.

.. _`tower_disconnect`:

tower_disconnect
================

.. c:function:: void tower_disconnect(struct usb_interface *interface)

    :param struct usb_interface \*interface:
        *undescribed*

.. _`tower_disconnect.description`:

Description
-----------

Called by the usb core when the device is removed from the system.

.. This file was automatic generated / don't edit.

