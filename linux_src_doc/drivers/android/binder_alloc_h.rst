.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/android/binder_alloc.h

.. _`binder_buffer`:

struct binder_buffer
====================

.. c:type:: struct binder_buffer

    buffer used for binder transactions

.. _`binder_buffer.definition`:

Definition
----------

.. code-block:: c

    struct binder_buffer {
        struct list_head entry;
        struct rb_node rb_node;
        unsigned free:1;
        unsigned allow_user_free:1;
        unsigned async_transaction:1;
        unsigned free_in_progress:1;
        unsigned debug_id:28;
        struct binder_transaction *transaction;
        struct binder_node *target_node;
        size_t data_size;
        size_t offsets_size;
        size_t extra_buffers_size;
        void *data;
    }

.. _`binder_buffer.members`:

Members
-------

entry
    entry alloc->buffers

rb_node
    node for allocated_buffers/free_buffers rb trees

free
    true if buffer is free

allow_user_free
    describe the second member of struct blah,

async_transaction
    describe the second member of struct blah,

free_in_progress
    *undescribed*

debug_id
    describe the second member of struct blah,

transaction
    describe the second member of struct blah,

target_node
    describe the second member of struct blah,

data_size
    describe the second member of struct blah,

offsets_size
    describe the second member of struct blah,

extra_buffers_size
    describe the second member of struct blah,

data
    i              describe the second member of struct blah,

.. _`binder_buffer.description`:

Description
-----------

Bookkeeping structure for binder transaction buffers

.. _`binder_lru_page`:

struct binder_lru_page
======================

.. c:type:: struct binder_lru_page

    page object used for binder shrinker

.. _`binder_lru_page.definition`:

Definition
----------

.. code-block:: c

    struct binder_lru_page {
        struct list_head lru;
        struct page *page_ptr;
        struct binder_alloc *alloc;
    }

.. _`binder_lru_page.members`:

Members
-------

lru
    entry in binder_alloc_lru

page_ptr
    pointer to physical page in mmap'd space

alloc
    binder_alloc for a proc

.. _`binder_alloc`:

struct binder_alloc
===================

.. c:type:: struct binder_alloc

    per-binder proc state for binder allocator

.. _`binder_alloc.definition`:

Definition
----------

.. code-block:: c

    struct binder_alloc {
        struct mutex mutex;
        struct task_struct *tsk;
        struct vm_area_struct *vma;
        struct mm_struct *vma_vm_mm;
        void *buffer;
        ptrdiff_t user_buffer_offset;
        struct list_head buffers;
        struct rb_root free_buffers;
        struct rb_root allocated_buffers;
        size_t free_async_space;
        struct binder_lru_page *pages;
        size_t buffer_size;
        uint32_t buffer_free;
        int pid;
    }

.. _`binder_alloc.members`:

Members
-------

mutex
    *undescribed*

tsk
    tid for task that called init for this proc
    (invariant after init)

vma
    vm_area_struct passed to mmap_handler
    (invarient after mmap)

vma_vm_mm
    copy of vma->vm_mm (invarient after mmap)

buffer
    base of per-proc address space mapped via mmap

user_buffer_offset
    offset between user and kernel VAs for buffer

buffers
    list of all buffers for this proc

free_buffers
    rb tree of buffers available for allocation
    sorted by size

allocated_buffers
    rb tree of allocated buffers sorted by address

free_async_space
    VA space available for async buffers. This is
    initialized at mmap time to 1/2 the full VA space

pages
    array of binder_lru_page

buffer_size
    size of address space specified via mmap

buffer_free
    *undescribed*

pid
    pid for associated binder_proc (invariant after init)

.. _`binder_alloc.description`:

Description
-----------

Bookkeeping structure for per-proc address space management for binder
buffers. It is normally initialized during \ :c:func:`binder_init`\  and \ :c:func:`binder_mmap`\ 
calls. The address space is used for both user-visible buffers and for
struct binder_buffer objects used to track the user buffers

.. _`binder_alloc_get_free_async_space`:

binder_alloc_get_free_async_space
=================================

.. c:function:: size_t binder_alloc_get_free_async_space(struct binder_alloc *alloc)

    get free space available for async

    :param struct binder_alloc \*alloc:
        binder_alloc for this proc

.. _`binder_alloc_get_free_async_space.return`:

Return
------

the bytes remaining in the address-space for async transactions

.. _`binder_alloc_get_user_buffer_offset`:

binder_alloc_get_user_buffer_offset
===================================

.. c:function:: ptrdiff_t binder_alloc_get_user_buffer_offset(struct binder_alloc *alloc)

    get offset between kernel/user addrs

    :param struct binder_alloc \*alloc:
        binder_alloc for this proc

.. _`binder_alloc_get_user_buffer_offset.return`:

Return
------

the offset between kernel and user-space addresses to use for
virtual address conversion

.. This file was automatic generated / don't edit.

