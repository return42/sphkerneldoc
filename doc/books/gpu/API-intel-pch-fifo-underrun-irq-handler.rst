.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-pch-fifo-underrun-irq-handler:

===================================
intel_pch_fifo_underrun_irq_handler
===================================

*man intel_pch_fifo_underrun_irq_handler(9)*

*4.6.0-rc5*

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

This handles a PCH fifo underrun interrupt, generating an underrun
warning into dmesg if underrun reporting is enabled and then disables
the underrun interrupt to avoid an irq storm.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
