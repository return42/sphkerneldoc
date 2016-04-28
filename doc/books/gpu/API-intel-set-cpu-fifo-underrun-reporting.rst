.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-set-cpu-fifo-underrun-reporting:

=====================================
intel_set_cpu_fifo_underrun_reporting
=====================================

*man intel_set_cpu_fifo_underrun_reporting(9)*

*4.6.0-rc5*

set cpu fifo underrrun reporting state


Synopsis
========

.. c:function:: bool intel_set_cpu_fifo_underrun_reporting( struct drm_i915_private * dev_priv, enum pipe pipe, bool enable )

Arguments
=========

``dev_priv``
    i915 device instance

``pipe``
    (CPU) pipe to set state for

``enable``
    whether underruns should be reported or not


Description
===========

This function sets the fifo underrun state for ``pipe``. It is used in
the modeset code to avoid false positives since on many platforms
underruns are expected when disabling or enabling the pipe.

Notice that on some platforms disabling underrun reports for one pipe
disables for all due to shared interrupts. Actual reporting is still
per-pipe though.

Returns the previous state of underrun reporting.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
