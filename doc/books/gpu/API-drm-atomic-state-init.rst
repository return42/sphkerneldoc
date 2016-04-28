.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-state-init:

=====================
drm_atomic_state_init
=====================

*man drm_atomic_state_init(9)*

*4.6.0-rc5*

init new atomic state


Synopsis
========

.. c:function:: int drm_atomic_state_init( struct drm_device * dev, struct drm_atomic_state * state )

Arguments
=========

``dev``
    DRM device

``state``
    atomic state


Description
===========

Default implementation for filling in a new atomic state. This is useful
for drivers that subclass the atomic state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
