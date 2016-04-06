
.. _API-drm-mm-takedown:

===============
drm_mm_takedown
===============

*man drm_mm_takedown(9)*

*4.6.0-rc1*

clean up a drm_mm allocator


Synopsis
========

.. c:function:: void drm_mm_takedown( struct drm_mm * mm )

Arguments
=========

``mm``
    drm_mm allocator to clean up


Description
===========

Note that it is a bug to call this function on an allocator which is not clean.
