.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uio/uio.c

.. _`uio_event_notify`:

uio_event_notify
================

.. c:function:: void uio_event_notify(struct uio_info *info)

    trigger an interrupt event

    :param info:
        UIO device capabilities
    :type info: struct uio_info \*

.. _`uio_interrupt`:

uio_interrupt
=============

.. c:function:: irqreturn_t uio_interrupt(int irq, void *dev_id)

    hardware interrupt handler

    :param irq:
        IRQ number, can be UIO_IRQ_CYCLIC for cyclic timer
    :type irq: int

    :param dev_id:
        Pointer to the devices uio_device structure
    :type dev_id: void \*

.. _`__uio_register_device`:

__uio_register_device
=====================

.. c:function:: int __uio_register_device(struct module *owner, struct device *parent, struct uio_info *info)

    register a new userspace IO device

    :param owner:
        module that creates the new device
    :type owner: struct module \*

    :param parent:
        parent device
    :type parent: struct device \*

    :param info:
        UIO device capabilities
    :type info: struct uio_info \*

.. _`__uio_register_device.description`:

Description
-----------

returns zero on success or a negative error code.

.. _`uio_unregister_device`:

uio_unregister_device
=====================

.. c:function:: void uio_unregister_device(struct uio_info *info)

    unregister a industrial IO device

    :param info:
        UIO device capabilities
    :type info: struct uio_info \*

.. This file was automatic generated / don't edit.

