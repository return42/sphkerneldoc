.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-vma-offset-unlock-lookup:

============================
drm_vma_offset_unlock_lookup
============================

*man drm_vma_offset_unlock_lookup(9)*

*4.6.0-rc5*

Unlock lookup for extended private use


Synopsis
========

.. c:function:: void drm_vma_offset_unlock_lookup( struct drm_vma_offset_manager * mgr )

Arguments
=========

``mgr``
    Manager object


Description
===========

Release lookup-lock. See ``drm_vma_offset_lock_lookup`` for more
information.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
