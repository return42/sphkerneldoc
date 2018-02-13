.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/virt/vboxguest/vboxguest_linux.c

.. _`vbg_misc_device_close`:

vbg_misc_device_close
=====================

.. c:function:: int vbg_misc_device_close(struct inode *inode, struct file *filp)

    :param struct inode \*inode:
        Pointer to inode info structure.

    :param struct file \*filp:
        Associated file pointer.

.. _`vbg_misc_device_close.return`:

Return
------

0 on success, negated errno on failure.

.. _`vbg_misc_device_ioctl`:

vbg_misc_device_ioctl
=====================

.. c:function:: long vbg_misc_device_ioctl(struct file *filp, unsigned int req, unsigned long arg)

    :param struct file \*filp:
        Associated file pointer.

    :param unsigned int req:
        The request specified to \ :c:func:`ioctl`\ .

    :param unsigned long arg:
        The argument specified to \ :c:func:`ioctl`\ .

.. _`vbg_misc_device_ioctl.return`:

Return
------

0 on success, negated errno on failure.

.. _`vbg_input_open`:

vbg_input_open
==============

.. c:function:: int vbg_input_open(struct input_dev *input)

    :param struct input_dev \*input:
        *undescribed*

.. _`vbg_input_open.description`:

Description
-----------

Sets up absolute mouse reporting.

.. _`vbg_input_close`:

vbg_input_close
===============

.. c:function:: void vbg_input_close(struct input_dev *input)

    :param struct input_dev \*input:
        *undescribed*

.. _`vbg_input_close.description`:

Description
-----------

Disables absolute reporting.

.. _`vbg_create_input_device`:

vbg_create_input_device
=======================

.. c:function:: int vbg_create_input_device(struct vbg_dev *gdev)

    :param struct vbg_dev \*gdev:
        *undescribed*

.. _`vbg_create_input_device.return`:

Return
------

0 on success, negated errno on failure.

.. _`vbg_pci_probe`:

vbg_pci_probe
=============

.. c:function:: int vbg_pci_probe(struct pci_dev *pci, const struct pci_device_id *id)

    :param struct pci_dev \*pci:
        *undescribed*

    :param const struct pci_device_id \*id:
        *undescribed*

.. _`vbg_pci_probe.return`:

Return
------

0 on success, negated errno on failure.

.. _`vbg_linux_mouse_event`:

vbg_linux_mouse_event
=====================

.. c:function:: void vbg_linux_mouse_event(struct vbg_dev *gdev)

    :param struct vbg_dev \*gdev:
        The device extension.

.. _`vbg_linux_mouse_event.description`:

Description
-----------

This is called at the end of the ISR, after leaving the event spinlock, if
VMMDEV_EVENT_MOUSE_POSITION_CHANGED was raised by the host.

.. This file was automatic generated / don't edit.

