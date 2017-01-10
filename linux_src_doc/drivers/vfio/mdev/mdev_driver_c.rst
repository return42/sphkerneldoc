.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/vfio/mdev/mdev_driver.c

.. _`mdev_register_driver`:

mdev_register_driver
====================

.. c:function:: int mdev_register_driver(struct mdev_driver *drv, struct module *owner)

    register a new MDEV driver

    :param struct mdev_driver \*drv:
        the driver to register

    :param struct module \*owner:
        module owner of driver to be registered

.. _`mdev_register_driver.description`:

Description
-----------

Returns a negative value on error, otherwise 0.

.. This file was automatic generated / don't edit.

