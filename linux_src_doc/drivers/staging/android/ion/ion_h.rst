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
        phys_addr_t base;
        size_t size;
        phys_addr_t align;
        void *priv;
    }

.. _`ion_platform_heap.members`:

Members
-------

type
    type of the heap from ion_heap_type enum

id
    unique identifier for heap.  When allocating higher numb ers
    will be allocated from first.  At allocation these are passed
    as a bit mask and therefore can not exceed ION_NUM_HEAP_IDS.

name
    used for debug purposes

base
    base address of heap in physical memory if applicable

size
    size of the heap in bytes if applicable

align
    *undescribed*

priv
    private info passed from the board file

.. _`ion_platform_heap.description`:

Description
-----------

Provided by the board file.

.. _`ion_buffer`:

struct ion_buffer
=================

.. c:type:: struct ion_buffer

    metadata for a particular buffer

.. _`ion_buffer.definition`:

Definition
----------

.. code-block:: c

    struct ion_buffer {
        union {unnamed_union};
        struct ion_device *dev;
        struct ion_heap *heap;
        unsigned long flags;
        unsigned long private_flags;
        size_t size;
        void *priv_virt;
        struct mutex lock;
        int kmap_cnt;
        void *vaddr;
        struct sg_table *sg_table;
        struct page **pages;
        struct list_head vmas;
        struct list_head attachments;
        int handle_count;
        char task_comm;
        pid_t pid;
    }

.. _`ion_buffer.members`:

Members
-------

{unnamed_union}
    anonymous


dev
    back pointer to the ion_device

heap
    back pointer to the heap the buffer came from

flags
    buffer specific flags

private_flags
    internal buffer specific flags

size
    size of the buffer

priv_virt
    private data to the buffer representable as
    a void \*

lock
    protects the buffers cnt fields

kmap_cnt
    number of times the buffer is mapped to the kernel

vaddr
    the kernel mapping if kmap_cnt is not zero

sg_table
    the sg table for the buffer if dmap_cnt is not zero

pages
    flat array of pages in the buffer -- used by fault
    handler and only valid for buffers that are faulted in

vmas
    list of vma's mapping this buffer

attachments
    *undescribed*

handle_count
    count of handles referencing this buffer

task_comm
    taskcomm of last client to reference this buffer in a
    handle, used for debugging

pid
    pid of last client to reference this buffer in a
    handle, used for debugging

.. _`ion_device`:

struct ion_device
=================

.. c:type:: struct ion_device

    the metadata of the ion device node

.. _`ion_device.definition`:

Definition
----------

.. code-block:: c

    struct ion_device {
        struct miscdevice dev;
        struct rb_root buffers;
        struct mutex buffer_lock;
        struct rw_semaphore lock;
        struct plist_head heaps;
        struct dentry *debug_root;
        int heap_cnt;
    }

.. _`ion_device.members`:

Members
-------

dev
    the actual misc device

buffers
    an rb tree of all the existing buffers

buffer_lock
    lock protecting the tree of buffers

lock
    rwsem protecting the tree of heaps and clients

heaps
    *undescribed*

debug_root
    *undescribed*

heap_cnt
    *undescribed*

.. _`ion_heap_ops`:

struct ion_heap_ops
===================

.. c:type:: struct ion_heap_ops

    ops to operate on a given heap

.. _`ion_heap_ops.definition`:

Definition
----------

.. code-block:: c

    struct ion_heap_ops {
        int (*allocate)(struct ion_heap *heap,struct ion_buffer *buffer, unsigned long len,unsigned long flags);
        void (*free)(struct ion_buffer *buffer);
        void * (*map_kernel)(struct ion_heap *heap, struct ion_buffer *buffer);
        void (*unmap_kernel)(struct ion_heap *heap, struct ion_buffer *buffer);
        int (*map_user)(struct ion_heap *mapper, struct ion_buffer *buffer,struct vm_area_struct *vma);
        int (*shrink)(struct ion_heap *heap, gfp_t gfp_mask, int nr_to_scan);
    }

