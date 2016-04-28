.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-connector-attach-encoder:

=================================
drm_mode_connector_attach_encoder
=================================

*man drm_mode_connector_attach_encoder(9)*

*4.6.0-rc5*

attach a connector to an encoder


Synopsis
========

.. c:function:: int drm_mode_connector_attach_encoder( struct drm_connector * connector, struct drm_encoder * encoder )

Arguments
=========

``connector``
    connector to attach

``encoder``
    encoder to attach ``connector`` to


Description
===========

This function links up a connector to an encoder. Note that the routing
restrictions between encoders and crtcs are exposed to userspace through
the possible_clones and possible_crtcs bitmasks.


Returns
=======

Zero on success, negative errno on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
