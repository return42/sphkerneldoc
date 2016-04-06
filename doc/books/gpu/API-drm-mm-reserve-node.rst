
.. _API-drm-mm-reserve-node:

===================
drm_mm_reserve_node
===================

*man drm_mm_reserve_node(9)*

*4.6.0-rc1*

insert an pre-initialized node


Synopsis
========

.. c:function:: int drm_mm_reserve_node( struct drm_mm * mm, struct drm_mm_node * node )

Arguments
=========

``mm``
    drm_mm allocator to insert ``node`` into

``node``
    drm_mm_node to insert


Description
===========

This functions inserts an already set-up drm_mm_node into the allocator, meaning that start, size and color must be set by the caller. This is useful to initialize the allocator
with preallocated objects which must be set-up before the range allocator can be set-up, e.g. when taking over a firmware framebuffer.


Returns
=======

0 on success, -ENOSPC if there's no hole where ``node`` is.
