.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-bridge-attach:

=================
drm_bridge_attach
=================

*man drm_bridge_attach(9)*

*4.6.0-rc5*

associate given bridge to our DRM device


Synopsis
========

.. c:function:: int drm_bridge_attach( struct drm_device * dev, struct drm_bridge * bridge )

Arguments
=========

``dev``
    DRM device

``bridge``
    bridge control structure


Description
===========

called by a kms driver to link one of our encoder/bridge to the given
bridge.

Note that setting up links between the bridge and our encoder/bridge
objects needs to be handled by the kms driver itself


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
