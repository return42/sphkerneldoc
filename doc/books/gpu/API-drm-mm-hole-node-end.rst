
.. _API-drm-mm-hole-node-end:

====================
drm_mm_hole_node_end
====================

*man drm_mm_hole_node_end(9)*

*4.6.0-rc1*

computes the end of the hole following ``node``


Synopsis
========

.. c:function:: u64 drm_mm_hole_node_end( struct drm_mm_node * hole_node )

Arguments
=========

``hole_node``
    drm_mm_node which implicitly tracks the following hole


Description
===========

This is useful for driver-sepific debug dumpers. Otherwise drivers should not inspect holes themselves. Drivers must check first whether a hole indeed follows by looking at
node->hole_follows.


Returns
=======

End of the subsequent hole.
