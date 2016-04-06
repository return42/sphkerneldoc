
.. _API-intel-guc-ucode-init:

====================
intel_guc_ucode_init
====================

*man intel_guc_ucode_init(9)*

*4.6.0-rc1*

define parameters and fetch firmware


Synopsis
========

.. c:function:: void intel_guc_ucode_init( struct drm_device * dev )

Arguments
=========

``dev``
    drm device


Description
===========

Called early during driver load, but after GEM is initialised.

The firmware will be transferred to the GuC's memory later, when ``intel_guc_ucode_load`` is called.
