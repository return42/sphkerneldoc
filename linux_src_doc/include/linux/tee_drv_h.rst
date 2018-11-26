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
        struct kref refcount;
        bool releasing;
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

refcount
    reference counter for this structure

releasing
    flag that indicates if context is being released right now.
    It is needed to break circular dependency on context during
    shared memory release.

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
        void (*get_version)(struct tee_device *teedev, struct tee_ioctl_version_data *vers);
        int (*open)(struct tee_context *ctx);
        void (*release)(struct tee_context *ctx);
        int (*open_session)(struct tee_context *ctx,struct tee_ioctl_open_session_arg *arg, struct tee_param *param);
        int (*close_session)(struct tee_context *ctx, u32 session);
        int (*invoke_func)(struct tee_context *ctx,struct tee_ioctl_invoke_arg *arg, struct tee_param *param);
        int (*cancel_req)(struct tee_context *ctx, u32 cancel_id, u32 session);
        int (*supp_recv)(struct tee_context *ctx, u32 *func, u32 *num_params, struct tee_param *param);
        int (*supp_send)(struct tee_context *ctx, u32 ret, u32 num_params, struct tee_param *param);
        int (*shm_register)(struct tee_context *ctx, struct tee_shm *shm,struct page **pages, size_t num_pages, unsigned long start);
        int (*shm_unregister)(struct tee_context *ctx, struct tee_shm *shm);
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

shm_register
    register shared memory buffer in TEE

shm_unregister
    unregister shared memory buffer in TEE

.. _`tee_device_alloc`:

tee_device_alloc
================

.. c:function:: struct tee_device *tee_device_alloc(const struct tee_desc *teedesc, struct device *dev, struct tee_shm_pool *pool, void *driver_data)

    Allocate a new struct tee_device instance

    :param teedesc:
        Descriptor for this driver
    :type teedesc: const struct tee_desc \*

    :param dev:
        Parent device for this device
    :type dev: struct device \*

    :param pool:
        Shared memory pool, NULL if not used
    :type pool: struct tee_shm_pool \*

    :param driver_data:
        Private driver data for this device
    :type driver_data: void \*

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

    :param teedev:
        Device to register
    :type teedev: struct tee_device \*

.. _`tee_device_register.description`:

Description
-----------

\ :c:func:`tee_device_unregister`\  need to be called to remove the \ ``teedev``\  if
this function fails.

\ ``returns``\  < 0 on failure

.. _`tee_device_unregister`:

tee_device_unregister
=====================

.. c:function:: void tee_device_unregister(struct tee_device *teedev)

    Removes a TEE device

    :param teedev:
        Device to unregister
    :type teedev: struct tee_device \*

.. _`tee_device_unregister.description`:

Description
-----------

This function should be called to remove the \ ``teedev``\  even if
\ :c:func:`tee_device_register`\  hasn't been called yet. Does nothing if
\ ``teedev``\  is NULL.

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
        unsigned int offset;
        struct page **pages;
        size_t num_pages;
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

offset
    offset of buffer in user space

pages
    locked pages from userspace

num_pages
    number of locked pages

dmabuf
    dmabuf used to for exporting to user space

flags
    defined by TEE_SHM\_\* in tee_drv.h

id
    unique id of a shared memory object on this device

.. _`tee_shm.description`:

Description
-----------

This pool is only supposed to be accessed directly from the TEE
subsystem and from drivers that implements their own shm pool manager.

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
        void (*destroy_poolmgr)(struct tee_shm_pool_mgr *poolmgr);
    }

.. _`tee_shm_pool_mgr_ops.members`:

Members
-------

alloc
    called when allocating shared memory

free
    called when freeing shared memory

destroy_poolmgr
    called when destroying the pool manager

.. _`tee_shm_pool_alloc`:

tee_shm_pool_alloc
==================

