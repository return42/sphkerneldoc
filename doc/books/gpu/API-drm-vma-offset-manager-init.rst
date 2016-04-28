.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-vma-offset-manager-init:

===========================
drm_vma_offset_manager_init
===========================

*man drm_vma_offset_manager_init(9)*

*4.6.0-rc5*

Initialize new offset-manager


Synopsis
========

.. c:function:: void drm_vma_offset_manager_init( struct drm_vma_offset_manager * mgr, unsigned long page_offset, unsigned long size )

Arguments
=========

``mgr``
    Manager object

``page_offset``
    Offset of available memory area (page-based)

``size``
    Size of available address space range (page-based)


Description
===========

Initialize a new offset-manager. The offset and area size available for
the manager are given as ``page_offset`` and ``size``. Both are
interpreted as page-numbers, not bytes.

Adding/removing nodes from the manager is locked internally and
protected against concurrent access. However, node allocation and
destruction is left for the caller. While calling into the vma-manager,
a given node must always be guaranteed to be referenced.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
