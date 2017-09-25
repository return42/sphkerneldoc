.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tee/tee_private.h

.. _`tee_shm`:

struct tee_shm
==============

.. c:type:: struct tee_shm

    shared memory object

.. _`tee_shm.definition`:

Definition
----------

.. code-block:: c

    struct tee_shm {
        struct tee_device *teedev;
        struct tee_context *ctx;
        struct list_head link;
        phys_addr_t paddr;
        void *kaddr;
        size_t size;
        struct dma_buf *dmabuf;
        u32 flags;
        int id;
    }

.. _`tee_shm.members`:

Members
-------

teedev
    device used to allocate the object

ctx
    context using the object, if NULL the context is gone
    \ ``link``\         link element

link
    *undescribed*

paddr
    physical address of the shared memory

kaddr
    virtual address of the shared memory

size
    size of shared memory

dmabuf
    dmabuf used to for exporting to user space

flags
    defined by TEE_SHM\_\* in tee_drv.h

id
    unique id of a shared memory object on this device

.. _`tee_shm_pool_mgr_ops`:

struct tee_shm_pool_mgr_ops
===========================

.. c:type:: struct tee_shm_pool_mgr_ops

    shared memory pool manager operations

.. _`tee_shm_pool_mgr_ops.definition`:

Definition
----------

.. code-block:: c

    struct tee_shm_pool_mgr_ops {
        int (*alloc)(struct tee_shm_pool_mgr *poolmgr, struct tee_shm *shm, size_t size);
        void (*free)(struct tee_shm_pool_mgr *poolmgr, struct tee_shm *shm);
    }

.. _`tee_shm_pool_mgr_ops.members`:

Members
-------

alloc
    called when allocating shared memory

free
    called when freeing shared memory

.. _`tee_shm_pool_mgr`:

struct tee_shm_pool_mgr
=======================

.. c:type:: struct tee_shm_pool_mgr

    shared memory manager

.. _`tee_shm_pool_mgr.definition`:

Definition
----------

.. code-block:: c

    struct tee_shm_pool_mgr {
        const struct tee_shm_pool_mgr_ops *ops;
        void *private_data;
    }

.. _`tee_shm_pool_mgr.members`:

Members
-------

ops
    operations

private_data
    private data for the shared memory manager

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
        struct tee_shm_pool_mgr private_mgr;
        struct tee_shm_pool_mgr dma_buf_mgr;
        void (*destroy)(struct tee_shm_pool *pool);
        void *private_data;
    }

.. _`tee_shm_pool.members`:

Members
-------

private_mgr
    pool manager for shared memory only between kernel
    and secure world

dma_buf_mgr
    pool manager for shared memory exported to user space

destroy
    called when destroying the pool

private_data
    private data for the pool

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

