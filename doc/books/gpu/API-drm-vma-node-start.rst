.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-vma-node-start:

==================
drm_vma_node_start
==================

*man drm_vma_node_start(9)*

*4.6.0-rc5*

Return start address for page-based addressing


Synopsis
========

.. c:function:: unsigned long drm_vma_node_start( struct drm_vma_offset_node * node )

Arguments
=========

``node``
    Node to inspect


Description
===========

Return the start address of the given node. This can be used as offset
into the linear VM space that is provided by the VMA offset manager.
Note that this can only be used for page-based addressing. If you need a
proper offset for user-space mappings, you must apply “<< PAGE_SHIFT”
or use the ``drm_vma_node_offset_addr`` helper instead.


RETURNS
=======

Start address of ``node`` for page-based addressing. 0 if the node does
not have an offset allocated.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
