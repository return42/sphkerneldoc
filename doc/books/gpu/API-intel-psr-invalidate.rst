.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-psr-invalidate:

====================
intel_psr_invalidate
====================

*man intel_psr_invalidate(9)*

*4.6.0-rc5*

Invalidade PSR


Synopsis
========

.. c:function:: void intel_psr_invalidate( struct drm_device * dev, unsigned frontbuffer_bits )

Arguments
=========

``dev``
    DRM device

``frontbuffer_bits``
    frontbuffer plane tracking bits


Description
===========

Since the hardware frontbuffer tracking has gaps we need to integrate
with the software frontbuffer tracking. This function gets called every
time frontbuffer rendering starts and a buffer gets dirtied. PSR must be
disabled if the frontbuffer mask contains a buffer relevant to PSR.

Dirty frontbuffers relevant to PSR are tracked in
busy_frontbuffer_bits."


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