.. c:function:: struct tee_shm_pool *tee_shm_pool_alloc(struct tee_shm_pool_mgr *priv_mgr, struct tee_shm_pool_mgr *dmabuf_mgr)

    Create a shared memory pool from shm managers

    :param priv_mgr:
        manager for driver private shared memory allocations
    :type priv_mgr: struct tee_shm_pool_mgr \*

    :param dmabuf_mgr:
        manager for dma-buf shared memory allocations
    :type dmabuf_mgr: struct tee_shm_pool_mgr \*

.. _`tee_shm_pool_alloc.description`:

Description
-----------

Allocation with the flag TEE_SHM_DMA_BUF set will use the range supplied
in \ ``dmabuf``\ , others will use the range provided by \ ``priv``\ .

\ ``returns``\  pointer to a 'struct tee_shm_pool' or an ERR_PTR on failure.

.. _`tee_shm_pool_mgr_destroy`:

tee_shm_pool_mgr_destroy
========================

.. c:function:: void tee_shm_pool_mgr_destroy(struct tee_shm_pool_mgr *poolm)

    Free a shared memory manager

    :param poolm:
        *undescribed*
    :type poolm: struct tee_shm_pool_mgr \*

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

    :param priv_info:
        Information for driver private shared memory pool
    :type priv_info: struct tee_shm_pool_mem_info \*

    :param dmabuf_info:
        Information for dma-buf shared memory pool
    :type dmabuf_info: struct tee_shm_pool_mem_info \*

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

    :param pool:
        The shared memory pool to free
    :type pool: struct tee_shm_pool \*

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

    :param teedev:
        *undescribed*
    :type teedev: struct tee_device \*

.. _`tee_shm_alloc`:

tee_shm_alloc
=============

.. c:function:: struct tee_shm *tee_shm_alloc(struct tee_context *ctx, size_t size, u32 flags)

    Allocate shared memory

    :param ctx:
        Context that allocates the shared memory
    :type ctx: struct tee_context \*

    :param size:
        Requested size of shared memory
    :type size: size_t

    :param flags:
        Flags setting properties for the requested shared memory.
    :type flags: u32

.. _`tee_shm_alloc.description`:

Description
-----------

Memory allocated as global shared memory is automatically freed when the
TEE file pointer is closed. The \ ``flags``\  field uses the bits defined by
TEE_SHM\_\* above. TEE_SHM_MAPPED must currently always be set. If
TEE_SHM_DMA_BUF global shared memory will be allocated and associated
with a dma-buf handle, else driver private memory.

\ ``returns``\  a pointer to 'struct tee_shm'

.. _`tee_shm_priv_alloc`:

tee_shm_priv_alloc
==================

.. c:function:: struct tee_shm *tee_shm_priv_alloc(struct tee_device *teedev, size_t size)

    Allocate shared memory privately

    :param teedev:
        *undescribed*
    :type teedev: struct tee_device \*

    :param size:
        Requested size of shared memory
    :type size: size_t

.. _`tee_shm_priv_alloc.description`:

Description
-----------

Allocates shared memory buffer that is not associated with any client
context. Such buffers are owned by TEE driver and used for internal calls.

\ ``returns``\  a pointer to 'struct tee_shm'

.. _`tee_shm_register`:

tee_shm_register
================

.. c:function:: struct tee_shm *tee_shm_register(struct tee_context *ctx, unsigned long addr, size_t length, u32 flags)

    Register shared memory buffer

    :param ctx:
        Context that registers the shared memory
    :type ctx: struct tee_context \*

    :param addr:
        Address is userspace of the shared buffer
    :type addr: unsigned long

    :param length:
        Length of the shared buffer
    :type length: size_t

    :param flags:
        Flags setting properties for the requested shared memory.
    :type flags: u32

.. _`tee_shm_register.description`:

Description
-----------

\ ``returns``\  a pointer to 'struct tee_shm'

.. _`tee_shm_is_registered`:

tee_shm_is_registered
=====================

.. c:function:: bool tee_shm_is_registered(struct tee_shm *shm)

    Check if shared memory object in registered in TEE

    :param shm:
        Shared memory handle
        \ ``returns``\  true if object is registered in TEE
    :type shm: struct tee_shm \*

.. _`tee_shm_free`:

tee_shm_free
============