.. _`ion_heap_ops.members`:

Members
-------

allocate
    allocate memory

free
    free memory
    \ ``map_kernel``\           map memory to the kernel
    \ ``unmap_kernel``\         unmap memory to the kernel
    \ ``map_user``\             map memory to userspace

map_kernel
    *undescribed*

unmap_kernel
    *undescribed*

map_user
    *undescribed*

shrink
    *undescribed*

.. _`ion_heap_ops.description`:

Description
-----------

allocate, phys, and map_user return 0 on success, -errno on error.
map_dma and map_kernel return pointer on success, ERR_PTR on
error. \ ``free``\  will be called with ION_PRIV_FLAG_SHRINKER_FREE set in
the buffer's private_flags when called from a shrinker. In that
case, the pages being free'd must be truly free'd back to the
system, not put in a page pool or otherwise cached.

.. _`ion_heap_flag_defer_free`:

ION_HEAP_FLAG_DEFER_FREE
========================

.. c:function::  ION_HEAP_FLAG_DEFER_FREE()

    flags between the heaps and core ion code

.. _`ion_priv_flag_shrinker_free`:

ION_PRIV_FLAG_SHRINKER_FREE
===========================

.. c:function::  ION_PRIV_FLAG_SHRINKER_FREE()

    flags internal to ion

.. _`ion_heap`:

struct ion_heap
===============

.. c:type:: struct ion_heap

    represents a heap in the system

.. _`ion_heap.definition`:

Definition
----------

.. code-block:: c

    struct ion_heap {
        struct plist_node node;
        struct ion_device *dev;
        enum ion_heap_type type;
        struct ion_heap_ops *ops;
        unsigned long flags;
        unsigned int id;
        const char *name;
        struct shrinker shrinker;
        struct list_head free_list;
        size_t free_list_size;
        spinlock_t free_lock;
        wait_queue_head_t waitqueue;
        struct task_struct *task;
        int (*debug_show)(struct ion_heap *heap, struct seq_file *, void *);
    }

.. _`ion_heap.members`:

Members
-------

node
    rb node to put the heap on the device's tree of heaps

dev
    back pointer to the ion_device

type
    type of heap

ops
    ops struct as above

flags
    flags

id
    id of heap, also indicates priority of this heap when
    allocating.  These are specified by platform data and
    MUST be unique

name
    used for debugging

shrinker
    a shrinker for the heap

free_list
    free list head if deferred free is used
    \ ``free_list_size``\       size of the deferred free list in bytes

free_list_size
    *undescribed*

free_lock
    *undescribed*

waitqueue
    queue to wait on from deferred free thread

task
    task struct of deferred free thread

debug_show
    called when heap debug file is read to add any
    heap specific debug info to output

.. _`ion_heap.description`:

Description
-----------

Represents a pool of memory from which buffers can be made.  In some
systems the only heap is regular system memory allocated via vmalloc.
On others, some blocks might require large physically contiguous buffers
that are allocated from a specially reserved heap.

.. _`ion_buffer_cached`:

ion_buffer_cached
=================

.. c:function:: bool ion_buffer_cached(struct ion_buffer *buffer)

    this ion buffer is cached

    :param struct ion_buffer \*buffer:
        buffer

.. _`ion_buffer_cached.description`:

Description
-----------

indicates whether this ion buffer is cached

.. _`ion_buffer_fault_user_mappings`:

ion_buffer_fault_user_mappings
==============================

.. c:function:: bool ion_buffer_fault_user_mappings(struct ion_buffer *buffer)

    fault in user mappings of this buffer

    :param struct ion_buffer \*buffer:
        buffer

.. _`ion_buffer_fault_user_mappings.description`:

Description
-----------

indicates whether userspace mappings of this buffer will be faulted
in, this can affect how buffers are allocated from the heap.

