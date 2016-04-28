.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dp-mst-deallocate-vcpi:

==========================
drm_dp_mst_deallocate_vcpi
==========================

*man drm_dp_mst_deallocate_vcpi(9)*

*4.6.0-rc5*

deallocate a VCPI


Synopsis
========

.. c:function:: void drm_dp_mst_deallocate_vcpi( struct drm_dp_mst_topology_mgr * mgr, struct drm_dp_mst_port * port )

Arguments
=========

``mgr``
    manager for this port

``port``
    unverified port to deallocate vcpi for


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
