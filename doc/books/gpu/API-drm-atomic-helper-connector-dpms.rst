.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-connector-dpms:

================================
drm_atomic_helper_connector_dpms
================================

*man drm_atomic_helper_connector_dpms(9)*

*4.6.0-rc5*

connector dpms helper implementation


Synopsis
========

.. c:function:: int drm_atomic_helper_connector_dpms( struct drm_connector * connector, int mode )

Arguments
=========

``connector``
    affected connector

``mode``
    DPMS mode


Description
===========

This is the main helper function provided by the atomic helper framework
for implementing the legacy DPMS connector interface. It computes the
new desired ->active state for the corresponding CRTC (if the connector
is enabled) and updates it.


Returns
=======

Returns 0 on success, negative errno numbers on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
