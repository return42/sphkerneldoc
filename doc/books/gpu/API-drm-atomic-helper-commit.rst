
.. _API-drm-atomic-helper-commit:

========================
drm_atomic_helper_commit
========================

*man drm_atomic_helper_commit(9)*

*4.6.0-rc1*

commit validated state object


Synopsis
========

.. c:function:: int drm_atomic_helper_commit( struct drm_device * dev, struct drm_atomic_state * state, bool async )

Arguments
=========

``dev``
    DRM device

``state``
    the driver state object

``async``
    asynchronous commit


Description
===========

This function commits a with ``drm_atomic_helper_check`` pre-validated state object. This can still fail when e.g. the framebuffer reservation fails. For now this doesn't implement
asynchronous commits.

Note that right now this function does not support async commits, and hence driver writers must implement their own version for now. Also note that the default ordering of how the
various stages are called is to match the legacy modeset helper library closest. One peculiarity of that is that it doesn't mesh well with runtime PM at all.

For drivers supporting runtime PM the recommended sequence is

drm_atomic_helper_commit_modeset_disables(dev, state);

drm_atomic_helper_commit_modeset_enables(dev, state);

drm_atomic_helper_commit_planes(dev, state, true);

See the kerneldoc entries for these three functions for more details.

RETURNS Zero for success or -errno.
