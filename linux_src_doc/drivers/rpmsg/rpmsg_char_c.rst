.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rpmsg/rpmsg_char.c

.. _`rpmsg_ctrldev`:

struct rpmsg_ctrldev
====================

.. c:type:: struct rpmsg_ctrldev

    control device for instantiating endpoint devices

.. _`rpmsg_ctrldev.definition`:

Definition
----------

.. code-block:: c

    struct rpmsg_ctrldev {
        struct rpmsg_device *rpdev;
        struct cdev cdev;
        struct device dev;
    }

.. _`rpmsg_ctrldev.members`:

Members
-------

rpdev
    underlaying rpmsg device

cdev
    cdev for the ctrl device

dev
    device for the ctrl device

.. _`rpmsg_eptdev`:

struct rpmsg_eptdev
===================

.. c:type:: struct rpmsg_eptdev

    endpoint device context

.. _`rpmsg_eptdev.definition`:

Definition
----------

.. code-block:: c

    struct rpmsg_eptdev {
        struct device dev;
        struct cdev cdev;
        struct rpmsg_device *rpdev;
        struct rpmsg_channel_info chinfo;
        struct mutex ept_lock;
        struct rpmsg_endpoint *ept;
        spinlock_t queue_lock;
        struct sk_buff_head queue;
        wait_queue_head_t readq;
    }

.. _`rpmsg_eptdev.members`:

Members
-------

dev
    endpoint device

cdev
    cdev for the endpoint device

rpdev
    underlaying rpmsg device

chinfo
    info used to open the endpoint

ept_lock
    synchronization of \ ``ept``\  modifications

ept
    rpmsg endpoint reference, when open

queue_lock
    synchronization of \ ``queue``\  operations

queue
    incoming message queue

readq
    wait object for incoming queue

.. This file was automatic generated / don't edit.

