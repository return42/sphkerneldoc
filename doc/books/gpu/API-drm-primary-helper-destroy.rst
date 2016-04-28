.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-primary-helper-destroy:

==========================
drm_primary_helper_destroy
==========================

*man drm_primary_helper_destroy(9)*

*4.6.0-rc5*

Helper for primary plane destruction


Synopsis
========

.. c:function:: void drm_primary_helper_destroy( struct drm_plane * plane )

Arguments
=========

``plane``
    plane to destroy


Description
===========

Provides a default plane destroy handler for primary planes. This
handler is called during CRTC destruction. We disable the primary plane,
remove it from the DRM plane list, and deallocate the plane structure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
