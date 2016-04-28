.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-edp-drrs-flush:

====================
intel_edp_drrs_flush
====================

*man intel_edp_drrs_flush(9)*

*4.6.0-rc5*

Restart Idleness DRRS


Synopsis
========

.. c:function:: void intel_edp_drrs_flush( struct drm_device * dev, unsigned frontbuffer_bits )

Arguments
=========

``dev``
    DRM device

``frontbuffer_bits``
    frontbuffer plane tracking bits


Description
===========

This function gets called every time rendering on the given planes has
completed or flip on a crtc is completed. So DRRS should be upclocked
(LOW_RR -> HIGH_RR). And also Idleness detection should be started
again, if no other planes are dirty.

Dirty frontbuffers relevant to DRRS are tracked in
busy_frontbuffer_bits.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
