.. -*- coding: utf-8; mode: rst -*-

===========
iowarrior.c
===========


.. _`iowarrior_delete`:

iowarrior_delete
================

.. c:function:: void iowarrior_delete (struct iowarrior *dev)

    :param struct iowarrior \*dev:

        *undescribed*



.. _`iowarrior_read`:

iowarrior_read
==============

.. c:function:: ssize_t iowarrior_read (struct file *file, char __user *buffer, size_t count, loff_t *ppos)

    :param struct file \*file:

        *undescribed*

    :param char __user \*buffer:

        *undescribed*

    :param size_t count:

        *undescribed*

    :param loff_t \*ppos:

        *undescribed*



.. _`iowarrior_ioctl`:

iowarrior_ioctl
===============

.. c:function:: long iowarrior_ioctl (struct file *file, unsigned int cmd, unsigned long arg)

    :param struct file \*file:

        *undescribed*

    :param unsigned int cmd:

        *undescribed*

    :param unsigned long arg:

        *undescribed*



.. _`iowarrior_open`:

iowarrior_open
==============

.. c:function:: int iowarrior_open (struct inode *inode, struct file *file)

    :param struct inode \*inode:

        *undescribed*

    :param struct file \*file:

        *undescribed*



.. _`iowarrior_release`:

iowarrior_release
=================

.. c:function:: int iowarrior_release (struct inode *inode, struct file *file)

    :param struct inode \*inode:

        *undescribed*

    :param struct file \*file:

        *undescribed*



.. _`iowarrior_probe`:

iowarrior_probe
===============

.. c:function:: int iowarrior_probe (struct usb_interface *interface, const struct usb_device_id *id)

    :param struct usb_interface \*interface:

        *undescribed*

    :param const struct usb_device_id \*id:

        *undescribed*



.. _`iowarrior_probe.description`:

Description
-----------


Called by the usb core when a new device is connected that it thinks
this driver might be interested in.



.. _`iowarrior_disconnect`:

iowarrior_disconnect
====================

.. c:function:: void iowarrior_disconnect (struct usb_interface *interface)

    :param struct usb_interface \*interface:

        *undescribed*



.. _`iowarrior_disconnect.description`:

Description
-----------


Called by the usb core when the device is removed from the system.

