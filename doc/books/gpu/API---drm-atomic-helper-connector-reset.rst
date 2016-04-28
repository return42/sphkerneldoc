.. -*- coding: utf-8; mode: rst -*-

.. _API---drm-atomic-helper-connector-reset:

===================================
__drm_atomic_helper_connector_reset
===================================

*man __drm_atomic_helper_connector_reset(9)*

*4.6.0-rc5*

reset state on connector


Synopsis
========

.. c:function:: void __drm_atomic_helper_connector_reset( struct drm_connector * connector, struct drm_connector_state * conn_state )

Arguments
=========

``connector``
    drm connector

``conn_state``
    connector state to assign


Description
===========

Initializes the newly allocated ``conn_state`` and assigns it to
#connector ->state, usually required when initializing the drivers or
when called from the ->reset hook.

This is useful for drivers that subclass the connector state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
