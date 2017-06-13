.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/tee_drv.h

.. _`tee_context`:

struct tee_context
==================

.. c:type:: struct tee_context

    driver specific context on file pointer data

.. _`tee_context.definition`:

Definition
----------

.. code-block:: c

    struct tee_context {
        struct tee_device *teedev;
        struct list_head list_shm;
        void *data;
    }

.. _`tee_context.members`:

Members
-------

teedev
    pointer to this drivers struct tee_device

list_shm
    List of shared memory object owned by this context

data
    driver specific context data, managed by the driver

.. _`tee_driver_ops`:

struct tee_driver_ops
=====================

.. c:type:: struct tee_driver_ops

    driver operations vtable

.. _`tee_driver_ops.definition`:

Definition
----------

.. code-block:: c

    struct tee_driver_ops {
        void (*get_version)(struct tee_device *teedev,struct tee_ioctl_version_data *vers);
        int (*open)(struct tee_context *ctx);
        void (*release)(struct tee_context *ctx);
        int (*open_session)(struct tee_context *ctx,struct tee_ioctl_open_session_arg *arg,struct tee_param *param);
        int (*close_session)(struct tee_context *ctx, u32 session);
        int (*invoke_func)(struct tee_context *ctx,struct tee_ioctl_invoke_arg *arg,struct tee_param *param);
        int (*cancel_req)(struct tee_context *ctx, u32 cancel_id, u32 session);
        int (*supp_recv)(struct tee_context *ctx, u32 *func, u32 *num_params,struct tee_param *param);
        int (*supp_send)(struct tee_context *ctx, u32 ret, u32 num_params,struct tee_param *param);
    }

.. _`tee_driver_ops.members`:

Members
-------

get_version
    returns version of driver

open
    called when the device file is opened

release
    release this open file

open_session
    open a new session

close_session
    close a session

invoke_func
    invoke a trusted function

cancel_req
    request cancel of an ongoing invoke or open

supp_recv
    *undescribed*

supp_send
    called for supplicant to send a response

.. _`tee_device_alloc`:

tee_device_alloc
================

.. c:function:: struct tee_device *tee_device_alloc(const struct tee_desc *teedesc, struct device *dev, struct tee_shm_pool *pool, void *driver_data)

    Allocate a new struct tee_device instance

    :param const struct tee_desc \*teedesc:
        Descriptor for this driver

    :param struct device \*dev:
        Parent device for this device

    :param struct tee_shm_pool \*pool:
        Shared memory pool, NULL if not used

    :param void \*driver_data:
        Private driver data for this device

.. _`tee_device_alloc.description`:

Description
-----------

Allocates a new struct tee_device instance. The device is
removed by \ :c:func:`tee_device_unregister`\ .

\ ``returns``\  a pointer to a 'struct tee_device' or an ERR_PTR on failure

.. _`tee_device_register`:

tee_device_register
===================

.. c:function:: int tee_device_register(struct tee_device *teedev)

    Registers a TEE device

    :param struct tee_device \*teedev:
        Device to register

.. _`tee_device_register.description`:

Description
-----------

tee_device_unregister() need to be called to remove the \ ``teedev``\  if
this function fails.

\ ``returns``\  < 0 on failure

.. _`tee_device_unregister`:

tee_device_unregister
=====================

.. c:function:: void tee_device_unregister(struct tee_device *teedev)

    Removes a TEE device

    :param struct tee_device \*teedev:
        Device to unregister

.. _`tee_device_unregister.description`:

Description
-----------

This function should be called to remove the \ ``teedev``\  even if
\ :c:func:`tee_device_register`\  hasn't been called yet. Does nothing if
\ ``teedev``\  is NULL.

.. _`tee_shm_pool_mem_info`:

struct tee_shm_pool_mem_info
============================

.. c:type:: struct tee_shm_pool_mem_info

    holds information needed to create a shared memory pool

.. _`tee_shm_pool_mem_info.definition`:

Definition
----------

.. code-block:: c

    struct tee_shm_pool_mem_info {
        unsigned long vaddr;
        phys_addr_t paddr;
        size_t size;
    }

.. _`tee_shm_pool_mem_info.members`:

Members
-------

vaddr
    Virtual address of start of pool

paddr
    Physical address of start of pool

size
    Size in bytes of the pool

.. _`tee_shm_pool_alloc_res_mem`:

tee_shm_pool_alloc_res_mem
==========================

.. c:function:: struct tee_shm_pool *tee_shm_pool_alloc_res_mem(struct tee_shm_pool_mem_info *priv_info, struct tee_shm_pool_mem_info *dmabuf_info)

    Create a shared memory pool from reserved memory range

    :param struct tee_shm_pool_mem_info \*priv_info:
        Information for driver private shared memory pool

    :param struct tee_shm_pool_mem_info \*dmabuf_info:
        Information for dma-buf shared memory pool

.. _`tee_shm_pool_alloc_res_mem.description`:

Description
-----------

Start and end of pools will must be page aligned.

