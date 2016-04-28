.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-psr-single-frame-update:

=============================
intel_psr_single_frame_update
=============================

*man intel_psr_single_frame_update(9)*

*4.6.0-rc5*

Single Frame Update


Synopsis
========

.. c:function:: void intel_psr_single_frame_update( struct drm_device * dev, unsigned frontbuffer_bits )

Arguments
=========

``dev``
    DRM device

``frontbuffer_bits``
    frontbuffer plane tracking bits


Description
===========

Some platforms support a single frame update feature that is used to
send and update only one frame on Remote Frame Buffer. So far it is only
implemented for Valleyview and Cherryview because hardware requires this
to be done before a page flip.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
