.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_fb_helper.h

.. _`drm_fb_helper_surface_size`:

struct drm_fb_helper_surface_size
=================================

.. c:type:: struct drm_fb_helper_surface_size

    describes fbdev size and scanout surface size

.. _`drm_fb_helper_surface_size.definition`:

Definition
----------

.. code-block:: c

    struct drm_fb_helper_surface_size {
        u32 fb_width;
        u32 fb_height;
        u32 surface_width;
        u32 surface_height;
        u32 surface_bpp;
        u32 surface_depth;
    }

.. _`drm_fb_helper_surface_size.members`:

Members
-------

fb_width
    fbdev width

fb_height
    fbdev height

surface_width
    scanout buffer width

surface_height
    scanout buffer height

surface_bpp
    scanout buffer bpp

surface_depth
    scanout buffer depth

.. _`drm_fb_helper_surface_size.description`:

Description
-----------

Note that the scanout surface width/height may be larger than the fbdev
width/height.  In case of multiple displays, the scanout surface is sized
according to the largest width/height (so it is large enough for all CRTCs
to scanout).  But the fbdev width/height is sized to the minimum width/
height of all the displays.  This ensures that fbcon fits on the smallest
of the attached displays.

So what is passed to \ :c:func:`drm_fb_helper_fill_var`\  should be fb_width/fb_height,
rather than the surface size.

.. _`drm_fb_helper_funcs`:

struct drm_fb_helper_funcs
==========================

.. c:type:: struct drm_fb_helper_funcs

    driver callbacks for the fbdev emulation library

.. _`drm_fb_helper_funcs.definition`:

Definition
----------

.. code-block:: c

    struct drm_fb_helper_funcs {
        void (* gamma_set) (struct drm_crtc *crtc, u16 red, u16 green,u16 blue, int regno);
        void (* gamma_get) (struct drm_crtc *crtc, u16 *red, u16 *green,u16 *blue, int regno);
        int (* fb_probe) (struct drm_fb_helper *helper,struct drm_fb_helper_surface_size *sizes);
        bool (* initial_config) (struct drm_fb_helper *fb_helper,struct drm_fb_helper_crtc **crtcs,struct drm_display_mode **modes,struct drm_fb_offset *offsets,bool *enabled, int width, int height);
    }

.. _`drm_fb_helper_funcs.members`:

Members
-------

gamma_set

    Set the given gamma LUT register on the given CRTC.

    This callback is optional.

    FIXME:

    This callback is functionally redundant with the core gamma table
    support and simply exists because the fbdev hasn't yet been
    refactored to use the core gamma table interfaces.

gamma_get

    Read the given gamma LUT register on the given CRTC, used to save the
    current LUT when force-restoring the fbdev for e.g. kdbg.

    This callback is optional.

    FIXME:

    This callback is functionally redundant with the core gamma table
    support and simply exists because the fbdev hasn't yet been
    refactored to use the core gamma table interfaces.

fb_probe

    Driver callback to allocate and initialize the fbdev info structure.
    Furthermore it also needs to allocate the DRM framebuffer used to
    back the fbdev.

    This callback is mandatory.

    RETURNS:

    The driver should return 0 on success and a negative error code on
    failure.

initial_config

    Driver callback to setup an initial fbdev display configuration.
    Drivers can use this callback to tell the fbdev emulation what the
    preferred initial configuration is. This is useful to implement
    smooth booting where the fbdev (and subsequently all userspace) never
    changes the mode, but always inherits the existing configuration.

    This callback is optional.

    RETURNS:

    The driver should return true if a suitable initial configuration has
    been filled out and false when the fbdev helper should fall back to
    the default probing logic.

.. _`drm_fb_helper_funcs.description`:

Description
-----------

Driver callbacks used by the fbdev emulation helper library.

.. _`drm_fb_helper`:

struct drm_fb_helper
====================

.. c:type:: struct drm_fb_helper

    main structure to emulate fbdev on top of KMS

.. _`drm_fb_helper.definition`:

Definition
----------

.. code-block:: c

    struct drm_fb_helper {
        struct drm_framebuffer *fb;
        struct drm_device *dev;
        int crtc_count;
        struct drm_fb_helper_crtc *crtc_info;
        int connector_count;
        int connector_info_alloc_count;
        struct drm_fb_helper_connector **connector_info;
        const struct drm_fb_helper_funcs *funcs;
        struct fb_info *fbdev;
        u32 pseudo_palette[17];
        struct drm_clip_rect dirty_clip;
        spinlock_t dirty_lock;
        struct work_struct dirty_work;
        struct list_head kernel_fb_list;
        bool delayed_hotplug;
        bool atomic;
    }

.. _`drm_fb_helper.members`:

Members
-------

fb
    Scanout framebuffer object

dev
    DRM device

crtc_count
    number of possible CRTCs

crtc_info
    per-CRTC helper state (mode, x/y offset, etc)

connector_count
    number of connected connectors

connector_info_alloc_count
    size of connector_info

connector_info
    array of per-connector information

funcs
    driver callbacks for fb helper

fbdev
    emulated fbdev device info struct

pseudo_palette
    fake palette of 16 colors

dirty_clip
    clip rectangle used with deferred_io to accumulate damage to
    the screen buffer

dirty_lock
    spinlock protecting \ ``dirty_clip``\ 

dirty_work
    worker used to flush the framebuffer

kernel_fb_list

    Entry on the global kernel_fb_helper_list, used for kgdb entry/exit.

delayed_hotplug

    A hotplug was received while fbdev wasn't in control of the DRM
    device, i.e. another KMS master was active. The output configuration
    needs to be reprobe when fbdev is in control again.

atomic

    Use atomic updates for \ :c:func:`restore_fbdev_mode`\ , etc.  This defaults to
    true if driver has DRIVER_ATOMIC feature flag, but drivers can
    override it to true after \ :c:func:`drm_fb_helper_init`\  if they support atomic
    modeset but do not yet advertise DRIVER_ATOMIC (note that fb-helper
    does not require ASYNC commits).

.. _`drm_fb_helper.description`:

Description
-----------

This is the main structure used by the fbdev helpers. Drivers supporting
fbdev emulation should embedded this into their overall driver structure.
Drivers must also fill out a struct \ :c:type:`struct drm_fb_helper_funcs <drm_fb_helper_funcs>` with a few
operations.

.. This file was automatic generated / don't edit.

