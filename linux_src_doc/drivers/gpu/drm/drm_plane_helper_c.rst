.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_plane_helper.c

.. _`drm_plane_helper_check_update`:

drm_plane_helper_check_update
=============================

.. c:function:: int drm_plane_helper_check_update(struct drm_plane *plane, struct drm_crtc *crtc, struct drm_framebuffer *fb, struct drm_rect *src, struct drm_rect *dest, const struct drm_rect *clip, int min_scale, int max_scale, bool can_position, bool can_update_disabled, bool *visible)

    Check plane update for validity

    :param struct drm_plane \*plane:
        plane object to update

    :param struct drm_crtc \*crtc:
        owning CRTC of owning plane

    :param struct drm_framebuffer \*fb:
        framebuffer to flip onto plane

    :param struct drm_rect \*src:
        source coordinates in 16.16 fixed point

    :param struct drm_rect \*dest:
        integer destination coordinates

    :param const struct drm_rect \*clip:
        integer clipping coordinates

    :param int min_scale:
        minimum \ ``src``\ :\ ``dest``\  scaling factor in 16.16 fixed point

    :param int max_scale:
        maximum \ ``src``\ :\ ``dest``\  scaling factor in 16.16 fixed point

    :param bool can_position:
        is it legal to position the plane such that it
        doesn't cover the entire crtc?  This will generally
        only be false for primary planes.

    :param bool can_update_disabled:
        can the plane be updated while the crtc
        is disabled?

    :param bool \*visible:
        output parameter indicating whether plane is still visible after
        clipping

.. _`drm_plane_helper_check_update.description`:

Description
-----------

Checks that a desired plane update is valid.  Drivers that provide
their own plane handling rather than helper-provided implementations may
still wish to call this function to avoid duplication of error checking
code.

.. _`drm_plane_helper_check_update.return`:

Return
------

Zero if update appears valid, error code on failure

.. _`drm_primary_helper_update`:

drm_primary_helper_update
=========================

.. c:function:: int drm_primary_helper_update(struct drm_plane *plane, struct drm_crtc *crtc, struct drm_framebuffer *fb, int crtc_x, int crtc_y, unsigned int crtc_w, unsigned int crtc_h, uint32_t src_x, uint32_t src_y, uint32_t src_w, uint32_t src_h)

    Helper for primary plane update

    :param struct drm_plane \*plane:
        plane object to update

    :param struct drm_crtc \*crtc:
        owning CRTC of owning plane

    :param struct drm_framebuffer \*fb:
        framebuffer to flip onto plane

    :param int crtc_x:
        x offset of primary plane on crtc

    :param int crtc_y:
        y offset of primary plane on crtc

    :param unsigned int crtc_w:
        width of primary plane rectangle on crtc

    :param unsigned int crtc_h:
        height of primary plane rectangle on crtc

    :param uint32_t src_x:
        x offset of \ ``fb``\  for panning

    :param uint32_t src_y:
        y offset of \ ``fb``\  for panning

    :param uint32_t src_w:
        width of source rectangle in \ ``fb``\ 

    :param uint32_t src_h:
        height of source rectangle in \ ``fb``\ 

.. _`drm_primary_helper_update.description`:

Description
-----------

Provides a default plane update handler for primary planes.  This is handler
is called in response to a userspace SetPlane operation on the plane with a
non-NULL framebuffer.  We call the driver's modeset handler to update the
framebuffer.

\ :c:func:`SetPlane`\  on a primary plane of a disabled CRTC is not supported, and will
return an error.

Note that we make some assumptions about hardware limitations that may not be
true for all hardware --
1) Primary plane cannot be repositioned.
2) Primary plane cannot be scaled.
3) Primary plane must cover the entire CRTC.
4) Subpixel positioning is not supported.
Drivers for hardware that don't have these restrictions can provide their
own implementation rather than using this helper.

.. _`drm_primary_helper_update.return`:

Return
------

Zero on success, error code on failure

.. _`drm_primary_helper_disable`:

drm_primary_helper_disable
==========================

.. c:function:: int drm_primary_helper_disable(struct drm_plane *plane)

    Helper for primary plane disable

    :param struct drm_plane \*plane:
        plane to disable

