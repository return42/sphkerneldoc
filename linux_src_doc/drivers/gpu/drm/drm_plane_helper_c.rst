.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_plane_helper.c

.. _`overview`:

overview
========

This helper library has two parts. The first part has support to implement
primary plane support on top of the normal CRTC configuration interface.
Since the legacy \ :c:type:`drm_mode_config_funcs.set_config <drm_mode_config_funcs>`\  interface ties the primary
plane together with the CRTC state this does not allow userspace to disable
the primary plane itself.  To avoid too much duplicated code use
\ :c:func:`drm_plane_helper_check_update`\  which can be used to enforce the same
restrictions as primary planes had thus. The default primary plane only
expose XRBG8888 and ARGB8888 as valid pixel formats for the attached
framebuffer.

Drivers are highly recommended to implement proper support for primary
planes, and newly merged drivers must not rely upon these transitional
helpers.

The second part also implements transitional helpers which allow drivers to
gradually switch to the atomic helper infrastructure for plane updates. Once
that switch is complete drivers shouldn't use these any longer, instead using
the proper legacy implementations for update and disable plane hooks provided
by the atomic helpers.

Again drivers are strongly urged to switch to the new interfaces.

The plane helpers share the function table structures with other helpers,
specifically also the atomic helpers. See \ :c:type:`struct drm_plane_helper_funcs <drm_plane_helper_funcs>`\  for
the details.

.. _`drm_plane_helper_check_update`:

drm_plane_helper_check_update
=============================

.. c:function:: int drm_plane_helper_check_update(struct drm_plane *plane, struct drm_crtc *crtc, struct drm_framebuffer *fb, struct drm_rect *src, struct drm_rect *dst, unsigned int rotation, int min_scale, int max_scale, bool can_position, bool can_update_disabled, bool *visible)

    Check plane update for validity

    :param plane:
        plane object to update
    :type plane: struct drm_plane \*

    :param crtc:
        owning CRTC of owning plane
    :type crtc: struct drm_crtc \*

    :param fb:
        framebuffer to flip onto plane
    :type fb: struct drm_framebuffer \*

    :param src:
        source coordinates in 16.16 fixed point
    :type src: struct drm_rect \*

    :param dst:
        integer destination coordinates
    :type dst: struct drm_rect \*

    :param rotation:
        plane rotation
    :type rotation: unsigned int

    :param min_scale:
        minimum \ ``src``\ :@dest scaling factor in 16.16 fixed point
    :type min_scale: int

    :param max_scale:
        maximum \ ``src``\ :@dest scaling factor in 16.16 fixed point
    :type max_scale: int

    :param can_position:
        is it legal to position the plane such that it
        doesn't cover the entire crtc?  This will generally
        only be false for primary planes.
    :type can_position: bool

    :param can_update_disabled:
        can the plane be updated while the crtc
        is disabled?
    :type can_update_disabled: bool

    :param visible:
        output parameter indicating whether plane is still visible after
        clipping
    :type visible: bool \*

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

.. c:function:: int drm_primary_helper_update(struct drm_plane *plane, struct drm_crtc *crtc, struct drm_framebuffer *fb, int crtc_x, int crtc_y, unsigned int crtc_w, unsigned int crtc_h, uint32_t src_x, uint32_t src_y, uint32_t src_w, uint32_t src_h, struct drm_modeset_acquire_ctx *ctx)

    Helper for primary plane update

    :param plane:
        plane object to update
    :type plane: struct drm_plane \*

    :param crtc:
        owning CRTC of owning plane
    :type crtc: struct drm_crtc \*

    :param fb:
        framebuffer to flip onto plane
    :type fb: struct drm_framebuffer \*

    :param crtc_x:
        x offset of primary plane on crtc
    :type crtc_x: int

    :param crtc_y:
        y offset of primary plane on crtc
    :type crtc_y: int

    :param crtc_w:
        width of primary plane rectangle on crtc
    :type crtc_w: unsigned int

    :param crtc_h:
        height of primary plane rectangle on crtc
    :type crtc_h: unsigned int

    :param src_x:
        x offset of \ ``fb``\  for panning
    :type src_x: uint32_t

    :param src_y:
        y offset of \ ``fb``\  for panning
    :type src_y: uint32_t

    :param src_w:
        width of source rectangle in \ ``fb``\ 
    :type src_w: uint32_t

    :param src_h:
        height of source rectangle in \ ``fb``\ 
    :type src_h: uint32_t

    :param ctx:
        lock acquire context, not used here
    :type ctx: struct drm_modeset_acquire_ctx \*

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

