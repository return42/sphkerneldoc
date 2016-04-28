.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-vblank-no-hw-counter:

========================
drm_vblank_no_hw_counter
========================

*man drm_vblank_no_hw_counter(9)*

*4.6.0-rc5*

"No hw counter" implementation of .\ ``get_vblank_counter``


Synopsis
========

.. c:function:: u32 drm_vblank_no_hw_counter( struct drm_device * dev, unsigned int pipe )

Arguments
=========

``dev``
    DRM device

``pipe``
    CRTC for which to read the counter


Description
===========

Drivers can plug this into the .\ ``get_vblank_counter`` function if
there is no useable hardware frame counter available.


Returns
=======

0


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
