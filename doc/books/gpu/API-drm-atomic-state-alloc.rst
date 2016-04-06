
.. _API-drm-atomic-state-alloc:

======================
drm_atomic_state_alloc
======================

*man drm_atomic_state_alloc(9)*

*4.6.0-rc1*

allocate atomic state


Synopsis
========

.. c:function:: struct drm_atomic_state ⋆ drm_atomic_state_alloc( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

This allocates an empty atomic state to track updates.
