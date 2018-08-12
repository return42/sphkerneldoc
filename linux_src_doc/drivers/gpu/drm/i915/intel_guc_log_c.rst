.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_guc_log.c

.. _`guc-firmware-log`:

GuC firmware log
================

Firmware log is enabled by setting i915.guc_log_level to the positive level.
Log data is printed out via reading debugfs i915_guc_log_dump. Reading from
i915_guc_load_status will print out firmware loading status and scratch
registers value.

.. This file was automatic generated / don't edit.

