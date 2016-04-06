
.. _API-intel-pch-fifo-underrun-irq-handler:

===================================
intel_pch_fifo_underrun_irq_handler
===================================

*man intel_pch_fifo_underrun_irq_handler(9)*

*4.6.0-rc1*

handle PCH fifo underrun interrupt


Synopsis
========

.. c:function:: void intel_pch_fifo_underrun_irq_handler( struct drm_i915_private * dev_priv, enum transcoder pch_transcoder )

Arguments
=========

``dev_priv``
    i915 device instance

``pch_transcoder``
    the PCH transcoder (same as pipe on IVB and older)


Description
===========

This handles a PCH fifo underrun interrupt, generating an underrun warning into dmesg if underrun reporting is enabled and then disables the underrun interrupt to avoid an irq
storm.
