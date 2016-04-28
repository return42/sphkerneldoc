.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mm-node-allocated:

=====================
drm_mm_node_allocated
=====================

*man drm_mm_node_allocated(9)*

*4.6.0-rc5*

checks whether a node is allocated


Synopsis
========

.. c:function:: bool drm_mm_node_allocated( struct drm_mm_node * node )

Arguments
=========

``node``
    drm_mm_node to check


Description
===========

Drivers should use this helpers for proper encapusulation of drm_mm
internals.


Returns
=======

True if the ``node`` is allocated.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
