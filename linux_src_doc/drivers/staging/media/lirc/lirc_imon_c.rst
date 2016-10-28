.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/media/lirc/lirc_imon.c

.. _`display_open`:

display_open
============

.. c:function:: int display_open(struct inode *inode, struct file *file)

    is opened by the application.

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*file:
        *undescribed*

.. _`display_close`:

display_close
=============

.. c:function:: int display_close(struct inode *inode, struct file *file)

    is closed by the application.

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*file:
        *undescribed*

.. _`send_packet`:

send_packet
===========

.. c:function:: int send_packet(struct imon_context *context)

    - this function must be called with context->ctx_lock held.

    :param struct imon_context \*context:
        *undescribed*

.. _`vfd_write`:

vfd_write
=========

.. c:function:: ssize_t vfd_write(struct file *file, const char __user *buf, size_t n_bytes, loff_t *pos)

    and requires data in 5 consecutive USB interrupt packets, each packet but the last carrying 7 bytes.

    :param struct file \*file:
        *undescribed*

    :param const char __user \*buf:
        *undescribed*

    :param size_t n_bytes:
        *undescribed*

    :param loff_t \*pos:
        *undescribed*

.. _`vfd_write.description`:

Description
-----------

I don't know if the VFD board supports features such as
scrolling, clearing rows, blanking, etc. so at
the caller must provide a full screen of data.  If fewer
than 32 bytes are provided spaces will be appended to
generate a full screen.

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

.. _`submit_data`:

submit_data
===========

.. c:function:: void submit_data(struct imon_context *context)

    the value to lirc_dev.

    :param struct imon_context \*context:
        *undescribed*

.. _`imon_incoming_packet`:

imon_incoming_packet
====================

.. c:function:: void imon_incoming_packet(struct imon_context *context, struct urb *urb, int intf)

    :param struct imon_context \*context:
        *undescribed*

    :param struct urb \*urb:
        *undescribed*

    :param int intf:
        *undescribed*

.. _`usb_rx_callback`:

usb_rx_callback
===============

.. c:function:: void usb_rx_callback(struct urb *urb)

    receive data

    :param struct urb \*urb:
        *undescribed*

.. _`imon_probe`:

imon_probe
==========

.. c:function:: int imon_probe(struct usb_interface *interface, const struct usb_device_id *id)

    Probe

    :param struct usb_interface \*interface:
        *undescribed*

    :param const struct usb_device_id \*id:
        *undescribed*

.. _`imon_disconnect`:

imon_disconnect
===============

.. c:function:: void imon_disconnect(struct usb_interface *interface)

    disconnect

    :param struct usb_interface \*interface:
        *undescribed*

.. This file was automatic generated / don't edit.

