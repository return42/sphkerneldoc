.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-guc-ucode-load:

====================
intel_guc_ucode_load
====================

*man intel_guc_ucode_load(9)*

*4.6.0-rc5*

load GuC uCode into the device


Synopsis
========

.. c:function:: int intel_guc_ucode_load( struct drm_device * dev )

Arguments
=========

``dev``
    drm device


Description
===========

Called from ``gem_init_hw`` during driver loading and also after a GPU
reset.

The firmware image should have already been fetched into memory by the
earlier call to ``intel_guc_ucode_init``, so here we need only check
that is succeeded, and then transfer the image to the h/w.


Return
======

non-zero code on error


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
