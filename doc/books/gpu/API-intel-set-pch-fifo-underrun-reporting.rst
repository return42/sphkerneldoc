.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-set-pch-fifo-underrun-reporting:

=====================================
intel_set_pch_fifo_underrun_reporting
=====================================

*man intel_set_pch_fifo_underrun_reporting(9)*

*4.6.0-rc5*

set PCH fifo underrun reporting state


Synopsis
========

.. c:function:: bool intel_set_pch_fifo_underrun_reporting( struct drm_i915_private * dev_priv, enum transcoder pch_transcoder, bool enable )

Arguments
=========

``dev_priv``
    i915 device instance

``pch_transcoder``
    the PCH transcoder (same as pipe on IVB and older)

``enable``
    whether underruns should be reported or not


Description
===========

This function makes us disable or enable PCH fifo underruns for a
specific PCH transcoder. Notice that on some PCHs (e.g. CPT/PPT),
disabling FIFO underrun reporting for one transcoder may also disable
all the other PCH error interruts for the other transcoders, due to the
fact that there's just one interrupt mask/enable bit for all the
transcoders.

Returns the previous state of underrun reporting.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
