.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-connector-register:

======================
drm_connector_register
======================

*man drm_connector_register(9)*

*4.6.0-rc5*

register a connector


Synopsis
========

.. c:function:: int drm_connector_register( struct drm_connector * connector )

Arguments
=========

``connector``
    the connector to register


Description
===========

Register userspace interfaces for a connector


Returns
=======

Zero on success, error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