.. _`drm_primary_helper_disable.description`:

Description
-----------

Provides a default plane disable handler for primary planes.  This is handler
is called in response to a userspace SetPlane operation on the plane with a
NULL framebuffer parameter.  It unconditionally fails the disable call with
-EINVAL the only way to disable the primary plane without driver support is
to disable the entier CRTC. Which does not match the plane ->disable hook.

Note that some hardware may be able to disable the primary plane without
disabling the whole CRTC.  Drivers for such hardware should provide their
own disable handler that disables just the primary plane (and they'll likely
need to provide their own update handler as well to properly re-enable a
disabled primary plane).

.. _`drm_primary_helper_disable.return`:

Return
------

Unconditionally returns -EINVAL.

.. _`drm_primary_helper_destroy`:

drm_primary_helper_destroy
==========================

.. c:function:: void drm_primary_helper_destroy(struct drm_plane *plane)

    Helper for primary plane destruction

    :param struct drm_plane \*plane:
        plane to destroy

.. _`drm_primary_helper_destroy.description`:

Description
-----------

Provides a default plane destroy handler for primary planes.  This handler
is called during CRTC destruction.  We disable the primary plane, remove
it from the DRM plane list, and deallocate the plane structure.

.. _`drm_crtc_init`:

drm_crtc_init
=============

.. c:function:: int drm_crtc_init(struct drm_device *dev, struct drm_crtc *crtc, const struct drm_crtc_funcs *funcs)

    Legacy CRTC initialization function

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_crtc \*crtc:
        CRTC object to init

    :param const struct drm_crtc_funcs \*funcs:
        callbacks for the new CRTC

.. _`drm_crtc_init.description`:

Description
-----------

Initialize a CRTC object with a default helper-provided primary plane and no
cursor plane.

.. _`drm_crtc_init.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_plane_helper_update`:

drm_plane_helper_update
=======================

.. c:function:: int drm_plane_helper_update(struct drm_plane *plane, struct drm_crtc *crtc, struct drm_framebuffer *fb, int crtc_x, int crtc_y, unsigned int crtc_w, unsigned int crtc_h, uint32_t src_x, uint32_t src_y, uint32_t src_w, uint32_t src_h)

    Transitional helper for plane update

    :param struct drm_plane \*plane:
        plane object to update

    :param struct drm_crtc \*crtc:
        owning CRTC of owning plane

    :param struct drm_framebuffer \*fb:
        framebuffer to flip onto plane

    :param int crtc_x:
        x offset of primary plane on crtc

    :param int crtc_y:
        y offset of primary plane on crtc

    :param unsigned int crtc_w:
        width of primary plane rectangle on crtc

    :param unsigned int crtc_h:
        height of primary plane rectangle on crtc

    :param uint32_t src_x:
        x offset of \ ``fb``\  for panning

    :param uint32_t src_y:
        y offset of \ ``fb``\  for panning

    :param uint32_t src_w:
        width of source rectangle in \ ``fb``\ 

    :param uint32_t src_h:
        height of source rectangle in \ ``fb``\ 

.. _`drm_plane_helper_update.description`:

Description
-----------

Provides a default plane update handler using the atomic plane update
functions. It is fully left to the driver to check plane constraints and
handle corner-cases like a fully occluded or otherwise invisible plane.

This is useful for piecewise transitioning of a driver to the atomic helpers.

.. _`drm_plane_helper_update.return`:

Return
------

Zero on success, error code on failure

.. _`drm_plane_helper_disable`:

drm_plane_helper_disable
========================

.. c:function:: int drm_plane_helper_disable(struct drm_plane *plane)

    Transitional helper for plane disable

    :param struct drm_plane \*plane:
        plane to disable

.. _`drm_plane_helper_disable.description`:

Description
-----------

Provides a default plane disable handler using the atomic plane update
functions. It is fully left to the driver to check plane constraints and
handle corner-cases like a fully occluded or otherwise invisible plane.

This is useful for piecewise transitioning of a driver to the atomic helpers.

.. _`drm_plane_helper_disable.return`:

Return
------

Zero on success, error code on failure

.. This file was automatic generated / don't edit.
