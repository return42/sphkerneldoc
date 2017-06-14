.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/android/uapi/ion.h

.. _`ion_heap_type`:

enum ion_heap_type
==================

.. c:type:: enum ion_heap_type

    list of all possible types of heaps

.. _`ion_heap_type.definition`:

Definition
----------

.. code-block:: c

    enum ion_heap_type {
        ION_HEAP_TYPE_SYSTEM,
        ION_HEAP_TYPE_SYSTEM_CONTIG,
        ION_HEAP_TYPE_CARVEOUT,
        ION_HEAP_TYPE_CHUNK,
        ION_HEAP_TYPE_DMA,
        ION_HEAP_TYPE_CUSTOM
    };

.. _`ion_heap_type.constants`:

Constants
---------

ION_HEAP_TYPE_SYSTEM
    memory allocated via vmalloc

ION_HEAP_TYPE_SYSTEM_CONTIG
    memory allocated via kmalloc

ION_HEAP_TYPE_CARVEOUT
    memory allocated from a prereserved
    carveout heap, allocations are physically
    contiguous

ION_HEAP_TYPE_CHUNK
    *undescribed*

ION_HEAP_TYPE_DMA
    memory allocated via DMA API

ION_HEAP_TYPE_CUSTOM
    *undescribed*

.. _`ion_flag_cached`:

ION_FLAG_CACHED
===============

.. c:function::  ION_FLAG_CACHED()

    the lower 16 bits are used by core ion, the upper 16 bits are reserved for use by the heaps themselves.

.. _`ion-userspace-api`:

Ion Userspace API
=================

create a client by opening /dev/ion
most operations handled via following ioctls

.. _`ion_allocation_data`:

struct ion_allocation_data
==========================

.. c:type:: struct ion_allocation_data

    metadata passed from userspace for allocations

.. _`ion_allocation_data.definition`:

Definition
----------

.. code-block:: c

    struct ion_allocation_data {
        __u64 len;
        __u32 heap_id_mask;
        __u32 flags;
        __u32 fd;
        __u32 unused;
    }

.. _`ion_allocation_data.members`:

Members
-------

len
    size of the allocation

heap_id_mask
    mask of heap ids to allocate from

flags
    flags passed to heap

fd
    *undescribed*

unused
    *undescribed*

.. _`ion_allocation_data.description`:

Description
-----------

Provided by userspace as an argument to the ioctl

.. _`ion_heap_data`:

struct ion_heap_data
====================

.. c:type:: struct ion_heap_data

    data about a heap \ ``name``\  - first 32 characters of the heap name \ ``type``\  - heap type \ ``heap_id``\  - heap id for the heap

.. _`ion_heap_data.definition`:

Definition
----------

.. code-block:: c

    struct ion_heap_data {
        char name;
        __u32 type;
        __u32 heap_id;
        __u32 reserved0;
        __u32 reserved1;
        __u32 reserved2;
    }

.. _`ion_heap_data.members`:

Members
-------

name
    *undescribed*

type
    *undescribed*

heap_id
    *undescribed*

reserved0
    *undescribed*

reserved1
    *undescribed*

reserved2
    *undescribed*

.. _`ion_heap_query`:

struct ion_heap_query
=====================

.. c:type:: struct ion_heap_query

    collection of data about all heaps \ ``cnt``\  - total number of heaps to be copied \ ``heaps``\  - buffer to copy heap data

.. _`ion_heap_query.definition`:

Definition
----------

.. code-block:: c

    struct ion_heap_query {
        __u32 cnt;
        __u32 reserved0;
        __u64 heaps;
        __u32 reserved1;
        __u32 reserved2;
    }

.. _`ion_heap_query.members`:

Members
-------

cnt
    *undescribed*

reserved0
    *undescribed*

heaps
    *undescribed*

reserved1
    *undescribed*

reserved2
    *undescribed*

.. _`ion_ioc_alloc---allocate-memory`:

ION_IOC_ALLOC - allocate memory
===============================

Takes an ion_allocation_data struct and returns it with the handle field
populated with the opaque handle for the allocation.

.. _`ion_ioc_free---free-memory`:

ION_IOC_FREE - free memory
==========================

Takes an ion_handle_data struct and frees the handle.

.. _`ion_ioc_share---creates-a-file-descriptor-to-use-to-share-an-allocation`:

ION_IOC_SHARE - creates a file descriptor to use to share an allocation
=======================================================================

Takes an ion_fd_data struct with the handle field populated with a valid
opaque handle.  Returns the struct with the fd field set to a file
descriptor open in the current address space.  This file descriptor
can then be passed to another process.  The corresponding opaque handle can
be retrieved via ION_IOC_IMPORT.

.. _`ion_ioc_heap_query---information-about-available-heaps`:

ION_IOC_HEAP_QUERY - information about available heaps
======================================================

Takes an ion_heap_query structure and populates information about
available Ion heaps.

.. This file was automatic generated / don't edit.

