
.. _API-drm-mm-init-scan:

================
drm_mm_init_scan
================

*man drm_mm_init_scan(9)*

*4.6.0-rc1*

initialize lru scanning


Synopsis
========

.. c:function:: void drm_mm_init_scan( struct drm_mm * mm, u64 size, unsigned alignment, unsigned long color )

Arguments
=========

``mm``
    drm_mm to scan

``size``
    size of the allocation

``alignment``
    alignment of the allocation

``color``
    opaque tag value to use for the allocation


Description
===========

This simply sets up the scanning routines with the parameters for the desired hole. Note that there's no need to specify allocation flags, since they only change the place a node
is allocated from within a suitable hole.


Warning
=======

As long as the scan list is non-empty, no other operations than adding/removing nodes to/from the scan list are allowed.
