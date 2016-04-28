.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-plane-check:

======================
drm_atomic_plane_check
======================

*man drm_atomic_plane_check(9)*

*4.6.0-rc5*

check plane state


Synopsis
========

.. c:function:: int drm_atomic_plane_check( struct drm_plane * plane, struct drm_plane_state * state )

Arguments
=========

``plane``
    plane to check

``state``
    plane state to check


Description
===========

Provides core sanity checks for plane state.


RETURNS
=======

Zero on success, error code on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
