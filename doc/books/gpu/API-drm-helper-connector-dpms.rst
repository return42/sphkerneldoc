.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-helper-connector-dpms:

=========================
drm_helper_connector_dpms
=========================

*man drm_helper_connector_dpms(9)*

*4.6.0-rc5*

connector dpms helper implementation


Synopsis
========

.. c:function:: int drm_helper_connector_dpms( struct drm_connector * connector, int mode )

Arguments
=========

``connector``
    affected connector

``mode``
    DPMS mode


Description
===========

The ``drm_helper_connector_dpms`` helper function implements the
->``dpms`` callback of struct ``drm_connector_funcs`` for drivers using
the legacy CRTC helpers.

This is the main helper function provided by the CRTC helper framework
for implementing the DPMS connector attribute. It computes the new
desired DPMS state for all encoders and CRTCs in the output mesh and
calls the ->``dpms`` callbacks provided by the driver in struct
``drm_crtc_helper_funcs`` and struct ``drm_encoder_helper_funcs``
appropriately.

This function is deprecated. New drivers must implement atomic modeset
support, for which this function is unsuitable. Instead drivers should
use ``drm_atomic_helper_connector_dpms``.


Returns
=======

Always returns 0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
