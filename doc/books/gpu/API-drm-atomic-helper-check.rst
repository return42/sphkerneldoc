
.. _API-drm-atomic-helper-check:

=======================
drm_atomic_helper_check
=======================

*man drm_atomic_helper_check(9)*

*4.6.0-rc1*

validate state object


Synopsis
========

.. c:function:: int drm_atomic_helper_check( struct drm_device * dev, struct drm_atomic_state * state )

Arguments
=========

``dev``
    DRM device

``state``
    the driver state object


Description
===========

Check the state object to see if the requested state is physically possible. Only crtcs and planes have check callbacks, so for any additional (global) checking that a driver needs
it can simply wrap that around this function. Drivers without such needs can directly use this as their ->``atomic_check`` callback.

This just wraps the two parts of the state checking for planes and modeset


state in the default order
==========================

First it calls ``drm_atomic_helper_check_modeset`` and then ``drm_atomic_helper_check_planes``. The assumption is that the ->atomic_check functions depend upon an updated
adjusted_mode.clock to e.g. properly compute watermarks.

RETURNS Zero for success or -errno
