.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-set-fb-for-plane:

===========================
drm_atomic_set_fb_for_plane
===========================

*man drm_atomic_set_fb_for_plane(9)*

*4.6.0-rc5*

set framebuffer for plane


Synopsis
========

.. c:function:: void drm_atomic_set_fb_for_plane( struct drm_plane_state * plane_state, struct drm_framebuffer * fb )

Arguments
=========

``plane_state``
    atomic state object for the plane

``fb``
    fb to use for the plane


Description
===========

Changing the assigned framebuffer for a plane requires us to grab a
reference to the new fb and drop the reference to the old fb, if there
is one. This function takes care of all these details besides updating
the pointer in the state object itself.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
