.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_blend.c

.. _`overview`:

overview
========

The basic plane composition model supported by standard plane properties only
has a source rectangle (in logical pixels within the \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\ ), with
sub-pixel accuracy, which is scaled up to a pixel-aligned destination
rectangle in the visible area of a \ :c:type:`struct drm_crtc <drm_crtc>`\ . The visible area of a CRTC is
defined by the horizontal and vertical visible pixels (stored in \ ``hdisplay``\ 
and \ ``vdisplay``\ ) of the requested mode (stored in \ :c:type:`drm_crtc_state.mode <drm_crtc_state>`\ ). These
two rectangles are both stored in the \ :c:type:`struct drm_plane_state <drm_plane_state>`\ .

For the atomic ioctl the following standard (atomic) properties on the plane object
encode the basic plane composition model:

SRC_X:
     X coordinate offset for the source rectangle within the
     \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\ , in 16.16 fixed point. Must be positive.
SRC_Y:
     Y coordinate offset for the source rectangle within the
     \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\ , in 16.16 fixed point. Must be positive.
SRC_W:
     Width for the source rectangle within the \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\ , in 16.16
     fixed point. SRC_X plus SRC_W must be within the width of the source
     framebuffer. Must be positive.
SRC_H:
     Height for the source rectangle within the \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\ , in 16.16
     fixed point. SRC_Y plus SRC_H must be within the height of the source
     framebuffer. Must be positive.
CRTC_X:
     X coordinate offset for the destination rectangle. Can be negative.
CRTC_Y:
     Y coordinate offset for the destination rectangle. Can be negative.
CRTC_W:
     Width for the destination rectangle. CRTC_X plus CRTC_W can extend past
     the currently visible horizontal area of the \ :c:type:`struct drm_crtc <drm_crtc>`\ .
CRTC_H:
     Height for the destination rectangle. CRTC_Y plus CRTC_H can extend past
     the currently visible vertical area of the \ :c:type:`struct drm_crtc <drm_crtc>`\ .
FB_ID:
     Mode object ID of the \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\  this plane should scan out.
CRTC_ID:
     Mode object ID of the \ :c:type:`struct drm_crtc <drm_crtc>`\  this plane should be connected to.

Note that the source rectangle must fully lie within the bounds of the
\ :c:type:`struct drm_framebuffer <drm_framebuffer>`\ . The destination rectangle can lie outside of the visible
area of the current mode of the CRTC. It must be apprpriately clipped by the
driver, which can be done by calling \ :c:func:`drm_plane_helper_check_update`\ . Drivers
are also allowed to round the subpixel sampling positions appropriately, but
only to the next full pixel. No pixel outside of the source rectangle may
ever be sampled, which is important when applying more sophisticated
filtering than just a bilinear one when scaling. The filtering mode when
scaling is unspecified.

On top of this basic transformation additional properties can be exposed by
the driver:

alpha:
     Alpha is setup with \ :c:func:`drm_plane_create_alpha_property`\ . It controls the
     plane-wide opacity, from transparent (0) to opaque (0xffff). It can be
     combined with pixel alpha.
     The pixel values in the framebuffers are expected to not be
     pre-multiplied by the global alpha associated to the plane.

rotation:
     Rotation is set up with \ :c:func:`drm_plane_create_rotation_property`\ . It adds a
     rotation and reflection step between the source and destination rectangles.
     Without this property the rectangle is only scaled, but not rotated or
     reflected.

zpos:
     Z position is set up with \ :c:func:`drm_plane_create_zpos_immutable_property`\  and
     \ :c:func:`drm_plane_create_zpos_property`\ . It controls the visibility of overlapping
     planes. Without this property the primary plane is always below the cursor
     plane, and ordering between all other planes is undefined.

Note that all the property extensions described here apply either to the
plane or the CRTC (e.g. for the background color, which currently is not
exposed and assumed to be black).

.. _`drm_plane_create_alpha_property`:

drm_plane_create_alpha_property
===============================

.. c:function:: int drm_plane_create_alpha_property(struct drm_plane *plane)

    create a new alpha property

    :param struct drm_plane \*plane:
        drm plane

.. _`drm_plane_create_alpha_property.description`:

Description
-----------

This function creates a generic, mutable, alpha property and enables support
for it in the DRM core. It is attached to \ ``plane``\ .

The alpha property will be allowed to be within the bounds of 0
(transparent) to 0xffff (opaque).

.. _`drm_plane_create_alpha_property.return`:

Return
------

0 on success, negative error code on failure.

.. _`drm_plane_create_rotation_property`:

drm_plane_create_rotation_property
==================================

.. c:function:: int drm_plane_create_rotation_property(struct drm_plane *plane, unsigned int rotation, unsigned int supported_rotations)

    create a new rotation property

    :param struct drm_plane \*plane:
        drm plane

    :param unsigned int rotation:
        initial value of the rotation property

    :param unsigned int supported_rotations:
        bitmask of supported rotations and reflections

.. _`drm_plane_create_rotation_property.description`:

Description
-----------

This creates a new property with the selected support for transformations.

Since a rotation by 180° degress is the same as reflecting both along the x
and the y axis the rotation property is somewhat redundant. Drivers can use
\ :c:func:`drm_rotation_simplify`\  to normalize values of this property.

The property exposed to userspace is a bitmask property (see
\ :c:func:`drm_property_create_bitmask`\ ) called "rotation" and has the following

.. _`drm_plane_create_rotation_property.drm_mode_rotate_0`:

DRM_MODE_ROTATE_0
-----------------


     "rotate-0"

