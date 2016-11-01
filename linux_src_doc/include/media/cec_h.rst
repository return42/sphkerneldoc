.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/cec.h

.. _`cec_devnode`:

struct cec_devnode
==================

.. c:type:: struct cec_devnode

    cec device node

.. _`cec_devnode.definition`:

Definition
----------

.. code-block:: c

    struct cec_devnode {
        struct device dev;
        struct cdev cdev;
        struct device *parent;
        int minor;
        bool registered;
        bool unregistered;
        struct list_head fhs;
        struct mutex lock;
    }

.. _`cec_devnode.members`:

Members
-------

dev
    cec device

cdev
    cec character device

parent
    parent device

minor
    device node minor number

registered
    the device was correctly registered

unregistered
    the device was unregistered

fhs
    the list of open filehandles (cec_fh)

lock
    *undescribed*

.. _`cec_devnode.description`:

Description
-----------

This structure represents a cec-related device node.

The \ ``parent``\  is a physical device. It must be set by core or device drivers
before registering the node.

.. This file was automatic generated / don't edit.

