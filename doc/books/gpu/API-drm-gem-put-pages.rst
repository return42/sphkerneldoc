.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-put-pages:

=================
drm_gem_put_pages
=================

*man drm_gem_put_pages(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
