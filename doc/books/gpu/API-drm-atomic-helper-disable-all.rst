.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-disable-all:

=============================
drm_atomic_helper_disable_all
=============================

*man drm_atomic_helper_disable_all(9)*

*4.6.0-rc5*

disable all currently active outputs


Synopsis
========

.. c:function:: int drm_atomic_helper_disable_all( struct drm_device * dev, struct drm_modeset_acquire_ctx * ctx )

Arguments
=========

``dev``
    DRM device

``ctx``
    lock acquisition context


Description
===========

Loops through all connectors, finding those that aren't turned off and
then turns them off by setting their DPMS mode to OFF and deactivating
the CRTC that they are connected to.

This is used for example in suspend/resume to disable all currently
active functions when suspending.

Note that if callers haven't already acquired all modeset locks this
might return -EDEADLK, which must be handled by calling
``drm_modeset_backoff``.


Returns
=======

0 on success or a negative error code on failure.


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
