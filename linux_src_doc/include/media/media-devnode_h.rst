.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/media-devnode.h

.. _`media_file_operations`:

struct media_file_operations
============================

.. c:type:: struct media_file_operations

    Media device file operations

.. _`media_file_operations.definition`:

Definition
----------

.. code-block:: c

    struct media_file_operations {
        struct module *owner;
        ssize_t (*read)(struct file *, char __user *, size_t, loff_t *);
        ssize_t (*write)(struct file *, const char __user *, size_t, loff_t *);
        unsigned int (*poll)(struct file *, struct poll_table_struct *);
        long (*ioctl)(struct file *, unsigned int, unsigned long);
        long (*compat_ioctl)(struct file *, unsigned int, unsigned long);
        int (*open)(struct file *);
        int (*release)(struct file *);
    }

.. _`media_file_operations.members`:

Members
-------

owner
    should be filled with \ ``THIS_MODULE``\ 

read
    pointer to the function that implements \ :c:func:`read`\  syscall

write
    pointer to the function that implements \ :c:func:`write`\  syscall

poll
    pointer to the function that implements \ :c:func:`poll`\  syscall

ioctl
    pointer to the function that implements \ :c:func:`ioctl`\  syscall

compat_ioctl
    pointer to the function that will handle 32 bits userspace
    calls to the the \ :c:func:`ioctl`\  syscall on a Kernel compiled with 64 bits.

open
    pointer to the function that implements \ :c:func:`open`\  syscall

release
    pointer to the function that will release the resources allocated
    by the \ ``open``\  function.

.. _`media_devnode`:

struct media_devnode
====================

.. c:type:: struct media_devnode

    Media device node

.. _`media_devnode.definition`:

Definition
----------

.. code-block:: c

    struct media_devnode {
        struct media_device *media_dev;
        const struct media_file_operations *fops;
        struct device dev;
        struct cdev cdev;
        struct device *parent;
        int minor;
        unsigned long flags;
        void (*release)(struct media_devnode *devnode);
    }

.. _`media_devnode.members`:

Members
-------

media_dev
    pointer to struct \ :c:type:`struct media_device <media_device>`\ 

fops
    pointer to struct \ :c:type:`struct media_file_operations <media_file_operations>`\  with media device ops

dev
    pointer to struct \ :c:type:`struct device <device>`\  containing the media controller device

cdev
    struct cdev pointer character device

parent
    parent device

minor
    device node minor number

flags
    flags, combination of the ``MEDIA_FLAG_*`` constants

release
    release callback called at the end of ``media_devnode_release()``
    routine at media-device.c.

.. _`media_devnode.description`:

Description
-----------

This structure represents a media-related device node.

The \ ``parent``\  is a physical device. It must be set by core or device drivers
before registering the node.

.. _`media_devnode_register`:

media_devnode_register
======================

.. c:function:: int media_devnode_register(struct media_device *mdev, struct media_devnode *devnode, struct module *owner)

    register a media device node

    :param struct media_device \*mdev:
        struct media_device we want to register a device node

    :param struct media_devnode \*devnode:
        media device node structure we want to register

    :param struct module \*owner:
        should be filled with \ ``THIS_MODULE``\ 

.. _`media_devnode_register.description`:

Description
-----------

The registration code assigns minor numbers and registers the new device node
with the kernel. An error is returned if no free minor number can be found,
or if the registration of the device node fails.

Zero is returned on success.

Note that if the media_devnode_register call fails, the \ :c:func:`release`\  callback of
the media_devnode structure is *not* called, so the caller is responsible for
freeing any data.

.. _`media_devnode_unregister_prepare`:

media_devnode_unregister_prepare
================================

.. c:function:: void media_devnode_unregister_prepare(struct media_devnode *devnode)

    clear the media device node register bit

    :param struct media_devnode \*devnode:
        the device node to prepare for unregister

.. _`media_devnode_unregister_prepare.description`:

Description
-----------

This clears the passed device register bit. Future open calls will be met
with errors. Should be called before \ :c:func:`media_devnode_unregister`\  to avoid
races with unregister and device file open calls.

This function can safely be called if the device node has never been
registered or has already been unregistered.

.. _`media_devnode_unregister`:

media_devnode_unregister
========================

.. c:function:: void media_devnode_unregister(struct media_devnode *devnode)

    unregister a media device node

    :param struct media_devnode \*devnode:
        the device node to unregister

.. _`media_devnode_unregister.description`:

Description
-----------

This unregisters the passed device. Future open calls will be met with
errors.

Should be called after \ :c:func:`media_devnode_unregister_prepare`\ 

.. _`media_devnode_data`:

media_devnode_data
==================

.. c:function:: struct media_devnode *media_devnode_data(struct file *filp)

    returns a pointer to the \ :c:type:`struct media_devnode <media_devnode>`\ 

    :param struct file \*filp:
        pointer to struct \ :c:type:`struct file <file>`\ 

.. _`media_devnode_is_registered`:

media_devnode_is_registered
===========================

.. c:function:: int media_devnode_is_registered(struct media_devnode *devnode)

    returns true if \ :c:type:`struct media_devnode <media_devnode>`\  is registered; false otherwise.

    :param struct media_devnode \*devnode:
        pointer to struct \ :c:type:`struct media_devnode <media_devnode>`\ .

.. _`media_devnode_is_registered.note`:

Note
----

If mdev is NULL, it also returns false.

.. This file was automatic generated / don't edit.

