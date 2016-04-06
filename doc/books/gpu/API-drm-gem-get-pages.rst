
.. _API-drm-gem-get-pages:

=================
drm_gem_get_pages
=================

*man drm_gem_get_pages(9)*

*4.6.0-rc1*

helper to allocate backing pages for a GEM object from shmem


Synopsis
========

.. c:function:: struct page ⋆⋆ drm_gem_get_pages( struct drm_gem_object * obj )

Arguments
=========

``obj``
    obj in question


Description
===========

This reads the page-array of the shmem-backing storage of the given gem object. An array of pages is returned. If a page is not allocated or swapped-out, this will allocate/swap-in
the required pages. Note that the whole object is covered by the page-array and pinned in memory.

Use ``drm_gem_put_pages`` to release the array and unpin all pages.

This uses the GFP-mask set on the shmem-mapping (see ``mapping_set_gfp_mask``). If you require other GFP-masks, you have to do those allocations yourself.

Note that you are not allowed to change gfp-zones during runtime. That is, ``shmem_read_mapping_page_gfp`` must be called with the same gfp_zone(gfp) as set during initialization.
If you have special zone constraints, set them after ``drm_gem_init_object`` via ``mapping_set_gfp_mask``. shmem-core takes care to keep pages in the required zone during swap-in.