.. c:function:: void tee_shm_free(struct tee_shm *shm)

    Free shared memory

    :param shm:
        Handle to shared memory to free
    :type shm: struct tee_shm \*

.. _`tee_shm_put`:

tee_shm_put
===========

.. c:function:: void tee_shm_put(struct tee_shm *shm)

    Decrease reference count on a shared memory handle

    :param shm:
        Shared memory handle
    :type shm: struct tee_shm \*

.. _`tee_shm_va2pa`:

tee_shm_va2pa
=============

.. c:function:: int tee_shm_va2pa(struct tee_shm *shm, void *va, phys_addr_t *pa)

    Get physical address of a virtual address

    :param shm:
        Shared memory handle
    :type shm: struct tee_shm \*

    :param va:
        Virtual address to tranlsate
    :type va: void \*

    :param pa:
        Returned physical address
        \ ``returns``\  0 on success and < 0 on failure
    :type pa: phys_addr_t \*

.. _`tee_shm_pa2va`:

tee_shm_pa2va
=============

.. c:function:: int tee_shm_pa2va(struct tee_shm *shm, phys_addr_t pa, void **va)

    Get virtual address of a physical address

    :param shm:
        Shared memory handle
    :type shm: struct tee_shm \*

    :param pa:
        Physical address to tranlsate
    :type pa: phys_addr_t

    :param va:
        Returned virtual address
        \ ``returns``\  0 on success and < 0 on failure
    :type va: void \*\*

.. _`tee_shm_get_va`:

tee_shm_get_va
==============

.. c:function:: void *tee_shm_get_va(struct tee_shm *shm, size_t offs)

    Get virtual address of a shared memory plus an offset

    :param shm:
        Shared memory handle
    :type shm: struct tee_shm \*

    :param offs:
        Offset from start of this shared memory
        \ ``returns``\  virtual address of the shared memory + offs if offs is within
        the bounds of this shared memory, else an ERR_PTR
    :type offs: size_t

.. _`tee_shm_get_pa`:

tee_shm_get_pa
==============

.. c:function:: int tee_shm_get_pa(struct tee_shm *shm, size_t offs, phys_addr_t *pa)

    Get physical address of a shared memory plus an offset

    :param shm:
        Shared memory handle
    :type shm: struct tee_shm \*

    :param offs:
        Offset from start of this shared memory
    :type offs: size_t

    :param pa:
        Physical address to return
        \ ``returns``\  0 if offs is within the bounds of this shared memory, else an
        error code.
    :type pa: phys_addr_t \*

.. _`tee_shm_get_size`:

tee_shm_get_size
================

.. c:function:: size_t tee_shm_get_size(struct tee_shm *shm)

    Get size of shared memory buffer

    :param shm:
        Shared memory handle
        \ ``returns``\  size of shared memory
    :type shm: struct tee_shm \*

.. _`tee_shm_get_pages`:

tee_shm_get_pages
=================

.. c:function:: struct page **tee_shm_get_pages(struct tee_shm *shm, size_t *num_pages)

    Get list of pages that hold shared buffer

    :param shm:
        Shared memory handle
    :type shm: struct tee_shm \*

    :param num_pages:
        Number of pages will be stored there
        \ ``returns``\  pointer to pages array
    :type num_pages: size_t \*

.. _`tee_shm_get_page_offset`:

tee_shm_get_page_offset
=======================

.. c:function:: size_t tee_shm_get_page_offset(struct tee_shm *shm)

    Get shared buffer offset from page start

    :param shm:
        Shared memory handle
        \ ``returns``\  page offset of shared buffer
    :type shm: struct tee_shm \*

.. _`tee_shm_get_id`:

tee_shm_get_id
==============

.. c:function:: int tee_shm_get_id(struct tee_shm *shm)

    Get id of a shared memory object

    :param shm:
        Shared memory handle
        \ ``returns``\  id
    :type shm: struct tee_shm \*

.. _`tee_shm_get_from_id`:

tee_shm_get_from_id
===================

