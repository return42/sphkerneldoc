.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mm-insert-node:

==================
drm_mm_insert_node
==================

*man drm_mm_insert_node(9)*

*4.6.0-rc5*

search for space and insert ``node``


Synopsis
========

.. c:function:: int drm_mm_insert_node( struct drm_mm * mm, struct drm_mm_node * node, u64 size, unsigned alignment, enum drm_mm_search_flags flags )

Arguments
=========

``mm``
    drm_mm to allocate from

``node``
    preallocate node to insert

``size``
    size of the allocation

``alignment``
    alignment of the allocation

``flags``
    flags to fine-tune the allocation


Description
===========

This is a simplified version of ``drm_mm_insert_node_generic`` with
``color`` set to 0.

The preallocated node must be cleared to 0.


Returns
=======

0 on success, -ENOSPC if there's no suitable hole.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
