.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-bios-init:

===============
intel_bios_init
===============

*man intel_bios_init(9)*

*4.6.0-rc5*

find VBT and initialize settings from the BIOS


Synopsis
========

.. c:function:: int intel_bios_init( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

Loads the Video BIOS and checks that the VBT exists. Sets scratch
registers to appropriate values.

Returns 0 on success, nonzero on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
