.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-modeset-lock-interruptible:

==============================
drm_modeset_lock_interruptible
==============================

*man drm_modeset_lock_interruptible(9)*

*4.6.0-rc5*

take modeset lock


Synopsis
========

.. c:function:: int drm_modeset_lock_interruptible( struct drm_modeset_lock * lock, struct drm_modeset_acquire_ctx * ctx )

Arguments
=========

``lock``
    lock to take

``ctx``
    acquire ctx


Description
===========

Interruptible version of ``drm_modeset_lock``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