.. _`ion_device_add_heap`:

ion_device_add_heap
===================

.. c:function:: void ion_device_add_heap(struct ion_heap *heap)

    adds a heap to the ion device

    :param struct ion_heap \*heap:
        the heap to add

.. _`ion_heap_map_kernel`:

ion_heap_map_kernel
===================

.. c:function:: void *ion_heap_map_kernel(struct ion_heap *heap, struct ion_buffer *buffer)

    and vaddr fields

    :param struct ion_heap \*heap:
        *undescribed*

    :param struct ion_buffer \*buffer:
        *undescribed*

.. _`ion_heap_init_shrinker`:

ion_heap_init_shrinker
======================

.. c:function:: void ion_heap_init_shrinker(struct ion_heap *heap)

    :param struct ion_heap \*heap:
        the heap

.. _`ion_heap_init_shrinker.description`:

Description
-----------

If a heap sets the ION_HEAP_FLAG_DEFER_FREE flag or defines the shrink op
this function will be called to setup a shrinker to shrink the freelists
and call the heap's shrink op.

.. _`ion_heap_init_deferred_free`:

ion_heap_init_deferred_free
===========================

.. c:function:: int ion_heap_init_deferred_free(struct ion_heap *heap)

    - initialize deferred free functionality

    :param struct ion_heap \*heap:
        the heap

.. _`ion_heap_init_deferred_free.description`:

Description
-----------

If a heap sets the ION_HEAP_FLAG_DEFER_FREE flag this function will
be called to setup deferred frees. Calls to free the buffer will
return immediately and the actual free will occur some time later

.. _`ion_heap_freelist_add`:

ion_heap_freelist_add
=====================

.. c:function:: void ion_heap_freelist_add(struct ion_heap *heap, struct ion_buffer *buffer)

    add a buffer to the deferred free list

    :param struct ion_heap \*heap:
        the heap

    :param struct ion_buffer \*buffer:
        the buffer

.. _`ion_heap_freelist_add.description`:

Description
-----------

Adds an item to the deferred freelist.

.. _`ion_heap_freelist_drain`:

ion_heap_freelist_drain
=======================

.. c:function:: size_t ion_heap_freelist_drain(struct ion_heap *heap, size_t size)

    drain the deferred free list

    :param struct ion_heap \*heap:
        the heap

    :param size_t size:
        amount of memory to drain in bytes

.. _`ion_heap_freelist_drain.description`:

Description
-----------

Drains the indicated amount of memory from the deferred freelist immediately.
Returns the total amount freed.  The total freed may be higher depending
on the size of the items in the list, or lower if there is insufficient
total memory on the freelist.

.. _`ion_heap_freelist_shrink`:

ion_heap_freelist_shrink
========================

.. c:function:: size_t ion_heap_freelist_shrink(struct ion_heap *heap, size_t size)

    drain the deferred free list, skipping any heap-specific pooling or caching mechanisms

    :param struct ion_heap \*heap:
        the heap

    :param size_t size:
        amount of memory to drain in bytes

.. _`ion_heap_freelist_shrink.description`:

Description
-----------

Drains the indicated amount of memory from the deferred freelist immediately.
Returns the total amount freed.  The total freed may be higher depending
on the size of the items in the list, or lower if there is insufficient
total memory on the freelist.

Unlike with \ ``ion_heap_freelist_drain``\ , don't put any pages back into
page pools or otherwise cache the pages. Everything must be
genuinely free'd back to the system. If you're free'ing from a
shrinker you probably want to use this. Note that this relies on
the heap.ops.free callback honoring the ION_PRIV_FLAG_SHRINKER_FREE
flag.

.. _`ion_heap_freelist_size`:

ion_heap_freelist_size
======================

.. c:function:: size_t ion_heap_freelist_size(struct ion_heap *heap)

    returns the size of the freelist in bytes

    :param struct ion_heap \*heap:
        the heap

.. This file was automatic generated / don't edit.

