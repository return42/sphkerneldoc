
.. _API-drm-mm-debug-table:

==================
drm_mm_debug_table
==================

*man drm_mm_debug_table(9)*

*4.6.0-rc1*

dump allocator state to dmesg


Synopsis
========

.. c:function:: void drm_mm_debug_table( struct drm_mm * mm, const char * prefix )

Arguments
=========

``mm``
    drm_mm allocator to dump

``prefix``
    prefix to use for dumping to dmesg
