
.. _API-snd-malloc-pages:

================
snd_malloc_pages
================

*man snd_malloc_pages(9)*

*4.6.0-rc1*

allocate pages with the given size


Synopsis
========

.. c:function:: void ⋆ snd_malloc_pages( size_t size, gfp_t gfp_flags )

Arguments
=========

``size``
    the size to allocate in bytes

``gfp_flags``
    the allocation conditions, GFP_XXX


Description
===========

Allocates the physically contiguous pages with the given size.


Return
======

The pointer of the buffer, or ``NULL`` if no enough memory.
