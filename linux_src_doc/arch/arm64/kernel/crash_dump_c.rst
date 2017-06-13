.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kernel/crash_dump.c

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
        if set, \ ``buf``\  is in a user address space

.. _`copy_oldmem_page.description`:

Description
-----------

This function copies one page from old kernel memory into buffer pointed by
\ ``buf``\ . If \ ``buf``\  is in userspace, set \ ``userbuf``\  to \ ``1``\ . Returns number of bytes
copied or negative error in case of failure.

.. _`elfcorehdr_read`:

elfcorehdr_read
===============

.. c:function:: ssize_t elfcorehdr_read(char *buf, size_t count, u64 *ppos)

    read from ELF core header

    :param char \*buf:
        buffer where the data is placed

    :param size_t count:
        *undescribed*

    :param u64 \*ppos:
        address in the memory

.. _`elfcorehdr_read.description`:

Description
-----------

This function reads \ ``count``\  bytes from elf core header which exists
on crash dump kernel's memory.

.. This file was automatic generated / don't edit.

