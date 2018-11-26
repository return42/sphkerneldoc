.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/misc/iowarrior.c

.. _`iowarrior_delete`:

iowarrior_delete
================

.. c:function:: void iowarrior_delete(struct iowarrior *dev)

    :param dev:
        *undescribed*
    :type dev: struct iowarrior \*

.. _`iowarrior_read`:

iowarrior_read
==============

.. c:function:: ssize_t iowarrior_read(struct file *file, char __user *buffer, size_t count, loff_t *ppos)

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

.. _`iowarrior_ioctl`:

iowarrior_ioctl
===============

.. c:function:: long iowarrior_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    :param file:
        *undescribed*
    :type file: struct file \*

    :param cmd:
        *undescribed*
    :type cmd: unsigned int

    :param arg:
        *undescribed*
    :type arg: unsigned long

.. _`iowarrior_open`:

iowarrior_open
==============

.. c:function:: int iowarrior_open(struct inode *inode, struct file *file)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param file:
        *undescribed*
    :type file: struct file \*

.. _`iowarrior_release`:

iowarrior_release
=================

.. c:function:: int iowarrior_release(struct inode *inode, struct file *file)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param file:
        *undescribed*
    :type file: struct file \*

.. _`iowarrior_probe`:

iowarrior_probe
===============

.. c:function:: int iowarrior_probe(struct usb_interface *interface, const struct usb_device_id *id)

    :param interface:
        *undescribed*
    :type interface: struct usb_interface \*

    :param id:
        *undescribed*
    :type id: const struct usb_device_id \*

.. _`iowarrior_probe.description`:

Description
-----------

Called by the usb core when a new device is connected that it thinks
this driver might be interested in.

.. _`iowarrior_disconnect`:

iowarrior_disconnect
====================

.. c:function:: void iowarrior_disconnect(struct usb_interface *interface)

    :param interface:
        *undescribed*
    :type interface: struct usb_interface \*

.. _`iowarrior_disconnect.description`:

Description
-----------

Called by the usb core when the device is removed from the system.

.. This file was automatic generated / don't edit.

