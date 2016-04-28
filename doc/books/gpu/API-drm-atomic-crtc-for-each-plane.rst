.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-crtc-for-each-plane:

==============================
drm_atomic_crtc_for_each_plane
==============================

*man drm_atomic_crtc_for_each_plane(9)*

*4.6.0-rc5*

iterate over planes currently attached to CRTC


Synopsis
========

.. c:function:: drm_atomic_crtc_for_each_plane( plane, crtc )

Arguments
=========

``plane``
    the loop cursor

``crtc``
    the crtc whose planes are iterated


Description
===========

This iterates over the current state, useful (for example) when applying
atomic state after it has been checked and swapped. To iterate over the
planes which *will* be attached (for ->``atomic_check``) see
``drm_crtc_for_each_pending_plane``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
