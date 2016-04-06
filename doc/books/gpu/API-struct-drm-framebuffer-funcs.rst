
.. _API-struct-drm-framebuffer-funcs:

============================
struct drm_framebuffer_funcs
============================

*man struct drm_framebuffer_funcs(9)*

*4.6.0-rc1*

framebuffer hooks


Synopsis
========

.. code-block:: c

    struct drm_framebuffer_funcs {
      void (* destroy) (struct drm_framebuffer *framebuffer);
      int (* create_handle) (struct drm_framebuffer *fb,struct drm_file *file_priv,unsigned int *handle);
      int (* dirty) (struct drm_framebuffer *framebuffer,struct drm_file *file_priv, unsigned flags,unsigned color, struct drm_clip_rect *clips,unsigned num_clips);
    };


Members
=======

destroy
    Clean up framebuffer resources, specifically also unreference the backing storage. The core guarantees to call this function for every framebuffer successfully created by
    ->``fb_create`` in ``drm_mode_config_funcs``. Drivers must also call ``drm_framebuffer_cleanup`` to release DRM core resources for this framebuffer.

create_handle
    Create a buffer handle in the driver-specific buffer manager (either GEM or TTM) valid for the passed-in struct ``drm_file``. This is used by the core to implement the GETFB
    IOCTL, which returns (for sufficiently priviledged user) also a native buffer handle. This can be used for seamless transitions between modesetting clients by copying the
    current screen contents to a private buffer and blending between that and the new contents.

    GEM based drivers should call ``drm_gem_handle_create`` to create the handle.

    RETURNS:

    0 on success or a negative error code on failure.

dirty
    Optional callback for the dirty fb IOCTL.

    Userspace can notify the driver via this callback that an area of the framebuffer has changed and should be flushed to the display hardware. This can also be used internally,
    e.g. by the fbdev emulation, though that's not the case currently.

    See documentation in drm_mode.h for the struct drm_mode_fb_dirty_cmd for more information as all the semantics and arguments have a one to one mapping on this function.

    RETURNS:

    0 on success or a negative error code on failure.
