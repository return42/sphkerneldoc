.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-vma-offset-lock-lookup:

==========================
drm_vma_offset_lock_lookup
==========================

*man drm_vma_offset_lock_lookup(9)*

*4.6.0-rc5*

Lock lookup for extended private use


Synopsis
========

.. c:function:: void drm_vma_offset_lock_lookup( struct drm_vma_offset_manager * mgr )

Arguments
=========

``mgr``
    Manager object


Description
===========

Lock VMA manager for extended lookups. Only locked VMA function calls
are allowed while holding this lock. All other contexts are blocked from
VMA until the lock is released via ``drm_vma_offset_unlock_lookup``.

Use this if you need to take a reference to the objects returned by
``drm_vma_offset_lookup_locked`` before releasing this lock again.

This lock must not be used for anything else than extended lookups. You
must not call any other VMA helpers while holding this lock.


Note
====

You're in atomic-context while holding this lock!


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
