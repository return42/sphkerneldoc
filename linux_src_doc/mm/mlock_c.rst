.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/mlock.c

.. _`munlock_vma_page`:

munlock_vma_page
================

.. c:function:: unsigned int munlock_vma_page(struct page *page)

    munlock a vma page

    :param struct page \*page:
        page to be unlocked, either a normal page or THP page head

.. _`munlock_vma_page.description`:

Description
-----------

returns the size of the page as a page mask (0 for normal page,
HPAGE_PMD_NR - 1 for THP head page)

called from \ :c:func:`munlock`\ /munmap() path with page supposedly on the LRU.
When we munlock a page, because the vma where we found the page is being
\ :c:func:`munlock`\ ed or \ :c:func:`munmap`\ ed, we want to check whether other vmas hold the
page locked so that we can leave it on the unevictable lru list and not
bother vmscan with it.  However, to walk the page's rmap list in
\ :c:func:`try_to_munlock`\  we must isolate the page from the LRU.  If some other
task has removed the page from the LRU, we won't be able to do that.
So we clear the PageMlocked as we might not get another chance.  If we
can't isolate the page, we leave it for \ :c:func:`putback_lru_page`\  and vmscan
[page_referenced()/try_to_unmap()] to deal with.

.. This file was automatic generated / don't edit.

