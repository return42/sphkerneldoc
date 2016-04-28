.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mm-debug-table:

==================
drm_mm_debug_table
==================

*man drm_mm_debug_table(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
