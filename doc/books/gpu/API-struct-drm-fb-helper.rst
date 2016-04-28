.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-fb-helper:

====================
struct drm_fb_helper
====================

*man struct drm_fb_helper(9)*

*4.6.0-rc5*

main structure to emulate fbdev on top of KMS


Synopsis
========

.. code-block:: c

    struct drm_fb_helper {
      struct drm_framebuffer * fb;
      struct drm_device * dev;
      int crtc_count;
      struct drm_fb_helper_crtc * crtc_info;
      int connector_count;
      int connector_info_alloc_count;
      struct drm_fb_helper_connector ** connector_info;
      const struct drm_fb_helper_funcs * funcs;
      struct fb_info * fbdev;
      u32 pseudo_palette[17];
      struct list_head kernel_fb_list;
      bool delayed_hotplug;
      bool atomic;
    };


Members
=======

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

pseudo_palette[17]
    fake palette of 16 colors

kernel_fb_list
    Entry on the global kernel_fb_helper_list, used for kgdb
    entry/exit.

delayed_hotplug
    A hotplug was received while fbdev wasn't in control of the DRM
    device, i.e. another KMS master was active. The output configuration
    needs to be reprobe when fbdev is in control again.

atomic
    Use atomic updates for ``restore_fbdev_mode``, etc. This defaults to
    true if driver has DRIVER_ATOMIC feature flag, but drivers can
    override it to true after ``drm_fb_helper_init`` if they support
    atomic modeset but do not yet advertise DRIVER_ATOMIC (note that
    fb-helper does not require ASYNC commits).


Description
===========

This is the main structure used by the fbdev helpers. Drivers supporting
fbdev emulation should embedded this into their overall driver
structure. Drivers must also fill out a struct ``drm_fb_helper_funcs``
with a few operations.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
