.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/crash_dump_64.c

.. _`copy_oldmem_page`:

copy_oldmem_page
================

.. c:function:: ssize_t copy_oldmem_page(unsigned long pfn, char *buf, size_t csize, unsigned long offset, int userbuf)

    copy one page of memory

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

Copy a page from the old kernel's memory. For this page, there is no pte
mapped in the current kernel. We stitch up a pte, similar to kmap_atomic.

.. _`copy_oldmem_page_encrypted`:

copy_oldmem_page_encrypted
==========================

.. c:function:: ssize_t copy_oldmem_page_encrypted(unsigned long pfn, char *buf, size_t csize, unsigned long offset, int userbuf)

    same as \ :c:func:`copy_oldmem_page`\  above but ioremap the memory with the encryption mask set to accomodate kdump on SME-enabled machines.

    :param pfn:
        *undescribed*
    :type pfn: unsigned long

    :param buf:
        *undescribed*
    :type buf: char \*

    :param csize:
        *undescribed*
    :type csize: size_t

    :param offset:
        *undescribed*
    :type offset: unsigned long

    :param userbuf:
        *undescribed*
    :type userbuf: int

.. This file was automatic generated / don't edit.

