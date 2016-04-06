
.. _API-drm-framebuffer-cleanup:

=======================
drm_framebuffer_cleanup
=======================

*man drm_framebuffer_cleanup(9)*

*4.6.0-rc1*

remove a framebuffer object


Synopsis
========

.. c:function:: void drm_framebuffer_cleanup( struct drm_framebuffer * fb )

Arguments
=========

``fb``
    framebuffer to remove


Description
===========

Cleanup framebuffer. This function is intended to be used from the drivers ->destroy callback. It can also be used to clean up driver private framebuffers embedded into a larger
structure.

Note that this function does not remove the fb from active usuage - if it is still used anywhere, hilarity can ensue since userspace could call getfb on the id and get back
-EINVAL. Obviously no concern at driver unload time.

Also, the framebuffer will not be removed from the lookup idr - for user-created framebuffers this will happen in in the rmfb ioctl. For driver-private objects (e.g. for fbdev)
drivers need to explicitly call drm_framebuffer_unregister_private.
