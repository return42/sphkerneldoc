
.. _API-intel-guc-ucode-load:

====================
intel_guc_ucode_load
====================

*man intel_guc_ucode_load(9)*

*4.6.0-rc1*

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

Called from ``gem_init_hw`` during driver loading and also after a GPU reset.

The firmware image should have already been fetched into memory by the earlier call to ``intel_guc_ucode_init``, so here we need only check that is succeeded, and then transfer the
image to the h/w.


Return
======

non-zero code on error
