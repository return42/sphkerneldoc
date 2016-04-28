.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-fb-helper-funcs:

==========================
struct drm_fb_helper_funcs
==========================

*man struct drm_fb_helper_funcs(9)*

*4.6.0-rc5*

driver callbacks for the fbdev emulation library


Synopsis
========

.. code-block:: c

    struct drm_fb_helper_funcs {
      void (* gamma_set) (struct drm_crtc *crtc, u16 red, u16 green,u16 blue, int regno);
      void (* gamma_get) (struct drm_crtc *crtc, u16 *red, u16 *green,u16 *blue, int regno);
      int (* fb_probe) (struct drm_fb_helper *helper,struct drm_fb_helper_surface_size *sizes);
      bool (* initial_config) (struct drm_fb_helper *fb_helper,struct drm_fb_helper_crtc **crtcs,struct drm_display_mode **modes,struct drm_fb_offset *offsets,bool *enabled, int width, int height);
    };


Members
=======

gamma_set
    Set the given gamma LUT register on the given CRTC.

    This callback is optional.

    FIXME:

    This callback is functionally redundant with the core gamma table
    support and simply exists because the fbdev hasn't yet been
    refactored to use the core gamma table interfaces.

gamma_get
    Read the given gamma LUT register on the given CRTC, used to save
    the current LUT when force-restoring the fbdev for e.g. kdbg.

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
    smooth booting where the fbdev (and subsequently all userspace)
    never changes the mode, but always inherits the existing
    configuration.

    This callback is optional.

    RETURNS:

    The driver should return true if a suitable initial configuration
    has been filled out and false when the fbdev helper should fall back
    to the default probing logic.


Description
===========

Driver callbacks used by the fbdev emulation helper library.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
