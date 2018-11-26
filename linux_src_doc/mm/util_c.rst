.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/util.c

.. _`kfree_const`:

kfree_const
===========

.. c:function:: void kfree_const(const void *x)

    conditionally free memory

    :param x:
        pointer to the memory
    :type x: const void \*

.. _`kfree_const.description`:

Description
-----------

Function calls kfree only if \ ``x``\  is not in .rodata section.

.. _`kstrdup`:

kstrdup
=======

.. c:function:: char *kstrdup(const char *s, gfp_t gfp)

    allocate space for and copy an existing string

    :param s:
        the string to duplicate
    :type s: const char \*

    :param gfp:
        the GFP mask used in the \ :c:func:`kmalloc`\  call when allocating memory
    :type gfp: gfp_t

.. _`kstrdup_const`:

kstrdup_const
=============

.. c:function:: const char *kstrdup_const(const char *s, gfp_t gfp)

    conditionally duplicate an existing const string

    :param s:
        the string to duplicate
    :type s: const char \*

    :param gfp:
        the GFP mask used in the \ :c:func:`kmalloc`\  call when allocating memory
    :type gfp: gfp_t

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

    :param s:
        the string to duplicate
    :type s: const char \*

    :param max:
        read at most \ ``max``\  chars from \ ``s``\ 
    :type max: size_t

    :param gfp:
        the GFP mask used in the \ :c:func:`kmalloc`\  call when allocating memory
    :type gfp: gfp_t

.. _`kstrndup.note`:

Note
----

Use \ :c:func:`kmemdup_nul`\  instead if the size is known exactly.

.. _`kmemdup`:

kmemdup
=======

.. c:function:: void *kmemdup(const void *src, size_t len, gfp_t gfp)

    duplicate region of memory

    :param src:
        memory region to duplicate
    :type src: const void \*

    :param len:
        memory region length
    :type len: size_t

    :param gfp:
        GFP mask to use
    :type gfp: gfp_t

.. _`kmemdup_nul`:

kmemdup_nul
===========

.. c:function:: char *kmemdup_nul(const char *s, size_t len, gfp_t gfp)

    Create a NUL-terminated string from unterminated data

    :param s:
        The data to stringify
    :type s: const char \*

    :param len:
        The size of the data
    :type len: size_t

    :param gfp:
        the GFP mask used in the \ :c:func:`kmalloc`\  call when allocating memory
    :type gfp: gfp_t

.. _`memdup_user`:

memdup_user
===========

.. c:function:: void *memdup_user(const void __user *src, size_t len)

    duplicate memory region from user space

    :param src:
        source address in user space
    :type src: const void __user \*

    :param len:
        number of bytes to copy
    :type len: size_t

.. _`memdup_user.description`:

Description
-----------

Returns an \ :c:func:`ERR_PTR`\  on failure.  Result is physically
contiguous, to be freed by \ :c:func:`kfree`\ .

.. _`vmemdup_user`:

vmemdup_user
============

.. c:function:: void *vmemdup_user(const void __user *src, size_t len)

    duplicate memory region from user space

    :param src:
        source address in user space
    :type src: const void __user \*

    :param len:
        number of bytes to copy
    :type len: size_t

.. _`vmemdup_user.description`:

Description
-----------

Returns an \ :c:func:`ERR_PTR`\  on failure.  Result may be not
physically contiguous.  Use \ :c:func:`kvfree`\  to free.

.. _`strndup_user`:

strndup_user
============

.. c:function:: char *strndup_user(const char __user *s, long n)

    duplicate an existing string from user space

    :param s:
        The string to duplicate
    :type s: const char __user \*

    :param n:
        Maximum number of bytes to copy, including the trailing NUL.
    :type n: long

.. _`memdup_user_nul`:

memdup_user_nul
===============

.. c:function:: void *memdup_user_nul(const void __user *src, size_t len)

    duplicate memory region from user space and NUL-terminate

    :param src:
        source address in user space
    :type src: const void __user \*

    :param len:
        number of bytes to copy
    :type len: size_t

.. _`memdup_user_nul.description`:

Description
-----------

Returns an \ :c:func:`ERR_PTR`\  on failure.

.. _`get_user_pages_fast`:

get_user_pages_fast
===================

.. c:function:: int get_user_pages_fast(unsigned long start, int nr_pages, int write, struct page **pages)

    pin user pages in memory

    :param start:
        starting user address
    :type start: unsigned long

    :param nr_pages:
        number of pages from start to pin
    :type nr_pages: int

    :param write:
        whether pages will be written to
    :type write: int

    :param pages:
        array that receives pointers to the pages pinned.
        Should be at least nr_pages long.
    :type pages: struct page \*\*

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

    :param size:
        size of the request.
    :type size: size_t

    :param flags:
        gfp mask for the allocation - must be compatible (superset) with GFP_KERNEL.
    :type flags: gfp_t

    :param node:
        numa node to allocate from
    :type node: int

.. _`kvmalloc_node.description`:

Description
-----------

Uses kmalloc to get the memory but if the allocation fails then falls back
to the vmalloc allocator. Use kvfree for freeing the memory.

Reclaim modifiers - __GFP_NORETRY and __GFP_NOFAIL are not supported.
__GFP_RETRY_MAYFAIL is supported, and it should be used only if kmalloc is
preferable to the vmalloc fallback, due to visible performance drawbacks.

Please note that any use of gfp flags outside of GFP_KERNEL is careful to not
fall back to vmalloc.

.. _`kvfree`:

kvfree
======

.. c:function:: void kvfree(const void *addr)

    Free memory.

    :param addr:
        Pointer to allocated memory.
    :type addr: const void \*

.. _`kvfree.description`:

Description
-----------

kvfree frees memory allocated by any of \ :c:func:`vmalloc`\ , \ :c:func:`kmalloc`\  or \ :c:func:`kvmalloc`\ .
It is slightly more efficient to use \ :c:func:`kfree`\  or \ :c:func:`vfree`\  if you are certain
that you know which one to use.

.. _`kvfree.context`:

Context
-------

Either preemptible task context or not-NMI interrupt.

.. _`get_cmdline`:

get_cmdline
===========

.. c:function:: int get_cmdline(struct task_struct *task, char *buffer, int buflen)

    copy the cmdline value to a buffer.

    :param task:
        the task whose cmdline value to copy.
    :type task: struct task_struct \*

    :param buffer:
        the buffer to copy to.
    :type buffer: char \*

    :param buflen:
        the length of the buffer. Larger cmdline values are truncated
        to this length.
        Returns the size of the cmdline field copied. Note that the copy does
        not guarantee an ending NULL byte.
    :type buflen: int

.. This file was automatic generated / don't edit.

