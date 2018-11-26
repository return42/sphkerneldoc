.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/virt/vboxguest/vboxguest_linux.c

.. _`vbg_misc_device_close`:

vbg_misc_device_close
=====================

.. c:function:: int vbg_misc_device_close(struct inode *inode, struct file *filp)

    :param inode:
        Pointer to inode info structure.
    :type inode: struct inode \*

    :param filp:
        Associated file pointer.
    :type filp: struct file \*

.. _`vbg_misc_device_close.return`:

Return
------

0 on success, negated errno on failure.

.. _`vbg_misc_device_ioctl`:

vbg_misc_device_ioctl
=====================

.. c:function:: long vbg_misc_device_ioctl(struct file *filp, unsigned int req, unsigned long arg)

    :param filp:
        Associated file pointer.
    :type filp: struct file \*

    :param req:
        The request specified to \ :c:func:`ioctl`\ .
    :type req: unsigned int

    :param arg:
        The argument specified to \ :c:func:`ioctl`\ .
    :type arg: unsigned long

.. _`vbg_misc_device_ioctl.return`:

Return
------

0 on success, negated errno on failure.

.. _`vbg_input_open`:

vbg_input_open
==============

.. c:function:: int vbg_input_open(struct input_dev *input)

    :param input:
        *undescribed*
    :type input: struct input_dev \*

.. _`vbg_input_open.description`:

Description
-----------

Sets up absolute mouse reporting.

.. _`vbg_input_close`:

vbg_input_close
===============

.. c:function:: void vbg_input_close(struct input_dev *input)

    :param input:
        *undescribed*
    :type input: struct input_dev \*

.. _`vbg_input_close.description`:

Description
-----------

Disables absolute reporting.

.. _`vbg_create_input_device`:

vbg_create_input_device
=======================

.. c:function:: int vbg_create_input_device(struct vbg_dev *gdev)

    :param gdev:
        *undescribed*
    :type gdev: struct vbg_dev \*

.. _`vbg_create_input_device.return`:

Return
------

0 on success, negated errno on failure.

.. _`vbg_pci_probe`:

vbg_pci_probe
=============

.. c:function:: int vbg_pci_probe(struct pci_dev *pci, const struct pci_device_id *id)

    :param pci:
        *undescribed*
    :type pci: struct pci_dev \*

    :param id:
        *undescribed*
    :type id: const struct pci_device_id \*

.. _`vbg_pci_probe.return`:

Return
------

0 on success, negated errno on failure.

.. _`vbg_linux_mouse_event`:

vbg_linux_mouse_event
=====================

.. c:function:: void vbg_linux_mouse_event(struct vbg_dev *gdev)

    :param gdev:
        The device extension.
    :type gdev: struct vbg_dev \*

.. _`vbg_linux_mouse_event.description`:

Description
-----------

This is called at the end of the ISR, after leaving the event spinlock, if
VMMDEV_EVENT_MOUSE_POSITION_CHANGED was raised by the host.

.. This file was automatic generated / don't edit.

