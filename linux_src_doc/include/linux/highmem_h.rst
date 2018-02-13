.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/highmem.h

.. _`__alloc_zeroed_user_highpage`:

\__alloc_zeroed_user_highpage
=============================

.. c:function:: struct page *__alloc_zeroed_user_highpage(gfp_t movableflags, struct vm_area_struct *vma, unsigned long vaddr)

    Allocate a zeroed HIGHMEM page for a VMA with caller-specified movable GFP flags

    :param gfp_t movableflags:
        The GFP flags related to the pages future ability to move like \__GFP_MOVABLE

    :param struct vm_area_struct \*vma:
        The VMA the page is to be allocated for

    :param unsigned long vaddr:
        The virtual address the page will be inserted into

.. _`__alloc_zeroed_user_highpage.description`:

Description
-----------

This function will allocate a page for a VMA but the caller is expected
to specify via movableflags whether the page will be movable in the
future or not

An architecture may override this function by defining
\__HAVE_ARCH_ALLOC_ZEROED_USER_HIGHPAGE and providing their own
implementation.

.. _`alloc_zeroed_user_highpage_movable`:

alloc_zeroed_user_highpage_movable
==================================

.. c:function:: struct page *alloc_zeroed_user_highpage_movable(struct vm_area_struct *vma, unsigned long vaddr)

    Allocate a zeroed HIGHMEM page for a VMA that the caller knows can move

    :param struct vm_area_struct \*vma:
        The VMA the page is to be allocated for

    :param unsigned long vaddr:
        The virtual address the page will be inserted into

.. _`alloc_zeroed_user_highpage_movable.description`:

Description
-----------

This function will allocate a page for a VMA that the caller knows will
be able to migrate in the future using \ :c:func:`move_pages`\  or reclaimed

.. This file was automatic generated / don't edit.

