
.. _API-drm-atomic-state-default-clear:

==============================
drm_atomic_state_default_clear
==============================

*man drm_atomic_state_default_clear(9)*

*4.6.0-rc1*

clear base atomic state


Synopsis
========

.. c:function:: void drm_atomic_state_default_clear( struct drm_atomic_state * state )

Arguments
=========

``state``
    atomic state


Description
===========

Default implementation for clearing atomic state. This is useful for drivers that subclass the atomic state.
