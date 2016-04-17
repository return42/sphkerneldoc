.. -*- coding: utf-8; mode: rst -*-

===========
sunxi-rsb.c
===========


.. _`sunxi_rsb_device_create`:

sunxi_rsb_device_create
=======================

.. c:function:: struct sunxi_rsb_device *sunxi_rsb_device_create (struct sunxi_rsb *rsb, struct device_node *node, u16 hwaddr, u8 rtaddr)

    allocate and add an RSB device

    :param struct sunxi_rsb \*rsb:
        RSB controller

    :param struct device_node \*node:
        RSB slave device node

    :param u16 hwaddr:
        RSB slave hardware address

    :param u8 rtaddr:
        RSB slave runtime address



.. _`sunxi_rsb_device_unregister`:

sunxi_rsb_device_unregister
===========================

.. c:function:: void sunxi_rsb_device_unregister (struct sunxi_rsb_device *rdev)

    :param struct sunxi_rsb_device \*rdev:
        rsb_device to be removed



.. _`sunxi_rsb_driver_register`:

sunxi_rsb_driver_register
=========================

.. c:function:: int sunxi_rsb_driver_register (struct sunxi_rsb_driver *rdrv)

    Register device driver with RSB core

    :param struct sunxi_rsb_driver \*rdrv:
        device driver to be associated with slave-device.



.. _`sunxi_rsb_driver_register.description`:

Description
-----------

This API will register the client driver with the RSB framework.
It is typically called from the driver's module-init function.

