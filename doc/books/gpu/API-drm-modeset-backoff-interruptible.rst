.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-modeset-backoff-interruptible:

=================================
drm_modeset_backoff_interruptible
=================================

*man drm_modeset_backoff_interruptible(9)*

*4.6.0-rc5*

deadlock avoidance backoff


Synopsis
========

.. c:function:: int drm_modeset_backoff_interruptible( struct drm_modeset_acquire_ctx * ctx )

Arguments
=========

``ctx``
    the acquire context


Description
===========

Interruptible version of ``drm_modeset_backoff``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
