
.. _API-drm-framebuffer-unregister-private:

==================================
drm_framebuffer_unregister_private
==================================

*man drm_framebuffer_unregister_private(9)*

*4.6.0-rc1*

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

Drivers need to call this when cleaning up driver-private framebuffers, e.g. those used for fbdev. Note that the caller must hold a reference of it's own, i.e. the object may not
be destroyed through this call (since it'll lead to a locking inversion).
