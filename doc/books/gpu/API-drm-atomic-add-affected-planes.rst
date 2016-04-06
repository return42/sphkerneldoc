
.. _API-drm-atomic-add-affected-planes:

==============================
drm_atomic_add_affected_planes
==============================

*man drm_atomic_add_affected_planes(9)*

*4.6.0-rc1*

add planes for crtc


Synopsis
========

.. c:function:: int drm_atomic_add_affected_planes( struct drm_atomic_state * state, struct drm_crtc * crtc )

Arguments
=========

``state``
    atomic state

``crtc``
    DRM crtc


Description
===========

This function walks the current configuration and adds all planes currently used by ``crtc`` to the atomic configuration ``state``. This is useful when an atomic commit also needs
to check all currently enabled plane on ``crtc``, e.g. when changing the mode. It's also useful when re-enabling a CRTC to avoid special code to force-enable all planes.

Since acquiring a plane state will always also acquire the w/w mutex of the current CRTC for that plane (if there is any) adding all the plane states for a CRTC will not reduce
parallism of atomic updates.


Returns
=======

0 on success or can fail with -EDEADLK or -ENOMEM. When the error is EDEADLK then the w/w mutex code has detected a deadlock and the entire atomic sequence must be restarted. All
other errors are fatal.
