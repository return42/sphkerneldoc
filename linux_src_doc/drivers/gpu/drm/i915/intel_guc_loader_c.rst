.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_guc_loader.c

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

.. _`intel_guc_init_hw`:

intel_guc_init_hw
=================

.. c:function:: int intel_guc_init_hw(struct intel_guc *guc)

    finish preparing the GuC for activity

    :param struct intel_guc \*guc:
        intel_guc structure

.. _`intel_guc_init_hw.description`:

Description
-----------

Called during driver loading and also after a GPU reset.

The main action required here it to load the GuC uCode into the device.
The firmware image should have already been fetched into memory by the
earlier call to \ :c:func:`intel_guc_init`\ , so here we need only check that
worked, and then transfer the image to the h/w.

.. _`intel_guc_init_hw.return`:

Return
------

non-zero code on error

.. _`intel_guc_select_fw`:

intel_guc_select_fw
===================

.. c:function:: int intel_guc_select_fw(struct intel_guc *guc)

    selects GuC firmware for loading

    :param struct intel_guc \*guc:
        intel_guc struct

.. _`intel_guc_select_fw.return`:

Return
------

zero when we know firmware, non-zero in other case

.. This file was automatic generated / don't edit.

