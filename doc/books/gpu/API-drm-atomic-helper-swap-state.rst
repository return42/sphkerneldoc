
.. _API-drm-atomic-helper-swap-state:

============================
drm_atomic_helper_swap_state
============================

*man drm_atomic_helper_swap_state(9)*

*4.6.0-rc1*

store atomic state into current sw state


Synopsis
========

.. c:function:: void drm_atomic_helper_swap_state( struct drm_device * dev, struct drm_atomic_state * state )

Arguments
=========

``dev``
    DRM device

``state``
    atomic state


Description
===========

This function stores the atomic state into the current state pointers in all driver objects. It should be called after all failing steps have been done and succeeded, but before
the actual hardware state is committed.

For cleanup and error recovery the current state for all changed objects will be swaped into ``state``.

With that sequence it fits perfectly into the plane prepare/cleanup sequence:

1. Call ``drm_atomic_helper_prepare_planes`` with the staged atomic state.

2. Do any other steps that might fail.

3. Put the staged state into the current state pointers with this function.

4. Actually commit the hardware state.

5. Call ``drm_atomic_helper_cleanup_planes`` with ``state``, which since step 3 contains the old state. Also do any other cleanup required with that state.
