.. -*- coding: utf-8; mode: rst -*-

=========
pgtable.c
=========


.. _`shatter_huge_page`:

shatter_huge_page
=================

.. c:function:: void shatter_huge_page (unsigned long addr)

    ensure a given address is mapped by a small page.

    :param unsigned long addr:
        Address at which to shatter any existing huge page.



.. _`shatter_huge_page.description`:

Description
-----------


This function converts a huge PTE mapping kernel LOWMEM into a bunch
of small PTEs with the same caching.  No cache flush required, but we
must do a global TLB flush.

Any caller that wishes to modify a kernel mapping that might
have been made with a huge page should call this function,
since doing so properly avoids race conditions with installing the
newly-shattered page and then flushing all the TLB entries.

