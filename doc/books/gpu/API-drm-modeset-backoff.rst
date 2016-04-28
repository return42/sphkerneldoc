.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-modeset-backoff:

===================
drm_modeset_backoff
===================

*man drm_modeset_backoff(9)*

*4.6.0-rc5*

deadlock avoidance backoff


Synopsis
========

.. c:function:: void drm_modeset_backoff( struct drm_modeset_acquire_ctx * ctx )

Arguments
=========

``ctx``
    the acquire context


Description
===========

If deadlock is detected (ie. ``drm_modeset_lock`` returns -EDEADLK), you
must call this function to drop all currently held locks and block until
the contended lock becomes available.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
