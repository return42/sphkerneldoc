
.. _API-drm-gem-put-pages:

=================
drm_gem_put_pages
=================

*man drm_gem_put_pages(9)*

*4.6.0-rc1*

helper to free backing pages for a GEM object


Synopsis
========

.. c:function:: void drm_gem_put_pages( struct drm_gem_object * obj, struct page ** pages, bool dirty, bool accessed )

Arguments
=========

``obj``
    obj in question

``pages``
    pages to free

``dirty``
    if true, pages will be marked as dirty

``accessed``
    if true, the pages will be marked as accessed
