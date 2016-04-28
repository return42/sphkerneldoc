.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-vma-node-size:

=================
drm_vma_node_size
=================

*man drm_vma_node_size(9)*

*4.6.0-rc5*

Return size (page-based)


Synopsis
========

.. c:function:: unsigned long drm_vma_node_size( struct drm_vma_offset_node * node )

Arguments
=========

``node``
    Node to inspect


Description
===========

Return the size as number of pages for the given node. This is the same
size that was passed to ``drm_vma_offset_add``. If no offset is
allocated for the node, this is 0.


RETURNS
=======

Size of ``node`` as number of pages. 0 if the node does not have an
offset allocated.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
