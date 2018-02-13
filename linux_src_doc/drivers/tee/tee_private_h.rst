.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tee/tee_private.h

.. _`tee_shm_pool`:

struct tee_shm_pool
===================

.. c:type:: struct tee_shm_pool

    shared memory pool

.. _`tee_shm_pool.definition`:

Definition
----------

.. code-block:: c

    struct tee_shm_pool {
        struct tee_shm_pool_mgr *private_mgr;
        struct tee_shm_pool_mgr *dma_buf_mgr;
    }

.. _`tee_shm_pool.members`:

Members
-------

private_mgr
    pool manager for shared memory only between kernel
    and secure world

dma_buf_mgr
    pool manager for shared memory exported to user space

.. _`tee_device`:

struct tee_device
=================

.. c:type:: struct tee_device

    TEE Device representation

.. _`tee_device.definition`:

Definition
----------

.. code-block:: c

    struct tee_device {
        char name[TEE_MAX_DEV_NAME_LEN];
        const struct tee_desc *desc;
        int id;
        unsigned int flags;
        struct device dev;
        struct cdev cdev;
        size_t num_users;
        struct completion c_no_users;
        struct mutex mutex;
        struct idr idr;
        struct tee_shm_pool *pool;
    }

.. _`tee_device.members`:

Members
-------

name
    name of device

desc
    description of device

id
    unique id of device

flags
    represented by TEE_DEVICE_FLAG_REGISTERED above

dev
    embedded basic device structure

cdev
    embedded cdev

num_users
    number of active users of this device

c_no_users
    *undescribed*

mutex
    mutex protecting \ ``num_users``\  and \ ``idr``\ 

idr
    register of shared memory object allocated on this device

pool
    shared memory pool

.. This file was automatic generated / don't edit.

