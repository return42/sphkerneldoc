.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mdev.h

.. _`mdev_parent_ops`:

struct mdev_parent_ops
======================

.. c:type:: struct mdev_parent_ops

    Structure to be registered for each parent device to register the device to mdev module.

.. _`mdev_parent_ops.definition`:

Definition
----------

.. code-block:: c

    struct mdev_parent_ops {
        struct module *owner;
        const struct attribute_group **dev_attr_groups;
        const struct attribute_group **mdev_attr_groups;
        struct attribute_group **supported_type_groups;
        int (*create)(struct kobject *kobj, struct mdev_device *mdev);
        int (*remove)(struct mdev_device *mdev);
        int (*open)(struct mdev_device *mdev);
        void (*release)(struct mdev_device *mdev);
        ssize_t (*read)(struct mdev_device *mdev, char __user *buf,size_t count, loff_t *ppos);
        ssize_t (*write)(struct mdev_device *mdev, const char __user *buf,size_t count, loff_t *ppos);
        long (*ioctl)(struct mdev_device *mdev, unsigned int cmd,unsigned long arg);
        int (*mmap)(struct mdev_device *mdev, struct vm_area_struct *vma);
    }

.. _`mdev_parent_ops.members`:

Members
-------

owner
    The module owner.

dev_attr_groups
    Attributes of the parent device.

mdev_attr_groups
    Attributes of the mediated device.

supported_type_groups
    Attributes to define supported types. It is mandatory
    to provide supported types.

create
    Called to allocate basic resources in parent device's
    driver for a particular mediated device. It is
    mandatory to provide create ops.
    \ ``kobj``\ : kobject of type for which 'create' is called.
    \ ``mdev``\ : mdev_device structure on of mediated device
    that is being created
    Returns integer: success (0) or error (< 0)

remove
    Called to free resources in parent device's driver for a
    a mediated device. It is mandatory to provide 'remove'
    ops.
    \ ``mdev``\ : mdev_device device structure which is being
    destroyed
    Returns integer: success (0) or error (< 0)

open
    Open mediated device.
    \ ``mdev``\ : mediated device.
    Returns integer: success (0) or error (< 0)

release
    release mediated device
    \ ``mdev``\ : mediated device.

read
    Read emulation callback
    \ ``mdev``\ : mediated device structure
    \ ``buf``\ : read buffer
    \ ``count``\ : number of bytes to read
    \ ``ppos``\ : address.
    Retuns number on bytes read on success or error.

write
    Write emulation callback
    \ ``mdev``\ : mediated device structure
    \ ``buf``\ : write buffer
    \ ``count``\ : number of bytes to be written
    \ ``ppos``\ : address.
    Retuns number on bytes written on success or error.

ioctl
    IOCTL callback
    \ ``mdev``\ : mediated device structure
    \ ``cmd``\ : ioctl command
    \ ``arg``\ : arguments to ioctl

mmap
    mmap callback
    \ ``mdev``\ : mediated device structure
    \ ``vma``\ : vma structure
    Parent device that support mediated device should be registered with mdev
    module with mdev_parent_ops structure.

.. _`mdev_driver`:

struct mdev_driver
==================

.. c:type:: struct mdev_driver

    Mediated device driver

.. _`mdev_driver.definition`:

Definition
----------

.. code-block:: c

    struct mdev_driver {
        const char *name;
        int (*probe)(struct device *dev);
        void (*remove)(struct device *dev);
        struct device_driver driver;
    }

.. _`mdev_driver.members`:

Members
-------

name
    driver name

probe
    called when new device created

remove
    called when device removed

driver
    device driver structure

.. This file was automatic generated / don't edit.

