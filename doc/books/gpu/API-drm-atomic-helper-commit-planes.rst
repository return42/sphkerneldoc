.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-commit-planes:

===============================
drm_atomic_helper_commit_planes
===============================

*man drm_atomic_helper_commit_planes(9)*

*4.6.0-rc5*

commit plane state


Synopsis
========

.. c:function:: void drm_atomic_helper_commit_planes( struct drm_device * dev, struct drm_atomic_state * old_state, bool active_only )

Arguments
=========

``dev``
    DRM device

``old_state``
    atomic state object with old state structures

``active_only``
    Only commit on active CRTC if set


Description
===========

This function commits the new plane state using the plane and atomic
helper functions for planes and crtcs. It assumes that the atomic state
has already been pushed into the relevant object state pointers, since
this step can no longer fail.

It still requires the global state object ``old_state`` to know which
planes and crtcs need to be updated though.

Note that this function does all plane updates across all CRTCs in one
step. If the hardware can't support this approach look at
``drm_atomic_helper_commit_planes_on_crtc`` instead.

Plane parameters can be updated by applications while the associated
CRTC is disabled. The DRM/KMS core will store the parameters in the
plane state, which will be available to the driver when the CRTC is
turned on. As a result most drivers don't need to be immediately
notified of plane updates for a disabled CRTC.

Unless otherwise needed, drivers are advised to set the ``active_only``
parameters to true in order not to receive plane update notifications
related to a disabled CRTC. This avoids the need to manually ignore
plane updates in driver code when the driver and/or hardware can't or
just don't need to deal with updates on disabled CRTCs, for example when
supporting runtime PM.

The ``drm_atomic_helper_commit`` default implementation only sets
``active_only`` to false to most closely match the behaviour of the
legacy helpers. This should not be copied blindly by drivers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
