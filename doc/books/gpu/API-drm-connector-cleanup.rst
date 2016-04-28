.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-connector-cleanup:

=====================
drm_connector_cleanup
=====================

*man drm_connector_cleanup(9)*

*4.6.0-rc5*

cleans up an initialised connector


Synopsis
========

.. c:function:: void drm_connector_cleanup( struct drm_connector * connector )

Arguments
=========

``connector``
    connector to cleanup


Description
===========

Cleans up the connector but doesn't free the object.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
