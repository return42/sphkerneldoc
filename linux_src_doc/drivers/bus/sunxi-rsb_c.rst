.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/sunxi-rsb.c

.. _`sunxi_rsb_device_create`:

sunxi_rsb_device_create
=======================

.. c:function:: struct sunxi_rsb_device *sunxi_rsb_device_create(struct sunxi_rsb *rsb, struct device_node *node, u16 hwaddr, u8 rtaddr)

    allocate and add an RSB device

    :param rsb:
        RSB controller
    :type rsb: struct sunxi_rsb \*

    :param node:
        RSB slave device node
    :type node: struct device_node \*

    :param hwaddr:
        RSB slave hardware address
    :type hwaddr: u16

    :param rtaddr:
        RSB slave runtime address
    :type rtaddr: u8

.. _`sunxi_rsb_device_unregister`:

sunxi_rsb_device_unregister
===========================

.. c:function:: void sunxi_rsb_device_unregister(struct sunxi_rsb_device *rdev)

    unregister an RSB device

    :param rdev:
        rsb_device to be removed
    :type rdev: struct sunxi_rsb_device \*

.. _`sunxi_rsb_driver_register`:

sunxi_rsb_driver_register
=========================

.. c:function:: int sunxi_rsb_driver_register(struct sunxi_rsb_driver *rdrv)

    Register device driver with RSB core

    :param rdrv:
        device driver to be associated with slave-device.
    :type rdrv: struct sunxi_rsb_driver \*

.. _`sunxi_rsb_driver_register.description`:

Description
-----------

This API will register the client driver with the RSB framework.
It is typically called from the driver's module-init function.

.. This file was automatic generated / don't edit.

