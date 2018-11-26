.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/vfio/mdev/mdev_driver.c

.. _`mdev_register_driver`:

mdev_register_driver
====================

.. c:function:: int mdev_register_driver(struct mdev_driver *drv, struct module *owner)

    register a new MDEV driver

    :param drv:
        the driver to register
    :type drv: struct mdev_driver \*

    :param owner:
        module owner of driver to be registered
    :type owner: struct module \*

.. _`mdev_register_driver.description`:

Description
-----------

Returns a negative value on error, otherwise 0.

.. This file was automatic generated / don't edit.

