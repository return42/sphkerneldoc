
.. _API-drm-mm-clean:

============
drm_mm_clean
============

*man drm_mm_clean(9)*

*4.6.0-rc1*

checks whether an allocator is clean


Synopsis
========

.. c:function:: bool drm_mm_clean( struct drm_mm * mm )

Arguments
=========

``mm``
    drm_mm allocator to check


Returns
=======

True if the allocator is completely free, false if there's still a node allocated in it.
