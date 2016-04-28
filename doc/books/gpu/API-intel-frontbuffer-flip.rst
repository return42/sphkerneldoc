.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-frontbuffer-flip:

======================
intel_frontbuffer_flip
======================

*man intel_frontbuffer_flip(9)*

*4.6.0-rc5*

synchronous frontbuffer flip


Synopsis
========

.. c:function:: void intel_frontbuffer_flip( struct drm_device * dev, unsigned frontbuffer_bits )

Arguments
=========

``dev``
    DRM device

``frontbuffer_bits``
    frontbuffer plane tracking bits


Description
===========

This function gets called after scheduling a flip on ``obj``. This is
for synchronous plane updates which will happen on the next vblank and
which will not get delayed by pending gpu rendering.

Can be called without any locks held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
