.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-kms-helper-poll-init:

========================
drm_kms_helper_poll_init
========================

*man drm_kms_helper_poll_init(9)*

*4.6.0-rc5*

initialize and enable output polling


Synopsis
========

.. c:function:: void drm_kms_helper_poll_init( struct drm_device * dev )

Arguments
=========

``dev``
    drm_device


Description
===========

This function intializes and then also enables output polling support
for ``dev``. Drivers which do not have reliable hotplug support in
hardware can use this helper infrastructure to regularly poll such
connectors for changes in their connection state.

Drivers can control which connectors are polled by setting the
DRM_CONNECTOR_POLL_CONNECT and DRM_CONNECTOR_POLL_DISCONNECT
flags. On connectors where probing live outputs can result in visual
distortion drivers should not set the DRM_CONNECTOR_POLL_DISCONNECT
flag to avoid this. Connectors which have no flag or only
DRM_CONNECTOR_POLL_HPD set are completely ignored by the polling
logic.

Note that a connector can be both polled and probed from the hotplug
handler, in case the hotplug interrupt is known to be unreliable.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