.. c:function:: struct tee_shm *tee_shm_get_from_id(struct tee_context *ctx, int id)

    Find shared memory object and increase reference count

    :param ctx:
        Context owning the shared memory
    :type ctx: struct tee_context \*

    :param id:
        Id of shared memory object
        \ ``returns``\  a pointer to 'struct tee_shm' on success or an ERR_PTR on failure
    :type id: int

.. _`tee_client_open_context`:

tee_client_open_context
=======================

.. c:function:: struct tee_context *tee_client_open_context(struct tee_context *start, int (*match)(struct tee_ioctl_version_data *, const void *), const void *data, struct tee_ioctl_version_data *vers)

    Open a TEE context

    :param start:
        if not NULL, continue search after this context
    :type start: struct tee_context \*

    :param int (\*match)(struct tee_ioctl_version_data \*, const void \*):
        function to check TEE device

    :param data:
        data for match function
    :type data: const void \*

    :param vers:
        if not NULL, version data of TEE device of the context returned
    :type vers: struct tee_ioctl_version_data \*

.. _`tee_client_open_context.description`:

Description
-----------

This function does an operation similar to open("/dev/teeX") in user space.
A returned context must be released with \ :c:func:`tee_client_close_context`\ .

Returns a TEE context of the first TEE device matched by the \ :c:func:`match`\ 
callback or an ERR_PTR.

.. _`tee_client_close_context`:

tee_client_close_context
========================

.. c:function:: void tee_client_close_context(struct tee_context *ctx)

    Close a TEE context

    :param ctx:
        TEE context to close
    :type ctx: struct tee_context \*

.. _`tee_client_close_context.description`:

Description
-----------

Note that all sessions previously opened with this context will be
closed when this function is called.

.. _`tee_client_get_version`:

tee_client_get_version
======================

.. c:function:: void tee_client_get_version(struct tee_context *ctx, struct tee_ioctl_version_data *vers)

    Query version of TEE

    :param ctx:
        TEE context to TEE to query
    :type ctx: struct tee_context \*

    :param vers:
        Pointer to version data
    :type vers: struct tee_ioctl_version_data \*

.. _`tee_client_open_session`:

tee_client_open_session
=======================

.. c:function:: int tee_client_open_session(struct tee_context *ctx, struct tee_ioctl_open_session_arg *arg, struct tee_param *param)

    Open a session to a Trusted Application

    :param ctx:
        TEE context
    :type ctx: struct tee_context \*

    :param arg:
        Open session arguments, see description of
        struct tee_ioctl_open_session_arg
    :type arg: struct tee_ioctl_open_session_arg \*

    :param param:
        Parameters passed to the Trusted Application
    :type param: struct tee_param \*

.. _`tee_client_open_session.description`:

Description
-----------

Returns < 0 on error else see \ ``arg->ret``\  for result. If \ ``arg->ret``\ 
is TEEC_SUCCESS the session identifier is available in \ ``arg->session``\ .

.. _`tee_client_close_session`:

tee_client_close_session
========================

.. c:function:: int tee_client_close_session(struct tee_context *ctx, u32 session)

    Close a session to a Trusted Application

    :param ctx:
        TEE Context
    :type ctx: struct tee_context \*

    :param session:
        Session id
    :type session: u32

.. _`tee_client_close_session.description`:

Description
-----------

Return < 0 on error else 0, regardless the session will not be
valid after this function has returned.

.. _`tee_client_invoke_func`:

tee_client_invoke_func
======================

.. c:function:: int tee_client_invoke_func(struct tee_context *ctx, struct tee_ioctl_invoke_arg *arg, struct tee_param *param)

    Invoke a function in a Trusted Application

    :param ctx:
        TEE Context
    :type ctx: struct tee_context \*

    :param arg:
        Invoke arguments, see description of
        struct tee_ioctl_invoke_arg
    :type arg: struct tee_ioctl_invoke_arg \*

    :param param:
        Parameters passed to the Trusted Application
    :type param: struct tee_param \*

.. _`tee_client_invoke_func.description`:

Description
-----------

Returns < 0 on error else see \ ``arg->ret``\  for result.

.. This file was automatic generated / don't edit.

