
.. _API-drm-atomic-state-init:

=====================
drm_atomic_state_init
=====================

*man drm_atomic_state_init(9)*

*4.6.0-rc1*

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

Default implementation for filling in a new atomic state. This is useful for drivers that subclass the atomic state.
