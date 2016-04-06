.. -*- coding: utf-8; mode: rst -*-

============
intel_bios.c
============



.. _xref_intel_bios_is_valid_vbt:

intel_bios_is_valid_vbt
=======================

.. c:function:: bool intel_bios_is_valid_vbt (const void * buf, size_t size)

    does the given buffer contain a valid VBT

    :param const void * buf:
        pointer to a buffer to validate

    :param size_t size:
        size of the buffer



Description
-----------

Returns true on valid VBT.




.. _xref_intel_bios_init:

intel_bios_init
===============

.. c:function:: int intel_bios_init (struct drm_i915_private * dev_priv)

    find VBT and initialize settings from the BIOS

    :param struct drm_i915_private * dev_priv:
        i915 device instance



Description
-----------

Loads the Video BIOS and checks that the VBT exists.  Sets scratch registers
to appropriate values.


Returns 0 on success, nonzero on failure.