1. Primary plane cannot be repositioned.
2. Primary plane cannot be scaled.
3. Primary plane must cover the entire CRTC.
4. Subpixel positioning is not supported.

Drivers for hardware that don't have these restrictions can provide their
own implementation rather than using this helper.

.. _`drm_primary_helper_update.return`:

Return
------

Zero on success, error code on failure

.. _`drm_primary_helper_disable`:

drm_primary_helper_disable
==========================

.. c:function:: int drm_primary_helper_disable(struct drm_plane *plane, struct drm_modeset_acquire_ctx *ctx)

    Helper for primary plane disable

    :param plane:
        plane to disable
    :type plane: struct drm_plane \*

    :param ctx:
        lock acquire context, not used here
    :type ctx: struct drm_modeset_acquire_ctx \*

.. _`drm_primary_helper_disable.description`:

Description
-----------

Provides a default plane disable handler for primary planes.  This is handler
is called in response to a userspace SetPlane operation on the plane with a
NULL framebuffer parameter.  It unconditionally fails the disable call with
-EINVAL the only way to disable the primary plane without driver support is
to disable the entire CRTC. Which does not match the plane
\ :c:type:`drm_plane_funcs.disable_plane <drm_plane_funcs>`\  hook.

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

    :param plane:
        plane to destroy
    :type plane: struct drm_plane \*

.. _`drm_primary_helper_destroy.description`:

Description
-----------

Provides a default plane destroy handler for primary planes.  This handler
is called during CRTC destruction.  We disable the primary plane, remove
it from the DRM plane list, and deallocate the plane structure.

.. _`drm_plane_helper_update`:

drm_plane_helper_update
=======================

.. c:function:: int drm_plane_helper_update(struct drm_plane *plane, struct drm_crtc *crtc, struct drm_framebuffer *fb, int crtc_x, int crtc_y, unsigned int crtc_w, unsigned int crtc_h, uint32_t src_x, uint32_t src_y, uint32_t src_w, uint32_t src_h, struct drm_modeset_acquire_ctx *ctx)

    Transitional helper for plane update

    :param plane:
        plane object to update
    :type plane: struct drm_plane \*

    :param crtc:
        owning CRTC of owning plane
    :type crtc: struct drm_crtc \*

    :param fb:
        framebuffer to flip onto plane
    :type fb: struct drm_framebuffer \*

    :param crtc_x:
        x offset of primary plane on crtc
    :type crtc_x: int

    :param crtc_y:
        y offset of primary plane on crtc
    :type crtc_y: int

    :param crtc_w:
        width of primary plane rectangle on crtc
    :type crtc_w: unsigned int

    :param crtc_h:
        height of primary plane rectangle on crtc
    :type crtc_h: unsigned int

    :param src_x:
        x offset of \ ``fb``\  for panning
    :type src_x: uint32_t

    :param src_y:
        y offset of \ ``fb``\  for panning
    :type src_y: uint32_t

    :param src_w:
        width of source rectangle in \ ``fb``\ 
    :type src_w: uint32_t

    :param src_h:
        height of source rectangle in \ ``fb``\ 
    :type src_h: uint32_t

    :param ctx:
        lock acquire context, not used here
    :type ctx: struct drm_modeset_acquire_ctx \*

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

.. c:function:: int drm_plane_helper_disable(struct drm_plane *plane, struct drm_modeset_acquire_ctx *ctx)

    Transitional helper for plane disable

    :param plane:
        plane to disable
    :type plane: struct drm_plane \*

    :param ctx:
        lock acquire context, not used here
    :type ctx: struct drm_modeset_acquire_ctx \*

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

