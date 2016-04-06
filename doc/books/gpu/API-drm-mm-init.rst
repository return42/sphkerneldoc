
.. _API-drm-mm-init:

===========
drm_mm_init
===========

*man drm_mm_init(9)*

*4.6.0-rc1*

initialize a drm-mm allocator


Synopsis
========

.. c:function:: void drm_mm_init( struct drm_mm * mm, u64 start, u64 size )

Arguments
=========

``mm``
    the drm_mm structure to initialize

``start``
    start of the range managed by ``mm``

``size``
    end of the range managed by ``mm``


Description
===========

Note that ``mm`` must be cleared to 0 before calling this function.
