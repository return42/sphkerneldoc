.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/android/ion/ion.c

.. _`ion_device`:

struct ion_device
=================

.. c:type:: struct ion_device

    the metadata of the ion device node

.. _`ion_device.definition`:

Definition
----------

.. code-block:: c

    struct ion_device {
        struct miscdevice dev;
        struct rb_root buffers;
        struct mutex buffer_lock;
        struct rw_semaphore lock;
        struct plist_head heaps;
        long (*custom_ioctl)(struct ion_client *client, unsigned int cmd,unsigned long arg);
        struct rb_root clients;
        struct dentry *debug_root;
        struct dentry *heaps_debug_root;
        struct dentry *clients_debug_root;
    }

.. _`ion_device.members`:

Members
-------

dev
    the actual misc device

buffers
    an rb tree of all the existing buffers

buffer_lock
    lock protecting the tree of buffers

lock
    rwsem protecting the tree of heaps and clients

heaps
    list of all the heaps in the system

custom_ioctl
    *undescribed*

clients
    *undescribed*

debug_root
    *undescribed*

heaps_debug_root
    *undescribed*

clients_debug_root
    *undescribed*

.. _`ion_client`:

struct ion_client
=================

.. c:type:: struct ion_client

    a process/hw block local address space

.. _`ion_client.definition`:

Definition
----------

.. code-block:: c

    struct ion_client {
        struct rb_node node;
        struct ion_device *dev;
        struct rb_root handles;
        struct idr idr;
        struct mutex lock;
        const char *name;
        char *display_name;
        int display_serial;
        struct task_struct *task;
        pid_t pid;
        struct dentry *debug_root;
    }

.. _`ion_client.members`:

Members
-------

node
    node in the tree of all clients

dev
    backpointer to ion device

handles
    an rb tree of all the handles in this client

idr
    an idr space for allocating handle ids

lock
    lock protecting the tree of handles

name
    used for debugging

display_name
    used for debugging (unique version of \ ``name``\ )

display_serial
    used for debugging (to make display_name unique)

task
    used for debugging

pid
    *undescribed*

debug_root
    *undescribed*

.. _`ion_client.description`:

Description
-----------

A client represents a list of buffers this client may access.
The mutex stored here is used to protect both handles tree
as well as the handles themselves, and should be held while modifying either.

.. This file was automatic generated / don't edit.

