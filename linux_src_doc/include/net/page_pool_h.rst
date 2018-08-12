.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/page_pool.h

.. _`page_pool-allocator`:

page_pool allocator
===================

This page_pool allocator is optimized for the XDP mode that
uses one-frame-per-page, but have fallbacks that act like the
regular page allocator APIs.

Basic use involve replacing \ :c:func:`alloc_pages`\  calls with the
\ :c:func:`page_pool_alloc_pages`\  call.  Drivers should likely use
\ :c:func:`page_pool_dev_alloc_pages`\  replacing \ :c:func:`dev_alloc_pages`\ .

If page_pool handles DMA mapping (use page->private), then API user
is responsible for invoking \ :c:func:`page_pool_put_page`\  once.  In-case of
elevated refcnt, the DMA state is released, assuming other users of
the page will eventually call \ :c:func:`put_page`\ .

If no DMA mapping is done, then it can act as shim-layer that
fall-through to alloc_page.  As no state is kept on the page, the
regular \ :c:func:`put_page`\  call is sufficient.

.. This file was automatic generated / don't edit.

