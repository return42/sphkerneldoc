.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/android/binder_alloc.c

.. _`binder_alloc_prepare_to_free`:

binder_alloc_prepare_to_free
============================

.. c:function:: struct binder_buffer *binder_alloc_prepare_to_free(struct binder_alloc *alloc, uintptr_t user_ptr)

    get buffer given user ptr

    :param alloc:
        binder_alloc for this proc
    :type alloc: struct binder_alloc \*

    :param user_ptr:
        User pointer to buffer data
    :type user_ptr: uintptr_t

.. _`binder_alloc_prepare_to_free.description`:

Description
-----------

Validate userspace pointer to buffer data and return buffer corresponding to
that user pointer. Search the rb tree for buffer that matches user data
pointer.

.. _`binder_alloc_prepare_to_free.return`:

Return
------

Pointer to buffer or NULL

.. _`binder_alloc_new_buf`:

binder_alloc_new_buf
====================

.. c:function:: struct binder_buffer *binder_alloc_new_buf(struct binder_alloc *alloc, size_t data_size, size_t offsets_size, size_t extra_buffers_size, int is_async)

    Allocate a new binder buffer

    :param alloc:
        binder_alloc for this proc
    :type alloc: struct binder_alloc \*

    :param data_size:
        size of user data buffer
    :type data_size: size_t

    :param offsets_size:
        user specified buffer offset
    :type offsets_size: size_t

    :param extra_buffers_size:
        size of extra space for meta-data (eg, security context)
    :type extra_buffers_size: size_t

    :param is_async:
        buffer for async transaction
    :type is_async: int

.. _`binder_alloc_new_buf.description`:

Description
-----------

Allocate a new buffer given the requested sizes. Returns
the kernel version of the buffer pointer. The size allocated
is the sum of the three given sizes (each rounded up to
pointer-sized boundary)

.. _`binder_alloc_new_buf.return`:

Return
------

The allocated buffer or \ ``NULL``\  if error

.. _`binder_alloc_free_buf`:

binder_alloc_free_buf
=====================

.. c:function:: void binder_alloc_free_buf(struct binder_alloc *alloc, struct binder_buffer *buffer)

    free a binder buffer

    :param alloc:
        binder_alloc for this proc
    :type alloc: struct binder_alloc \*

    :param buffer:
        kernel pointer to buffer
    :type buffer: struct binder_buffer \*

.. _`binder_alloc_free_buf.description`:

Description
-----------

Free the buffer allocated via \ :c:func:`binder_alloc_new_buffer`\ 

.. _`binder_alloc_mmap_handler`:

binder_alloc_mmap_handler
=========================

.. c:function:: int binder_alloc_mmap_handler(struct binder_alloc *alloc, struct vm_area_struct *vma)

    map virtual address space for proc

    :param alloc:
        alloc structure for this proc
    :type alloc: struct binder_alloc \*

    :param vma:
        vma passed to \ :c:func:`mmap`\ 
    :type vma: struct vm_area_struct \*

.. _`binder_alloc_mmap_handler.description`:

Description
-----------

Called by \ :c:func:`binder_mmap`\  to initialize the space specified in
vma for allocating binder buffers

.. _`binder_alloc_mmap_handler.return`:

Return
------

0 = success
-EBUSY = address space already mapped
-ENOMEM = failed to map memory to given address space

.. _`binder_alloc_print_allocated`:

binder_alloc_print_allocated
============================

.. c:function:: void binder_alloc_print_allocated(struct seq_file *m, struct binder_alloc *alloc)

    print buffer info

    :param m:
        seq_file for output via \ :c:func:`seq_printf`\ 
    :type m: struct seq_file \*

    :param alloc:
        binder_alloc for this proc
    :type alloc: struct binder_alloc \*

.. _`binder_alloc_print_allocated.description`:

Description
-----------

Prints information about every buffer associated with
the binder_alloc state to the given seq_file

.. _`binder_alloc_print_pages`:

binder_alloc_print_pages
========================

.. c:function:: void binder_alloc_print_pages(struct seq_file *m, struct binder_alloc *alloc)

    print page usage

    :param m:
        seq_file for output via \ :c:func:`seq_printf`\ 
    :type m: struct seq_file \*

    :param alloc:
        binder_alloc for this proc
    :type alloc: struct binder_alloc \*

.. _`binder_alloc_get_allocated_count`:

binder_alloc_get_allocated_count
================================

.. c:function:: int binder_alloc_get_allocated_count(struct binder_alloc *alloc)

    return count of buffers

    :param alloc:
        binder_alloc for this proc
    :type alloc: struct binder_alloc \*

.. _`binder_alloc_get_allocated_count.return`:

Return
------

count of allocated buffers

.. _`binder_alloc_vma_close`:

binder_alloc_vma_close
======================

.. c:function:: void binder_alloc_vma_close(struct binder_alloc *alloc)

    invalidate address space

    :param alloc:
        binder_alloc for this proc
    :type alloc: struct binder_alloc \*

.. _`binder_alloc_vma_close.description`:

Description
-----------

Called from \ :c:func:`binder_vma_close`\  when releasing address space.
Clears alloc->vma to prevent new incoming transactions from
allocating more buffers.

.. _`binder_alloc_free_page`:

binder_alloc_free_page
======================

.. c:function:: enum lru_status binder_alloc_free_page(struct list_head *item, struct list_lru_one *lru, spinlock_t *lock, void *cb_arg)

    shrinker callback to free pages

    :param item:
        item to free
    :type item: struct list_head \*

    :param lru:
        *undescribed*
    :type lru: struct list_lru_one \*

    :param lock:
        lock protecting the item
    :type lock: spinlock_t \*

    :param cb_arg:
        callback argument
    :type cb_arg: void \*

.. _`binder_alloc_free_page.description`:

Description
-----------

Called from \ :c:func:`list_lru_walk`\  in \ :c:func:`binder_shrink_scan`\  to free
up pages when the system is under memory pressure.

.. _`binder_alloc_init`:

binder_alloc_init
=================

.. c:function:: void binder_alloc_init(struct binder_alloc *alloc)

    called by \ :c:func:`binder_open`\  for per-proc initialization

    :param alloc:
        binder_alloc for this proc
    :type alloc: struct binder_alloc \*

.. _`binder_alloc_init.description`:

Description
-----------

Called from \ :c:func:`binder_open`\  to initialize binder_alloc fields for
new binder proc

.. This file was automatic generated / don't edit.

