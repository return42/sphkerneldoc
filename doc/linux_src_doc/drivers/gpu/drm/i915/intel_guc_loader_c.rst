.. -*- coding: utf-8; mode: rst -*-

==================
intel_guc_loader.c
==================

.. _`guc-specific-firmware-loader`:

GuC-specific firmware loader
============================

intel_guc:
Top level structure of guc. It handles firmware loading and manages client
pool and doorbells. intel_guc owns a i915_guc_client to replace the legacy
ExecList submission.

Firmware versioning:
The firmware build process will generate a version header file with major and
minor version defined. The versions are built into CSS header of firmware.
i915 kernel driver set the minimal firmware version required per platform.
The firmware installation package will install (symbolic link) proper version
of firmware.

GuC address space:
GuC does not allow any gfx GGTT address that falls into range [0, WOPCM_TOP),
which is reserved for Boot ROM, SRAM and WOPCM. Currently this top address is
512K. In order to exclude 0-512K address space from GGTT, all gfx objects
used by GuC is pinned with PIN_OFFSET_BIAS along with size of WOPCM.

Firmware log:
Firmware log is enabled by setting i915.guc_log_level to non-negative level.
Log data is printed out via reading debugfs i915_guc_log_dump. Reading from
i915_guc_load_status will print out firmware loading status and scratch
registers value.


.. _`intel_guc_ucode_load`:

intel_guc_ucode_load
====================

.. c:function:: int intel_guc_ucode_load (struct drm_device *dev)

    load GuC uCode into the device

    :param struct drm_device \*dev:
        drm device


.. _`intel_guc_ucode_load.description`:

Description
-----------

Called from :c:func:`gem_init_hw` during driver loading and also after a GPU reset.

The firmware image should have already been fetched into memory by the
earlier call to :c:func:`intel_guc_ucode_init`, so here we need only check that
is succeeded, and then transfer the image to the h/w.

Return:        non-zero code on error


.. _`intel_guc_ucode_init`:

intel_guc_ucode_init
====================

.. c:function:: void intel_guc_ucode_init (struct drm_device *dev)

    define parameters and fetch firmware

    :param struct drm_device \*dev:
        drm device


.. _`intel_guc_ucode_init.description`:

Description
-----------

Called early during driver load, but after GEM is initialised.

The firmware will be transferred to the GuC's memory later,
when :c:func:`intel_guc_ucode_load` is called.


.. _`intel_guc_ucode_fini`:

intel_guc_ucode_fini
====================

.. c:function:: void intel_guc_ucode_fini (struct drm_device *dev)

    clean up all allocated resources

    :param struct drm_device \*dev:
        drm device

