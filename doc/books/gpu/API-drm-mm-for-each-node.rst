.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mm-for-each-node:

====================
drm_mm_for_each_node
====================

*man drm_mm_for_each_node(9)*

*4.6.0-rc5*

iterator to walk over all allocated nodes


Synopsis
========

.. c:function:: drm_mm_for_each_node( entry, mm )

Arguments
=========

``entry``
    drm_mm_node structure to assign to in each iteration step

``mm``
    drm_mm allocator to walk


Description
===========

This iterator walks over all nodes in the range allocator. It is
implemented with list_for_each, so not save against removal of
elements.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
