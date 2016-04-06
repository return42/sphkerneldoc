
.. _API-drm-dp-mst-dump-topology:

========================
drm_dp_mst_dump_topology
========================

*man drm_dp_mst_dump_topology(9)*

*4.6.0-rc1*


Synopsis
========

.. c:function:: void drm_dp_mst_dump_topology( struct seq_file * m, struct drm_dp_mst_topology_mgr * mgr )

Arguments
=========

``m``
    seq_file to dump output to

``mgr``
    manager to dump current topology for.


Description
===========

helper to dump MST topology to a seq file for debugfs.
