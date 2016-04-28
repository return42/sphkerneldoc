.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-cpu-fifo-underrun-irq-handler:

===================================
intel_cpu_fifo_underrun_irq_handler
===================================

*man intel_cpu_fifo_underrun_irq_handler(9)*

*4.6.0-rc5*

handle CPU fifo underrun interrupt


Synopsis
========

.. c:function:: void intel_cpu_fifo_underrun_irq_handler( struct drm_i915_private * dev_priv, enum pipe pipe )

Arguments
=========

``dev_priv``
    i915 device instance

``pipe``
    (CPU) pipe to set state for


Description
===========

This handles a CPU fifo underrun interrupt, generating an underrun
warning into dmesg if underrun reporting is enabled and then disables
the underrun interrupt to avoid an irq storm.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
