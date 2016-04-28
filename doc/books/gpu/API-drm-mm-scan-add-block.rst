.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mm-scan-add-block:

=====================
drm_mm_scan_add_block
=====================

*man drm_mm_scan_add_block(9)*

*4.6.0-rc5*

add a node to the scan list


Synopsis
========

.. c:function:: bool drm_mm_scan_add_block( struct drm_mm_node * node )

Arguments
=========

``node``
    drm_mm_node to add


Description
===========

Add a node to the scan list that might be freed to make space for the
desired hole.


Returns
=======

True if a hole has been found, false otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
