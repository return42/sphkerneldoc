.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-framebuffer-unregister-private:

==================================
drm_framebuffer_unregister_private
==================================

*man drm_framebuffer_unregister_private(9)*

*4.6.0-rc5*

unregister a private fb from the lookup idr


Synopsis
========

.. c:function:: void drm_framebuffer_unregister_private( struct drm_framebuffer * fb )

Arguments
=========

``fb``
    fb to unregister


Description
===========

Drivers need to call this when cleaning up driver-private framebuffers,
e.g. those used for fbdev. Note that the caller must hold a reference of
it's own, i.e. the object may not be destroyed through this call (since
it'll lead to a locking inversion).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
