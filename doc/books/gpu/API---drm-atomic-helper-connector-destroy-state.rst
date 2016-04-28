.. -*- coding: utf-8; mode: rst -*-

.. _API---drm-atomic-helper-connector-destroy-state:

===========================================
__drm_atomic_helper_connector_destroy_state
===========================================

*man __drm_atomic_helper_connector_destroy_state(9)*

*4.6.0-rc5*

release connector state


Synopsis
========

.. c:function:: void __drm_atomic_helper_connector_destroy_state( struct drm_connector * connector, struct drm_connector_state * state )

Arguments
=========

``connector``
    connector object

``state``
    connector state object to release


Description
===========

Releases all resources stored in the connector state without actually
freeing the memory of the connector state. This is useful for drivers
that subclass the connector state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