Allocation with the flag TEE_SHM_DMA_BUF set will use the range supplied
in \ ``dmabuf``\ , others will use the range provided by \ ``priv``\ .

\ ``returns``\  pointer to a 'struct tee_shm_pool' or an ERR_PTR on failure.

.. _`tee_shm_pool_free`:

tee_shm_pool_free
=================

.. c:function:: void tee_shm_pool_free(struct tee_shm_pool *pool)

    Free a shared memory pool

    :param struct tee_shm_pool \*pool:
        The shared memory pool to free

.. _`tee_shm_pool_free.description`:

Description
-----------

The must be no remaining shared memory allocated from this pool when
this function is called.

.. _`tee_get_drvdata`:

tee_get_drvdata
===============

.. c:function:: void *tee_get_drvdata(struct tee_device *teedev)

    Return driver_data pointer \ ``returns``\  the driver_data pointer supplied to \ :c:func:`tee_register`\ .

    :param struct tee_device \*teedev:
        *undescribed*

.. _`tee_shm_alloc`:

tee_shm_alloc
=============

.. c:function:: struct tee_shm *tee_shm_alloc(struct tee_context *ctx, size_t size, u32 flags)

    Allocate shared memory

    :param struct tee_context \*ctx:
        Context that allocates the shared memory

    :param size_t size:
        Requested size of shared memory

    :param u32 flags:
        Flags setting properties for the requested shared memory.

.. _`tee_shm_alloc.description`:

Description
-----------

Memory allocated as global shared memory is automatically freed when the
TEE file pointer is closed. The \ ``flags``\  field uses the bits defined by
TEE_SHM\_\* above. TEE_SHM_MAPPED must currently always be set. If
TEE_SHM_DMA_BUF global shared memory will be allocated and associated
with a dma-buf handle, else driver private memory.

\ ``returns``\  a pointer to 'struct tee_shm'

.. _`tee_shm_free`:

tee_shm_free
============

.. c:function:: void tee_shm_free(struct tee_shm *shm)

    Free shared memory

    :param struct tee_shm \*shm:
        Handle to shared memory to free

.. _`tee_shm_put`:

tee_shm_put
===========

.. c:function:: void tee_shm_put(struct tee_shm *shm)

    Decrease reference count on a shared memory handle

    :param struct tee_shm \*shm:
        Shared memory handle

.. _`tee_shm_va2pa`:

tee_shm_va2pa
=============

.. c:function:: int tee_shm_va2pa(struct tee_shm *shm, void *va, phys_addr_t *pa)

    Get physical address of a virtual address

    :param struct tee_shm \*shm:
        Shared memory handle

    :param void \*va:
        Virtual address to tranlsate

    :param phys_addr_t \*pa:
        Returned physical address
        \ ``returns``\  0 on success and < 0 on failure

.. _`tee_shm_pa2va`:

tee_shm_pa2va
=============

.. c:function:: int tee_shm_pa2va(struct tee_shm *shm, phys_addr_t pa, void **va)

    Get virtual address of a physical address

    :param struct tee_shm \*shm:
        Shared memory handle

    :param phys_addr_t pa:
        Physical address to tranlsate

    :param void \*\*va:
        Returned virtual address
        \ ``returns``\  0 on success and < 0 on failure

.. _`tee_shm_get_va`:

tee_shm_get_va
==============

.. c:function:: void *tee_shm_get_va(struct tee_shm *shm, size_t offs)

    Get virtual address of a shared memory plus an offset

    :param struct tee_shm \*shm:
        Shared memory handle

    :param size_t offs:
        Offset from start of this shared memory
        \ ``returns``\  virtual address of the shared memory + offs if offs is within
        the bounds of this shared memory, else an ERR_PTR

.. _`tee_shm_get_pa`:

tee_shm_get_pa
==============

.. c:function:: int tee_shm_get_pa(struct tee_shm *shm, size_t offs, phys_addr_t *pa)

    Get physical address of a shared memory plus an offset

    :param struct tee_shm \*shm:
        Shared memory handle

    :param size_t offs:
        Offset from start of this shared memory

    :param phys_addr_t \*pa:
        Physical address to return
        \ ``returns``\  0 if offs is within the bounds of this shared memory, else an
        error code.

.. _`tee_shm_get_id`:

tee_shm_get_id
==============

.. c:function:: int tee_shm_get_id(struct tee_shm *shm)

    Get id of a shared memory object

    :param struct tee_shm \*shm:
        Shared memory handle
        \ ``returns``\  id

.. _`tee_shm_get_from_id`:

tee_shm_get_from_id
===================

.. c:function:: struct tee_shm *tee_shm_get_from_id(struct tee_context *ctx, int id)

    Find shared memory object and increase reference count

    :param struct tee_context \*ctx:
        Context owning the shared memory

    :param int id:
        Id of shared memory object
        \ ``returns``\  a pointer to 'struct tee_shm' on success or an ERR_PTR on failure

.. This file was automatic generated / don't edit.

