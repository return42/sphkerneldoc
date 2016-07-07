.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/android/ion/ion.h

.. _`ion_platform_heap`:

struct ion_platform_heap
========================

.. c:type:: struct ion_platform_heap

    defines a heap in the given platform

.. _`ion_platform_heap.definition`:

Definition
----------

.. code-block:: c

    struct ion_platform_heap {
        enum ion_heap_type type;
        unsigned int id;
        const char *name;
        ion_phys_addr_t base;
        size_t size;
        ion_phys_addr_t align;
        void *priv;
    }

.. _`ion_platform_heap.members`:

Members
-------

type
    type of the heap from ion_heap_type enum

id
    unique identifier for heap.  When allocating higher numbers
    will be allocated from first.  At allocation these are passed
    as a bit mask and therefore can not exceed ION_NUM_HEAP_IDS.

name
    used for debug purposes

base
    base address of heap in physical memory if applicable

size
    size of the heap in bytes if applicable

align
    required alignment in physical memory if applicable

priv
    private info passed from the board file

.. _`ion_platform_heap.description`:

Description
-----------

Provided by the board file.

.. _`ion_platform_data`:

struct ion_platform_data
========================

.. c:type:: struct ion_platform_data

    array of platform heaps passed from board file

.. _`ion_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct ion_platform_data {
        int nr;
        struct ion_platform_heap *heaps;
    }

.. _`ion_platform_data.members`:

Members
-------

nr
    number of structures in the array

heaps
    array of platform_heap structions

.. _`ion_platform_data.description`:

Description
-----------

Provided by the board file in the form of platform data to a platform device.

.. _`ion_reserve`:

ion_reserve
===========

.. c:function:: void ion_reserve(struct ion_platform_data *data)

    reserve memory for ion heaps if applicable

    :param struct ion_platform_data \*data:
        platform data specifying starting physical address and
        size

.. _`ion_reserve.description`:

Description
-----------

Calls memblock reserve to set aside memory for heaps that are
located at specific memory addresses or of specific sizes not
managed by the kernel

.. _`ion_client_create`:

ion_client_create
=================

.. c:function:: struct ion_client *ion_client_create(struct ion_device *dev, const char *name)

    allocate a client and returns it

    :param struct ion_device \*dev:
        the global ion device

    :param const char \*name:
        used for debugging

.. _`ion_client_destroy`:

ion_client_destroy
==================

.. c:function:: void ion_client_destroy(struct ion_client *client)

    free's a client and all it's handles

    :param struct ion_client \*client:
        the client

.. _`ion_client_destroy.description`:

Description
-----------

Free the provided client and all it's resources including
any handles it is holding.

.. _`ion_alloc`:

ion_alloc
=========

.. c:function:: struct ion_handle *ion_alloc(struct ion_client *client, size_t len, size_t align, unsigned int heap_id_mask, unsigned int flags)

    allocate ion memory

    :param struct ion_client \*client:
        the client

    :param size_t len:
        size of the allocation

    :param size_t align:
        requested allocation alignment, lots of hardware blocks
        have alignment requirements of some kind

    :param unsigned int heap_id_mask:
        mask of heaps to allocate from, if multiple bits are set
        heaps will be tried in order from highest to lowest
        id

    :param unsigned int flags:
        heap flags, the low 16 bits are consumed by ion, the
        high 16 bits are passed on to the respective heap and
        can be heap custom

.. _`ion_alloc.description`:

Description
-----------

Allocate memory in one of the heaps provided in heap mask and return
an opaque handle to it.

.. _`ion_free`:

ion_free
========

.. c:function:: void ion_free(struct ion_client *client, struct ion_handle *handle)

    free a handle

    :param struct ion_client \*client:
        the client

    :param struct ion_handle \*handle:
        the handle to free

.. _`ion_free.description`:

Description
-----------

Free the provided handle.

.. _`ion_phys`:

ion_phys
========

.. c:function:: int ion_phys(struct ion_client *client, struct ion_handle *handle, ion_phys_addr_t *addr, size_t *len)

    returns the physical address and len of a handle

    :param struct ion_client \*client:
        the client

    :param struct ion_handle \*handle:
        the handle

    :param ion_phys_addr_t \*addr:
        a pointer to put the address in

    :param size_t \*len:
        a pointer to put the length in

.. _`ion_phys.description`:

Description
-----------

This function queries the heap for a particular handle to get the
handle's physical address.  It't output is only correct if
a heap returns physically contiguous memory -- in other cases
this api should not be implemented -- ion_sg_table should be used
instead.  Returns -EINVAL if the handle is invalid.  This has
no implications on the reference counting of the handle --
the returned value may not be valid if the caller is not
holding a reference.

.. _`ion_sg_table`:

ion_sg_table
============

.. c:function:: struct sg_table *ion_sg_table(struct ion_client *client, struct ion_handle *handle)

    return an sg_table describing a handle

    :param struct ion_client \*client:
        the client

    :param struct ion_handle \*handle:
        the handle

.. _`ion_sg_table.description`:

Description
-----------

This function returns the sg_table describing
a particular ion handle.

.. _`ion_map_kernel`:

ion_map_kernel
==============

.. c:function:: void *ion_map_kernel(struct ion_client *client, struct ion_handle *handle)

    create mapping for the given handle

    :param struct ion_client \*client:
        the client

    :param struct ion_handle \*handle:
        handle to map

.. _`ion_map_kernel.description`:

Description
-----------

Map the given handle into the kernel and return a kernel address that
can be used to access this address.

.. _`ion_unmap_kernel`:

ion_unmap_kernel
================

.. c:function:: void ion_unmap_kernel(struct ion_client *client, struct ion_handle *handle)

    destroy a kernel mapping for a handle

    :param struct ion_client \*client:
        the client

    :param struct ion_handle \*handle:
        handle to unmap

.. _`ion_share_dma_buf`:

ion_share_dma_buf
=================

.. c:function:: struct dma_buf *ion_share_dma_buf(struct ion_client *client, struct ion_handle *handle)

    share buffer as dma-buf

    :param struct ion_client \*client:
        the client

    :param struct ion_handle \*handle:
        the handle

.. _`ion_share_dma_buf_fd`:

ion_share_dma_buf_fd
====================

.. c:function:: int ion_share_dma_buf_fd(struct ion_client *client, struct ion_handle *handle)

    given an ion client, create a dma-buf fd

    :param struct ion_client \*client:
        the client

    :param struct ion_handle \*handle:
        the handle

.. _`ion_import_dma_buf`:

ion_import_dma_buf
==================

.. c:function:: struct ion_handle *ion_import_dma_buf(struct ion_client *client, struct dma_buf *dmabuf)

    get ion_handle from dma-buf

    :param struct ion_client \*client:
        the client

    :param struct dma_buf \*dmabuf:
        the dma-buf

.. _`ion_import_dma_buf.description`:

Description
-----------

Get the ion_buffer associated with the dma-buf and return the ion_handle.
If no ion_handle exists for this buffer, return newly created ion_handle.
If dma-buf from another exporter is passed, return ERR_PTR(-EINVAL)

.. _`ion_import_dma_buf_fd`:

ion_import_dma_buf_fd
=====================

.. c:function:: struct ion_handle *ion_import_dma_buf_fd(struct ion_client *client, int fd)

    given a dma-buf fd from the ion exporter get handle

    :param struct ion_client \*client:
        the client

    :param int fd:
        the dma-buf fd

.. _`ion_import_dma_buf_fd.description`:

Description
-----------

Given an dma-buf fd that was allocated through ion via ion_share_dma_buf_fd,
import that fd and return a handle representing it. If a dma-buf from
another exporter is passed in this function will return ERR_PTR(-EINVAL)

.. This file was automatic generated / don't edit.

