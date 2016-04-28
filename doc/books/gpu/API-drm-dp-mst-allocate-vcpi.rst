.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dp-mst-allocate-vcpi:

========================
drm_dp_mst_allocate_vcpi
========================

*man drm_dp_mst_allocate_vcpi(9)*

*4.6.0-rc5*

Allocate a virtual channel


Synopsis
========

.. c:function:: bool drm_dp_mst_allocate_vcpi( struct drm_dp_mst_topology_mgr * mgr, struct drm_dp_mst_port * port, int pbn, int * slots )

Arguments
=========

``mgr``
    manager for this port

``port``
    port to allocate a virtual channel for.

``pbn``
    payload bandwidth number to request

``slots``
    returned number of slots for this PBN.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
