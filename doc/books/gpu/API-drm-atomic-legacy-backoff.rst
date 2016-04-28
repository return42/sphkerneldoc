.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-legacy-backoff:

=========================
drm_atomic_legacy_backoff
=========================

*man drm_atomic_legacy_backoff(9)*

*4.6.0-rc5*

locking backoff for legacy ioctls


Synopsis
========

.. c:function:: void drm_atomic_legacy_backoff( struct drm_atomic_state * state )

Arguments
=========

``state``
    atomic state


Description
===========

This function should be used by legacy entry points which don't
understand -EDEADLK semantics. For simplicity this one will grab all
modeset locks after the slowpath completed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
