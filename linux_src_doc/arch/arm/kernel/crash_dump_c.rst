.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kernel/crash_dump.c

.. _`copy_oldmem_page`:

copy_oldmem_page
================

.. c:function:: ssize_t copy_oldmem_page(unsigned long pfn, char *buf, size_t csize, unsigned long offset, int userbuf)

    copy one page from old kernel memory

    :param unsigned long pfn:
        page frame number to be copied

    :param char \*buf:
        buffer where the copied page is placed

    :param size_t csize:
        number of bytes to copy

    :param unsigned long offset:
        offset in bytes into the page

    :param int userbuf:
        if set, \ ``buf``\  is int he user address space

.. _`copy_oldmem_page.description`:

Description
-----------

This function copies one page from old kernel memory into buffer pointed by
\ ``buf``\ . If \ ``buf``\  is in userspace, set \ ``userbuf``\  to \ ``1``\ . Returns number of bytes
copied or negative error in case of failure.

.. This file was automatic generated / don't edit.

