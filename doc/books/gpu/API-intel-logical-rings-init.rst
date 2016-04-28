.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-logical-rings-init:

========================
intel_logical_rings_init
========================

*man intel_logical_rings_init(9)*

*4.6.0-rc5*

allocate, populate and init the Engine Command Streamers


Synopsis
========

.. c:function:: int intel_logical_rings_init( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device.


Description
===========

This function inits the engines for an Execlists submission style (the
equivalent in the legacy ringbuffer submission world would be
i915_gem_init_rings). It does it only for those engines that are
present in the hardware.


Return
======

non-zero if the initialization failed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