.. _`drm_plane_create_rotation_property.drm_mode_rotate_90`:

DRM_MODE_ROTATE_90
------------------

     "rotate-90"

.. _`drm_plane_create_rotation_property.drm_mode_rotate_180`:

DRM_MODE_ROTATE_180
-------------------

     "rotate-180"

.. _`drm_plane_create_rotation_property.drm_mode_rotate_270`:

DRM_MODE_ROTATE_270
-------------------

     "rotate-270"

.. _`drm_plane_create_rotation_property.drm_mode_reflect_x`:

DRM_MODE_REFLECT_X
------------------

     "reflect-x"

.. _`drm_plane_create_rotation_property.drm_mode_reflect_y`:

DRM_MODE_REFLECT_Y
------------------

     "reflect-y"

Rotation is the specified amount in degrees in counter clockwise direction,
the X and Y axis are within the source rectangle, i.e.  the X/Y axis before
rotation. After reflection, the rotation is applied to the image sampled from
the source rectangle, before scaling it to fit the destination rectangle.

.. _`drm_rotation_simplify`:

drm_rotation_simplify
=====================

.. c:function:: unsigned int drm_rotation_simplify(unsigned int rotation, unsigned int supported_rotations)

    Try to simplify the rotation

    :param unsigned int rotation:
        Rotation to be simplified

    :param unsigned int supported_rotations:
        Supported rotations

.. _`drm_rotation_simplify.description`:

Description
-----------

Attempt to simplify the rotation to a form that is supported.
Eg. if the hardware supports everything except DRM_MODE_REFLECT_X

.. _`drm_rotation_simplify.one-could-call-this-function-like-this`:

one could call this function like this
--------------------------------------


drm_rotation_simplify(rotation, DRM_MODE_ROTATE_0 |
                      DRM_MODE_ROTATE_90 | DRM_MODE_ROTATE_180 |
                      DRM_MODE_ROTATE_270 | DRM_MODE_REFLECT_Y);

to eliminate the DRM_MODE_ROTATE_X flag. Depending on what kind of
transforms the hardware supports, this function may not
be able to produce a supported transform, so the caller should
check the result afterwards.

.. _`drm_plane_create_zpos_property`:

drm_plane_create_zpos_property
==============================

.. c:function:: int drm_plane_create_zpos_property(struct drm_plane *plane, unsigned int zpos, unsigned int min, unsigned int max)

    create mutable zpos property

    :param struct drm_plane \*plane:
        drm plane

    :param unsigned int zpos:
        initial value of zpos property

    :param unsigned int min:
        minimal possible value of zpos property

    :param unsigned int max:
        maximal possible value of zpos property

.. _`drm_plane_create_zpos_property.description`:

Description
-----------

This function initializes generic mutable zpos property and enables support
for it in drm core. Drivers can then attach this property to planes to enable
support for configurable planes arrangement during blending operation.
Drivers that attach a mutable zpos property to any plane should call the
\ :c:func:`drm_atomic_normalize_zpos`\  helper during their implementation of
\ :c:type:`drm_mode_config_funcs.atomic_check() <drm_mode_config_funcs>`\ , which will update the normalized zpos
values and store them in \ :c:type:`drm_plane_state.normalized_zpos <drm_plane_state>`\ . Usually min
should be set to 0 and max to maximal number of planes for given crtc - 1.

If zpos of some planes cannot be changed (like fixed background or
cursor/topmost planes), driver should adjust min/max values and assign those
planes immutable zpos property with lower or higher values (for more
information, see \ :c:func:`drm_plane_create_zpos_immutable_property`\  function). In such
case driver should also assign proper initial zpos values for all planes in
its \ :c:func:`plane_reset`\  callback, so the planes will be always sorted properly.

See also \ :c:func:`drm_atomic_normalize_zpos`\ .

The property exposed to userspace is called "zpos".

.. _`drm_plane_create_zpos_property.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_plane_create_zpos_immutable_property`:

drm_plane_create_zpos_immutable_property
========================================

.. c:function:: int drm_plane_create_zpos_immutable_property(struct drm_plane *plane, unsigned int zpos)

    create immuttable zpos property

    :param struct drm_plane \*plane:
        drm plane

    :param unsigned int zpos:
        value of zpos property

.. _`drm_plane_create_zpos_immutable_property.description`:

Description
-----------

This function initializes generic immutable zpos property and enables
support for it in drm core. Using this property driver lets userspace
to get the arrangement of the planes for blending operation and notifies
it that the hardware (or driver) doesn't support changing of the planes'
order. For mutable zpos see \ :c:func:`drm_plane_create_zpos_property`\ .

The property exposed to userspace is called "zpos".

.. _`drm_plane_create_zpos_immutable_property.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_atomic_normalize_zpos`:

drm_atomic_normalize_zpos
=========================

.. c:function:: int drm_atomic_normalize_zpos(struct drm_device *dev, struct drm_atomic_state *state)

    calculate normalized zpos values for all crtcs

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*state:
        atomic state of DRM device

.. _`drm_atomic_normalize_zpos.description`:

Description
-----------

This function calculates normalized zpos value for all modified planes in
the provided atomic state of DRM device.

For every CRTC this function checks new states of all planes assigned to
it and calculates normalized zpos value for these planes. Planes are compared
first by their zpos values, then by plane id (if zpos is equal). The plane
with lowest zpos value is at the bottom. The \ :c:type:`drm_plane_state.normalized_zpos <drm_plane_state>`\ 
is then filled with unique values from 0 to number of active planes in crtc
minus one.

RETURNS
Zero for success or -errno

.. This file was automatic generated / don't edit.

