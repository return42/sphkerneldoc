.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-connector-list-update:

==============================
drm_mode_connector_list_update
==============================

*man drm_mode_connector_list_update(9)*

*4.6.0-rc5*

update the mode list for the connector


Synopsis
========

.. c:function:: void drm_mode_connector_list_update( struct drm_connector * connector )

Arguments
=========

``connector``
    the connector to update


Description
===========

This moves the modes from the ``connector`` probed_modes list to the
actual mode list. It compares the probed mode against the current list
and only adds different/new modes.

This is just a helper functions doesn't validate any modes itself and
also doesn't prune any invalid modes. Callers need to do that
themselves.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
