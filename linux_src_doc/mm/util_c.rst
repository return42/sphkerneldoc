.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/util.c

.. _`kfree_const`:

kfree_const
===========

.. c:function:: void kfree_const(const void *x)

    conditionally free memory

    :param const void \*x:
        pointer to the memory

.. _`kfree_const.description`:

Description
-----------

Function calls kfree only if \ ``x``\  is not in .rodata section.

.. _`kstrdup`:

kstrdup
=======

.. c:function:: char *kstrdup(const char *s, gfp_t gfp)

    allocate space for and copy an existing string

    :param const char \*s:
        the string to duplicate

    :param gfp_t gfp:
        the GFP mask used in the \ :c:func:`kmalloc`\  call when allocating memory

.. _`kstrdup_const`:

kstrdup_const
=============

.. c:function:: const char *kstrdup_const(const char *s, gfp_t gfp)

    conditionally duplicate an existing const string

    :param const char \*s:
        the string to duplicate

    :param gfp_t gfp:
        the GFP mask used in the \ :c:func:`kmalloc`\  call when allocating memory

.. _`kstrdup_const.description`:

Description
-----------

Function returns source string if it is in .rodata section otherwise it
fallbacks to kstrdup.
Strings allocated by kstrdup_const should be freed by kfree_const.

.. _`kstrndup`:

kstrndup
========

.. c:function:: char *kstrndup(const char *s, size_t max, gfp_t gfp)

    allocate space for and copy an existing string

    :param const char \*s:
        the string to duplicate

    :param size_t max:
        read at most \ ``max``\  chars from \ ``s``\ 

    :param gfp_t gfp:
        the GFP mask used in the \ :c:func:`kmalloc`\  call when allocating memory

.. _`kmemdup`:

kmemdup
=======

.. c:function:: void *kmemdup(const void *src, size_t len, gfp_t gfp)

    duplicate region of memory

    :param const void \*src:
        memory region to duplicate

    :param size_t len:
        memory region length

    :param gfp_t gfp:
        GFP mask to use

.. _`memdup_user`:

memdup_user
===========

.. c:function:: void *memdup_user(const void __user *src, size_t len)

    duplicate memory region from user space

    :param const void __user \*src:
        source address in user space

    :param size_t len:
        number of bytes to copy

.. _`memdup_user.description`:

Description
-----------

Returns an \ :c:func:`ERR_PTR`\  on failure.

.. _`memdup_user_nul`:

memdup_user_nul
===============

.. c:function:: void *memdup_user_nul(const void __user *src, size_t len)

    duplicate memory region from user space and NUL-terminate

    :param const void __user \*src:
        source address in user space

    :param size_t len:
        number of bytes to copy

.. _`memdup_user_nul.description`:

Description
-----------

Returns an \ :c:func:`ERR_PTR`\  on failure.

.. _`get_user_pages_fast`:

get_user_pages_fast
===================

.. c:function:: int get_user_pages_fast(unsigned long start, int nr_pages, int write, struct page **pages)

    pin user pages in memory

    :param unsigned long start:
        starting user address

    :param int nr_pages:
        number of pages from start to pin

    :param int write:
        whether pages will be written to

    :param struct page \*\*pages:
        array that receives pointers to the pages pinned.
        Should be at least nr_pages long.

.. _`get_user_pages_fast.description`:

Description
-----------

Returns number of pages pinned. This may be fewer than the number
requested. If nr_pages is 0 or negative, returns 0. If no pages
were pinned, returns -errno.

get_user_pages_fast provides equivalent functionality to get_user_pages,
operating on current and current->mm, with force=0 and vma=NULL. However
unlike get_user_pages, it must be called without mmap_sem held.

get_user_pages_fast may take mmap_sem and page table locks, so no
assumptions can be made about lack of locking. get_user_pages_fast is to be
implemented in a way that is advantageous (vs \ :c:func:`get_user_pages`\ ) when the
user memory area is already faulted in and present in ptes. However if the
pages have to be faulted in, it may turn out to be slightly slower so
callers need to carefully consider what to use. On many architectures,
get_user_pages_fast simply falls back to get_user_pages.

.. _`kvmalloc_node`:

kvmalloc_node
=============

.. c:function:: void *kvmalloc_node(size_t size, gfp_t flags, int node)

    attempt to allocate physically contiguous memory, but upon failure, fall back to non-contiguous (vmalloc) allocation.

    :param size_t size:
        size of the request.

    :param gfp_t flags:
        gfp mask for the allocation - must be compatible (superset) with GFP_KERNEL.

    :param int node:
        numa node to allocate from

.. _`kvmalloc_node.description`:

Description
-----------

Uses kmalloc to get the memory but if the allocation fails then falls back
to the vmalloc allocator. Use kvfree for freeing the memory.

Reclaim modifiers - __GFP_NORETRY and __GFP_NOFAIL are not supported. __GFP_REPEAT
is supported only for large (>32kB) allocations, and it should be used only if
kmalloc is preferable to the vmalloc fallback, due to visible performance drawbacks.

Any use of gfp flags outside of GFP_KERNEL should be consulted with mm people.

.. _`get_cmdline`:

get_cmdline
===========

.. c:function:: int get_cmdline(struct task_struct *task, char *buffer, int buflen)

    copy the cmdline value to a buffer.

    :param struct task_struct \*task:
        the task whose cmdline value to copy.

    :param char \*buffer:
        the buffer to copy to.

    :param int buflen:
        the length of the buffer. Larger cmdline values are truncated
        to this length.
        Returns the size of the cmdline field copied. Note that the copy does
        not guarantee an ending NULL byte.

.. This file was automatic generated / don't edit.

