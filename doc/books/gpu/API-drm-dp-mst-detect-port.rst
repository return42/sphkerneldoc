.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dp-mst-detect-port:

======================
drm_dp_mst_detect_port
======================

*man drm_dp_mst_detect_port(9)*

*4.6.0-rc5*

get connection status for an MST port


Synopsis
========

.. c:function:: enum drm_connector_status drm_dp_mst_detect_port( struct drm_connector * connector, struct drm_dp_mst_topology_mgr * mgr, struct drm_dp_mst_port * port )

Arguments
=========

``connector``
    -- undescribed --

``mgr``
    manager for this port

``port``
    unverified pointer to a port


Description
===========

This returns the current connection state for a port. It validates the
port pointer still exists so the caller doesn't require a reference


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
