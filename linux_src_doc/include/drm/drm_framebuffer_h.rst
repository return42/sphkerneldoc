.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_framebuffer.h

.. _`drm_framebuffer_funcs`:

struct drm_framebuffer_funcs
============================

.. c:type:: struct drm_framebuffer_funcs

    framebuffer hooks

.. _`drm_framebuffer_funcs.definition`:

Definition
----------

.. code-block:: c

    struct drm_framebuffer_funcs {
        void (*destroy)(struct drm_framebuffer *framebuffer);
        int (*create_handle)(struct drm_framebuffer *fb,struct drm_file *file_priv, unsigned int *handle);
        int (*dirty)(struct drm_framebuffer *framebuffer,struct drm_file *file_priv, unsigned flags,unsigned color, struct drm_clip_rect *clips, unsigned num_clips);
    }

.. _`drm_framebuffer_funcs.members`:

Members
-------

destroy

    Clean up framebuffer resources, specifically also unreference the
    backing storage. The core guarantees to call this function for every
    framebuffer successfully created by calling
    \ :c:type:`drm_mode_config_funcs.fb_create <drm_mode_config_funcs>`\ . Drivers must also call
    \ :c:func:`drm_framebuffer_cleanup`\  to release DRM core resources for this
    framebuffer.

create_handle

    Create a buffer handle in the driver-specific buffer manager (either
    GEM or TTM) valid for the passed-in \ :c:type:`struct drm_file <drm_file>`\ . This is used by
    the core to implement the GETFB IOCTL, which returns (for
    sufficiently priviledged user) also a native buffer handle. This can
    be used for seamless transitions between modesetting clients by
    copying the current screen contents to a private buffer and blending
    between that and the new contents.

    GEM based drivers should call \ :c:func:`drm_gem_handle_create`\  to create the
    handle.

    RETURNS:

    0 on success or a negative error code on failure.

dirty

    Optional callback for the dirty fb IOCTL.

    Userspace can notify the driver via this callback that an area of the
    framebuffer has changed and should be flushed to the display
    hardware. This can also be used internally, e.g. by the fbdev
    emulation, though that's not the case currently.

    See documentation in drm_mode.h for the struct drm_mode_fb_dirty_cmd
    for more information as all the semantics and arguments have a one to
    one mapping on this function.

    RETURNS:

    0 on success or a negative error code on failure.

.. _`drm_framebuffer`:

struct drm_framebuffer
======================

.. c:type:: struct drm_framebuffer

    frame buffer object

.. _`drm_framebuffer.definition`:

Definition
----------

.. code-block:: c

    struct drm_framebuffer {
        struct drm_device *dev;
        struct list_head head;
        struct drm_mode_object base;
        const struct drm_format_info *format;
        const struct drm_framebuffer_funcs *funcs;
        unsigned int pitches[4];
        unsigned int offsets[4];
        uint64_t modifier;
        unsigned int width;
        unsigned int height;
        int flags;
        int hot_x;
        int hot_y;
        struct list_head filp_head;
        struct drm_gem_object *obj[4];
    }

.. _`drm_framebuffer.members`:

Members
-------

dev
    DRM device this framebuffer belongs to

head
    Place on the \ :c:type:`drm_mode_config.fb_list <drm_mode_config>`\ , access protected by&drm_mode_config.fb_lock.

base
    base modeset object structure, contains the reference count.

format
    framebuffer format information

funcs
    framebuffer vfunc table

pitches
    Line stride per buffer. For userspace created object thisis copied from drm_mode_fb_cmd2.

offsets
    Offset from buffer start to the actual pixel data in bytes,per buffer. For userspace created object this is copied from
    drm_mode_fb_cmd2.

    Note that this is a linear offset and does not take into account
    tiling or buffer laytou per \ ``modifier``\ . It meant to be used when the
    actual pixel data for this framebuffer plane starts at an offset,
    e.g.  when multiple planes are allocated within the same backing
    storage buffer object. For tiled layouts this generally means it
    \ ``offsets``\  must at least be tile-size aligned, but hardware often has
    stricter requirements.

    This should not be used to specifiy x/y pixel offsets into the buffer
    data (even for linear buffers). Specifying an x/y pixel offset is
    instead done through the source rectangle in \ :c:type:`struct drm_plane_state <drm_plane_state>`\ .

modifier
    Data layout modifier. This is used to describetiling, or also special layouts (like compression) of auxiliary
    buffers. For userspace created object this is copied from
    drm_mode_fb_cmd2.

