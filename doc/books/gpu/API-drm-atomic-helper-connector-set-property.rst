.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-connector-set-property:

========================================
drm_atomic_helper_connector_set_property
========================================

*man drm_atomic_helper_connector_set_property(9)*

*4.6.0-rc5*

helper for connector properties


Synopsis
========

.. c:function:: int drm_atomic_helper_connector_set_property( struct drm_connector * connector, struct drm_property * property, uint64_t val )

Arguments
=========

``connector``
    DRM connector

``property``
    DRM property

``val``
    value of property


Description
===========

Provides a default connector set_property handler using the atomic
driver interface.


RETURNS
=======

Zero on success, error code on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
