
.. _API-struct-drm-display-mode:

=======================
struct drm_display_mode
=======================

*man struct drm_display_mode(9)*

*4.6.0-rc1*

DRM kernel-internal display mode structure


Synopsis
========

.. code-block:: c

    struct drm_display_mode {
      struct list_head head;
      struct drm_mode_object base;
      char name[DRM_DISPLAY_MODE_LEN];
      enum drm_mode_status status;
      unsigned int type;
      int clock;
      int hdisplay;
      int hsync_start;
      int hsync_end;
      int htotal;
      int hskew;
      int vdisplay;
      int vsync_start;
      int vsync_end;
      int vtotal;
      int vscan;
      unsigned int flags;
      int width_mm;
      int height_mm;
      int crtc_clock;
      int crtc_hdisplay;
      int crtc_hblank_start;
      int crtc_hblank_end;
      int crtc_hsync_start;
      int crtc_hsync_end;
      int crtc_htotal;
      int crtc_hskew;
      int crtc_vdisplay;
      int crtc_vblank_start;
      int crtc_vblank_end;
      int crtc_vsync_start;
      int crtc_vsync_end;
      int crtc_vtotal;
      int * private;
      int private_flags;
      int vrefresh;
      int hsync;
      enum hdmi_picture_aspect picture_aspect_ratio;
    };


Members
=======

head
    struct list_head for mode lists.

base
    A display mode is a normal modeset object, possibly including public userspace id.

    FIXME:

    This can probably be removed since the entire concept of userspace managing modes explicitly has never landed in upstream kernel mode setting support.

name[DRM_DISPLAY_MODE_LEN]
    Human-readable name of the mode, filled out with ``drm_mode_set_name``.

status
    Status of the mode, used to filter out modes not supported by the hardware. See enum ``drm_mode_status``.

type
    A bitmask of flags, mostly about the source of a mode. Possible flags are:

    - DRM_MODE_TYPE_BUILTIN: Meant for hard-coded modes, effectively unused. - DRM_MODE_TYPE_PREFERRED: Preferred mode, usually the native resolution of an LCD panel. There
    should only be one preferred mode per connector at any given time. - DRM_MODE_TYPE_DRIVER: Mode created by the driver, which is all of them really. Drivers must set this bit
    for all modes they create and expose to userspace.

    Plus a big list of flags which shouldn't be used at all, but are still around since these flags are also used in the userspace ABI:

    - DRM_MODE_TYPE_DEFAULT: Again a leftover, use DRM_MODE_TYPE_PREFERRED instead. - DRM_MODE_TYPE_CLOCK_C and DRM_MODE_TYPE_CRTC_C: Define leftovers which are stuck
    around for hysterical raisins only. No one has an idea what they were meant for. Don't use. - DRM_MODE_TYPE_USERDEF: Mode defined by userspace, again a vestige from older
    kms designs where userspace had to first add a custom mode to the kernel's mode list before it could use it. Don't use.

clock
    Pixel clock in kHz.

hdisplay
    horizontal display size

hsync_start
    horizontal sync start

hsync_end
    horizontal sync end

htotal
    horizontal total size

hskew
    horizontal skew?!

vdisplay
    vertical display size

vsync_start
    vertical sync start

vsync_end
    vertical sync end

vtotal
    vertical total size

vscan
    vertical scan?!

