.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serdev/core.c

.. _`serdev_device_add`:

serdev_device_add
=================

.. c:function:: int serdev_device_add(struct serdev_device *serdev)

    add a device previously constructed via \ :c:func:`serdev_device_alloc`\ 

    :param struct serdev_device \*serdev:
        serdev_device to be added

.. _`serdev_device_remove`:

serdev_device_remove
====================

.. c:function:: void serdev_device_remove(struct serdev_device *serdev)

    remove an serdev device

    :param struct serdev_device \*serdev:
        serdev_device to be removed

.. _`serdev_device_alloc`:

serdev_device_alloc
===================

.. c:function:: struct serdev_device *serdev_device_alloc(struct serdev_controller *ctrl)

    Allocate a new serdev device

    :param struct serdev_controller \*ctrl:
        associated controller

.. _`serdev_device_alloc.description`:

Description
-----------

Caller is responsible for either calling \ :c:func:`serdev_device_add`\  to add the
newly allocated controller, or calling \ :c:func:`serdev_device_put`\  to discard it.

.. _`serdev_controller_alloc`:

serdev_controller_alloc
=======================

.. c:function:: struct serdev_controller *serdev_controller_alloc(struct device *parent, size_t size)

    Allocate a new serdev controller

    :param struct device \*parent:
        parent device

    :param size_t size:
        size of private data

.. _`serdev_controller_alloc.description`:

Description
-----------

Caller is responsible for either calling \ :c:func:`serdev_controller_add`\  to add the
newly allocated controller, or calling \ :c:func:`serdev_controller_put`\  to discard it.
The allocated private data region may be accessed via
\ :c:func:`serdev_controller_get_drvdata`\ 

.. _`serdev_controller_add`:

serdev_controller_add
=====================

.. c:function:: int serdev_controller_add(struct serdev_controller *ctrl)

    Add an serdev controller

    :param struct serdev_controller \*ctrl:
        controller to be registered.

.. _`serdev_controller_add.description`:

Description
-----------

Register a controller previously allocated via \ :c:func:`serdev_controller_alloc`\  with
the serdev core.

.. _`serdev_controller_remove`:

serdev_controller_remove
========================

.. c:function:: void serdev_controller_remove(struct serdev_controller *ctrl)

    remove an serdev controller

    :param struct serdev_controller \*ctrl:
        controller to remove

.. _`serdev_controller_remove.description`:

Description
-----------

Remove a serdev controller.  Caller is responsible for calling
\ :c:func:`serdev_controller_put`\  to discard the allocated controller.

.. _`__serdev_device_driver_register`:

\__serdev_device_driver_register
================================

.. c:function:: int __serdev_device_driver_register(struct serdev_device_driver *sdrv, struct module *owner)

    Register client driver with serdev core

    :param struct serdev_device_driver \*sdrv:
        client driver to be associated with client-device.

    :param struct module \*owner:
        *undescribed*

.. _`__serdev_device_driver_register.description`:

Description
-----------

This API will register the client driver with the serdev framework.
It is typically called from the driver's module-init function.

.. This file was automatic generated / don't edit.