width
    Logical width of the visible area of the framebuffer, inpixels.

height
    Logical height of the visible area of the framebuffer, inpixels.

flags
    Framebuffer flags like DRM_MODE_FB_INTERLACED orDRM_MODE_FB_MODIFIERS.

hot_x
    X coordinate of the cursor hotspot. Used by the legacy cursorIOCTL when the driver supports cursor through a DRM_PLANE_TYPE_CURSOR
    universal plane.

hot_y
    Y coordinate of the cursor hotspot. Used by the legacy cursorIOCTL when the driver supports cursor through a DRM_PLANE_TYPE_CURSOR
    universal plane.

filp_head
    Placed on \ :c:type:`drm_file.fbs <drm_file>`\ , protected by \ :c:type:`drm_file.fbs_lock <drm_file>`\ .

obj
    GEM objects backing the framebuffer, one per plane (optional).
    This is used by the GEM framebuffer helpers, see e.g.
    \ :c:func:`drm_gem_fb_create`\ .

.. _`drm_framebuffer.description`:

Description
-----------

Note that the fb is refcounted for the benefit of driver internals,
for example some hw, disabling a CRTC/plane is asynchronous, and
scanout does not actually complete until the next vblank.  So some
cleanup (like releasing the reference(s) on the backing GEM bo(s))
should be deferred.  In cases like this, the driver would like to
hold a ref to the fb even though it has already been removed from
userspace perspective. See \ :c:func:`drm_framebuffer_get`\  and
\ :c:func:`drm_framebuffer_put`\ .

The refcount is stored inside the mode object \ ``base``\ .

.. _`drm_framebuffer_get`:

drm_framebuffer_get
===================

.. c:function:: void drm_framebuffer_get(struct drm_framebuffer *fb)

    acquire a framebuffer reference

    :param struct drm_framebuffer \*fb:
        DRM framebuffer

.. _`drm_framebuffer_get.description`:

Description
-----------

This function increments the framebuffer's reference count.

.. _`drm_framebuffer_put`:

drm_framebuffer_put
===================

.. c:function:: void drm_framebuffer_put(struct drm_framebuffer *fb)

    release a framebuffer reference

    :param struct drm_framebuffer \*fb:
        DRM framebuffer

.. _`drm_framebuffer_put.description`:

Description
-----------

This function decrements the framebuffer's reference count and frees the
framebuffer if the reference count drops to zero.

.. _`drm_framebuffer_reference`:

drm_framebuffer_reference
=========================

.. c:function:: void drm_framebuffer_reference(struct drm_framebuffer *fb)

    acquire a framebuffer reference

    :param struct drm_framebuffer \*fb:
        DRM framebuffer

.. _`drm_framebuffer_reference.description`:

Description
-----------

This is a compatibility alias for \ :c:func:`drm_framebuffer_get`\  and should not be
used by new code.

.. _`drm_framebuffer_unreference`:

drm_framebuffer_unreference
===========================

.. c:function:: void drm_framebuffer_unreference(struct drm_framebuffer *fb)

    release a framebuffer reference

    :param struct drm_framebuffer \*fb:
        DRM framebuffer

.. _`drm_framebuffer_unreference.description`:

Description
-----------

This is a compatibility alias for \ :c:func:`drm_framebuffer_put`\  and should not be
used by new code.

.. _`drm_framebuffer_read_refcount`:

drm_framebuffer_read_refcount
=============================

.. c:function:: uint32_t drm_framebuffer_read_refcount(struct drm_framebuffer *fb)

    read the framebuffer reference count.

    :param struct drm_framebuffer \*fb:
        framebuffer

.. _`drm_framebuffer_read_refcount.description`:

Description
-----------

This functions returns the framebuffer's reference count.

.. _`drm_framebuffer_assign`:

drm_framebuffer_assign
======================

.. c:function:: void drm_framebuffer_assign(struct drm_framebuffer **p, struct drm_framebuffer *fb)

    store a reference to the fb

    :param struct drm_framebuffer \*\*p:
        location to store framebuffer

    :param struct drm_framebuffer \*fb:
        new framebuffer (maybe NULL)

.. _`drm_framebuffer_assign.description`:

Description
-----------

This functions sets the location to store a reference to the framebuffer,
unreferencing the framebuffer that was previously stored in that location.

.. This file was automatic generated / don't edit.

