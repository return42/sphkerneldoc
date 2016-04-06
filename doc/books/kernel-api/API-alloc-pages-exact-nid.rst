
.. _API-alloc-pages-exact-nid:

=====================
alloc_pages_exact_nid
=====================

*man alloc_pages_exact_nid(9)*

*4.6.0-rc1*

allocate an exact number of physically-contiguous pages on a node.


Synopsis
========

.. c:function:: void ⋆ alloc_pages_exact_nid( int nid, size_t size, gfp_t gfp_mask )

Arguments
=========

``nid``
    the preferred node ID where memory should be allocated

``size``
    the number of bytes to allocate

``gfp_mask``
    GFP flags for the allocation


Description
===========

Like ``alloc_pages_exact``, but try to allocate on node nid first before falling back.
