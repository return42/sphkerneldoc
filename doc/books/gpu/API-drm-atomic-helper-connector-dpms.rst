
.. _API-drm-atomic-helper-connector-dpms:

================================
drm_atomic_helper_connector_dpms
================================

*man drm_atomic_helper_connector_dpms(9)*

*4.6.0-rc1*

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

This is the main helper function provided by the atomic helper framework for implementing the legacy DPMS connector interface. It computes the new desired ->active state for the
corresponding CRTC (if the connector is enabled) and updates it.


Returns
=======

Returns 0 on success, negative errno numbers on failure.
