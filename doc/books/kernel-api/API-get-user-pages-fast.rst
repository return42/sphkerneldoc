
.. _API-get-user-pages-fast:

===================
get_user_pages_fast
===================

*man get_user_pages_fast(9)*

*4.6.0-rc1*

pin user pages in memory


Synopsis
========

.. c:function:: int get_user_pages_fast( unsigned long start, int nr_pages, int write, struct page ** pages )

Arguments
=========

``start``
    starting user address

``nr_pages``
    number of pages from start to pin

``write``
    whether pages will be written to

``pages``
    array that receives pointers to the pages pinned. Should be at least nr_pages long.


Description
===========

Returns number of pages pinned. This may be fewer than the number requested. If nr_pages is 0 or negative, returns 0. If no pages were pinned, returns -errno.

get_user_pages_fast provides equivalent functionality to get_user_pages, operating on current and current->mm, with force=0 and vma=NULL. However unlike get_user_pages, it
must be called without mmap_sem held.

get_user_pages_fast may take mmap_sem and page table locks, so no assumptions can be made about lack of locking. get_user_pages_fast is to be implemented in a way that is
advantageous (vs ``get_user_pages``) when the user memory area is already faulted in and present in ptes. However if the pages have to be faulted in, it may turn out to be slightly
slower so callers need to carefully consider what to use. On many architectures, get_user_pages_fast simply falls back to get_user_pages.