flags
    Sync and timing flags:

    - DRM_MODE_FLAG_PHSYNC: horizontal sync is active high. - DRM_MODE_FLAG_NHSYNC: horizontal sync is active low. - DRM_MODE_FLAG_PVSYNC: vertical sync is active high. -
    DRM_MODE_FLAG_NVSYNC: vertical sync is active low. - DRM_MODE_FLAG_INTERLACE: mode is interlaced. - DRM_MODE_FLAG_DBLSCAN: mode uses doublescan. -
    DRM_MODE_FLAG_CSYNC: mode uses composite sync. - DRM_MODE_FLAG_PCSYNC: composite sync is active high. - DRM_MODE_FLAG_NCSYNC: composite sync is active low. -
    DRM_MODE_FLAG_HSKEW: hskew provided (not used?). - DRM_MODE_FLAG_BCAST: not used? - DRM_MODE_FLAG_PIXMUX: not used? - DRM_MODE_FLAG_DBLCLK: double-clocked mode. -
    DRM_MODE_FLAG_CLKDIV2: half-clocked mode.

    Additionally there's flags to specify how 3D modes are packed:

    - DRM_MODE_FLAG_3D_NONE: normal, non-3D mode. - DRM_MODE_FLAG_3D_FRAME_PACKING: 2 full frames for left and right. - DRM_MODE_FLAG_3D_FIELD_ALTERNATIVE:
    interleaved like fields. - DRM_MODE_FLAG_3D_LINE_ALTERNATIVE: interleaved lines. - DRM_MODE_FLAG_3D_SIDE_BY_SIDE_FULL: side-by-side full frames. -
    DRM_MODE_FLAG_3D_L_DEPTH: ? - DRM_MODE_FLAG_3D_L_DEPTH_GFX_GFX_DEPTH: ? - DRM_MODE_FLAG_3D_TOP_AND_BOTTOM: frame split into top and bottom parts. -
    DRM_MODE_FLAG_3D_SIDE_BY_SIDE_HALF: frame split into left and right parts.

width_mm
    Addressable size of the output in mm, projectors should set this to 0.

height_mm
    Addressable size of the output in mm, projectors should set this to 0.

crtc_clock
    Actual pixel or dot clock in the hardware. This differs from the logical ``clock`` when e.g. using interlacing, double-clocking, stereo modes or other fancy stuff that changes
    the timings and signals actually sent over the wire.

    This is again in kHz.

    Note that with digital outputs like HDMI or DP there's usually a massive confusion between the dot clock and the signal clock at the bit encoding level. Especially when a
    8b/10b encoding is used and the difference is exactly a factor of 10.

crtc_hdisplay
    hardware mode horizontal display size

crtc_hblank_start
    hardware mode horizontal blank start

crtc_hblank_end
    hardware mode horizontal blank end

crtc_hsync_start
    hardware mode horizontal sync start

crtc_hsync_end
    hardware mode horizontal sync end

crtc_htotal
    hardware mode horizontal total size

crtc_hskew
    hardware mode horizontal skew?!

crtc_vdisplay
    hardware mode vertical display size

crtc_vblank_start
    hardware mode vertical blank start

crtc_vblank_end
    hardware mode vertical blank end

crtc_vsync_start
    hardware mode vertical sync start

crtc_vsync_end
    hardware mode vertical sync end

crtc_vtotal
    hardware mode vertical total size

private
    Pointer for driver private data. This can only be used for mode objects passed to drivers in modeset operations. It shouldn't be used by atomic drivers since they can store any
    additional data by subclassing state structures.

private_flags
    Similar to ``private``, but just an integer.

vrefresh
    Vertical refresh rate, for debug output in human readable form. Not used in a functional way.

    This value is in Hz.

hsync
    Horizontal refresh rate, for debug output in human readable form. Not used in a functional way.

    This value is in kHz.

picture_aspect_ratio
    Field for setting the HDMI picture aspect ratio of a mode.


Description
===========

The horizontal and vertical timings are defined per the following diagram.

Active Front Sync Back Region Porch Porch <-----------------------><----------------><-------------><--------------> //////////////////////| ////////////////////// |
////////////////////// |.................. ................ _______________ <----- [hv]display -----> <------------- [hv]sync_start ------------>
<--------------------- [hv]sync_end ---------------------> <-------------------------------- [hv]total ----------------------------->⋆

This structure contains two copies of timings. First are the plain timings, which specify the logical mode, as it would be for a progressive 1:1 scanout at the refresh rate
userspace can observe through vblank timestamps. Then there's the hardware timings, which are corrected for interlacing, double-clocking and similar things. They are provided as a
convenience, and can be appropriately computed using ``drm_mode_set_crtcinfo``.
