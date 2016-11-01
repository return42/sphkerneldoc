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
        size_t len;
        size_t align;
        unsigned int heap_id_mask;
        unsigned int flags;
        ion_user_handle_t handle;
    }

.. _`ion_allocation_data.members`:

Members
-------

len
    size of the allocation

align
    required alignment of the allocation

heap_id_mask
    mask of heap ids to allocate from

flags
    flags passed to heap

handle
    pointer that will be populated with a cookie to use to
    refer to this allocation

.. _`ion_allocation_data.description`:

Description
-----------

Provided by userspace as an argument to the ioctl

.. _`ion_fd_data`:

struct ion_fd_data
==================

.. c:type:: struct ion_fd_data

    metadata passed to/from userspace for a handle/fd pair

.. _`ion_fd_data.definition`:

Definition
----------

.. code-block:: c

    struct ion_fd_data {
        ion_user_handle_t handle;
        int fd;
    }

.. _`ion_fd_data.members`:

Members
-------

handle
    a handle

fd
    a file descriptor representing that handle

.. _`ion_fd_data.description`:

Description
-----------

For ION_IOC_SHARE or ION_IOC_MAP userspace populates the handle field with
the handle returned from ion alloc, and the kernel returns the file
descriptor to share or map in the fd field.  For ION_IOC_IMPORT, userspace
provides the file descriptor and the kernel returns the handle.

.. _`ion_handle_data`:

struct ion_handle_data
======================

.. c:type:: struct ion_handle_data

    a handle passed to/from the kernel

.. _`ion_handle_data.definition`:

Definition
----------

.. code-block:: c

    struct ion_handle_data {
        ion_user_handle_t handle;
    }

.. _`ion_handle_data.members`:

Members
-------

handle
    a handle

.. _`ion_custom_data`:

struct ion_custom_data
======================

.. c:type:: struct ion_custom_data

    metadata passed to/from userspace for a custom ioctl

.. _`ion_custom_data.definition`:

Definition
----------

.. code-block:: c

    struct ion_custom_data {
        unsigned int cmd;
        unsigned long arg;
    }

.. _`ion_custom_data.members`:

Members
-------

cmd
    the custom ioctl function to call

arg
    additional data to pass to the custom ioctl, typically a user
    pointer to a predefined structure

.. _`ion_custom_data.description`:

Description
-----------

This works just like the regular cmd and arg fields of an ioctl.

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
        char name[MAX_HEAP_NAME];
        __u32 type;
        __u32 heap_id;
        __u32 reserved0;
        __u32 reserved1;
        __u32 reserved2;
    }

.. _`ion_heap_data.members`:

Members
-------

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

.. This file was automatic generated / don't edit.

