
.. _API-intel-check-pch-fifo-underruns:

==============================
intel_check_pch_fifo_underruns
==============================

*man intel_check_pch_fifo_underruns(9)*

*4.6.0-rc1*

check for PCH fifo underruns immediately


Synopsis
========

.. c:function:: void intel_check_pch_fifo_underruns( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

Check for PCH fifo underruns immediately. Useful on CPT/PPT where the shared error interrupt may have been disabled, and so PCH fifo underruns won't necessarily raise an interrupt.
