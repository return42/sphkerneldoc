.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tee/tee_shm.c

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
TEE_SHM\_\* in <linux/tee_drv.h>. TEE_SHM_MAPPED must currently always be
set. If TEE_SHM_DMA_BUF global shared memory will be allocated and
associated with a dma-buf handle, else driver private memory.

.. _`tee_shm_get_fd`:

tee_shm_get_fd
==============

.. c:function:: int tee_shm_get_fd(struct tee_shm *shm)

    Increase reference count and return file descriptor

    :param shm:
        Shared memory handle
        \ ``returns``\  user space file descriptor to shared memory
    :type shm: struct tee_shm \*

.. _`tee_shm_free`:

tee_shm_free
============

.. c:function:: void tee_shm_free(struct tee_shm *shm)

    Free shared memory

    :param shm:
        Handle to shared memory to free
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

.. _`tee_shm_put`:

tee_shm_put
===========

.. c:function:: void tee_shm_put(struct tee_shm *shm)

    Decrease reference count on a shared memory handle

    :param shm:
        Shared memory handle
    :type shm: struct tee_shm \*

.. This file was automatic generated / don't edit.

