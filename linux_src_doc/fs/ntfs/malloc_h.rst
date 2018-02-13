.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/malloc.h

.. _`__ntfs_malloc`:

\__ntfs_malloc
==============

.. c:function:: void *__ntfs_malloc(unsigned long size, gfp_t gfp_mask)

    allocate memory in multiples of pages

    :param unsigned long size:
        number of bytes to allocate

    :param gfp_t gfp_mask:
        extra flags for the allocator

.. _`__ntfs_malloc.description`:

Description
-----------

Internal function.  You probably want \ :c:func:`ntfs_malloc_nofs`\ ...

Allocates \ ``size``\  bytes of memory, rounded up to multiples of PAGE_SIZE and
returns a pointer to the allocated memory.

If there was insufficient memory to complete the request, return NULL.
Depending on \ ``gfp_mask``\  the allocation may be guaranteed to succeed.

.. _`ntfs_malloc_nofs`:

ntfs_malloc_nofs
================

.. c:function:: void *ntfs_malloc_nofs(unsigned long size)

    allocate memory in multiples of pages

    :param unsigned long size:
        number of bytes to allocate

.. _`ntfs_malloc_nofs.description`:

Description
-----------

Allocates \ ``size``\  bytes of memory, rounded up to multiples of PAGE_SIZE and
returns a pointer to the allocated memory.

If there was insufficient memory to complete the request, return NULL.

.. _`ntfs_malloc_nofs_nofail`:

ntfs_malloc_nofs_nofail
=======================

.. c:function:: void *ntfs_malloc_nofs_nofail(unsigned long size)

    allocate memory in multiples of pages

    :param unsigned long size:
        number of bytes to allocate

.. _`ntfs_malloc_nofs_nofail.description`:

Description
-----------

Allocates \ ``size``\  bytes of memory, rounded up to multiples of PAGE_SIZE and
returns a pointer to the allocated memory.

This function guarantees that the allocation will succeed.  It will sleep
for as long as it takes to complete the allocation.

If there was insufficient memory to complete the request, return NULL.

.. This file was automatic generated / don't edit.

