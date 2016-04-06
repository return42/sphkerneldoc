
.. _API-drm-calc-vbltimestamp-from-scanoutpos:

=====================================
drm_calc_vbltimestamp_from_scanoutpos
=====================================

*man drm_calc_vbltimestamp_from_scanoutpos(9)*

*4.6.0-rc1*

precise vblank timestamp helper


Synopsis
========

.. c:function:: int drm_calc_vbltimestamp_from_scanoutpos( struct drm_device * dev, unsigned int pipe, int * max_error, struct timeval * vblank_time, unsigned flags, const struct drm_display_mode * mode )

Arguments
=========

``dev``
    DRM device

``pipe``
    index of CRTC whose vblank timestamp to retrieve

``max_error``
    Desired maximum allowable error in timestamps (nanosecs) On return contains true maximum error of timestamp

``vblank_time``
    Pointer to struct timeval which should receive the timestamp

``flags``
    Flags to pass to driver: 0 = Default, DRM_CALLED_FROM_VBLIRQ = If function is called from vbl IRQ handler

``mode``
    mode which defines the scanout timings


Description
===========

Implements calculation of exact vblank timestamps from given drm_display_mode timings and current video scanout position of a CRTC. This can be called from within
``get_vblank_timestamp`` implementation of a kms driver to implement the actual timestamping.

Should return timestamps conforming to the OML_sync_control OpenML extension specification. The timestamp corresponds to the end of the vblank interval, aka start of scanout of
topmost-leftmost display pixel in the following video frame.

Requires support for optional dev->driver-> ``get_scanout_position`` in kms driver, plus a bit of setup code to provide a drm_display_mode that corresponds to the true scanout
timing.

The current implementation only handles standard video modes. It returns as no operation if a doublescan or interlaced video mode is active. Higher level code is expected to handle
this.


Returns
=======

Negative value on error, failure or if not supported in current


video mode
==========

-EINVAL - Invalid CRTC. -EAGAIN - Temporary unavailable, e.g., called before initial modeset. -ENOTSUPP - Function not supported in current display mode. -EIO - Failed, e.g., due
to failed scanout position query.

Returns or'ed positive status flags on success:

DRM_VBLANKTIME_SCANOUTPOS_METHOD - Signal this method used for timestamping. DRM_VBLANKTIME_INVBL - Timestamp taken while scanout was in vblank interval.
