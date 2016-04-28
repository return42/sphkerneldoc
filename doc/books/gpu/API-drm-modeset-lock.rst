.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-modeset-lock:

================
drm_modeset_lock
================

*man drm_modeset_lock(9)*

*4.6.0-rc5*

take modeset lock


Synopsis
========

.. c:function:: int drm_modeset_lock( struct drm_modeset_lock * lock, struct drm_modeset_acquire_ctx * ctx )

Arguments
=========

``lock``
    lock to take

``ctx``
    acquire ctx


Description
===========

If ctx is not NULL, then its ww acquire context is used and the lock
will be tracked by the context and can be released by calling
``drm_modeset_drop_locks``. If -EDEADLK is returned, this means a
deadlock scenario has been detected and it is an error to attempt to
take any more locks without first calling ``drm_modeset_backoff``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
