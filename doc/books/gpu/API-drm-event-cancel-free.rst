.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-event-cancel-free:

=====================
drm_event_cancel_free
=====================

*man drm_event_cancel_free(9)*

*4.6.0-rc5*

free a DRM event and release it's space


Synopsis
========

.. c:function:: void drm_event_cancel_free( struct drm_device * dev, struct drm_pending_event * p )

Arguments
=========

``dev``
    DRM device

``p``
    tracking structure for the pending event


Description
===========

This function frees the event ``p`` initialized with
``drm_event_reserve_init`` and releases any allocated space.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
