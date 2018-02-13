.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/serdev.h

.. _`serdev_device_ops`:

struct serdev_device_ops
========================

.. c:type:: struct serdev_device_ops

    Callback operations for a serdev device

.. _`serdev_device_ops.definition`:

Definition
----------

.. code-block:: c

    struct serdev_device_ops {
        int (*receive_buf)(struct serdev_device *, const unsigned char *, size_t);
        void (*write_wakeup)(struct serdev_device *);
    }

.. _`serdev_device_ops.members`:

Members
-------

receive_buf
    Function called with data received from device;
    returns number of bytes accepted; may sleep.

write_wakeup
    Function called when ready to transmit more data; must
    not sleep.

.. _`serdev_device`:

struct serdev_device
====================

.. c:type:: struct serdev_device

    Basic representation of an serdev device

.. _`serdev_device.definition`:

Definition
----------

.. code-block:: c

    struct serdev_device {
        struct device dev;
        int nr;
        struct serdev_controller *ctrl;
        const struct serdev_device_ops *ops;
        struct completion write_comp;
        struct mutex write_lock;
    }

.. _`serdev_device.members`:

Members
-------

dev
    Driver model representation of the device.

nr
    Device number on serdev bus.

ctrl
    serdev controller managing this device.

ops
    Device operations.
    \ ``write_comp``\   Completion used by \ :c:func:`serdev_device_write`\  internally
    \ ``write_lock``\   Lock to serialize access when writing data

write_comp
    *undescribed*

write_lock
    *undescribed*

.. _`serdev_device_driver`:

struct serdev_device_driver
===========================

.. c:type:: struct serdev_device_driver

    serdev slave device driver

.. _`serdev_device_driver.definition`:

Definition
----------

.. code-block:: c

    struct serdev_device_driver {
        struct device_driver driver;
        int (*probe)(struct serdev_device *);
        void (*remove)(struct serdev_device *);
    }

.. _`serdev_device_driver.members`:

Members
-------

driver
    serdev device drivers should initialize name field of this
    structure.

probe
    binds this driver to a serdev device.

remove
    unbinds this driver from the serdev device.

.. _`serdev_controller`:

struct serdev_controller
========================

.. c:type:: struct serdev_controller

    interface to the serdev controller

.. _`serdev_controller.definition`:

Definition
----------

.. code-block:: c

    struct serdev_controller {
        struct device dev;
        unsigned int nr;
        struct serdev_device *serdev;
        const struct serdev_controller_ops *ops;
    }

.. _`serdev_controller.members`:

Members
-------

dev
    Driver model representation of the device.

nr
    number identifier for this controller/bus.

serdev
    Pointer to slave device for this controller.

ops
    Controller operations.

.. _`serdev_device_put`:

serdev_device_put
=================

.. c:function:: void serdev_device_put(struct serdev_device *serdev)

    decrement serdev device refcount \ ``serdev``\       serdev device.

    :param struct serdev_device \*serdev:
        *undescribed*

.. _`serdev_controller_put`:

serdev_controller_put
=====================

.. c:function:: void serdev_controller_put(struct serdev_controller *ctrl)

    decrement controller refcount \ ``ctrl``\         serdev controller.

    :param struct serdev_controller \*ctrl:
        *undescribed*

.. _`serdev_device_driver_unregister`:

serdev_device_driver_unregister
===============================

.. c:function:: void serdev_device_driver_unregister(struct serdev_device_driver *sdrv)

    unregister an serdev client driver

    :param struct serdev_device_driver \*sdrv:
        the driver to unregister

.. This file was automatic generated / don't edit.

