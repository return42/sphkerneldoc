
.. _API-drm-mm-scan-add-block:

=====================
drm_mm_scan_add_block
=====================

*man drm_mm_scan_add_block(9)*

*4.6.0-rc1*

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

Add a node to the scan list that might be freed to make space for the desired hole.


Returns
=======

True if a hole has been found, false otherwise.
