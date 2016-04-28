.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-plane-cleanup:

=================
drm_plane_cleanup
=================

*man drm_plane_cleanup(9)*

*4.6.0-rc5*

Clean up the core plane usage


Synopsis
========

.. c:function:: void drm_plane_cleanup( struct drm_plane * plane )

Arguments
=========

``plane``
    plane to cleanup


Description
===========

This function cleans up ``plane`` and removes it from the DRM mode
setting core. Note that the function does *not* free the plane structure
itself, this is the responsibility of the caller.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
