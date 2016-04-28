.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-commit-modeset-enables:

========================================
drm_atomic_helper_commit_modeset_enables
========================================

*man drm_atomic_helper_commit_modeset_enables(9)*

*4.6.0-rc5*

modeset commit to enable outputs


Synopsis
========

.. c:function:: void drm_atomic_helper_commit_modeset_enables( struct drm_device * dev, struct drm_atomic_state * old_state )

Arguments
=========

``dev``
    DRM device

``old_state``
    atomic state object with old state structures


Description
===========

This function enables all the outputs with the new configuration which
had to be turned off for the update.

For compatibility with legacy crtc helpers this should be called after
``drm_atomic_helper_commit_planes``, which is what the default commit
function does. But drivers with different needs can group the modeset
commits together and do the plane commits at the end. This is useful for
drivers doing runtime PM since planes updates then only happen when the
CRTC is actually enabled.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
