.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-primary-helper-disable:

==========================
drm_primary_helper_disable
==========================

*man drm_primary_helper_disable(9)*

*4.6.0-rc5*

Helper for primary plane disable


Synopsis
========

.. c:function:: int drm_primary_helper_disable( struct drm_plane * plane )

Arguments
=========

``plane``
    plane to disable


Description
===========

Provides a default plane disable handler for primary planes. This is
handler is called in response to a userspace SetPlane operation on the
plane with a NULL framebuffer parameter. It unconditionally fails the
disable call with -EINVAL the only way to disable the primary plane
without driver support is to disable the entier CRTC. Which does not
match the plane ->disable hook.

Note that some hardware may be able to disable the primary plane without
disabling the whole CRTC. Drivers for such hardware should provide their
own disable handler that disables just the primary plane (and they'll
likely need to provide their own update handler as well to properly
re-enable a disabled primary plane).


RETURNS
=======

Unconditionally returns -EINVAL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
