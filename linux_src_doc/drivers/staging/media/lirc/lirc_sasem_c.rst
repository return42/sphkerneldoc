.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/media/lirc/lirc_sasem.c

.. _`vfd_open`:

vfd_open
========

.. c:function:: int vfd_open(struct inode *inode, struct file *file)

    is opened by the application.

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*file:
        *undescribed*

.. _`vfd_ioctl`:

vfd_ioctl
=========

.. c:function:: long vfd_ioctl(struct file *file, unsigned cmd, unsigned long arg)

    is closed by the application.

    :param struct file \*file:
        *undescribed*

    :param unsigned cmd:
        *undescribed*

    :param unsigned long arg:
        *undescribed*

.. _`vfd_close`:

vfd_close
=========

.. c:function:: int vfd_close(struct inode *inode, struct file *file)

    is closed by the application.

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*file:
        *undescribed*

.. _`send_packet`:

send_packet
===========

.. c:function:: int send_packet(struct sasem_context *context)

    :param struct sasem_context \*context:
        *undescribed*

.. _`vfd_write`:

vfd_write
=========

.. c:function:: ssize_t vfd_write(struct file *file, const char __user *buf, size_t n_bytes, loff_t *pos)

    and requires data in 9 consecutive USB interrupt packets, each packet carrying 8 bytes.

    :param struct file \*file:
        *undescribed*

    :param const char __user \*buf:
        *undescribed*

    :param size_t n_bytes:
        *undescribed*

    :param loff_t \*pos:
        *undescribed*

.. _`usb_tx_callback`:

usb_tx_callback
===============

.. c:function:: void usb_tx_callback(struct urb *urb)

    transmit data

    :param struct urb \*urb:
        *undescribed*

.. _`ir_open`:

ir_open
=======

.. c:function:: int ir_open(void *data)

    :param void \*data:
        *undescribed*

.. _`ir_close`:

ir_close
========

.. c:function:: void ir_close(void *data)

    :param void \*data:
        *undescribed*

.. _`incoming_packet`:

incoming_packet
===============

.. c:function:: void incoming_packet(struct sasem_context *context, struct urb *urb)

    :param struct sasem_context \*context:
        *undescribed*

    :param struct urb \*urb:
        *undescribed*

.. _`usb_rx_callback`:

usb_rx_callback
===============

.. c:function:: void usb_rx_callback(struct urb *urb)

    receive data

    :param struct urb \*urb:
        *undescribed*

.. _`sasem_probe`:

sasem_probe
===========

.. c:function:: int sasem_probe(struct usb_interface *interface, const struct usb_device_id *id)

    Probe

    :param struct usb_interface \*interface:
        *undescribed*

    :param const struct usb_device_id \*id:
        *undescribed*

.. _`sasem_disconnect`:

sasem_disconnect
================

.. c:function:: void sasem_disconnect(struct usb_interface *interface)

    disconnect

    :param struct usb_interface \*interface:
        *undescribed*

.. This file was automatic generated / don't edit.

