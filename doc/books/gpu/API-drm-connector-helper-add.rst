.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-connector-helper-add:

========================
drm_connector_helper_add
========================

*man drm_connector_helper_add(9)*

*4.6.0-rc5*

sets the helper vtable for a connector


Synopsis
========

.. c:function:: void drm_connector_helper_add( struct drm_connector * connector, const struct drm_connector_helper_funcs * funcs )

Arguments
=========

``connector``
    DRM connector

``funcs``
    helper vtable to set for ``connector``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
