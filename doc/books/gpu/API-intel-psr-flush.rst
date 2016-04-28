.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-psr-flush:

===============
intel_psr_flush
===============

*man intel_psr_flush(9)*

*4.6.0-rc5*

Flush PSR


Synopsis
========

.. c:function:: void intel_psr_flush( struct drm_device * dev, unsigned frontbuffer_bits, enum fb_op_origin origin )

Arguments
=========

``dev``
    DRM device

``frontbuffer_bits``
    frontbuffer plane tracking bits

``origin``
    which operation caused the flush


Description
===========

Since the hardware frontbuffer tracking has gaps we need to integrate
with the software frontbuffer tracking. This function gets called every
time frontbuffer rendering has completed and flushed out to memory. PSR
can be enabled again if no other frontbuffer relevant to PSR is dirty.

Dirty frontbuffers relevant to PSR are tracked in
busy_frontbuffer_bits.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
