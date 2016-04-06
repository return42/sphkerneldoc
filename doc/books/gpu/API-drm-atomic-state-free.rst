
.. _API-drm-atomic-state-free:

=====================
drm_atomic_state_free
=====================

*man drm_atomic_state_free(9)*

*4.6.0-rc1*

free all memory for an atomic state


Synopsis
========

.. c:function:: void drm_atomic_state_free( struct drm_atomic_state * state )

Arguments
=========

``state``
    atomic state to deallocate


Description
===========

This frees all memory associated with an atomic state, including all the per-object state for planes, crtcs and connectors.
