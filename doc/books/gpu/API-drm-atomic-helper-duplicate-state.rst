.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-duplicate-state:

=================================
drm_atomic_helper_duplicate_state
=================================

*man drm_atomic_helper_duplicate_state(9)*

*4.6.0-rc5*

duplicate an atomic state object


Synopsis
========

.. c:function:: struct drm_atomic_state * drm_atomic_helper_duplicate_state( struct drm_device * dev, struct drm_modeset_acquire_ctx * ctx )

Arguments
=========

``dev``
    DRM device

``ctx``
    lock acquisition context


Description
===========

Makes a copy of the current atomic state by looping over all objects and
duplicating their respective states. This is used for example by
suspend/ resume support code to save the state prior to suspend such
that it can be restored upon resume.

Note that this treats atomic state as persistent between save and
restore. Drivers must make sure that this is possible and won't result
in confusion or erroneous behaviour.

Note that if callers haven't already acquired all modeset locks this
might return -EDEADLK, which must be handled by calling
``drm_modeset_backoff``.


Returns
=======

A pointer to the copy of the atomic state object on success or an
``ERR_PTR``-encoded error code on failure.


See also
========

``drm_atomic_helper_suspend``, ``drm_atomic_helper_resume``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
