
.. _API-intel-edp-drrs-invalidate:

=========================
intel_edp_drrs_invalidate
=========================

*man intel_edp_drrs_invalidate(9)*

*4.6.0-rc1*

Disable Idleness DRRS


Synopsis
========

.. c:function:: void intel_edp_drrs_invalidate( struct drm_device * dev, unsigned frontbuffer_bits )

Arguments
=========

``dev``
    DRM device

``frontbuffer_bits``
    frontbuffer plane tracking bits


Description
===========

This function gets called everytime rendering on the given planes start. Hence DRRS needs to be Upclocked, i.e. (LOW_RR -> HIGH_RR).

Dirty frontbuffers relevant to DRRS are tracked in busy_frontbuffer_bits.
