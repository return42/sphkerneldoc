.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/highmem.c

.. _`kmap_flush_unused`:

kmap_flush_unused
=================

.. c:function:: void kmap_flush_unused( void)

    flush all unused kmap mappings in order to remove stray mappings

    :param void:
        no arguments
    :type void: 

.. _`kmap_high`:

kmap_high
=========

.. c:function:: void *kmap_high(struct page *page)

    map a highmem page into memory

    :param page:
        \ :c:type:`struct page <page>`\  to map
    :type page: struct page \*

.. _`kmap_high.description`:

Description
-----------

Returns the page's virtual memory address.

We cannot call this from interrupts, as it may block.

.. _`kmap_high_get`:

kmap_high_get
=============

.. c:function:: void *kmap_high_get(struct page *page)

    pin a highmem page into memory

    :param page:
        \ :c:type:`struct page <page>`\  to pin
    :type page: struct page \*

.. _`kmap_high_get.description`:

Description
-----------

Returns the page's current virtual memory address, or NULL if no mapping
exists.  If and only if a non null address is returned then a
matching call to \ :c:func:`kunmap_high`\  is necessary.

This can be called from any context.

.. _`kunmap_high`:

kunmap_high
===========

.. c:function:: void kunmap_high(struct page *page)

    unmap a highmem page into memory

    :param page:
        \ :c:type:`struct page <page>`\  to unmap
    :type page: struct page \*

.. _`kunmap_high.description`:

Description
-----------

If ARCH_NEEDS_KMAP_HIGH_GET is not defined then this may be called
only from user context.

.. _`page_address`:

page_address
============

.. c:function:: void *page_address(const struct page *page)

    get the mapped virtual address of a page

    :param page:
        \ :c:type:`struct page <page>`\  to get the virtual address of
    :type page: const struct page \*

.. _`page_address.description`:

Description
-----------

Returns the page's virtual address.

.. _`set_page_address`:

set_page_address
================

.. c:function:: void set_page_address(struct page *page, void *virtual)

    set a page's virtual address

    :param page:
        \ :c:type:`struct page <page>`\  to set
    :type page: struct page \*

    :param virtual:
        virtual address to use
    :type virtual: void \*

.. This file was automatic generated / don't edit.

