.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kernel/crash_dump.c

.. _`copy_oldmem_page`:

copy_oldmem_page
================

.. c:function:: ssize_t copy_oldmem_page(unsigned long pfn, char *buf, size_t csize, unsigned long offset, int userbuf)

    copy one page from "oldmem"

    :param pfn:
        page frame number to be copied
    :type pfn: unsigned long

    :param buf:
        target memory address for the copy; this can be in kernel address
        space or user address space (see \ ``userbuf``\ )
    :type buf: char \*

    :param csize:
        number of bytes to copy
    :type csize: size_t

    :param offset:
        offset in bytes into the page (based on pfn) to begin the copy
    :type offset: unsigned long

    :param userbuf:
        if set, \ ``buf``\  is in user address space, use \ :c:func:`copy_to_user`\ ,
        otherwise \ ``buf``\  is in kernel address space, use \ :c:func:`memcpy`\ .
    :type userbuf: int

.. _`copy_oldmem_page.description`:

Description
-----------

Copy a page from "oldmem". For this page, there is no pte mapped
in the current kernel.

Calling \ :c:func:`copy_to_user`\  in atomic context is not desirable. Hence first
copying the data to a pre-allocated kernel page and then copying to user
space in non-atomic context.

.. This file was automatic generated / don't edit.

