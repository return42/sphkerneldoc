.. -*- coding: utf-8; mode: rst -*-

=====
gup.c
=====


.. _`follow_page_mask`:

follow_page_mask
================

.. c:function:: struct page *follow_page_mask (struct vm_area_struct *vma, unsigned long address, unsigned int flags, unsigned int *page_mask)

    look up a page descriptor from a user-virtual address

    :param struct vm_area_struct \*vma:
        vm_area_struct mapping ``address``

    :param unsigned long address:
        virtual address to look up

    :param unsigned int flags:
        flags modifying lookup behaviour

    :param unsigned int \*page_mask:
        on output, \*page_mask is set according to the size of the page



.. _`follow_page_mask.description`:

Description
-----------

``flags`` can have FOLL_ flags set, defined in <linux/mm.h>

Returns the mapped (struct page *), ``NULL`` if no mapping exists, or
an error pointer if there is a mapping to something not represented
by a page descriptor (see also :c:func:`vm_normal_page`).



.. _`__get_user_pages`:

__get_user_pages
================

.. c:function:: long __get_user_pages (struct task_struct *tsk, struct mm_struct *mm, unsigned long start, unsigned long nr_pages, unsigned int gup_flags, struct page **pages, struct vm_area_struct **vmas, int *nonblocking)

    pin user pages in memory

    :param struct task_struct \*tsk:
        task_struct of target task

    :param struct mm_struct \*mm:
        mm_struct of target mm

    :param unsigned long start:
        starting user address

    :param unsigned long nr_pages:
        number of pages from start to pin

    :param unsigned int gup_flags:
        flags modifying pin behaviour

    :param struct page \*\*pages:
        array that receives pointers to the pages pinned.
        Should be at least nr_pages long. Or NULL, if caller
        only intends to ensure the pages are faulted in.

    :param struct vm_area_struct \*\*vmas:
        array of pointers to vmas corresponding to each page.
        Or NULL if the caller does not require them.

    :param int \*nonblocking:
        whether waiting for disk IO or mmap_sem contention



.. _`__get_user_pages.description`:

Description
-----------

Returns number of pages pinned. This may be fewer than the number
requested. If nr_pages is 0 or negative, returns 0. If no pages
were pinned, returns -errno. Each page returned must be released
with a :c:func:`put_page` call when it is finished with. vmas will only
remain valid while mmap_sem is held.

Must be called with mmap_sem held.  It may be released.  See below.

__get_user_pages walks a process's page tables and takes a reference to
each struct page that each user address corresponds to at a given
instant. That is, it takes the page that would be accessed if a user
thread accesses the given user virtual address at that instant.

This does not guarantee that the page exists in the user mappings when
__get_user_pages returns, and there may even be a completely different
page there in some cases (eg. if mmapped pagecache has been invalidated
and subsequently re faulted). However it does guarantee that the page
won't be freed completely. And mostly callers simply care that the page
contains data that was valid \*at some point in time\*. Typically, an IO
or similar operation cannot guarantee anything stronger anyway because
locks can't be held over the syscall boundary.

If ``gup_flags`` & FOLL_WRITE == 0, the page must not be written to. If
the page is written to, set_page_dirty (or set_page_dirty_lock, as
appropriate) must be called after the page is finished with, and
before put_page is called.

If ``nonblocking`` != NULL, __get_user_pages will not wait for disk IO
or mmap_sem contention, and if waiting is needed to pin all pages,
*\ ``nonblocking`` will be set to 0.  Further, if ``gup_flags`` does not
include FOLL_NOWAIT, the mmap_sem will be released via :c:func:`up_read` in
this case.

A caller using such a combination of ``nonblocking`` and ``gup_flags``
must therefore hold the mmap_sem for reading only, and recognize
when it's been released.  Otherwise, it must be held for either
reading or writing and will not be released.

In most cases, get_user_pages or get_user_pages_fast should be used
instead of __get_user_pages. __get_user_pages should be used only if
you need some special ``gup_flags``\ .



.. _`populate_vma_page_range`:

populate_vma_page_range
=======================

.. c:function:: long populate_vma_page_range (struct vm_area_struct *vma, unsigned long start, unsigned long end, int *nonblocking)

    populate a range of pages in the vma.

    :param struct vm_area_struct \*vma:
        target vma

    :param unsigned long start:
        start address

    :param unsigned long end:
        end address

    :param int \*nonblocking:



.. _`populate_vma_page_range.description`:

Description
-----------

This takes care of mlocking the pages too if VM_LOCKED is set.

return 0 on success, negative error code on error.

vma->vm_mm->mmap_sem must be held.

If ``nonblocking`` is NULL, it may be held for read or write and will
be unperturbed.

If ``nonblocking`` is non-NULL, it must held for read only and may be
released.  If it's released, \*\ ``nonblocking`` will be set to 0.



.. _`get_dump_page`:

get_dump_page
=============

.. c:function:: struct page *get_dump_page (unsigned long addr)

    pin user page in memory while writing it to core dump

    :param unsigned long addr:
        user address



.. _`get_dump_page.description`:

Description
-----------

Returns struct page pointer of user page pinned for dump,
to be freed afterwards by :c:func:`put_page`.

Returns NULL on any kind of failure - a hole must then be inserted into
the corefile, to preserve alignment with its headers; and also returns
NULL wherever the ZERO_PAGE, or an anonymous pte_none, has been found -
allowing a hole to be left in the corefile to save diskspace.

Called without mmap_sem, but after all other threads have been killed.



.. _`get_user_pages_fast`:

get_user_pages_fast
===================

.. c:function:: int get_user_pages_fast (unsigned long start, int nr_pages, int write, struct page **pages)

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

Attempt to pin user pages in memory without taking mm->mmap_sem.
If not successful, it will fall back to taking the lock and
calling :c:func:`get_user_pages`.

Returns number of pages pinned. This may be fewer than the number
requested. If nr_pages is 0 or negative, returns 0. If no pages
were pinned, returns -errno.

