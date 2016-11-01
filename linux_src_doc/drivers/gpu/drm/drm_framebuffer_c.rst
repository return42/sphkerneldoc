.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_framebuffer.c

.. _`drm_mode_addfb`:

drm_mode_addfb
==============

.. c:function:: int drm_mode_addfb(struct drm_device *dev, void *data, struct drm_file *file_priv)

    add an FB to the graphics configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_addfb.description`:

Description
-----------

Add a new FB to the specified CRTC, given a user request. This is the
original addfb ioctl which only supported RGB formats.

Called by the user via ioctl.

.. _`drm_mode_addfb.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_addfb2`:

drm_mode_addfb2
===============

.. c:function:: int drm_mode_addfb2(struct drm_device *dev, void *data, struct drm_file *file_priv)

    add an FB to the graphics configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_addfb2.description`:

Description
-----------

Add a new FB to the specified CRTC, given a user request with format. This is
the 2nd version of the addfb ioctl, which supports multi-planar framebuffers
and uses fourcc codes as pixel format specifiers.

Called by the user via ioctl.

.. _`drm_mode_addfb2.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_rmfb`:

drm_mode_rmfb
=============

.. c:function:: int drm_mode_rmfb(struct drm_device *dev, void *data, struct drm_file *file_priv)

    remove an FB from the configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_rmfb.description`:

Description
-----------

Remove the FB specified by the user.

Called by the user via ioctl.

.. _`drm_mode_rmfb.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_getfb`:

drm_mode_getfb
==============

.. c:function:: int drm_mode_getfb(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get FB info

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_getfb.description`:

Description
-----------

Lookup the FB given its ID and return info about it.

Called by the user via ioctl.

.. _`drm_mode_getfb.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_dirtyfb_ioctl`:

drm_mode_dirtyfb_ioctl
======================

.. c:function:: int drm_mode_dirtyfb_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    flush frontbuffer rendering on an FB

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_dirtyfb_ioctl.description`:

Description
-----------

Lookup the FB and flush out the damaged area supplied by userspace as a clip
rectangle list. Generic userspace which does frontbuffer rendering must call
this ioctl to flush out the changes on manual-update display outputs, e.g.
usb display-link, mipi manual update panels or edp panel self refresh modes.

Modesetting drivers which always update the frontbuffer do not need to
implement the corresponding ->dirty framebuffer callback.

Called by the user via ioctl.

.. _`drm_mode_dirtyfb_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_fb_release`:

drm_fb_release
==============

.. c:function:: void drm_fb_release(struct drm_file *priv)

    remove and free the FBs on this file

    :param struct drm_file \*priv:
        drm file for the ioctl

.. _`drm_fb_release.description`:

Description
-----------

Destroy all the FBs associated with \ ``filp``\ .

Called by the user via ioctl.

.. _`drm_fb_release.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_framebuffer_init`:

drm_framebuffer_init
====================

.. c:function:: int drm_framebuffer_init(struct drm_device *dev, struct drm_framebuffer *fb, const struct drm_framebuffer_funcs *funcs)

    initialize a framebuffer

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_framebuffer \*fb:
        framebuffer to be initialized

    :param const struct drm_framebuffer_funcs \*funcs:
        ... with these functions

.. _`drm_framebuffer_init.description`:

Description
-----------

Allocates an ID for the framebuffer's parent mode object, sets its mode
functions & device file and adds it to the master fd list.

.. _`drm_framebuffer_init.important`:

IMPORTANT
---------

This functions publishes the fb and makes it available for concurrent access
by other users. Which means by this point the fb _must_ be fully set up -
since all the fb attributes are invariant over its lifetime, no further
locking but only correct reference counting is required.

.. _`drm_framebuffer_init.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_framebuffer_lookup`:

drm_framebuffer_lookup
======================

.. c:function:: struct drm_framebuffer *drm_framebuffer_lookup(struct drm_device *dev, uint32_t id)

    look up a drm framebuffer and grab a reference

    :param struct drm_device \*dev:
        drm device

    :param uint32_t id:
        id of the fb object

.. _`drm_framebuffer_lookup.description`:

Description
-----------

If successful, this grabs an additional reference to the framebuffer -
callers need to make sure to eventually unreference the returned framebuffer
again, using \ ``drm_framebuffer_unreference``\ .

.. _`drm_framebuffer_unregister_private`:

drm_framebuffer_unregister_private
==================================

.. c:function:: void drm_framebuffer_unregister_private(struct drm_framebuffer *fb)

    unregister a private fb from the lookup idr

    :param struct drm_framebuffer \*fb:
        fb to unregister

.. _`drm_framebuffer_unregister_private.description`:

Description
-----------

Drivers need to call this when cleaning up driver-private framebuffers, e.g.
those used for fbdev. Note that the caller must hold a reference of it's own,
i.e. the object may not be destroyed through this call (since it'll lead to a
locking inversion).

.. _`drm_framebuffer_cleanup`:

drm_framebuffer_cleanup
=======================

.. c:function:: void drm_framebuffer_cleanup(struct drm_framebuffer *fb)

    remove a framebuffer object

    :param struct drm_framebuffer \*fb:
        framebuffer to remove

.. _`drm_framebuffer_cleanup.description`:

Description
-----------

Cleanup framebuffer. This function is intended to be used from the drivers
->destroy callback. It can also be used to clean up driver private
framebuffers embedded into a larger structure.

Note that this function does not remove the fb from active usuage - if it is
still used anywhere, hilarity can ensue since userspace could call getfb on
the id and get back -EINVAL. Obviously no concern at driver unload time.

Also, the framebuffer will not be removed from the lookup idr - for
user-created framebuffers this will happen in in the rmfb ioctl. For
driver-private objects (e.g. for fbdev) drivers need to explicitly call
drm_framebuffer_unregister_private.

.. _`drm_framebuffer_remove`:

drm_framebuffer_remove
======================

.. c:function:: void drm_framebuffer_remove(struct drm_framebuffer *fb)

    remove and unreference a framebuffer object

    :param struct drm_framebuffer \*fb:
        framebuffer to remove

.. _`drm_framebuffer_remove.description`:

Description
-----------

Scans all the CRTCs and planes in \ ``dev``\ 's mode_config.  If they're
using \ ``fb``\ , removes it, setting it to NULL. Then drops the reference to the
passed-in framebuffer. Might take the modeset locks.

Note that this function optimizes the cleanup away if the caller holds the
last reference to the framebuffer. It is also guaranteed to not take the
modeset locks in this case.

.. This file was automatic generated / don't edit.
