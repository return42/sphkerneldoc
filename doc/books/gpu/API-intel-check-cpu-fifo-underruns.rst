
.. _API-intel-check-cpu-fifo-underruns:

==============================
intel_check_cpu_fifo_underruns
==============================

*man intel_check_cpu_fifo_underruns(9)*

*4.6.0-rc1*

check for CPU fifo underruns immediately


Synopsis
========

.. c:function:: void intel_check_cpu_fifo_underruns( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

Check for CPU fifo underruns immediately. Useful on IVB/HSW where the shared error interrupt may have been disabled, and so CPU fifo underruns won't necessarily raise an interrupt,
and on GMCH platforms where underruns never raise an interrupt.
